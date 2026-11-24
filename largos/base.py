"""Plantilla de los videos largos diarios (estructura pensada para retener al público).

ESTRUCTURA (basada en los videos más vistos del nicho):
  0:00-0:08  APERTURA EN FRÍO: la escena más espectacular de la historia + pregunta (bucle abierto).
  0:08-0:30  PROMESA: qué va a ver el público ("hoy verás..."), sin saludos largos.
  ~0:30      PRIMER CAMBIO DE RITMO (rótulo CAPÍTULO 1 + cambio de fondo).
  Cada 60-90 s  un CAPÍTULO nuevo con rótulo (YouTube crea los capítulos solo).
  Final de cada capítulo: mini-suspenso ("pero lo que pasó después nadie lo esperaba").
  Mitad del video: pregunta para comentar (sube la interacción).
  Final: enseñanza corta + pregunta + suscríbete (máx. 20 s).
"""
import json
from pathlib import Path

E = []


def S(fondo, texto, pers=(), cosas=None, efectos=None, **kw):
    e = {"fondo": fondo, "texto": texto, "personajes": list(pers)}
    if cosas:
        e["cosas"] = cosas
    if efectos:
        e["efectos"] = efectos
    e.update(kw)
    E.append(e)


def P(id, x, **kw):
    return {"id": id, "x": x, **kw}


def gente(x=0.5, esc=0.65, y=-160, prof=-70, **kw):
    return {"tipo": "multitud", "x": x, "escala": esc, "y": y, "profundidad": prof, **kw}


def guardar(archivo, titulo, gancho, resaltar, personajes=None, miniatura=None):
    for e in E:
        for c in e.get("cosas", []):
            if c.get("profundidad", 0) is None:
                c.pop("profundidad")
    h = {
        "titulo": titulo, "gancho": gancho, "final": "", "formato": "horizontal",
        "voz_narrador": "es_MX-claude-high", "velocidad_narrador": 1.1, "pausa_escenas": 0.35,
        "corte_seg": 3.0, "musica": "auto", "volumen_musica": 0.1, "efectos_sonido": True,
        "barra_progreso": False, "resaltar": resaltar + ["DIOS", "COMENTARIOS", "SUSCRÍBETE"],
        "personajes": personajes or {}, "escenas": E,
    }
    if miniatura:
        h["miniatura"] = miniatura
    out = Path(__file__).resolve().parent.parent / "historias_largas" / archivo
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(h, ensure_ascii=False, indent=1), encoding="utf-8")
    w = sum(len(e["texto"].split()) for e in E)
    print(f"{out.name}: {len(E)} escenas, {w} palabras, ~{w / 165 + len(E) * 0.35 / 60:.1f} min")
