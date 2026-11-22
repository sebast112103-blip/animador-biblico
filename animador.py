#!/usr/bin/env python3
"""
ANIMADOR BIBLICO 2D - gratis, sin creditos
==========================================
Convierte una historia escrita en un archivo .json en un video animado 2D
vertical (9:16) con personajes estilo "doodle", voz narrada y subtitulos.

Uso:
    python animador.py historias/david_y_goliat.json
    python animador.py historias/david_y_goliat.json --sin-voz    (prueba rapida)
    python animador.py historias/david_y_goliat.json --borrador   (mitad de resolucion, rapido)
"""
import argparse
import asyncio
import io
import json
import math
import random
import re
import shutil
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(errors="replace")
    except Exception:
        pass

def _buscar_ffmpeg():
    """Si ffmpeg no esta en el PATH (pasa en Windows recien instalado con winget), lo busca."""
    import os
    if shutil.which("ffmpeg"):
        return
    candidatos = []
    la = os.environ.get("LOCALAPPDATA", "")
    if la:
        candidatos.append(Path(la) / "Microsoft" / "WinGet" / "Links")
        pk = Path(la) / "Microsoft" / "WinGet" / "Packages"
        if pk.exists():
            candidatos += [f.parent for f in pk.glob("*FFmpeg*/**/bin/ffmpeg.exe")]
    for c in ("C:/ffmpeg/bin", "C:/Program Files/ffmpeg/bin"):
        candidatos.append(Path(c))
    for c in candidatos:
        if (c / "ffmpeg.exe").exists() or (c / "ffmpeg").exists():
            os.environ["PATH"] = str(c) + os.pathsep + os.environ.get("PATH", "")
            return


_buscar_ffmpeg()

W, H, FPS = 1080, 1920, 30
SS = 2                 # supermuestreo de personajes (bordes suaves)
TINTA = (24, 20, 18, 255)
SR = 24000             # frecuencia del audio
TMP = str(__import__("os").getpid())   # nombre unico para archivos temporales

# ======================================================================
#  Utilidades de color y forma
# ======================================================================

def col(c, a=255):
    if c is None:
        return None
    if isinstance(c, (tuple, list)):
        return tuple(c) if len(c) == 4 else (*c, a)
    c = c.lstrip("#")
    if len(c) == 3:
        c = "".join(ch * 2 for ch in c)
    return (int(c[0:2], 16), int(c[2:4], 16), int(c[4:6], 16), a)


def oscuro(c, f=0.72):
    c = col(c)
    return (int(c[0] * f), int(c[1] * f), int(c[2] * f), c[3])


def mezcla(a, b, t):
    a, b = col(a), col(b)
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(4))


def suave(p):
    p = max(0.0, min(1.0, p))
    return p * p * (3 - 2 * p)


