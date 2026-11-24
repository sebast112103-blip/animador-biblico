"""Crea la miniatura de YouTube (1280x720) de una historia larga.

Uso:  python miniatura.py historias_largas/08_rut.json CARPETA_SALIDA

La historia puede traer un bloque "miniatura":
  "miniatura": {"texto": ["¡SE LO TRAGÓ", "UN PEZ!"], "escena": { ...una escena normal... }}
La escena se dibuja con los personajes a la derecha; el texto va grande a la izquierda.
Si no trae bloque, usa la escena marcada como portada y el titulo.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont

RAIZ = Path(__file__).resolve().parent


def fuente(n, tam):
    return ImageFont.truetype(str(RAIZ / "fuentes" / n), tam)


def nombre(t):
    return re.sub(r"[^\w-]+", "_", t).strip("_")


def main():
    ruta, salida = Path(sys.argv[1]), Path(sys.argv[2])
    salida.mkdir(parents=True, exist_ok=True)
    h = json.loads(ruta.read_text(encoding="utf-8"))
    m = h.get("miniatura") or {}
    escena = m.get("escena") or next((e for e in h["escenas"] if e.get("portada")), h["escenas"][0])
    escena = dict(escena, portada=True, camara="fijo", texto="Hola a todos, bienvenidos a esta historia.")
    escena.pop("rotulo", None)
    temp = salida / "_mini_tmp"
    temp.mkdir(exist_ok=True)
    hm = {k: v for k, v in h.items() if k not in ("escenas", "miniatura")}
    hm.update(titulo="MINI", gancho="", final="", musica=None, efectos_sonido=False, cortes=False, escenas=[escena])
    (temp / "mini.json").write_text(json.dumps(hm, ensure_ascii=False), encoding="utf-8")
    subprocess.run([sys.executable, str(RAIZ / "animador.py"), str(temp / "mini.json"), "--sin-voz", "--borrador",
                    "--salida", str(temp)], check=True, stdout=subprocess.DEVNULL)
    W, H = 1280, 720
    img = Image.open(temp / "MINI_portada.png").convert("RGB").resize((W, H), Image.LANCZOS)
    img = ImageEnhance.Contrast(ImageEnhance.Color(img).enhance(1.35)).enhance(1.12)
    sombra = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sombra).rectangle([0, 0, int(W * 0.42), H], fill=175)
    img = Image.composite(Image.new("RGB", (W, H)), img, sombra.filter(ImageFilter.GaussianBlur(70)))
    d = ImageDraw.Draw(img)
    lineas = m.get("texto") or [h.get("titulo", "").split(" - ")[0].upper()]
    y = 160 if len(lineas) > 1 else 230
    for i, t in enumerate(lineas[:2]):
        grande = i == len(lineas[:2]) - 1
        tam = 150 if grande else 105
        f = fuente("Anton-Regular.ttf", tam)
        while d.textlength(t, font=f) > W * 0.46 and tam > 40:
            tam -= 6
            f = fuente("Anton-Regular.ttf", tam)
        d.text((45, y), t, font=f, fill=(255, 214, 0) if grande else (255, 255, 255), stroke_width=9, stroke_fill=(0, 0, 0))
        y += tam + 15
    fb = fuente("ArchivoBlack-Regular.ttf", 32)
    sello = m.get("sello", "HISTORIA COMPLETA")
    sw = d.textlength(sello, font=fb)
    d.rounded_rectangle([45, y + 20, 45 + sw + 40, y + 82], 16, fill=(220, 30, 40))
    d.text((65, y + 27), sello, font=fb, fill=(255, 255, 255))
    destino = salida / f"{nombre(h.get('titulo') or ruta.stem)}_miniatura.jpg"
    img.save(destino, quality=92)
    for f in temp.iterdir():
        if f.is_file():
            f.unlink()
    print(f"Miniatura: {destino}")


if __name__ == "__main__":
    main()
