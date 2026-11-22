"""Une los videos horizontales en recopilaciones largas para YouTube.

Uso:  python recopilar.py CARPETA_CON_LOS_VIDEOS
Lee recopilaciones.json (lo crea construir_youtube.py) y para cada recopilacion deja:
  - Recopilacion_<titulo>.mp4      el video largo (intro + historias + despedida)
  - Recopilacion_<titulo>_miniatura.jpg   miniatura 1280x720 para YouTube
  - Recopilacion_<titulo>_descripcion.txt titulo, descripcion y capitulos (marcas de tiempo)
"""
import json
import re
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = Path(__file__).resolve().parent


def nombre(t):
    return re.sub(r"[^\w-]+", "_", t).strip("_")


def duracion(f):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "default=nw=1:nk=1", str(f)], capture_output=True, text=True)
    return float(r.stdout.strip())


def marca(seg):
    seg = int(seg)
    h, m, s = seg // 3600, seg % 3600 // 60, seg % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def fuente(n, tam):
    for f in (RAIZ / "fuentes" / n, RAIZ / "fuentes" / "Anton-Regular.ttf"):
        if f.exists():
            return ImageFont.truetype(str(f), tam)
    return ImageFont.load_default()


def miniatura(portadas, texto, n, destino, sello=None):
    W, H = 1280, 720
    img = Image.new("RGB", (W, H), (20, 20, 30))
    usadas = [Image.open(p).convert("RGB") for p in portadas[:3] if p.exists()]
    if usadas:
        ancho = W // len(usadas)
        for i, p in enumerate(usadas):
            k = max(ancho / p.width, H / p.height)
            p = p.resize((int(p.width * k) + 1, int(p.height * k) + 1), Image.LANCZOS)
            l = (p.width - ancho) // 2
            img.paste(p.crop((l, 0, l + ancho, H)), (i * ancho, 0))
        d = ImageDraw.Draw(img)
        for i in range(1, len(usadas)):
            d.rectangle([i * ancho - 4, 0, i * ancho + 4, H], fill=(255, 214, 0))
    # franja oscura abajo para el titulo
    sombra = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sombra).rectangle([0, int(H * .58), W, H], fill=200)
    sombra = sombra.filter(ImageFilter.GaussianBlur(40))
    img = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), img, sombra)
    d = ImageDraw.Draw(img)
    tam = 130
    f = fuente("Anton-Regular.ttf", tam)
    while d.textlength(texto, font=f) > W - 80 and tam > 50:
        tam -= 6
        f = fuente("Anton-Regular.ttf", tam)
    tw = d.textlength(texto, font=f)
    d.text(((W - tw) / 2, H - tam - 70), texto, font=f, fill=(255, 214, 0),
           stroke_width=8, stroke_fill=(0, 0, 0))
    # sello con la cantidad de historias
    fb = fuente("ArchivoBlack-Regular.ttf", 46)
    sello = sello or f"{n} HISTORIAS"
    sw = d.textlength(sello, font=fb)
    d.rounded_rectangle([30, 30, 30 + sw + 50, 110], 20, fill=(220, 30, 40))
    d.text((55, 38), sello, font=fb, fill=(255, 255, 255))
    img.save(destino, quality=92)


def main():
    carpeta = Path(sys.argv[1] if len(sys.argv) > 1 else "videos")
    recs = json.loads((RAIZ / "recopilaciones.json").read_text(encoding="utf-8"))
    hechas = 0
    for rec in recs:
        if not (carpeta / f"{nombre(rec['intro'])}.mp4").exists():
            continue
        partes = [rec["intro"]] + [c["video"] for c in rec["capitulos"]] + [rec["despedida"]]
        archivos = [carpeta / f"{nombre(p)}.mp4" for p in partes]
        faltan = [a.name for a in archivos if not a.exists()]
        if faltan:
            print(f"[aviso] '{rec['titulo']}' no se puede armar, faltan: {', '.join(faltan)}")
            continue
        base = "Recopilacion_" + nombre(rec["titulo"])
        lista = carpeta / f"_{base}.txt"
        lista.write_text("".join(f"file '{a.resolve().as_posix()}'\n" for a in archivos), encoding="utf-8")
        salida = carpeta / f"{base}.mp4"
        r = subprocess.run(["ffmpeg", "-y", "-v", "error", "-f", "concat", "-safe", "0", "-i", str(lista),
                            "-c", "copy", "-movflags", "+faststart", str(salida)])
        lista.unlink()
        if r.returncode != 0:
            print(f"[ERROR] No se pudo unir '{rec['titulo']}'")
            continue

        # capitulos para la descripcion de YouTube
        t = duracion(archivos[0])
        caps = ["0:00 Introducción"]
        for c, a in zip(rec["capitulos"], archivos[1:-1]):
            caps.append(f"{marca(t)} {c['titulo']}")
            t += duracion(a)
        caps.append(f"{marca(t)} Despedida")
        total = duracion(salida)
        n = len(rec["capitulos"])
        desc = (f"TÍTULO:\n{rec['titulo']} | Historias de la Biblia animadas\n\n"
                f"DESCRIPCIÓN:\n{n} historias de la Biblia contadas en dibujos animados, "
                f"ideales para ver en familia y con los niños. "
                f"¿Cuál es tu favorita? Cuéntame en los comentarios.\n\n"
                f"🔔 Suscríbete para más historias de la Biblia.\n\n"
                f"CAPÍTULOS:\n" + "\n".join(caps) + "\n\n"
                "#biblia #historiasbiblicas #dibujosanimados #fe #Dios #Jesus #niños\n")
        (carpeta / f"{base}_descripcion.txt").write_text(desc, encoding="utf-8")

        portadas = [carpeta / f"{nombre(c['video'])}_portada.png" for c in rec["capitulos"]]
        miniatura(portadas, rec["miniatura"], n, carpeta / f"{base}_miniatura.jpg")
        print(f"Listo: {salida.name}  ({marca(total)})")
        hechas += 1
    print(f"{hechas} recopilacion(es) creadas en {carpeta}")

    # videos largos del dia: miniatura + descripcion con capitulos
    for caps in sorted(carpeta.glob("*_capitulos.txt")):
        base = caps.name[:-len("_capitulos.txt")]
        if not (carpeta / f"{base}.mp4").exists():
            continue
        titulo = base.replace("_", " ")
        texto = titulo.split(" - ")[0].upper()
        sub = titulo.split(" - ")[1].upper() if " - " in titulo else ""
        portada = carpeta / f"{base}_portada.png"
        miniatura([portada] if portada.exists() else [], texto, 0, carpeta / f"{base}_miniatura.jpg", sello=sub or None)
        desc = (f"TÍTULO:\n{titulo} | Historia de la Biblia animada\n\n"
                f"DESCRIPCIÓN:\nLa historia completa de {titulo.split(' - ')[0]}, contada en dibujos animados "
                f"para ver en familia. ¿Qué parte te gustó más? Cuéntame en los comentarios.\n\n"
                f"🔔 Suscríbete: cada día una nueva historia de la Biblia.\n\n"
                f"CAPÍTULOS:\n{caps.read_text(encoding='utf-8')}\n"
                "#biblia #historiasbiblicas #dibujosanimados #fe #Dios #Jesus #niños\n")
        (carpeta / f"{base}_descripcion.txt").write_text(desc, encoding="utf-8")
        caps.unlink()
        print(f"Listo: miniatura y descripcion de {base}")


if __name__ == "__main__":
    main()