class Lapiz:
    """Dibuja en coordenadas locales del personaje (pies en 0,0; y hacia arriba negativo),
    con espejo segun hacia donde mira, escala y un leve temblor de linea 'hecho a mano'."""

    def __init__(self, img, ox, oy, esc, mira, semilla):
        self.d = ImageDraw.Draw(img)
        self.ox, self.oy, self.s, self.f = ox, oy, esc * SS, mira
        self.rng = random.Random(semilla)
        self.grosor = 6.5 * SS * esc ** 0.55

    def P(self, x, y):
        return (self.ox + x * self.f * self.s, self.oy + y * self.s)

    def _j(self, pts, amp=1.1):
        a = amp * SS
        return [(x + self.rng.uniform(-a, a), y + self.rng.uniform(-a, a)) for x, y in pts]

    def forma(self, pts, relleno, borde=TINTA, g=1.0, temblor=True):
        q = [self.P(x, y) for x, y in pts]
        if temblor:
            q = self._j(q)
        if relleno:
            self.d.polygon(q, fill=relleno)
        if borde and g > 0:
            self.d.line(q + [q[0]], fill=borde, width=max(1, int(self.grosor * g)), joint="curve")

    def linea(self, pts, g=1.0, color=TINTA):
        q = self._j([self.P(x, y) for x, y in pts], 0.8)
        self.d.line(q, fill=color, width=max(1, int(self.grosor * g)), joint="curve")
        r = self.grosor * g / 2
        for x, y in (q[0], q[-1]):
            self.d.ellipse([x - r, y - r, x + r, y + r], fill=color)

    def elipse(self, cx, cy, rx, ry, relleno, borde=TINTA, g=1.0, rot=0.0, n=34):
        pts = []
        for i in range(n):
            a = 2 * math.pi * i / n
            x, y = rx * math.cos(a), ry * math.sin(a)
            if rot:
                x, y = x * math.cos(rot) - y * math.sin(rot), x * math.sin(rot) + y * math.cos(rot)
            pts.append((cx + x, cy + y))
        self.forma(pts, relleno, borde, g)

    def arco(self, cx, cy, rx, ry, a0, a1, g=1.0, color=TINTA, n=16):
        pts = [(cx + rx * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
                cy + ry * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]
        self.linea(pts, g, color)

# ======================================================================
#  Personajes
# ======================================================================

DEFECTO = {
    "tipo": "persona", "piel": "#f1d2b0", "pelo": "#4a2c17", "pelo_largo": False,
    "barba": None, "tunica": "#d9c7a3", "manto": None, "cinturon": "#7a4a22",
    "tocado": None, "color_tocado": "#e9e4d8", "armadura": False, "escala": 1.0,
    "objeto": None, "aureola": False, "alas": False, "voz": None,
    "venda": False, "color_venda": "#e9e4d8", "color": None, "melena": None, "lana": None, "vela": True,
}


def pose_de(accion, t, dur, emocion, hablando):
    """Calcula la postura del personaje en el segundo t de la escena."""
    p = t / max(dur, 0.01)
    po = {"dy": math.sin(t * 2.2) * 3, "inclina": 0.0, "brazo_d": 8 + math.sin(t * 1.7) * 4,
          "brazo_t": -6 + math.sin(t * 1.5 + 1) * 4, "pierna": 0.0, "caida": 0.0,
          "agacha": 0.0, "emocion": emocion, "ojos_cerrados": False, "dx": 0.0, "girar_honda": None,
          "lanzo": False}
    if hablando:
        po["brazo_d"] = 35 + math.sin(t * 3.1) * 18
    if accion == "caminar":
        fase = t * 7.5
        po["pierna"] = math.sin(fase) * 26
        po["dy"] = -abs(math.sin(fase)) * 9
        po["brazo_d"] = math.sin(fase) * 28
        po["brazo_t"] = -math.sin(fase) * 28
    elif accion == "correr":
        fase = t * 12
        po["pierna"] = math.sin(fase) * 38
        po["dy"] = -abs(math.sin(fase)) * 16
        po["brazo_d"] = math.sin(fase) * 50
        po["brazo_t"] = -math.sin(fase) * 50
        po["inclina"] = 8
    elif accion == "saltar":
        po["dy"] = -abs(math.sin(t * 5)) * 90
        po["brazo_d"], po["brazo_t"] = 128, -135
    elif accion in ("celebrar", "alabar"):
        po["brazo_d"] = 125 + math.sin(t * 6) * 10
        po["brazo_t"] = -135 + math.sin(t * 6 + 1) * 10
        if accion == "celebrar":
            po["dy"] = -abs(math.sin(t * 5)) * 45
        else:
            po["ojos_cerrados"] = True
        po["emocion"] = "feliz"
    elif accion == "orar":
        po["brazo_d"] = po["brazo_t"] = 70
        po["ojos_cerrados"] = True
        po["agacha"] = 0.5
        po["inclina"] = 6
    elif accion == "agacharse":
        k = math.sin(min(p, 1) * math.pi)
        po["agacha"] = k
        po["inclina"] = 25 * k
        po["brazo_d"] = 20 + 30 * k
    elif accion == "levantar":     # levantar la vara / el brazo al cielo
        k = suave(min(1, p * 3))
        po["brazo_d"] = 40 + 120 * k
        po["emocion"] = emocion if emocion != "neutral" else "valiente"
    elif accion == "empujar":      # brazos abiertos empujando (Sanson)
        po["brazo_d"], po["brazo_t"] = 95, -95
        po["dx"] = math.sin(t * 30) * 3
        po["emocion"] = emocion if emocion != "neutral" else "enojado"
    elif accion == "abrazar":
        po["brazo_d"] = po["brazo_t"] = 85
        po["emocion"] = emocion if emocion != "neutral" else "feliz"
    elif accion == "arrodillarse":
        po["agacha"] = 0.75
        po["brazo_d"] = po["brazo_t"] = 60
        po["inclina"] = 5
    elif accion == "ofrecer":
        po["brazo_d"] = po["brazo_t"] = 75
    elif accion == "senalar":
        po["brazo_d"] = 88
    elif accion == "temblar":
        po["dx"] = math.sin(t * 40) * 4
        po["emocion"] = emocion if emocion != "neutral" else "asustado"
        po["brazo_d"] = po["brazo_t"] = 40
    elif accion == "lanzar":
        if p < 0.62:   # girar la honda sobre la cabeza
            po["girar_honda"] = t * 16
            po["brazo_d"] = 165
        else:          # soltar
            k = suave((p - 0.62) / 0.12)
            po["brazo_d"] = 165 - 95 * k
            po["inclina"] = 10 * k
            po["lanzo"] = True
        po["emocion"] = emocion if emocion != "neutral" else "valiente"
    elif accion in ("caer", "caer_de_cara"):
        po["de_cara"] = accion == "caer_de_cara"
        k = suave(p / 0.35)
        po["caida"] = 88 * k
        po["emocion"] = "noqueado" if k > 0.3 else "sorprendido"
        po["brazo_d"] = 100 * k
        po["brazo_t"] = 120 * k
        po["dy"] = 0
    elif accion == "dormir":
        po["caida"] = 86
        po["ojos_cerrados"] = True
        po["dy"] = 0
    return po


def brazo(L, hombro, ang, largo, mano_col, g=1.0):
    """ang: 0 = colgando, 90 = al frente, 180 = arriba."""
    a = math.radians(ang)
    codo = (hombro[0] + math.sin(a) * largo * 0.52, hombro[1] + math.cos(a) * largo * 0.52)
    a2 = math.radians(ang + 14)
    mano = (codo[0] + math.sin(a2) * largo * 0.5, codo[1] + math.cos(a2) * largo * 0.5)
    L.linea([hombro, codo, mano], g)
    L.elipse(mano[0], mano[1], 11, 11, mano_col, g=0.7)
    return mano


def objeto_en_mano(L, obj, mano, po, t, c):
    mx, my = mano
    if obj == "cayado":
        L.linea([(mx, my - 150), (mx, my + 140)], 1.5, col("#7b5230"))
        L.arco(mx - 22, my - 150, 22, 22, 180, 360, 1.5, col("#7b5230"))
    elif obj == "lanza":
        L.linea([(mx, my - 260), (mx, my + 180)], 1.6, col("#6e4a2a"))
        L.forma([(mx - 13, my - 255), (mx, my - 310), (mx + 13, my - 255)], col("#b9bcc2"))
    elif obj == "espada":
        L.forma([(mx - 6, my - 10), (mx - 6, my - 150), (mx, my - 168), (mx + 6, my - 150), (mx + 6, my - 10)],
                col("#c9ccd2"))
        L.linea([(mx - 24, my - 10), (mx + 24, my - 10)], 1.4, col("#8a6a2a"))
    elif obj == "honda":
        if po["girar_honda"] is not None:
            a = po["girar_honda"]
            px, py = mx + math.cos(a) * 75, my - 40 + math.sin(a) * 26
            L.linea([(mx, my), (px, py)], 0.5)
            L.elipse(px, py, 10, 10, col("#8d8d8d"), g=0.6)
        elif not po["lanzo"]:
            L.linea([(mx, my), (mx + 6, my + 55)], 0.5)
            L.elipse(mx + 6, my + 62, 9, 9, col("#8d8d8d"), g=0.6)
        else:
            L.linea([(mx, my), (mx + 10, my + 50)], 0.5)
    elif obj == "escudo":
        L.elipse(mx + 10, my, 48, 62, col("#b08a3a"), g=1.1)
        L.elipse(mx + 10, my, 14, 14, col("#d9b55a"), g=0.7)
    elif obj == "tablas":
        for dx in (-30, 30):
            L.forma([(mx + dx - 27, my - 70), (mx + dx - 27, my + 20), (mx + dx + 27, my + 20),
                     (mx + dx + 27, my - 70), (mx + dx, my - 92)], col("#bdb7aa"))
    elif obj == "pan":
        L.elipse(mx + 8, my - 6, 30, 20, col("#d39b52"), g=0.8)
    elif obj == "lampara":
        L.elipse(mx + 6, my - 4, 26, 14, col("#b07a3a"), g=0.8)
        L.elipse(mx + 30, my - 26, 7, 14, col("#ffcc33"), borde=None)


def dibujar_persona(L, c, po, t, hablando, boca_abierta, semilla):
    piel, tun = col(c["piel"]), col(c["tunica"])
    ag = po["agacha"]
    cadera_y = -150 + 55 * ag
    # alas (detras)
    if c.get("alas"):
        for lado, rot in ((-1, -0.35), (1, 0.35)):
            L.elipse(lado * 70 - 10, -330 + math.sin(t * 3) * 6, 70, 135, col("#ffffff"), g=1.0, rot=rot)
    # brazo trasero
    hombro_t = (-30, -305 + 55 * ag)
    brazo(L, hombro_t, po["brazo_t"], 140, piel)
    # piernas
    pa = po["pierna"]
    for lado, s in ((-1, 1), (1, -1)):
        a = math.radians(pa * s)
        cad = (lado * 20, cadera_y)
        if ag > 0.3:   # rodillas dobladas
            rod = (cad[0] + 45, cad[1] + 60)
            pie = (rod[0] - 15, 0)
            L.linea([cad, rod, pie], 1.0)
        else:
            pie = (cad[0] + math.sin(a) * 150, cad[1] + math.cos(a) * 150)
            L.linea([cad, pie], 1.0)
        L.elipse(pie[0] + 10, pie[1] - 4, 22, 10, col("#5a3a22"), g=0.7)
    # tunica
    top = -340 + 55 * ag
    if c.get("armadura"):
        L.forma([(-58, top), (58, top), (70, cadera_y - 10), (-70, cadera_y - 10)], col("#9b8a6a"))
        for k in range(-3, 4):
            L.forma([(k * 20 - 9, cadera_y - 12), (k * 20 + 9, cadera_y - 12),
                     (k * 20 + 9, cadera_y + 50), (k * 20 - 9, cadera_y + 50)], col("#7d6a4a"), g=0.6)
        L.forma([(-58, top), (58, top), (54, top + 95), (-54, top + 95)], col("#b8a37a"))
        for k in range(3):
            L.linea([(-50, top + 30 + k * 22), (50, top + 30 + k * 22)], 0.4, col("#6e5b3c"))
    else:
        L.forma([(-52, top), (52, top), (78, cadera_y + 45), (-78, cadera_y + 45)], tun)
        if c.get("manto"):
            L.forma([(-52, top), (-20, top), (60, cadera_y + 10), (30, cadera_y + 30)], col(c["manto"]), g=0.8)
        if c.get("cinturon"):
            L.linea([(-62, cadera_y - 35), (62, cadera_y - 35)], 1.4, col(c["cinturon"]))
    # cabeza
    cx, cy = 12, top - 82
    r = 95
    if c.get("aureola"):
        L.elipse(cx - 8, cy - 20, 118, 118, None, borde=col("#ffd34d"), g=1.6)
    if c.get("pelo") and c.get("pelo_largo"):
        L.forma([(cx - 90, cy - 30), (cx - 30, cy - 90), (cx - 40, cy + 100), (cx - 100, cy + 95)], col(c["pelo"]))
    L.elipse(cx, cy, r, r * 0.98, piel, g=1.1, n=40)
    if c.get("pelo"):
        pts = [(cx + r * math.cos(math.radians(a)), cy + r * math.sin(math.radians(a))) for a in range(150, 361, 15)]
        pts += [(cx + 60, cy - 70), (cx + 20, cy - 55), (cx - 30, cy - 60), (cx - 70, cy - 20)]
        L.forma(pts, col(c["pelo"]), g=0.9)
    if c.get("barba"):
        pts = [(cx + r * 0.96 * math.cos(math.radians(a)), cy + r * 0.96 * math.sin(math.radians(a)))
               for a in range(5, 176, 15)]
        pts += [(cx - 80, cy + 30), (cx - 20, cy + 30), (cx + 30, cy + 28), (cx + 85, cy + 22)]
        L.forma(pts, col(c["barba"]), g=0.9)
        L.elipse(cx + 22, cy + 45, 30, 17, piel, borde=None)   # hueco para la boca
    # ojos
    emo = po["emocion"]
    parpadeo = (t + semilla * 0.37) % 3.6 < 0.12
    cerrados = po["ojos_cerrados"] or parpadeo or emo == "noqueado"
    for k, ex in enumerate((cx - 12, cx + 48)):
        ey = cy - 12
        if emo == "noqueado":
            L.linea([(ex - 12, ey - 12), (ex + 12, ey + 12)], 0.8)
            L.linea([(ex - 12, ey + 12), (ex + 12, ey - 12)], 0.8)
            continue
        if cerrados:
            L.arco(ex, ey, 18, 9, 0, 180, 0.8)
            continue
        grande = emo in ("asustado", "sorprendido")
        rx, ry = (25, 31) if grande else (21, 26)
        L.elipse(ex, ey, rx, ry, col("#ffffff"), g=0.8)
        pr = 7 if grande else 10
        L.elipse(ex + 7, ey + 3, pr, pr, TINTA, borde=None)
    # cejas
    for k, ex in enumerate((cx - 12, cx + 48)):
        ey = cy - 50
        if emo in ("enojado", "valiente", "burlon"):
            inc = 10 if k == 0 else -10
            if emo == "burlon" and k == 0:
                inc = -4
        elif emo in ("triste", "asustado", "llorando"):
            inc = -9 if k == 0 else 9
        else:
            inc = 0
        alto = -6 if emo in ("sorprendido", "asustado", "feliz") else 0
        L.linea([(ex - 17, ey - inc + alto), (ex + 17, ey + inc + alto)], 0.8)
    if emo == "llorando":   # lagrimas que caen
        for k, ex in enumerate((cx - 12, cx + 48)):
            ty = cy + 10 + ((t * 60 + k * 25) % 70)
            L.elipse(ex + 5, ty, 7, 11, col("#6fb7f0"), g=0.4)
    if c.get("venda"):
        L.forma([(cx - r * .98, cy - 40), (cx + r * .98, cy - 40), (cx + r * .98, cy + 12), (cx - r * .98, cy + 12)],
                col(c.get("color_venda", "#e9e4d8")), g=0.9)
    # boca
    mx, my = cx + 22, cy + 45
    if hablando and boca_abierta > 0.08:
        L.elipse(mx, my, 15 + 4 * boca_abierta, 4 + 15 * boca_abierta, col("#7a2a2a"), g=0.8)
    elif emo in ("asustado", "sorprendido"):
        L.elipse(mx, my, 10, 13, col("#7a2a2a"), g=0.8)
    elif emo in ("feliz", "valiente"):
        L.arco(mx, my - 10, 24, 16, 20, 160, 0.8)
    elif emo == "burlon":
        L.arco(mx + 6, my - 12, 24, 14, 10, 120, 0.8)
    elif emo in ("triste", "enojado", "llorando"):
        L.arco(mx, my + 10, 20, 12, 200, 340, 0.8)
    elif emo == "noqueado":
        L.arco(mx, my, 16, 6, 200, 340, 0.8)
    else:
        L.linea([(mx - 12, my), (mx + 12, my)], 0.7)
    # tocados
    tc = col(c.get("color_tocado", "#e9e4d8"))
    if c.get("tocado") == "corona":
        b = cy - r * 0.78
        L.forma([(cx - 55, b), (cx - 60, b - 50), (cx - 30, b - 25), (cx, b - 62), (cx + 30, b - 25),
                 (cx + 60, b - 50), (cx + 55, b)], col("#f2c230"))
    elif c.get("tocado") == "casco":
        pts = [(cx + (r + 6) * math.cos(math.radians(a)), cy - 44 + (r + 2) * 0.9 * math.sin(math.radians(a)))
               for a in range(180, 361, 12)]
        L.forma(pts, col("#a8823e"))
        L.linea([(cx - r - 12, cy - 44), (cx + r + 12, cy - 44)], 1.6, col("#7a5a26"))
        L.forma([(cx - 10, cy - r - 12), (cx + 10, cy - r - 12), (cx + 30, cy - r - 70), (cx - 30, cy - r - 70)],
                col("#b33a2a"), g=0.8)
    elif c.get("tocado") == "velo":
        pts = [(cx + (r + 10) * math.cos(math.radians(a)), cy + (r + 10) * math.sin(math.radians(a)))
               for a in range(160, 361, 15)]
        pts += [(cx + r + 5, cy - 10), (cx - 35, cy - 40), (cx - 70, cy + 60), (cx - 95, cy + 120),
                (cx - 130, cy + 110)]
        L.forma(pts, tc)
    elif c.get("tocado") == "nemes":   # tocado del faraon
        pts = [(cx + (r + 12) * math.cos(math.radians(a)), cy - 15 + (r + 12) * math.sin(math.radians(a)))
               for a in range(180, 361, 15)]
        pts += [(cx + r + 12, cy - 15), (cx + 40, cy - 30), (cx - 40, cy - 25), (cx - 95, cy + 120),
                (cx - 135, cy + 110), (cx - r - 12, cy - 15)]
        L.forma(pts, col("#2f5fa8"))
        for k in range(4):
            L.arco(cx, cy - 15, r + 4 - k * 2, r * .9 - k * 18, 200, 340, 0.6, col("#e8c35a"))
        L.elipse(cx + 20, cy - r - 2, 12, 16, col("#e8c35a"), g=0.6)
    elif c.get("tocado") == "turbante":
        L.elipse(cx, cy - r * 0.8, r * 1.0, r * 0.4, tc)
        L.arco(cx, cy - r * 0.8, r * 0.78, r * 0.2, 200, 340, 0.6)
    # brazo delantero y objeto
    hombro_d = (35, -305 + 55 * ag)
    ang = po["brazo_d"]
    if po["ojos_cerrados"] and po["brazo_d"] == 70:   # manos juntas orando
        ang = 60
    mano = brazo(L, hombro_d, ang, 140, piel)
    if c.get("objeto"):
        objeto_en_mano(L, c["objeto"], mano, po, t, c)
    return mano


def dibujar_oveja(L, c, po, t):
    pa = po["pierna"]
    for k, x in enumerate((-45, -20, 25, 50)):
        a = math.radians(pa * (1 if k % 2 else -1))
        L.linea([(x, -60), (x + math.sin(a) * 60, 0)], 0.9)
    pts = []
    for i in range(18):
        a = 2 * math.pi * i / 18
        rr = 1 + 0.12 * math.sin(a * 6)
        pts.append((math.cos(a) * 85 * rr, -95 + math.sin(a) * 55 * rr))
    L.forma(pts, col(c.get("lana") or "#f4f1ea"))
    L.elipse(95, -120 + math.sin(t * 2) * 3, 30, 24, col("#3a302a"))
    L.elipse(103, -126, 6, 6, col("#ffffff"), borde=None)


def render_personaje(c, x_px, suelo_y, po, t, hablando, boca, mira, semilla, frame):
    esc = c["escala"]
    sw, sh = int(560 * esc * SS), int(820 * esc * SS)
    img = Image.new("RGBA", (sw, sh), (0, 0, 0, 0))
    ox, oy = sw / 2, sh - 30 * esc * SS
    L = Lapiz(img, ox, oy, esc, mira, semilla * 1000 + frame // 4)  # 'boil' cada 4 cuadros
    mano = None
    if c["tipo"] != "persona" and po["caida"]:   # animales: dormir = acostado
        po = dict(po, caida=0, acostado=True, ojos_cerrados=True)
    if c["tipo"] == "oveja":
        dibujar_oveja(L, c, po, t)
    elif c["tipo"] in ANIMALES:
        ANIMALES[c["tipo"]](L, c, po, t, boca)
    else:
        mano = dibujar_persona(L, c, po, t, hablando, boca, semilla)
    if po["caida"] or po["inclina"]:
        # caer: hacia atras (antihorario si mira a la derecha); inclinar: hacia delante
        if po["caida"]:
            ang = -po["caida"] * mira if po.get("de_cara") else po["caida"] * mira
        else:
            ang = -po["inclina"] * mira
        big = Image.new("RGBA", (sw * 2, sh), (0, 0, 0, 0))
        big.paste(img, (sw // 2, 0))
        img = big.rotate(ang, center=(sw // 2 + ox, oy), resample=Image.BICUBIC)
        ox += sw // 2
    caja = img.getbbox()
    if caja:
        x0, y0 = (caja[0] // SS) * SS, (caja[1] // SS) * SS
        x1 = min(img.width, -(-caja[2] // SS) * SS)
        y1 = min(img.height, -(-caja[3] // SS) * SS)
        img = img.crop((x0, y0, x1, y1))
        ox, oy = ox - x0, oy - y0
    fin = img.reduce(SS)
    pos = (int(x_px - ox / SS + po["dx"]), int(suelo_y - oy / SS + po["dy"]))
    mano_px = None
    if mano:
        mano_px = (x_px + (mano[0] * mira) * esc, suelo_y + mano[1] * esc + po["dy"])
    return fin, pos, mano_px

# ======================================================================
#  Fondos pintados
# ======================================================================

def gradiente(h, w, arriba, abajo):
    a, b = np.array(col(arriba)[:3], float), np.array(col(abajo)[:3], float)
    t = np.linspace(0, 1, h)[:, None]
    return np.repeat((a * (1 - t) + b * t)[:, None, :], w, axis=1).reshape(h, w, 3)


def cresta(w, base, amp, rng, suavidad=6, n=None):
    xs = np.arange(w)
    y = np.full(w, float(base))
    for k in range(1, 5):
        fr = rng.uniform(0.6, 1.4) * k / w * suavidad
        y += amp / k * np.sin(xs * fr * 2 * np.pi + rng.uniform(0, 6))
    return y


def capa(img, ys, color, desde_arriba=False, ruido=0.0, rng=None):
    h, w, _ = img.shape
    yy = np.arange(h)[:, None]
    m = (yy >= ys[None, :]) if not desde_arriba else (yy <= ys[None, :])
    c = np.array(col(color)[:3], float)
    if ruido and rng is not None:
        tex = rng.normal(0, ruido, (h, w, 1))
        img[:] = np.where(m[..., None], c + tex, img)
    else:
        img[:] = np.where(m[..., None], c, img)


def sol(img, cx, cy, r, color, brillo=0.5):
    h, w, _ = img.shape
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2)
    glow = np.clip(1 - d / (r * 5), 0, 1) ** 2 * brillo
    c = np.array(col(color)[:3], float)
    img[:] = img * (1 - glow[..., None]) + c * glow[..., None]
    img[d < r] = c


def nubes(pil, rng, n, y0, y1, color="#ffffff", alfa=210):
    d = ImageDraw.Draw(pil, "RGBA")
    for _ in range(n):
        x, y = rng.uniform(-100, W + 100), rng.uniform(y0, y1)
        for _ in range(7):
            rx, ry = rng.uniform(60, 130), rng.uniform(35, 60)
            dx, dy = rng.uniform(-110, 110), rng.uniform(-20, 20)
            d.ellipse([x + dx - rx, y + dy - ry, x + dx + rx, y + dy + ry], fill=col(color, alfa))


def arbol(d, x, y, esc, rng, copa="#4f7d3a"):
    d.rectangle([x - 10 * esc, y - 120 * esc, x + 10 * esc, y], fill=col("#5b3b22"))
    for _ in range(6):
        rx = rng.uniform(45, 70) * esc
        cx, cy = x + rng.uniform(-50, 50) * esc, y - 150 * esc + rng.uniform(-50, 30) * esc
        d.ellipse([cx - rx, cy - rx, cx + rx, cy + rx], fill=mezcla(copa, "#2e4f22", rng.uniform(0, .4)))


def palmera(d, x, y, esc):
    for k in range(8):
        d.ellipse([x - 9 * esc + k * 3 * esc, y - k * 32 * esc - 20 * esc,
                   x + 9 * esc + k * 3 * esc, y - k * 32 * esc], fill=col("#7a5634"))
    tx, ty = x + 24 * esc, y - 270 * esc
    for a in range(0, 360, 45):
        r = math.radians(a)
        d.polygon([(tx, ty), (tx + math.cos(r) * 130 * esc, ty + math.sin(r) * 50 * esc + 40 * esc),
                   (tx + math.cos(r + .3) * 90 * esc, ty + math.sin(r + .3) * 40 * esc + 20 * esc)],
                  fill=col("#3f6e34"))


def casa(d, x, y, w, h, color):
    d.rectangle([x, y - h, x + w, y], fill=col(color), outline=oscuro(color, .6), width=3)
    d.rectangle([x + w * .4, y - h * .45, x + w * .6, y], fill=col("#5a3a22"))
    d.rectangle([x + w * .12, y - h * .8, x + w * .3, y - h * .62], fill=col("#3a2a1a"))


FONDOS = {}

# ----------------------------------------------------------------------
#  Fondos adicionales
# ----------------------------------------------------------------------

def _ladrillos(d, x0, y0, x1, y1, alto, ancho, color, linea):
    fila = 0
    y = y0
    while y < y1:
        off = (ancho / 2) * (fila % 2)
        x = x0 - off
        while x < x1:
            d.rectangle([x, y, x + ancho, y + alto], fill=col(color), outline=col(linea), width=3)
            x += ancho
        y += alto
        fila += 1


def _f_egipto(rng, pr, suelo):
    img = gradiente(H, W, "#f3a85f", "#fde3ae")
    sol(img, W * .25, H * .2, 70, "#fff2c8", .55)
    capa(img, cresta(W, suelo - 30, 12, rng, 2), "#e3b06a", ruido=6, rng=rng)
    pil = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(pil, "RGBA")
    base = H * .62
    for cx, w, h in ((260, 520, 420), (720, 380, 300), (960, 240, 180)):
        d.polygon([(cx - w / 2, base + 40), (cx, base - h), (cx + w / 2, base + 40)], fill=col("#d6a25a"))
        d.polygon([(cx, base - h), (cx + w / 2, base + 40), (cx + w * .1, base + 40)], fill=col("#b9844a"))
    d.rectangle([0, base + 30, W, suelo], fill=col("#e8b673"))
    palmera(d, 90, suelo - 40, 1.1)
    return pil


def _f_prision(rng, pr, suelo):
    pil = Image.new("RGB", (W, H), col("#4a4640")[:3])
    d = ImageDraw.Draw(pil, "RGBA")
    _ladrillos(d, 0, 0, W, suelo, 95, 190, "#5a554d", "#3a3631")
    wx, wy = W * .62, H * .2
    d.rectangle([wx, wy, wx + 220, wy + 200], fill=col("#9fc7e0"))
    for k in range(1, 5):
        d.line([(wx + k * 44, wy), (wx + k * 44, wy + 200)], fill=col("#222"), width=10)
    d.polygon([(wx, wy), (wx + 220, wy), (W * .45, suelo), (W * .05, suelo)], fill=(255, 245, 200, 40))
    d.rectangle([0, suelo - 30, W, H], fill=col("#3a3530"))
    for _ in range(60):
        x, y = pr.uniform(0, W), pr.uniform(suelo, H)
        d.line([(x, y), (x + pr.uniform(-30, 30), y - pr.uniform(5, 20))], fill=col("#c9a95a"), width=3)
    return pil


def _f_foso(rng, pr, suelo):
    img = gradiente(H, W, "#2a1d14", "#5a4230")
    pil = Image.fromarray(img.astype(np.uint8))
    d = ImageDraw.Draw(pil, "RGBA")
    for _ in range(70):
        x, y, r = pr.uniform(0, W), pr.uniform(0, suelo), pr.uniform(40, 110)
        d.ellipse([x - r, y - r * .7, x + r, y + r * .7], fill=(*col("#6e5640")[:3], 120))
    d.ellipse([W * .3, -160, W * .7, 160], fill=col("#c9e3f2"))
    d.polygon([(W * .32, 0), (W * .68, 0), (W * .85, suelo), (W * .15, suelo)], fill=(255, 245, 210, 45))
    d.rectangle([0, suelo - 30, W, H], fill=col("#4a3828"))
    for _ in range(14):
        x = pr.uniform(0, W)
        yy = suelo + pr.uniform(10, 200)
        d.ellipse([x - 26, yy, x + 26, yy + 14], fill=col("#e8dcc0"))
    return pil


def _f_establo(rng, pr, suelo):
    img = gradiente(H, W, "#0e1838", "#2a3a6a")
    est = rng.integers(0, W, 150), rng.integers(0, int(H * .4), 150)
    img[est[1], est[0]] = 255
    pil = Image.fromarray(img.astype(np.uint8))
    d = ImageDraw.Draw(pil, "RGBA")
    techo = H * .30
    d.polygon([(-50, techo), (W / 2, H * .17), (W + 50, techo)], fill=col("#5e3a1a"))
    d.rectangle([0, techo, W, suelo], fill=col("#7a4f2a"))
    for x in range(0, W, 90):
        d.line([(x, techo), (x, suelo)], fill=col("#5a3818"), width=5)
    d.rectangle([W * .12, techo + 140, W * .3, techo + 300], fill=col("#1a2448"))
    d.rectangle([0, suelo - 30, W, H], fill=col("#d9b85a"))
    for _ in range(220):
        x, y = pr.uniform(0, W), pr.uniform(suelo - 30, H)
        d.line([(x, y), (x + pr.uniform(-25, 25), y - pr.uniform(10, 30))], fill=col("#b8962f"), width=3)
    d.ellipse([W * .5 - 300, H * .1 - 300, W * .5 + 300, H * .1 + 300], fill=(255, 240, 170, 25))
    return pil


def _f_templo(rng, pr, suelo):
    pil = Image.new("RGB", (W, H), col("#b9a98a")[:3])
    d = ImageDraw.Draw(pil, "RGBA")
    _ladrillos(d, 0, 0, W, suelo, 120, 260, "#c8b896", "#a2916e")
    d.rectangle([0, 0, W, H * .08], fill=col("#7a6a4a"))
    for x in (W * .15, W * .85):
        d.rectangle([x - 18, H * .32, x + 18, H * .40], fill=col("#5a3a1a"))
        d.ellipse([x - 30, H * .27, x + 30, H * .33], fill=col("#ffb030"))
    d.rectangle([0, suelo - 30, W, H], fill=col("#8a7a5a"))
    return pil


def _f_mar_tormenta(rng, pr, suelo):
    img = gradiente(H, W, "#1e2430", "#4a5568")
    mar = int(H * .52)
    img[mar:] = gradiente(H - mar, W, "#1f3b55", "#0f2236")
    pil = Image.fromarray(img.astype(np.uint8))
    d = ImageDraw.Draw(pil, "RGBA")
    nubes(pil, pr, 6, H * .02, H * .3, "#2a303c", 230)
    for k in range(26):
        y = pr.uniform(mar + 20, H)
        x = pr.uniform(-100, W)
        d.arc([x, y - 40, x + 220, y + 40], 200, 340, fill=(200, 220, 235, 160), width=6)
    return pil


def _f_mar_rojo(rng, pr, suelo):
    img = gradiente(H, W, "#7ab8e8", "#e6f2f8")
    pil = Image.fromarray(img.astype(np.uint8))
    d = ImageDraw.Draw(pil, "RGBA")
    hz = H * .42
    d.rectangle([0, hz, W, H], fill=col("#2f6fae"))
    d.polygon([(W / 2 - 70, hz), (W / 2 + 70, hz), (W / 2 + 380, H), (W / 2 - 380, H)], fill=col("#d9bf8a"))
    for lado in (-1, 1):
        borde_a, borde_b = W / 2 + lado * 70, W / 2 + lado * 380
        ext = 0 if lado < 0 else W
        d.polygon([(ext, H * .22), (borde_a, hz - 60), (borde_b, H * .55), (borde_b, H), (ext, H)],
                  fill=col("#2a64a0"))
        for i in range(9):
            y = H * .25 + i * 140
            d.line([(ext, y), (borde_a + (borde_b - borde_a) * (i / 9), y + 40)], fill=(170, 210, 240, 140), width=6)
        d.line([(borde_a, hz - 60), (borde_b, H * .55), (borde_b, H)], fill=(235, 248, 255, 230), width=12)
    nubes(pil, pr, 3, H * .05, H * .25)
    return pil


def _f_trigal(rng, pr, suelo):
    img = gradiente(H, W, "#7cc0ea", "#f4e6c0")
    sol(img, W * .8, H * .14, 60, "#fff6d0", .5)
    capa(img, cresta(W, H * .55, 30, rng, 2), "#c9a24a")
    capa(img, cresta(W, suelo - 40, 15, rng, 2), "#d9b04a", ruido=6, rng=rng)
    pil = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(pil, "RGBA")
    nubes(pil, pr, 3, H * .06, H * .3)
    for _ in range(420):
        x = pr.uniform(0, W)
        y = pr.uniform(H * .56, H)
        h = 40 + (y - H * .56) * .25
        d.line([(x, y), (x + pr.uniform(-6, 6), y - h)], fill=col("#a8802a"), width=3)
        d.ellipse([x - 5, y - h - 14, x + 5, y - h + 4], fill=col("#e8c25a"))
    return pil


def _f_dentro_pez(rng, pr, suelo):
    img = gradiente(H, W, "#3a0d14", "#7a2a2a")
    pil = Image.fromarray(img.astype(np.uint8))
    d = ImageDraw.Draw(pil, "RGBA")
    for k in range(7):
        y = H * .08 + k * 200
        d.arc([-W * .4, y - 200, W * 1.4, y + 500], 200, 340, fill=(200, 120, 120, 120), width=26)
    d.rectangle([0, suelo - 10, W, H], fill=(60, 90, 80, 255))
    for _ in range(20):
        x, y = pr.uniform(0, W), pr.uniform(suelo, H)
        d.ellipse([x - 30, y - 6, x + 30, y + 6], fill=(120, 160, 150, 180))
    return pil


def _f_camino(rng, pr, suelo):
    img = gradiente(H, W, "#f2b46c", "#fde7b8")
    sol(img, W * .5, H * .26, 80, "#fff8dc", .9)
    capa(img, cresta(W, H * .55, 30, rng, 2), "#d99a55")
    capa(img, cresta(W, H * .6, 25, rng, 2), "#e2ac68", ruido=5, rng=rng)
    pil = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(pil, "RGBA")
    d.polygon([(W / 2 - 25, H * .6), (W / 2 + 25, H * .6), (W / 2 + 330, H), (W / 2 - 330, H)], fill=col("#f0d4a0"))
    for x in (120, 950):
        d.ellipse([x - 60, suelo - 40, x + 60, suelo + 10], fill=col("#a89a80"))
    return pil


def _f_patio(rng, pr, suelo):
    img = gradiente(H, W, "#0b1330", "#24305a")
    est = rng.integers(0, W, 120), rng.integers(0, int(H * .3), 120)
    img[est[1], est[0]] = 255
    pil = Image.fromarray(img.astype(np.uint8))
    d = ImageDraw.Draw(pil, "RGBA")
    _ladrillos(d, 0, H * .32, W, suelo, 90, 200, "#4e4a5a", "#34303e")
    d.rectangle([W * .62, H * .45, W * .82, suelo], fill=col("#1a1622"))
    d.pieslice([W * .62, H * .40, W * .82, H * .50], 180, 360, fill=col("#1a1622"))
    d.rectangle([0, suelo - 30, W, H], fill=col("#3a3646"))
    return pil


FONDOS_EXTRA = {"egipto": _f_egipto, "prision": _f_prision, "foso": _f_foso, "establo": _f_establo,
                "templo": _f_templo, "mar_tormenta": _f_mar_tormenta, "mar_rojo": _f_mar_rojo,
                "trigal": _f_trigal, "dentro_pez": _f_dentro_pez, "camino": _f_camino, "patio": _f_patio}


def pintar(pil, rng):
    """Toque pintado: suavizado + grano + vineta."""
    pil = pil.filter(ImageFilter.GaussianBlur(1.2))
    arr = np.asarray(pil).astype(float)
    arr += rng.normal(0, 4, arr.shape[:2])[..., None]
    yy, xx = np.mgrid[0:H, 0:W]
    v = 1 - 0.28 * (((xx - W / 2) / (W * .75)) ** 2 + ((yy - H / 2) / (H * .75)) ** 2)
    arr *= np.clip(v, 0.6, 1)[..., None]
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))



def fondo(nombre, semilla):
    """Devuelve (imagen PIL RGB, y_del_suelo)."""
    rng = np.random.default_rng(semilla)
    pr = random.Random(semilla)
    h, w = H, W
    suelo = int(H * 0.80)
    if Path(nombre).suffix.lower() in (".png", ".jpg", ".jpeg", ".webp"):
        im = Image.open(nombre).convert("RGB")
        k = max(W / im.width, H / im.height)
        im = im.resize((int(im.width * k + 1), int(im.height * k + 1)), Image.LANCZOS)
        l, t = (im.width - W) // 2, (im.height - H) // 2
        return im.crop((l, t, l + W, t + H)), suelo
    n = nombre
    if n in FONDOS_EXTRA:
        return pintar(FONDOS_EXTRA[n](rng, pr, suelo), rng), suelo
    if n == "noche":
        img = gradiente(h, w, "#0b1330", "#2a3a6a")
        estrellas = rng.integers(0, w, 260), rng.integers(0, int(h * .6), 260)
        img[estrellas[1], estrellas[0]] = 255
        sol(img, w * .75, h * .16, 55, "#f4f0d8", .35)
        capa(img, cresta(w, h * .66, 40, rng), "#1d2748")
        capa(img, cresta(w, suelo - 25, 18, rng, 3), "#24331f", ruido=6, rng=rng)
    elif n == "desierto":
        img = gradiente(h, w, "#f6b56b", "#fde7b5")
        sol(img, w * .3, h * .22, 75, "#fff4d0", .6)
        capa(img, cresta(w, h * .62, 35, rng, 2), "#e2a35e")
        capa(img, cresta(w, h * .70, 30, rng, 2), "#d98f4a")
        capa(img, cresta(w, suelo - 30, 20, rng, 2), "#e8b26a", ruido=7, rng=rng)
    elif n == "mar":
        img = gradiente(h, w, "#5fa8de", "#cfe8f7")
        sol(img, w * .7, h * .2, 60, "#fff8de", .4)
        mar = int(h * .58)
        img[mar:] = gradiente(h - mar, w, "#2f7fb6", "#1b4f80")
        for k in range(40):
            y = rng.integers(mar + 10, suelo)
            x = rng.integers(0, w - 80)
            img[y:y + 3, x:x + rng.integers(30, 90)] = [200, 230, 245]
        capa(img, cresta(w, suelo + 10, 15, rng, 2), "#e6cf9a", ruido=6, rng=rng)
    elif n == "cielo":
        img = gradiente(h, w, "#ffe9a8", "#ffffff")
        sol(img, w * .5, h * .12, 90, "#fff6cf", .9)
        capa(img, cresta(w, suelo, 25, rng, 3), "#fdfbf5")
    elif n == "palacio":
        img = gradiente(h, w, "#c99a63", "#8a5a33")
        img[suelo - 40:] = gradiente(h - suelo + 40, w, "#7a4a2a", "#4e2d18")
    elif n == "montana":
        img = gradiente(h, w, "#6b7fa8", "#d8d0c0")
        xs = np.arange(w)
        pico = h * .25 + np.abs(xs - w * .5) * 1.25
        capa(img, pico, "#7b6a5a")
        capa(img, cresta(w, suelo - 40, 25, rng, 3), "#9c8a6a", ruido=6, rng=rng)
    elif n == "jardin":
        img = gradiente(h, w, "#8fd0f0", "#e8f6e0")
        capa(img, cresta(w, h * .6, 40, rng, 3), "#7fb36a")
        capa(img, cresta(w, suelo - 30, 20, rng, 3), "#5c9a48", ruido=6, rng=rng)
    elif n == "tormenta":
        img = gradiente(h, w, "#2f3440", "#6a7180")
        capa(img, cresta(w, h * .64, 40, rng), "#3d4652")
        capa(img, cresta(w, suelo - 30, 20, rng, 3), "#3e4a35", ruido=6, rng=rng)
    elif n == "ciudad":
        img = gradiente(h, w, "#8cc4e8", "#f3e2c0")
        sol(img, w * .8, h * .15, 55, "#fff4d0", .4)
        capa(img, cresta(w, suelo - 30, 8, rng, 2), "#d8b98a", ruido=6, rng=rng)
    else:  # "valle" / "campo" por defecto
        img = gradiente(h, w, "#6fb2e6", "#e3f1f7")
        sol(img, w * .78, h * .14, 60, "#fff7da", .45)
        capa(img, cresta(w, h * .56, 45, rng), "#9fb7c4")
        capa(img, cresta(w, h * .64, 40, rng), "#8aa978")
        verde = "#7ead55" if n == "campo" else "#a9a265"
        capa(img, cresta(w, suelo - 30, 22, rng, 3), verde, ruido=6, rng=rng)
    pil = Image.fromarray(np.clip(img, 0, 255).astype(np.uint8))
    d = ImageDraw.Draw(pil, "RGBA")
    if n in ("valle", "campo", "jardin", "desierto", "montana", "ciudad", "mar"):
        nubes(pil, pr, 3, H * .08, H * .35)
    if n == "jardin":
        for x in (120, 380, 760, 980):
            arbol(d, x, suelo - 30, 1.5, pr, "#3f8a3a")
            for _ in range(5):
                fx, fy = x + pr.uniform(-60, 60) * 1.5, suelo - 30 - 230 + pr.uniform(-30, 60)
                d.ellipse([fx - 10, fy - 10, fx + 10, fy + 10], fill=col("#d83a2a"))
    if n == "campo":
        for x in (90, 960):
            arbol(d, x, int(H * .66), 1.0, pr)
    if n == "desierto":
        palmera(d, 900, suelo - 60, 1.3)
    if n == "ciudad":
        for i, x in enumerate(range(-40, W, 210)):
            hh = 230 + (i % 3) * 70
            casa(d, x, suelo - 30, 190, hh, ["#e7cfa0", "#d9b27a", "#efdcb8"][i % 3])
    if n == "palacio":
        for x in (90, 380, 700, 990):
            d.rectangle([x - 45, H * .12, x + 45, suelo - 40], fill=col("#e8dcc0"), outline=col("#b8a77f"), width=6)
            d.rectangle([x - 60, H * .12 - 30, x + 60, H * .12], fill=col("#d8c8a0"))
        d.rectangle([0, 0, W, H * .1], fill=col("#5a1f1f"))
        for x in range(0, W, 90):
            d.pieslice([x, H * .1 - 45, x + 90, H * .1 + 45], 0, 180, fill=col("#7a2a2a"))
        d.rectangle([W * .32, suelo - 40, W * .68, H], fill=col("#9a2a2a", 230))
    if n == "cielo":
        for _ in range(6):
            x = pr.uniform(0, W)
            y = pr.uniform(H * .3, H * .75)
            for _ in range(8):
                rx, ry = pr.uniform(80, 150), pr.uniform(40, 70)
                dx, dy = pr.uniform(-140, 140), pr.uniform(-25, 25)
                d.ellipse([x + dx - rx, y + dy - ry, x + dx + rx, y + dy + ry], fill=(255, 255, 255, 235))
    return pintar(pil, rng), suelo


def rayos_luz():
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    cx, cy = W / 2, -200
    for a in range(-60, 61, 12):
        r = math.radians(a + 90)
        r2 = math.radians(a + 95)
        d.polygon([(cx, cy), (cx + math.cos(r) * 3000, cy + math.sin(r) * 3000),
                   (cx + math.cos(r2) * 3000, cy + math.sin(r2) * 3000)], fill=(255, 236, 160, 60))
    return img.filter(ImageFilter.GaussianBlur(25))

# ======================================================================
#  Voz en off
#   - Piper (codigo abierto, gratis, funciona SIN internet)  <- por defecto
#   - edge-tts (voces de Microsoft, gratis, necesita internet) <- opcional
# ======================================================================

VOZ_NARRADOR = "es_MX-claude-high"
CARPETA_VOCES = Path(__file__).resolve().parent / "voces"
URL_VOCES = "https://huggingface.co/rhasspy/piper-voices/resolve/main"
_modelos = {}


class ErrorVoz(Exception):
    pass


def es_voz_edge(nombre):
    return nombre.endswith("Neural")


def asegurar_modelo(nombre):
    """Descarga la voz de Piper la primera vez (unos 60-110 MB) y la guarda en /voces."""
    CARPETA_VOCES.mkdir(exist_ok=True)
    onnx = CARPETA_VOCES / f"{nombre}.onnx"
    js = CARPETA_VOCES / f"{nombre}.onnx.json"
    if onnx.exists() and js.exists():
        return onnx
    try:
        idioma, hablante, calidad = nombre.split("-")
    except ValueError:
        raise ErrorVoz(f"Nombre de voz no valido: {nombre} (ejemplo: es_MX-claude-high)")
    base = f"{URL_VOCES}/{idioma.split('_')[0]}/{idioma}/{hablante}/{calidad}/{nombre}"
    import urllib.request
    for url, destino in ((base + ".onnx.json", js), (base + ".onnx", onnx)):
        tmp = destino.with_suffix(destino.suffix + ".parcial")
        print(f"\n  Descargando voz {destino.name} (solo la primera vez)...")
        try:
            with urllib.request.urlopen(url, timeout=60) as r, open(tmp, "wb") as f:
                total = int(r.headers.get("Content-Length", 0))
                hecho = 0
                while True:
                    b = r.read(1 << 20)
                    if not b:
                        break
                    f.write(b)
                    hecho += len(b)
                    if total:
                        print(f"\r    {hecho * 100 // total}%", end="", flush=True)
            tmp.replace(destino)
        except Exception as ex:
            tmp.unlink(missing_ok=True)
            raise ErrorVoz(f"No pude descargar la voz '{nombre}' ({ex}). "
                           "Revisa tu internet (solo hace falta la primera vez).")
    print()
    return onnx


def _piper(texto, nombre, velocidad):
    try:
        from piper import PiperVoice
    except ImportError:
        raise ErrorVoz("Falta Piper. Ejecuta: pip install -r requirements.txt")
    onnx = asegurar_modelo(nombre)
    if nombre not in _modelos:
        _modelos[nombre] = PiperVoice.load(str(onnx))
    voz = _modelos[nombre]
    largo = 1.0 / max(0.5, float(velocidad))
    buf = io.BytesIO()
    with wave.open(buf, "wb") as wf:
        if hasattr(voz, "synthesize_wav"):   # piper-tts 1.3 o mas nuevo
            from piper import SynthesisConfig
            voz.synthesize_wav(texto, wf, syn_config=SynthesisConfig(length_scale=largo))
        else:                                # piper-tts 1.2
            voz.synthesize(texto, wf, length_scale=largo)
    buf.seek(0)
    with wave.open(buf, "rb") as wf:
        sr = wf.getframerate()
        a = np.frombuffer(wf.readframes(wf.getnframes()), dtype=np.int16).astype(np.float32) / 32768
    return a, sr


def procesar_audio(a, sr, semitonos=0.0):
    """Cambia el tono (voz mas grave o aguda) y lleva el audio a SR con ffmpeg."""
    filtros = []
    if semitonos:
        f = 2 ** (semitonos / 12)
        filtros += [f"asetrate={int(sr * f)}", f"aresample={SR}", f"atempo={1 / f:.4f}"]
    else:
        filtros += [f"aresample={SR}"]
    pcm = (np.clip(a, -1, 1) * 32767).astype(np.int16).tobytes()
    r = subprocess.run(["ffmpeg", "-v", "error", "-f", "s16le", "-ar", str(sr), "-ac", "1", "-i", "-",
                        "-af", ",".join(filtros), "-f", "s16le", "-ac", "1", "-ar", str(SR), "-"],
                       input=pcm, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if r.returncode != 0:
        raise ErrorVoz("ffmpeg no pudo procesar el audio: " + r.stderr.decode(errors="replace")[-300:])
    return np.frombuffer(r.stdout, dtype=np.int16).astype(np.float32) / 32768


async def _edge(texto, voz, tono, vel, mp3):
    import edge_tts
    try:
        com = edge_tts.Communicate(texto, voz, rate=vel, pitch=tono, boundary="WordBoundary")
    except TypeError:
        com = edge_tts.Communicate(texto, voz, rate=vel, pitch=tono)
    palabras = []
    with open(mp3, "wb") as f:
        async for ch in com.stream():
            if ch["type"] == "audio":
                f.write(ch["data"])
            elif ch["type"] == "WordBoundary":
                palabras.append({"start": ch["offset"] / 1e7, "end": (ch["offset"] + ch["duration"]) / 1e7,
                                 "text": ch["text"]})
    return palabras


def decodificar(mp3):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(mp3), "-f", "s16le", "-ac", "1", "-ar", str(SR), "-"],
                       stdout=subprocess.PIPE, check=True)
    return np.frombuffer(r.stdout, dtype=np.int16).astype(np.float32) / 32768


def palabras_estimadas(texto, dur, audio=None):
    """Reparte las palabras en el tiempo. Si hay audio, usa solo la parte con voz
    y da mas tiempo a las pausas de comas y puntos."""
    ws = texto.split()
    if not ws:
        return []
    t0, t1 = 0.15, dur - 0.15
    if audio is not None and len(audio) > SR // 10:
        blk = SR // 100
        env = np.sqrt(np.mean(audio[:len(audio) // blk * blk].reshape(-1, blk) ** 2, axis=1))
        voz = np.where(env > max(env.max() * 0.06, 1e-4))[0]
        if len(voz):
            t0, t1 = voz[0] / 100, (voz[-1] + 1) / 100
    pesos = []
    for w in ws:
        p = len(w) + 2
        if w[-1:] in ",;:":
            p += 4
        elif w[-1:] in ".!?":
            p += 7
        pesos.append(p)
    tot, t, res = sum(pesos), t0, []
    for w, p in zip(ws, pesos):
        d = (t1 - t0) * p / tot
        res.append({"start": t, "end": t + min(d, (len(w) + 2) / tot * (t1 - t0) * 1.1), "text": w})
        t += d
    return res


def _semitonos(v):
    """Acepta -4, "-4" o el formato viejo "-30Hz"."""
    if isinstance(v, (int, float)):
        return float(v)
    v = str(v).strip()
    if v.lower().endswith("hz"):
        return float(v[:-2]) / 7.5
    try:
        return float(v)
    except ValueError:
        return 0.0


def _velocidad(v):
    """Acepta 1.1 o el formato viejo "+10%"."""
    if isinstance(v, (int, float)):
        return float(v)
    v = str(v).strip()
    if v.endswith("%"):
        return 1 + float(v[:-1]) / 100
    try:
        return float(v)
    except ValueError:
        return 1.0


def preparar_voz(escenas, personajes, carpeta, sin_voz, voz_narr, vel_narr=1.0, pausa_def=0.35):
    """Genera el audio de cada escena. Devuelve lista de (audio np, palabras, duracion)."""
    res = []
    for i, e in enumerate(escenas):
        texto = e.get("texto", "").strip()
        quien = e.get("habla")
        conf = (personajes.get(quien, {}) or {}).get("voz") or {}
        nombre = conf.get("nombre", voz_narr)
        audio, palabras = None, []
        if texto and not sin_voz:
            try:
                if es_voz_edge(nombre):
                    mp3 = carpeta / f"_voz_{TMP}_{i:02d}.mp3"
                    tono = conf.get("tono", "+0Hz")
                    vel = conf.get("velocidad", "+0%")
                    if isinstance(tono, (int, float)):
                        tono = f"{int(tono * 7.5):+d}Hz"
                    if isinstance(vel, (int, float)):
                        vel = f"{int((vel - 1) * 100):+d}%"
                    palabras = asyncio.run(_edge(texto, nombre, tono, vel, mp3))
                    audio = decodificar(mp3)
                    mp3.unlink(missing_ok=True)
                else:
                    vel = _velocidad(conf["velocidad"]) * vel_narr if "velocidad" in conf else vel_narr
                    a, sr = _piper(texto, nombre, vel)
                    audio = procesar_audio(a, sr, _semitonos(conf.get("tono", 0)))
            except ErrorVoz as ex:
                sys.exit(f"\n[ERROR] {ex}")
            except Exception as ex:
                sys.exit(f"\n[ERROR] No pude crear la voz de la escena {i + 1} con '{nombre}': {ex}\n"
                         "Si quieres el video sin voz usa --sin-voz")
            if audio is None or len(audio) < SR // 10:
                sys.exit(f"\n[ERROR] La voz de la escena {i + 1} salio vacia.")
            dur = len(audio) / SR + e.get("pausa", pausa_def)
            if not palabras:
                palabras = palabras_estimadas(texto, len(audio) / SR, audio)
        else:
            n = len(texto.split())
            dur = e.get("duracion", max(2.0, n * 0.36 + 0.6))
            palabras = palabras_estimadas(texto, dur)
        dur = max(dur, e.get("duracion_min", 0))
        res.append((audio, palabras, dur))
        print(f"\r  Voz escena {i + 1}/{len(escenas)}", end="", flush=True)
    print()
    return res

# ======================================================================
#  Efectos de sonido y musica de fondo (generados aqui: sin derechos de autor)
# ======================================================================

def _ruido_banda(n, f_lo, f_hi, rng):
    x = rng.normal(0, 1, n)
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(n, 1 / SR)
    X[(f < f_lo) | (f > f_hi)] = 0
    y = np.fft.irfft(X, n)
    return y / (np.abs(y).max() + 1e-9)


def sfx_whoosh(rng, dur=0.5):
    n = int(SR * dur)
    t = np.linspace(0, 1, n)
    y = _ruido_banda(n, 400, 4500, rng) * np.sin(np.pi * t) ** 2
    return (y * 0.55).astype(np.float32)


def sfx_golpe(rng, dur=0.9):
    n = int(SR * dur)
    t = np.arange(n) / SR
    frec = 70 * np.exp(-t * 3) + 38
    fase = 2 * np.pi * np.cumsum(frec) / SR
    y = np.sin(fase) * np.exp(-t * 5)
    y += _ruido_banda(n, 30, 900, rng) * np.exp(-t * 9) * 0.6
    return (y / (np.abs(y).max() + 1e-9) * 0.9).astype(np.float32)


def sfx_pop(rng, dur=0.22):
    n = int(SR * dur)
    t = np.arange(n) / SR
    fase = 2 * np.pi * np.cumsum(600 + 900 * t / dur) / SR
    y = (np.sin(fase) + 0.4 * np.sin(2 * fase)) * np.exp(-t * 18)
    return (y / (np.abs(y).max() + 1e-9) * 0.5).astype(np.float32)


def musica_auto(total, rng, energica=False):
    """Fondo musical suave: acordes Rem - Sib - Fa - Do con un pulso grave."""
    n = int(SR * (total + 1))
    t = np.arange(n) / SR
    y = np.zeros(n, dtype=np.float64)
    acordes = [(146.83, 174.61, 220.00), (116.54, 146.83, 174.61), (174.61, 220.00, 261.63), (130.81, 164.81, 196.00)]
    dur_ac = 4.0
    for k in range(int(total / dur_ac) + 2):
        a0 = k * dur_ac
        i0, i1 = int(max(0, a0 - 0.5) * SR), min(n, int((a0 + dur_ac + 0.5) * SR))
        if i0 >= n:
            break
        tt = t[i0:i1] - a0
        env = np.clip((tt + 0.5) / 0.8, 0, 1) * np.clip((dur_ac + 0.5 - tt) / 0.8, 0, 1)
        for fr in acordes[k % 4]:
            for det in (0.998, 1.002):
                y[i0:i1] += np.sin(2 * np.pi * fr * det * tt) * env * 0.12
        y[i0:i1] += np.sin(2 * np.pi * acordes[k % 4][0] / 2 * tt) * env * 0.18
    paso = 0.5 if energica else 1.0
    for b in np.arange(0, total, paso):
        i0 = int(b * SR)
        m = min(n - i0, int(SR * 0.35))
        tt = np.arange(m) / SR
        y[i0:i0 + m] += np.sin(2 * np.pi * (55 + 40 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 12) * (0.35 if energica else 0.22)
    y *= np.clip(t / 1.5, 0, 1) * np.clip((total - t) / 1.5, 0, 1)
    return (y / (np.abs(y).max() + 1e-9)).astype(np.float32)


def mezclar_sonidos(pista, escenas, inicios, voces, total, h):
    """Agrega whoosh entre escenas, golpes en flash/temblor/rayo, pop en rotulos y musica."""
    rng = np.random.default_rng(7)
    out = pista.copy()

    def poner(sonido, seg, vol):
        i0 = int(max(0, seg) * SR)
        if i0 >= len(out):
            return
        m = min(len(sonido), len(out) - i0)
        out[i0:i0 + m] += sonido[:m] * vol

    if h.get("efectos_sonido", True):
        for k, (e, t0, (_, _, d)) in enumerate(zip(escenas, inicios, voces)):
            if k > 0:
                poner(sfx_whoosh(rng), t0 - 0.25, 0.35)
            if e.get("rotulo"):
                poner(sfx_pop(rng), t0 + 0.1, 0.45)
            for ef in e.get("efectos", []):
                tipo = ef.get("tipo")
                if tipo in ("flash", "temblor", "rayo", "abrir_mar", "cerrar_mar") or \
                        (tipo == "fuego" and ef.get("crece")):
                    poner(sfx_golpe(rng), t0 + ef.get("inicio", 0) * d, 0.5)
                elif tipo == "proyectil":
                    poner(sfx_whoosh(rng, 0.35), t0 + ef.get("inicio", 0) * d, 0.4)
    if h.get("musica") == "auto":
        mus = musica_auto(total, rng, h.get("formato") == "corto")
        m = min(len(mus), len(out))
        out[:m] += mus[:m] * h.get("volumen_musica", 0.12)
    pico = np.abs(out).max()
    if pico > 0.98:
        out *= 0.98 / pico
    return out

# ======================================================================
#  Subtitulos (ASS, palabra por palabra)
# ======================================================================

def ts(t):
    t = max(0, t)
    return f"{int(t // 3600)}:{int(t % 3600 // 60):02d}:{t % 60:05.2f}"


def limpiar(t):
    return re.sub(r"[{}\\]", "", t)


def crear_ass(todas, gancho, final, total, resaltar, ruta, rotulos=()):
    amarillo = "&H0000E6FF&"
    claves = {limpiar(r).upper().strip(".,;:!?¡¿") for r in resaltar}
    cab = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,Archivo Black,76,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,1,0,0,0,100,100,0,0,1,7,3,2,70,70,300,1
Style: Gancho,Archivo Black,80,&H00FFFFFF,&H00FFFFFF,&H00000000,&H90000000,1,0,0,0,100,100,0,0,1,8,4,8,60,60,190,1
Style: Rotulo,Anton,150,&H0000E6FF,&H00FFFFFF,&H00000000,&H90000000,0,0,0,0,100,100,2,0,1,9,5,8,60,60,400,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lineas = []

    def tinta(w):
        return (r"{\c" + amarillo + "}" + w + r"{\r}") if w.strip(".,;:!?¡¿") in claves else w

    if gancho:
        txt = " ".join(tinta(w) for w in limpiar(gancho).upper().split())
        lineas.append(rf"Dialogue: 1,{ts(0.1)},{ts(3.6)},Gancho,,0,0,0,,"
                      rf"{{\fad(100,250)\fscx60\fscy60\t(0,200,\fscx108\fscy108)\t(200,320,\fscx100\fscy100)}}{txt}")
    if final:
        txt = " ".join(tinta(w) for w in limpiar(final).upper().split())
        lineas.append(rf"Dialogue: 1,{ts(max(0, total - 3.2))},{ts(total)},Gancho,,0,0,0,,{{\fad(200,0)}}{txt}")
    for r0, r1, txt in rotulos:
        lineas.append(rf"Dialogue: 2,{ts(r0 + 0.1)},{ts(r1 - 0.1)},Rotulo,,0,0,0,,"
                      rf"{{\fad(60,150)\fscx30\fscy30\frz-6\t(0,180,\fscx118\fscy118\frz3)\t(180,320,\fscx100\fscy100\frz0)}}"
                      + limpiar(txt).upper())
    pal = [dict(p, text=limpiar(p["text"]).upper()) for p in todas if p["text"].strip()]
    grupos, g = [], []
    for p in pal:
        if g and (len(g) >= 3 or p["start"] - g[-1]["end"] > 0.5 or g[-1]["text"][-1:] in ".,!?;:"
                  or p.get("tope") != g[-1].get("tope")):
            grupos.append(g)
            g = []
        g.append(p)
    if g:
        grupos.append(g)
    for gi, g in enumerate(grupos):
        fin_g = grupos[gi + 1][0]["start"] if gi + 1 < len(grupos) else g[-1]["end"] + 0.5
        fin_g = min(fin_g, g[-1]["end"] + 0.7)
        for k, p in enumerate(g):
            a = p["start"]
            b = g[k + 1]["start"] if k + 1 < len(g) else fin_g
            b = min(b, p.get("tope", b))
            partes = []
            for q, o in enumerate(g):
                if q == k:
                    partes.append(r"{\c" + amarillo + r"\fscx92\fscy92\t(0,90,\fscx122\fscy122)}" + o["text"] + r"{\r}")
                else:
                    partes.append(tinta(o["text"]))
            lineas.append(f"Dialogue: 0,{ts(a)},{ts(b)},Sub,,0,0,0,,{' '.join(partes)}")
    Path(ruta).write_text(cab + "\n".join(lineas) + "\n", encoding="utf-8")

# ======================================================================
#  Animales (se usan como personajes: "tipo": "leon", "cerdo", ...)
# ======================================================================

def _patas(L, xs, y0, largo, po, g=1.3):
    for k, x in enumerate(xs):
        a = math.radians(po["pierna"] * (1 if k % 2 else -1))
        L.linea([(x, y0), (x + math.sin(a) * largo, y0 + math.cos(a) * largo)], g)


def _ojos(L, po, cx, cy, sep=34, r=15):
    for ex in (cx, cx + sep):
        if po["ojos_cerrados"]:
            L.arco(ex, cy, r * .8, r * .45, 0, 180, 0.7)
        else:
            L.elipse(ex, cy, r, r * 1.15, col("#ffffff"), g=0.7)
            L.elipse(ex + 4, cy + 2, r * .45, r * .45, TINTA, borde=None)


def dibujar_leon(L, c, po, t, boca):
    ac = po.get("acostado")
    by = -75 if ac else -165
    pelaje, melena = col(c.get("color") or "#d9a35a"), col(c.get("melena") or "#9a5a24")
    if not ac:
        _patas(L, (-120, -80, 85, 125), by + 30, 140, po, 1.9)
    L.linea([(-165, by - 10), (-225, by - 60), (-250, by - 120)], 1.1)
    L.elipse(-252, by - 128, 18, 22, melena, g=0.7)
    L.elipse(0, by, 180, 78, pelaje, g=1.2)
    if ac:
        L.elipse(-90, -20, 60, 22, pelaje, g=1.0)
        L.elipse(110, -20, 60, 22, pelaje, g=1.0)
    hx, hy = 175, by - (55 if ac else 85)
    pts = [(hx + (125 if i % 2 else 100) * math.cos(2 * math.pi * i / 22),
            hy + (125 if i % 2 else 100) * math.sin(2 * math.pi * i / 22)) for i in range(22)]
    if c.get("melena") is not False:
        L.forma(pts, melena, g=1.0)
    L.elipse(hx, hy, 74, 70, pelaje, g=1.0)
    _ojos(L, po, hx - 8, hy - 18, 42, 14)
    L.forma([(hx + 22, hy + 12), (hx + 48, hy + 12), (hx + 35, hy + 28)], TINTA, g=0.5)
    if boca > 0.1:
        L.elipse(hx + 35, hy + 50, 26 + 6 * boca, 8 + 20 * boca, col("#6a1e1e"), g=0.8)
        for dx in (-14, 14):
            L.forma([(hx + 35 + dx - 5, hy + 38), (hx + 35 + dx + 5, hy + 38), (hx + 35 + dx, hy + 50)],
                    col("#ffffff"), g=0.3)
    else:
        L.arco(hx + 25, hy + 32, 11, 8, 20, 160, 0.6)
        L.arco(hx + 46, hy + 32, 11, 8, 20, 160, 0.6)


def dibujar_cerdo(L, c, po, t, boca):
    ac = po.get("acostado")
    by = -60 if ac else -110
    rosa = col(c.get("color") or "#f2a7b5")
    if not ac:
        _patas(L, (-70, -40, 45, 75), by + 30, 80, po, 1.4)
    L.arco(-125, by - 15, 16, 16, 0, 300, 0.7)
    L.elipse(0, by, 125, 70, rosa, g=1.1)
    hx, hy = 115, by - 30
    L.forma([(hx - 30, hy - 40), (hx - 10, hy - 80), (hx + 5, hy - 40)], rosa, g=0.8)
    L.elipse(hx, hy, 55, 52, rosa, g=1.0)
    _ojos(L, po, hx - 15, hy - 12, 30, 11)
    L.elipse(hx + 48, hy + 15, 22, 17, oscuro(rosa, .88), g=0.8)
    L.elipse(hx + 42, hy + 15, 4, 6, TINTA, borde=None)
    L.elipse(hx + 55, hy + 15, 4, 6, TINTA, borde=None)


def dibujar_carnero(L, c, po, t, boca):
    dibujar_oveja(L, dict(c, lana=c.get("lana") or "#e6ddcc"), po, t)
    for dx, s in ((95, 1),):
        pts = [(dx + 8 + 22 * math.cos(a) * (1 - a / 12), -135 + 22 * math.sin(a) * (1 - a / 12))
               for a in [i * .4 for i in range(18)]]
        L.linea(pts, 1.3, col("#8a6a3a"))


def dibujar_gallo(L, c, po, t, boca):
    _patas(L, (-10, 20), -60, 60, po, 0.8)
    for k, cc in enumerate(("#2f6b3a", "#b8402a", "#1f3f6a")):
        L.arco(-60, -150 + k * 18, 55, 70, 150, 290, 1.6, col(cc))
    L.elipse(0, -110, 62, 52, col(c.get("color") or "#c8552e"), g=1.0)
    hx, hy = 45, -185
    L.forma([(hx - 15, hy - 28), (hx - 5, hy - 55), (hx + 5, hy - 32), (hx + 15, hy - 55), (hx + 22, hy - 25)],
            col("#e02a2a"), g=0.7)
    L.elipse(hx, hy, 30, 30, col("#f4ead8"), g=0.9)
    L.elipse(hx + 8, hy - 6, 6, 6, TINTA, borde=None)
    ab = 10 * boca
    L.forma([(hx + 25, hy - 4 - ab / 2), (hx + 55, hy + 2), (hx + 25, hy + 6 + ab / 2)], col("#f2c230"), g=0.6)
    L.elipse(hx + 18, hy + 24, 8, 12, col("#e02a2a"), g=0.5)


def dibujar_burro(L, c, po, t, boca):
    gris = col(c.get("color") or "#9a948c")
    by = -150
    _patas(L, (-95, -60, 60, 95), by + 25, 125, po, 1.5)
    L.linea([(-140, by - 5), (-175, by + 50)], 0.9)
    L.elipse(0, by, 150, 62, gris, g=1.1)
    L.forma([(110, by - 30), (150, by - 130), (185, by - 115), (150, by - 10)], gris, g=1.0)
    hx, hy = 185, by - 130
    for dx in (-25, -5):
        L.elipse(hx + dx, hy - 70, 13, 45, gris, g=0.8, rot=-0.3)
    L.elipse(hx + 25, hy + 5, 60, 34, gris, g=1.0, rot=0.35)
    L.elipse(hx + 60, hy + 22, 22, 17, col("#d8d2c8"), g=0.6)
    _ojos(L, po, hx + 5, hy - 10, 26, 10)


ANIMALES = {"leon": dibujar_leon, "cerdo": dibujar_cerdo, "carnero": dibujar_carnero,
            "gallo": dibujar_gallo, "burro": dibujar_burro}

# ======================================================================
#  Objetos de escena ("cosas"): arca, barca, pez gigante, altar, tumba...
# ======================================================================

COSAS = {}


def cosa(nombre, ancho, alto):
    def deco(f):
        COSAS[nombre] = (ancho, alto, f)
        return f
    return deco


@cosa("arca", 1000, 640)
def _arca(L, o):
    madera, osc = col("#8b5a2b"), col("#5e3a1a")
    L.forma([(-490, -270), (490, -270), (410, -50), (330, 0), (-330, 0), (-410, -50)], madera, g=1.5)
    for k in range(1, 5):
        L.linea([(-480 + k * 18, -270 + k * 52), (480 - k * 18, -270 + k * 52)], 0.5, osc)
    L.forma([(-270, -270), (270, -270), (270, -450), (-270, -450)], col("#a06a35"), g=1.3)
    L.forma([(-310, -445), (310, -445), (0, -610)], osc, g=1.3)
    for x in (-160, 0, 160):
        L.forma([(x - 38, -340), (x + 38, -340), (x + 38, -400), (x - 38, -400)], col("#2a1a10"), g=0.8)
    if o.get("puerta"):
        L.forma([(-80, -270), (80, -270), (80, -120), (-80, -120)], col("#3a2412"), g=1.0)


@cosa("barca", 720, 540)
def _barca(L, o):
    L.forma([(-340, -160), (340, -160), (270, -25), (210, 0), (-210, 0), (-270, -25)], col("#7a4a25"), g=1.4)
    L.linea([(-330, -128), (330, -128)], 0.5, col("#4e2e14"))
    L.linea([(-300, -70), (300, -70)], 0.5, col("#4e2e14"))
    if o.get("vela", True):
        L.linea([(40, -160), (40, -520)], 1.5, col("#5a3518"))
        L.forma([(40, -500), (40, -200), (230, -215)], col("#efe6d2"), g=1.0)


@cosa("pez_gigante", 1050, 600)
def _pez(L, o):
    azul = col(o.get("color", "#4f7fa8"))
    L.forma([(-380, -300), (-520, -460), (-470, -300), (-520, -130)], oscuro(azul, .85), g=1.2)
    L.elipse(0, -300, 440, 240, azul, g=1.4, n=48)
    L.elipse(30, -210, 330, 105, col("#b9d3e4"), borde=None)
    L.forma([(-40, -520), (60, -640), (140, -515)], oscuro(azul, .85), g=1.0)
    L.forma([(-20, -260), (-110, -170), (40, -200)], oscuro(azul, .85), g=0.9)
    L.elipse(270, -380, 46, 50, col("#ffffff"), g=1.0)
    L.elipse(285, -375, 20, 22, TINTA, borde=None)
    if o.get("abierta"):
        L.forma([(445, -340), (250, -290), (445, -190)], col("#5a1420"), g=1.1)
    else:
        L.arco(380, -300, 70, 30, 100, 200, 1.0)
    for k in range(3):
        L.arco(150 - k * 30, -300, 30, 70, -60, 60, 0.6, oscuro(azul, .7))


@cosa("altar", 380, 360)
def _altar(L, o):
    piedra = col("#9a9488")
    for fila, (y, n) in enumerate(((-55, 4), (-115, 4), (-170, 3))):
        ancho = 330 - fila * 40
        for i in range(n):
            x0 = -ancho / 2 + i * ancho / n
            L.forma([(x0 + 4, y + 55), (x0 + ancho / n - 4, y + 55), (x0 + ancho / n - 4, y + 2), (x0 + 4, y + 2)],
                    mezcla(piedra, "#6e685e", (i + fila) % 2 * .3), g=0.8)
    for k in range(3):
        L.elipse(0, -200 - k * 22, 135 - k * 10, 13, col("#7a4a25"), g=0.8)
    if o.get("sacrificio", True):
        L.elipse(0, -275, 80, 34, col("#e6ddcc"), g=0.9)


@cosa("pesebre", 380, 280)
def _pesebre(L, o):
    madera = col("#8b5a2b")
    L.linea([(-150, 0), (-90, -140)], 1.2, madera)
    L.linea([(150, 0), (90, -140)], 1.2, madera)
    L.linea([(-90, 0), (-150, -140)], 1.2, madera)
    L.linea([(90, 0), (150, -140)], 1.2, madera)
    L.forma([(-170, -165), (170, -165), (130, -75), (-130, -75)], madera, g=1.2)
    pts = [(-165 + i * 22, -165 - (18 if i % 2 else 4)) for i in range(16)]
    L.forma([(-165, -160)] + pts + [(165, -160)], col("#e8c55a"), g=0.7)
    if o.get("bebe", True):
        L.elipse(-15, -195, 85, 38, col("#f4efe4"), g=1.0)
        L.elipse(75, -205, 36, 34, col("#f1d2b0"), g=1.0)
        L.arco(68, -208, 8, 5, 0, 180, 0.5)
        L.arco(88, -208, 8, 5, 0, 180, 0.5)
        if o.get("aureola", True):
            L.elipse(75, -210, 52, 52, None, borde=col("#ffd34d"), g=1.0)


@cosa("tumba", 940, 720)
def _tumba(L, o):
    roca = col("#8f877a")
    pts = [(-460, 0), (-440, -300), (-380, -520), (-220, -660), (0, -700), (220, -650), (380, -520),
           (450, -300), (460, 0)]
    L.forma(pts, roca, g=1.4)
    L.forma([(-150, 0), (-150, -260), (-110, -360), (0, -400), (110, -360), (150, -260), (150, 0)],
            col("#1c1612"), g=1.2)
    for x, y in ((-300, -420), (260, -480), (330, -200), (-330, -150)):
        L.arco(x, y, 45, 20, 200, 340, 0.6, oscuro(roca, .7))


@cosa("piedra", 360, 340)
def _piedra(L, o):
    L.elipse(0, -165, 165, 165, col("#a39b8e"), g=1.4)
    L.elipse(0, -165, 120, 120, None, borde=oscuro("#a39b8e", .75), g=0.7)
    L.linea([(-60, -230), (20, -160)], 0.5, oscuro("#a39b8e", .7))


@cosa("columna", 230, 800)
def _columna(L, o):
    pie = col("#d8ceb4")
    L.forma([(-100, 0), (100, 0), (100, -50), (-100, -50)], pie, g=1.1)
    L.forma([(-70, -50), (70, -50), (62, -690), (-62, -690)], col("#e6dcc4"), g=1.2)
    for x in (-35, 0, 35):
        L.linea([(x, -70), (x * .9, -670)], 0.5, oscuro(pie, .8))
    L.forma([(-110, -690), (110, -690), (110, -760), (-110, -760)], pie, g=1.1)


@cosa("canasta", 240, 170)
def _canasta(L, o):
    for k in range(3):
        L.elipse(-50 + k * 50, -105, 38, 26, col("#d39b52"), g=0.8)
    L.forma([(-110, -100), (110, -100), (85, 0), (-85, 0)], col("#a8763a"), g=1.1)
    for k in range(1, 4):
        L.linea([(-105 + k * 4, -100 + k * 25), (105 - k * 4, -100 + k * 25)], 0.4, col("#6e4a20"))


@cosa("panes_peces", 300, 120)
def _panes(L, o):
    L.elipse(0, -20, 140, 22, col("#efe6d2"), g=0.8)
    for k in range(5):
        L.elipse(-100 + k * 42, -50, 26, 18, col("#d39b52"), g=0.7)
    for k in range(2):
        L.elipse(-30 + k * 80, -85, 38, 14, col("#9aa8b4"), g=0.7)
        L.forma([(-68 + k * 80, -85), (-90 + k * 80, -100), (-90 + k * 80, -70)], col("#9aa8b4"), g=0.6)


@cosa("multitud", 1400, 460)
def _multitud(L, o):
    rng = random.Random(o.get("semilla", 5))
    tipo = o.get("variante", "pueblo")
    paleta = {"pueblo": ["#c97b4a", "#5b8fd6", "#d9c7a3", "#8b6b3d", "#7a3fa0", "#a0522d", "#e8e0d0", "#6a8a4a"],
              "egipcios": ["#f2efe6", "#e8e2d2"], "soldados": ["#8a6a3a", "#7a5a2a", "#9a7a4a"],
              "filisteos": ["#8a6a3a", "#9a5a3a"]}[tipo]
    for fila in range(3):
        y = -fila * 70
        n = 9 - fila
        for i in range(n):
            x = -640 + (i + rng.uniform(.1, .9)) * 1280 / n + fila * 30
            s = 1 - fila * .12
            tun = col(rng.choice(paleta))
            L.forma([(x - 38 * s, y - 150 * s), (x + 38 * s, y - 150 * s), (x + 55 * s, y), (x - 55 * s, y)], tun, g=0.8)
            piel = col(rng.choice(["#f1d2b0", "#d9a77c", "#c08a5a", "#e8c39e"]))
            L.elipse(x, y - 200 * s, 48 * s, 46 * s, piel, g=0.8)
            if tipo == "egipcios":
                L.forma([(x - 52 * s, y - 210 * s), (x + 52 * s, y - 210 * s), (x + 60 * s, y - 150 * s),
                         (x - 60 * s, y - 150 * s), (x, y - 255 * s)], col("#2f5fa8"), g=0.6)
            elif tipo in ("soldados", "filisteos"):
                L.forma([(x + (50 * s) * math.cos(math.radians(a)), y - 215 * s + (50 * s) * math.sin(math.radians(a)))
                         for a in range(180, 361, 20)], col("#a8823e"), g=0.6)
                L.linea([(x + 45 * s, y - 40 * s), (x + 45 * s, y - 330 * s)], 0.7, col("#6e4a2a"))
            else:
                L.elipse(x + 14 * s, y - 205 * s, 6 * s, 6 * s, TINTA, borde=None)
                L.elipse(x - 10 * s, y - 205 * s, 6 * s, 6 * s, TINTA, borde=None)
                if rng.random() < .4:
                    L.forma([(x + (52 * s) * math.cos(math.radians(a)), y - 200 * s + (52 * s) * math.sin(math.radians(a)))
                             for a in range(170, 371, 20)] + [(x - 60 * s, y - 150 * s)], tun, g=0.6)


@cosa("trono", 380, 560)
def _trono(L, o):
    oro = col("#d9a62e")
    L.forma([(-150, 0), (-150, -520), (-100, -560), (100, -560), (150, -520), (150, 0)], oro, g=1.3)
    L.forma([(-110, -230), (110, -230), (110, -500), (-110, -500)], col("#9a2a2a"), g=1.0)
    L.forma([(-175, -200), (175, -200), (175, -250), (-175, -250)], oro, g=1.1)


@cosa("estrella", 360, 360)
def _estrella(L, o):
    for r, a in ((170, 50), (120, 90)):
        L.elipse(0, -180, r, r, col("#fff3b0", a), borde=None)
    pts = []
    for i in range(16):
        rr = 150 if i % 2 == 0 else 45
        if i % 4 == 2:
            rr = 95
        a = math.pi * 2 * i / 16 - math.pi / 2
        pts.append((rr * math.cos(a), -180 + rr * math.sin(a)))
    L.forma(pts, col("#ffe14d"), borde=col("#c9a12a"), g=0.7)


@cosa("mesa", 680, 300)
def _mesa(L, o):
    L.forma([(-320, -150), (320, -150), (320, -120), (-320, -120)], col("#8b5a2b"), g=1.1)
    for x in (-280, 280):
        L.linea([(x, -120), (x, 0)], 1.3, col("#6b4220"))
    L.elipse(-180, -175, 60, 28, col("#d39b52"), g=0.8)
    for k in range(6):
        L.elipse(-20 + (k % 3) * 22, -170 - (k // 3) * 20, 14, 14, col("#6a2a7a"), g=0.5)
    L.forma([(150, -150), (190, -150), (200, -230), (140, -230)], col("#d9a62e"), g=0.8)
    L.elipse(260, -178, 50, 28, col("#c8552e"), g=0.8)


@cosa("monedas", 260, 120)
def _monedas(L, o):
    for k, (x, y) in enumerate(((-60, -20), (0, -20), (60, -20), (-30, -50), (30, -50), (0, -80))):
        L.elipse(x, y, 32, 16, col("#f2c230"), g=0.7)


@cosa("arbol", 520, 760)
def _arbol(L, o):
    L.forma([(-35, 0), (35, 0), (25, -380), (-25, -380)], col("#6b4220"), g=1.2)
    rng = random.Random(3)
    for _ in range(9):
        x, y, r = rng.uniform(-170, 170), rng.uniform(-640, -420), rng.uniform(90, 130)
        L.elipse(x, y, r, r * .9, mezcla("#4f8a3a", "#2e5f22", rng.random() * .5), g=1.0)


@cosa("rocas", 600, 200)
def _rocas(L, o):
    for x, r in ((-180, 90), (20, 120), (200, 80)):
        L.elipse(x, -r * .7, r, r * .75, col("#8a8070"), g=1.1)


@cosa("cruz_vacia", 300, 700)
def _cruz(L, o):
    L.forma([(-25, 0), (25, 0), (25, -650), (-25, -650)], col("#6b4220"), g=1.2)
    L.forma([(-140, -500), (140, -500), (140, -450), (-140, -450)], col("#6b4220"), g=1.2)


_cache_cosas = {}
CLAVES_DINAMICAS = {"x", "hasta", "y", "profundidad", "balanceo", "entra_en", "caer", "caer_desde",
                    "caer_hasta", "girar", "delante", "sale_en", "sube"}


def sprite_cosa(o, mira):
    clave = json.dumps({k: v for k, v in o.items() if k not in CLAVES_DINAMICAS}, sort_keys=True) + str(mira)
    if clave in _cache_cosas:
        return _cache_cosas[clave]
    tipo = o.get("tipo")
    if tipo not in COSAS:
        print(f"\n  [aviso] No existe el objeto '{tipo}'. Opciones: {', '.join(sorted(COSAS))}")
        COSAS[tipo] = (10, 10, lambda L, o: None)
    ancho, alto, f = COSAS[tipo]
    esc = o.get("escala", 1.0)
    sw, sh = int((ancho + 80) * esc * SS), int((alto + 80) * esc * SS)
    img = Image.new("RGBA", (sw, sh), (0, 0, 0, 0))
    ox, oy = sw / 2, sh - 40 * esc * SS
    L = Lapiz(img, ox, oy, esc, mira, hash(clave) % 10000)
    f(L, o)
    fin = img.resize((max(1, sw // SS), max(1, sh // SS)), Image.LANCZOS)
    _cache_cosas[clave] = (fin, ox / SS, oy / SS)
    return _cache_cosas[clave]


def pegar_cosa(img, o, t, dur, suelo):
    p = t / max(dur, .01)
    if "entra_en" in o and t < o["entra_en"]:
        return
    if "sale_en" in o and t >= o["sale_en"]:
        return
    x0 = o.get("x", 0.5)
    x = x0 + (o.get("hasta", x0) - x0) * suave(p)
    mira = 1 if o.get("mira", "derecha") == "derecha" else -1
    spr, ax, ay = sprite_cosa(o, mira)
    y = suelo + o.get("y", 0)
    if "sube" in o:   # mover verticalmente (px) a lo largo de la escena
        y += o["sube"] * suave(p)
    if o.get("balanceo"):
        y += math.sin(t * 2.2) * 10
    ang = 0.0
    if o.get("caer"):
        c0, c1 = o.get("caer_desde", 0.2), o.get("caer_hasta", 0.6)
        ang = -mira * 80 * suave((p - c0) / max(c1 - c0, .01))
    if o.get("girar") and "hasta" in o:   # piedra que rueda sobre su centro
        r = 165 * o.get("escala", 1.0)
        spr = spr.rotate(-(x - x0) * W / r * 57.3 * mira, center=(ax, ay - r), resample=Image.BICUBIC)
    elif abs(ang) > 0.3:                    # columna que cae sobre su base
        big = Image.new("RGBA", (spr.width * 3, spr.height * 2), (0, 0, 0, 0))
        big.paste(spr, (spr.width, spr.height))
        cx, cy = spr.width + ax, spr.height + ay
        spr = big.rotate(ang, center=(cx, cy), resample=Image.BICUBIC)
        ax, ay = cx, cy
    img.paste(spr, (int(x * W - ax), int(y - ay)), spr)

# ======================================================================
#  Efectos extra
# ======================================================================

def efecto_mar(d, k, suelo, color="#2f6fae"):
    """Agua que tapa el camino del mar Rojo. k=0 cerrado (agua), k=1 abierto."""
    hz = H * .42
    ancho_arriba, ancho_abajo = 140, 760
    f = 1 - k
    if f <= 0.01:
        return
    pts = [(W / 2 - ancho_arriba / 2 * f, hz), (W / 2 + ancho_arriba / 2 * f, hz),
           (W / 2 + ancho_abajo / 2 * f, H), (W / 2 - ancho_abajo / 2 * f, H)]
    d.polygon(pts, fill=col(color))
    for i in range(6):
        y = hz + (H - hz) * (i + 1) / 7
        w = (ancho_arriba + (ancho_abajo - ancho_arriba) * (y - hz) / (H - hz)) / 2 * f
        d.line([(W / 2 - w * .8, y), (W / 2 + w * .8, y)], fill=(200, 230, 250, 150), width=5)


def efecto_agua(d, nivel, t, color=(47, 111, 174, 235)):
    top = H * (1 - nivel)
    pts = [(x, top + math.sin(x / 70 + t * 3) * 14) for x in range(0, W + 20, 20)]
    d.polygon(pts + [(W, H), (0, H)], fill=color)
    d.line(pts, fill=(220, 240, 255, 220), width=7)


def efecto_arcoiris(d, alfa):
    cx, cy = W / 2, H * .62
    colores = [(230, 60, 60), (240, 140, 40), (245, 220, 60), (80, 190, 90), (60, 130, 220), (120, 80, 190)]
    for i, c in enumerate(colores):
        r = 640 - i * 34
        d.arc([cx - r, cy - r, cx + r, cy + r], 180, 360, fill=(*c, int(200 * alfa)), width=36)


def efecto_rayo(d, rr):
    x = rr.uniform(W * .15, W * .85)
    y = 0
    pts = [(x, y)]
    while y < H * .55:
        y += rr.uniform(60, 120)
        x += rr.uniform(-70, 70)
        pts.append((x, y))
    d.line(pts, fill=(255, 250, 210, 255), width=10, joint="curve")
    d.line(pts, fill=(255, 255, 255, 255), width=4, joint="curve")


def efecto_brillo(d, cx, cy, t, n=14, radio=260):
    rr = random.Random(int(t * 6))
    for i in range(n):
        x = cx + rr.uniform(-radio, radio)
        y = cy + rr.uniform(-radio, radio)
        s = rr.uniform(8, 22)
        d.polygon([(x, y - s), (x + s * .25, y - s * .25), (x + s, y), (x + s * .25, y + s * .25),
                   (x, y + s), (x - s * .25, y + s * .25), (x - s, y), (x - s * .25, y - s * .25)],
                  fill=(255, 240, 150, 230))

# ======================================================================
#  Render principal
# ======================================================================

def estado_personaje(item, t, dur):
    p = t / max(dur, .01)
    x0 = item.get("x", 0.5)
    x1 = item.get("hasta", x0)
    acc = item.get("accion", "quieto")
    if acc in ("caminar", "correr") or "hasta" in item:
        k = suave(p) if acc not in ("caminar", "correr") else min(1, p * 1.05)
        x = x0 + (x1 - x0) * k
    else:
        x = x0
    if "entra_en" in item:   # aparece despues de cierto segundo
        if t < item["entra_en"]:
            return None
    return x


def main():
    ap = argparse.ArgumentParser(description="Animador biblico 2D gratis")
    ap.add_argument("historia", nargs="?", help="archivo .json de la historia")
    ap.add_argument("--todas", action="store_true",
                    help="crear los videos de todas las historias de /historias que aun no tengan video")
    ap.add_argument("--sin-voz", action="store_true", help="no generar voz (prueba rapida)")
    ap.add_argument("--borrador", action="store_true", help="render rapido a media calidad")
    ap.add_argument("--salida", default=None)
    ap.add_argument("--paralelo", type=int, default=0,
                    help="cuantos videos crear a la vez con --todas (por defecto: la mitad de los nucleos, max 4)")
    ap.add_argument("--vista", action="store_true",
                    help="no crea el video: guarda una imagen con un cuadro de cada escena para revisar rapido")
    a = ap.parse_args()
    if a.vista:
        a.sin_voz = True
    if not shutil.which("ffmpeg"):
        sys.exit("[ERROR] No encuentro ffmpeg. Mira el LEEME para instalarlo.")
    if a.todas:
        raiz = Path(__file__).resolve().parent
        salida = Path(a.salida) if a.salida else raiz / "videos"
        pendientes = []
        for j in sorted((raiz / "historias").glob("*.json")):
            try:
                tit = json.loads(j.read_text(encoding="utf-8")).get("titulo", j.stem)
            except Exception:
                tit = j.stem
            if not video_completo(salida / f"{nombre_video(tit, j)}.mp4"):
                pendientes.append(j)
        if not pendientes:
            print("Todas las historias ya tienen su video. Agrega nuevas en la carpeta 'historias'.")
            return
        crear_en_paralelo(pendientes, a, salida)
        return
    if not a.historia:
        ap.error("indica el archivo de la historia, o usa --todas")
    crear_video(Path(a.historia), a)


def voces_necesarias(rutas):
    """Nombres de voces Piper que usan estas historias (para descargarlas antes)."""
    lib = Path(__file__).resolve().parent / "personajes.json"
    biblio = json.loads(lib.read_text(encoding="utf-8")) if lib.exists() else {}
    voces = set()
    for r in rutas:
        try:
            h = json.loads(Path(r).read_text(encoding="utf-8"))
        except Exception:
            continue
        voces.add(h.get("voz_narrador", VOZ_NARRADOR))
        pers = {**{k: v for k, v in biblio.items() if isinstance(v, dict)}, **h.get("personajes", {})}
        for e in h.get("escenas", []):
            quien = e.get("habla")
            if quien and isinstance(pers.get(quien), dict) and pers[quien].get("voz"):
                voces.add(pers[quien]["voz"].get("nombre", VOZ_NARRADOR))
    return {v for v in voces if v and not es_voz_edge(v)}


def crear_en_paralelo(pendientes, a, salida):
    import os
    import time
    nucleos = os.cpu_count() or 2
    trabajos = max(1, min(a.paralelo or max(1, nucleos // 2), 4, len(pendientes)))
    print(f"Voy a crear {len(pendientes)} video(s), {trabajos} a la vez.\n")
    if not a.sin_voz:
        for v in sorted(voces_necesarias(pendientes)):
            try:
                asegurar_modelo(v)
            except ErrorVoz as ex:
                sys.exit(f"[ERROR] {ex}")
    registros = salida / "_registros"
    registros.mkdir(parents=True, exist_ok=True)
    extra = (["--sin-voz"] if a.sin_voz else []) + (["--borrador"] if a.borrador else []) + \
            (["--salida", str(salida)] if a.salida else [])
    cola = list(pendientes)
    activos = []
    hechos = errores = 0
    inicio = time.time()
    while cola or activos:
        while cola and len(activos) < trabajos:
            j = cola.pop(0)
            log = open(registros / (j.stem + ".txt"), "w", encoding="utf-8")
            pr = subprocess.Popen([sys.executable, str(Path(__file__).resolve()), str(j)] + extra,
                                  stdout=log, stderr=subprocess.STDOUT)
            activos.append((pr, j, log))
            print(f"  Empezando: {j.stem}")
        time.sleep(2)
        for pr, j, log in list(activos):
            if pr.poll() is not None:
                log.close()
                activos.remove((pr, j, log))
                if pr.returncode == 0:
                    hechos += 1
                    print(f"  LISTO ({hechos}/{len(pendientes)}): {j.stem}   [{(time.time() - inicio) / 60:.0f} min]")
                else:
                    errores += 1
                    print(f"  [ERROR] {j.stem}: revisa videos/_registros/{j.stem}.txt")
    print(f"\nTerminado: {hechos} video(s) creados, {errores} con error.")


def video_completo(ruta):
    """True si el video existe y se puede abrir (no quedo a medias)."""
    if not ruta.exists() or ruta.stat().st_size < 10000:
        return False
    try:
        r = subprocess.run(["ffmpeg", "-v", "error", "-sseof", "-1", "-i", str(ruta), "-f", "null", "-"],
                           stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120)
        return r.returncode == 0 and not r.stderr.strip()
    except Exception:
        return False


def nombre_video(titulo, ruta):
    return re.sub(r"[^\w-]+", "_", titulo or ruta.stem).strip("_")


def crear_video(ruta, a):
    try:
        h = json.loads(ruta.read_text(encoding="utf-8"))
    except json.JSONDecodeError as ex:
        sys.exit(f"[ERROR] El archivo de la historia tiene un error de formato: {ex}")
    base_dir = ruta.parent
    # Formato: vertical (TikTok/Shorts) o horizontal (YouTube normal).
    # El horizontal se dibuja a 3412x1920 (misma altura, mismo tamano de personajes)
    # y se entrega en 1920x1080.
    global W, H
    horizontal = h.get("formato") == "horizontal"
    W, H = (3412, 1920) if horizontal else (1080, 1920)

    personajes = {}
    biblioteca = {}
    lib = Path(__file__).resolve().parent / "personajes.json"
    if lib.exists():
        try:
            biblioteca = json.loads(lib.read_text(encoding="utf-8"))
        except json.JSONDecodeError as ex:
            sys.exit(f"[ERROR] personajes.json tiene un error de formato: {ex}")
    biblioteca = {k: v for k, v in biblioteca.items() if not k.startswith("_")}
    for k, v in {**biblioteca, **h.get("personajes", {})}.items():
        c = dict(DEFECTO)
        c.update(v)
        c["escala"] = c["escala"] * h.get("tamano_personajes", 1.4)
        personajes[k] = c
    escenas = h["escenas"]
    nombre = nombre_video(h.get("titulo"), ruta)
    carpeta = Path(a.salida) if a.salida else ruta.parent.parent / "videos"
    carpeta.mkdir(parents=True, exist_ok=True)

    print(f"Historia: {h.get('titulo', ruta.stem)}  ({len(escenas)} escenas)")
    print("[1/3] Generando voces...")
    voces = preparar_voz(escenas, personajes, carpeta, a.sin_voz, h.get("voz_narrador", VOZ_NARRADOR),
                         _velocidad(h.get("velocidad_narrador", 1.0)), h.get("pausa_escenas", 0.35))
    inicios, t = [], 0.0
    for (_, _, d) in voces:
        inicios.append(t)
        t += d
    total = t

    # audio completo + envolvente para mover bocas
    pista = np.zeros(int(total * SR) + SR, dtype=np.float32)
    todas = []
    for (au, pal, d), t0 in zip(voces, inicios):
        if au is not None:
            i0 = int(t0 * SR)
            pista[i0:i0 + len(au)] += au[:len(pista) - i0]
        todas += [dict(p, start=p["start"] + t0, end=p["end"] + t0, tope=t0 + d) for p in pal]
    hay_voz = bool(np.abs(pista).max() > 0.001)
    blk = SR // FPS
    env = np.sqrt(np.mean(pista[:len(pista) // blk * blk].reshape(-1, blk) ** 2, axis=1))
    env = env / (np.percentile(env[env > 0], 95) if hay_voz and (env > 0).any() else 1)
    pista = mezclar_sonidos(pista, escenas, inicios, voces, total, h)
    wav = carpeta / f"_narracion_{TMP}.wav"
    with wave.open(str(wav), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(pista, -1, 1) * 32767).astype(np.int16).tobytes())

    rotulos = [(t0, t0 + d, e["rotulo"]) for e, t0, (_, _, d) in zip(escenas, inicios, voces) if e.get("rotulo")]
    caps = [(t0, r.split(":", 1)[-1].strip().capitalize()) for t0, _, r in rotulos if r.upper().startswith("CAPÍTULO")]
    if caps:   # capitulos para la descripcion de YouTube
        mmss = lambda x: f"{int(x) // 60}:{int(x) % 60:02d}"
        lineas = ["0:00 Introducción"] + [f"{mmss(t0)} {txt}" for t0, txt in caps if t0 >= 10]
        (carpeta / f"{nombre}_capitulos.txt").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    crear_ass(todas, h.get("gancho"), h.get("final"), total, h.get("resaltar", []), carpeta / f"_subs_{TMP}.ass", rotulos)

    print(f"[2/3] Animando {total:.0f} segundos de video...")
    salida = f"_creando_{TMP}.mp4"
    final_mp4 = carpeta / f"{nombre}.mp4"
    if horizontal:
        escala_out = "960:540" if a.borrador else "1920:1080"
    else:
        escala_out = "540:960" if a.borrador else f"{W}:{H}"
    cmd = ["ffmpeg", "-y", "-v", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS),
           "-i", "-", "-i", f"_narracion_{TMP}.wav"]
    musica = h.get("musica") if h.get("musica") != "auto" else None
    fuentes = carpeta / "_fuentes"
    fuentes.mkdir(exist_ok=True)
    for ff in (Path(__file__).resolve().parent / "fuentes").glob("*.ttf"):
        if not (fuentes / ff.name).exists():
            try:
                shutil.copy(ff, fuentes / ff.name)
            except OSError:
                pass
    filtro_v = f"[0:v]ass=_subs_{TMP}.ass:fontsdir=_fuentes,scale={escala_out}[v]"
    if musica:
        mp = (base_dir / musica).resolve()
        if mp.exists():
            cmd += ["-stream_loop", "-1", "-i", str(mp)]
            vol = h.get("volumen_musica", 0.12)
            filtro = f"{filtro_v};[2:a]volume={vol}[m];[1:a][m]amix=inputs=2:duration=first:normalize=0[a]"
        else:
            print(f"  [aviso] No encontre la musica: {mp}")
            musica = None
    if not musica:
        filtro = f"{filtro_v};[1:a]anull[a]"
    cmd += ["-filter_complex", filtro, "-map", "[v]", "-map", "[a]", "-t", f"{total:.2f}",
            "-c:v", "libx264", "-preset", "veryfast" if not a.borrador else "ultrafast", "-crf", "20",
            "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", salida]
    proc = None if a.vista else subprocess.Popen(cmd, stdin=subprocess.PIPE, cwd=carpeta)
    vistas = []
    VW = 853 if horizontal else 270

    luz = rayos_luz()
    cache_fondo = {}
    portada_guardada = False
    frame = 0
    try:
        for ie, (e, t0, (au, pal, dur)) in enumerate(zip(escenas, inicios, voces)):
            fnom = e.get("fondo", "valle")
            if Path(fnom).suffix:
                fnom = str((base_dir / fnom).resolve())
            if fnom not in cache_fondo:
                cache_fondo[fnom] = fondo(fnom, len(cache_fondo) * 7 + 3)
            bg, suelo = cache_fondo[fnom]
            items = e.get("personajes", [])
            cosas = e.get("cosas", [])
            efectos = e.get("efectos", [])
            camara = e.get("camara", "fijo")
            nfr = max(1, int(round(dur * FPS)))
            capas = [(it.get("profundidad", 0), 0, "p", it) for it in items] + \
                    [(co.get("profundidad", 500 if co.get("delante") else -20), 1, "c", co) for co in cosas]
            capas.sort(key=lambda c: (c[0], c[1]))
            cuadros = range(nfr) if not a.vista else [int(nfr * 0.6)]
            for fi in cuadros:
                t = fi / FPS
                p = t / dur
                img = bg.copy()
                d = ImageDraw.Draw(img, "RGBA")
                manos, pos_cabeza = {}, {}
                # efectos que van detras de todo
                for ef in efectos:
                    tipo = ef.get("tipo")
                    a0, a1 = ef.get("inicio", 0.0), ef.get("fin", 1.0)
                    kk = suave((p - a0) / max(a1 - a0, .01))
                    if tipo == "abrir_mar":
                        efecto_mar(d, kk, suelo)
                    elif tipo == "cerrar_mar":
                        efecto_mar(d, 1 - kk, suelo)
                for j, (_, _, clase, it) in enumerate(capas):
                    if clase == "c":
                        pegar_cosa(img, it, t, dur, suelo)
                        continue
                    pid = it.get("id")
                    if pid is None:
                        continue
                    c = personajes.get(pid)
                    if c is None:
                        print(f"\n  [aviso] El personaje '{pid}' no esta definido.")
                        it["id"] = None
                        continue
                    cambios = {k: v for k, v in it.items() if k in DEFECTO and k not in ("escala", "tipo", "voz")}
                    if cambios:   # cambiar aspecto solo en esta escena (pelo, objeto, venda...)
                        c = dict(c, **cambios)
                    if "escala" in it:
                        c = dict(c, escala=c["escala"] * it["escala"])
                    x = estado_personaje(it, t, dur)
                    if x is None or ("sale_en" in it and t >= it["sale_en"]):
                        continue
                    hablando = e.get("habla") == pid
                    boca = 0.0
                    if hablando:
                        gi = int((t0 + t) * FPS)
                        if hay_voz:
                            boca = float(np.clip(env[min(gi, len(env) - 1)] * 1.3, 0, 1))
                        else:
                            en_palabra = any(w["start"] <= t <= w["end"] for w in pal)
                            boca = (0.5 + 0.5 * math.sin(t * 22)) if en_palabra else 0
                    if it.get("accion") == "rugir":
                        boca = max(boca, 0.55 + 0.45 * math.sin(t * 7))
                    mira = 1 if it.get("mira", "derecha") == "derecha" else -1
                    po = pose_de(it.get("accion", "quieto"), t, dur, it.get("emocion", "neutral"), hablando)
                    prof = it.get("profundidad", 0)
                    yb = suelo + prof + it.get("y", 0)
                    spr, pos, mano = render_personaje(c, x * W, yb, po, t, hablando, boca, mira,
                                                      j + 1 + ie, frame)
                    img.paste(spr, pos, spr)
                    manos[pid] = mano
                    if not po.get("caida"):   # acostados no sirven para primer plano
                        pos_cabeza[pid] = (x * W, yb - (430 + 30) * c["escala"])
                d = ImageDraw.Draw(img, "RGBA")
                sx = sy = 0
                for ef in efectos:
                    tipo = ef.get("tipo")
                    a0, a1 = ef.get("inicio", 0.0), ef.get("fin", 1.0)
                    activo = a0 <= p <= a1
                    kk = suave((p - a0) / max(a1 - a0, .01))
                    if tipo == "agua":
                        n0 = ef.get("nivel", 0.2)
                        efecto_agua(d, n0 + (ef.get("hasta", n0) - n0) * kk, t)
                    elif tipo == "arcoiris" and p >= a0:
                        efecto_arcoiris(d, kk)
                    elif tipo == "rayo" and activo and (frame // 4) % 9 == 0:
                        efecto_rayo(d, random.Random(frame // 4))
                        img = Image.blend(img, Image.new("RGB", (W, H), (230, 235, 255)), 0.35)
                        d = ImageDraw.Draw(img, "RGBA")
                    elif tipo == "oscuridad" and activo:
                        d.rectangle([0, 0, W, H], fill=(0, 0, 20, int(255 * ef.get("fuerza", 0.45))))
                    elif tipo == "brillo" and activo:
                        efecto_brillo(d, ef.get("x", .5) * W, suelo + ef.get("y", -250), t,
                                      ef.get("cantidad", 14), ef.get("radio", 260))
                    elif tipo == "proyectil" and activo:
                        k = (p - a0) / max(a1 - a0, .01)
                        o = manos.get(ef.get("de")) or (W * .3, suelo - 300)
                        dst = pos_cabeza.get(ef.get("a"), (W * .7, suelo - 500))
                        for tr in range(5, -1, -1):
                            k2 = max(0, k - tr * 0.03)
                            tx = o[0] + (dst[0] - o[0]) * k2
                            ty = o[1] + (dst[1] - o[1]) * k2 - math.sin(k2 * math.pi) * 160
                            r = 14 if tr == 0 else 13 - tr * 2
                            if tr == 0:
                                d.ellipse([tx - r, ty - r, tx + r, ty + r], fill=(130, 130, 130, 255),
                                          outline=TINTA, width=4)
                            elif r > 0:
                                d.ellipse([tx - r, ty - r, tx + r, ty + r], fill=(120, 120, 120, 220 - tr * 40))
                    elif tipo == "luz" and activo:
                        alfa = 0.6 + 0.4 * math.sin(t * 2)
                        l2 = luz.copy()
                        l2.putalpha(l2.getchannel("A").point(lambda v: int(v * alfa)))
                        if ef.get("x") is not None:
                            l2 = l2.transform(l2.size, Image.AFFINE, (1, 0, (0.5 - ef["x"]) * W, 0, 1, 0))
                        img.paste(l2, (0, 0), l2)
                        d = ImageDraw.Draw(img, "RGBA")
                    elif tipo == "temblor" and activo:
                        sx, sy = random.uniform(-14, 14), random.uniform(-14, 14)
                    elif tipo == "flash" and activo:
                        k = 1 - (p - a0) / max(a1 - a0, .01)
                        img = Image.blend(img, Image.new("RGB", (W, H), (255, 255, 255)), 0.85 * k)
                        d = ImageDraw.Draw(img, "RGBA")
                    elif tipo == "lluvia" and activo:
                        rr = random.Random(frame)
                        for _ in range(160):
                            x, y = rr.uniform(0, W), rr.uniform(0, H)
                            d.line([(x, y), (x - 12, y + 45)], fill=(200, 210, 230, 140), width=3)
                    elif tipo == "fuego" and activo:
                        rr = random.Random(frame // 2)
                        fx = ef.get("x", .5) * W
                        base = suelo + ef.get("y", 0)
                        tam = ef.get("tamano", 1.0) * (0.3 + 0.7 * kk if ef.get("crece") else 1)
                        for _ in range(int(30 * max(tam, .3))):
                            r = rr.uniform(20, 60) * tam
                            x = fx + rr.uniform(-90, 90) * tam
                            y = base - rr.uniform(0, 260) * tam * (1 - abs(x - fx) / (140 * tam))
                            d.ellipse([x - r, y - r * 1.5, x + r, y + r],
                                      fill=(255, rr.randint(90, 200), 30, 150))
                # camara
                z = 1.0
                if camara == "acercar":
                    z = 1 + 0.14 * suave(p)
                elif camara == "alejar":
                    z = 1.14 - 0.14 * suave(p)
                elif camara == "acercar_rapido":
                    z = 1 + 0.3 * suave(min(1, p * 3))
                fx, fy = e.get("foco_x", 0.5) * W, suelo - 420
                desp = 0.0
                if camara == "paneo":
                    z, desp = 1.1, (p - 0.5) * W * 0.08
                # cortes de camara: cada ~2 s cambia el plano (primer plano, plano medio...)
                corte = h.get("corte_seg", 2.2)
                centrado = None
                if h.get("cortes", True) and e.get("cortes", True) and dur >= corte * 1.5:
                    k = int(t // corte)
                    frac = (t % corte) / corte
                    caras = [pos_cabeza[i] for i in sorted(pos_cabeza)]
                    if k > 0:
                        if caras and k % 2 == 1:      # primer plano de un personaje
                            cx_, cy_ = caras[(k // 2) % len(caras)]
                            centrado = (1.6 + 0.06 * frac, cx_, cy_ + 120)
                        elif caras:                   # plano medio del grupo
                            mx_ = sum(c[0] for c in caras) / len(caras)
                            my_ = sum(c[1] for c in caras) / len(caras)
                            centrado = (1.25 + 0.05 * frac, mx_, my_ + 260)
                        else:                         # sin personajes: acercar a la escena
                            centrado = (1.2 + 0.08 * frac if k % 2 else 1.0 + 0.05 * frac, W / 2, suelo - 350)
                if centrado:
                    z, cx_, cy_ = centrado
                    cw, ch = W / z, H / z
                    l = min(max(cx_ - cw / 2 + sx, 0), W - cw)
                    tp = min(max(cy_ - ch * 0.42 + sy, 0), H - ch)
                    img = img.resize((W, H), Image.BILINEAR, box=(l, tp, l + cw, tp + ch))
                else:
                    if sx or sy:
                        z = max(z, 1.03)
                    if z != 1.0:
                        cw, ch = W / z, H / z
                        l = min(max(fx - fx / z + desp + sx, 0), W - cw)
                        tp = min(max(fy - fy / z + sy, 0), H - ch)
                        img = img.resize((W, H), Image.BILINEAR, box=(l, tp, l + cw, tp + ch))
                if h.get("barra_progreso"):
                    db = ImageDraw.Draw(img, "RGBA")
                    db.rectangle([0, 0, W, 16], fill=(0, 0, 0, 120))
                    db.rectangle([0, 0, int(W * min(1, (t0 + t) / total)), 16], fill=(255, 214, 0, 255))
                if not portada_guardada and e.get("portada") and fi == nfr // 2:
                    (img.resize((1920, 1080), Image.LANCZOS) if horizontal else img).save(carpeta / f"{nombre}_portada.png")
                    portada_guardada = True
                if a.vista:
                    vistas.append(img.resize((VW, 480), Image.LANCZOS))
                else:
                    proc.stdin.write(img.tobytes())
                frame += 1
            print(f"\r  Escena {ie + 1}/{len(escenas)} lista", end="", flush=True)
    except BrokenPipeError:
        pass
    if a.vista:
        cols = 6 if not horizontal else 3
        filas = (len(vistas) + cols - 1) // cols
        hoja = Image.new("RGB", (cols * VW, filas * 480), (30, 30, 30))
        for i, v in enumerate(vistas):
            hoja.paste(v, ((i % cols) * VW, (i // cols) * 480))
        hoja.save(carpeta / f"{nombre}_vista.png")
        for f in (f"_narracion_{TMP}.wav", f"_subs_{TMP}.ass"):
            (carpeta / f).unlink(missing_ok=True)
        print(f"\n  Vista previa: {(carpeta / (nombre + '_vista.png')).resolve()}")
        return
    proc.stdin.close()
    proc.wait()
    print()
    if proc.returncode != 0:
        sys.exit("[ERROR] ffmpeg no pudo crear el video.")
    for f in (f"_narracion_{TMP}.wav", f"_subs_{TMP}.ass"):
        (carpeta / f).unlink(missing_ok=True)
    import os
    os.replace(carpeta / salida, final_mp4)
    print(f"[3/3] Listo: {final_mp4.resolve()}")


if __name__ == "__main__":
    main()
