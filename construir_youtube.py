"""Prepara las versiones horizontales para YouTube (1920x1080).

Lee las historias de la carpeta "historias" y crea en "historias_youtube":
  - una version horizontal de cada historia (ritmo un poco mas tranquilo),
  - un video de bienvenida y uno de despedida para cada recopilacion,
  - recopilaciones.json: que historias van juntas en cada video largo.

Uso:  python construir_youtube.py
Luego los videos se crean en la nube con CREAR_YOUTUBE_EN_LA_NUBE.bat
"""
import json
from pathlib import Path

RAIZ = Path(__file__).resolve().parent
ORIGEN = RAIZ / "historias"
DESTINO = RAIZ / "historias_youtube"

# Ritmo para YouTube: un poco mas pausado que los Shorts, pero sin aburrir.
AJUSTES = {
    "formato": "horizontal",
    "velocidad_narrador": 1.1,
    "pausa_escenas": 0.3,
    "corte_seg": 3.0,
    "barra_progreso": False,
    "final": "",
}

# Cada recopilacion: titulo del video, texto de la miniatura y las historias (por numero).
RECOPILACIONES = [
    {
        "id": "A",
        "titulo": "7 Grandes Héroes de la Fe",
        "miniatura": "7 HÉROES DE LA FE",
        "bienvenida": "¡Hola! Hoy vas a conocer a siete grandes héroes de la Biblia. "
                      "Personas comunes que confiaron en Dios y vieron milagros increíbles.",
        "heroes": ["noe", "moises", "david"],
        "historias": [1, 8, 3, 4, 2, 5, 17],
    },
    {
        "id": "B",
        "titulo": "6 Historias de Fuerza y Esperanza",
        "miniatura": "FUERZA Y ESPERANZA",
        "bienvenida": "¡Hola! Hoy te traigo seis historias de la Biblia sobre fuerza, "
                      "lealtad y esperanza, aun en los momentos más difíciles.",
        "heroes": ["sanson", "rut", "elias"],
        "historias": [7, 10, 9, 19, 18, 6],
    },
    {
        "id": "C",
        "titulo": "La Vida de Jesús en 7 Historias",
        "miniatura": "LA VIDA DE JESÚS",
        "bienvenida": "¡Hola! Hoy vamos a recorrer la vida de Jesús: desde su nacimiento "
                      "en Belén hasta el día en que venció a la muerte.",
        "heroes": ["maria", "jesus", "pedro"],
        "historias": [11, 12, 13, 14, 15, 16, 20],
    },
    {
        "id": "D",
        "titulo": "20 Historias de la Biblia (Película Completa)",
        "miniatura": "20 HISTORIAS DE LA BIBLIA",
        "bienvenida": "¡Hola! Prepárate, porque hoy vas a ver veinte historias de la Biblia, "
                      "una detrás de otra. Desde Noé hasta el apóstol Pablo.",
        "heroes": ["noe", "jesus", "david"],
        "historias": list(range(1, 21)),
    },
]


def escena_presentacion(rec, numero):
    n = len(rec["historias"])
    h1, h2, h3 = rec["heroes"]
    return [
        {
            "fondo": "cielo",
            "texto": rec["bienvenida"],
            "personajes": [
                {"id": h1, "x": 0.3, "accion": "celebrar", "emocion": "feliz"},
                {"id": h2, "x": 0.5, "accion": "alabar", "emocion": "feliz"},
                {"id": h3, "x": 0.7, "accion": "celebrar", "emocion": "feliz"},
            ],
            "efectos": [{"tipo": "luz"}, {"tipo": "brillo", "y": -600}],
            "rotulo": rec["miniatura"],
            "portada": True,
            "camara": "acercar",
        },
        {
            "fondo": "valle",
            "texto": "Antes de empezar, suscríbete y activa la campanita, "
                     "así no te pierdes ninguna historia nueva.",
            "personajes": [{"id": h2, "x": 0.5, "accion": "senalar", "emocion": "feliz"}],
            "camara": "fijo",
        },
        {
            "fondo": "camino",
            "texto": f"¡Y quédate hasta el final, porque la historia número {n} te va a encantar! ¿Listo? ¡Comenzamos!",
            "personajes": [{"id": h1, "x": 0.35, "accion": "caminar", "emocion": "feliz"},
                           {"id": h3, "x": 0.65, "accion": "caminar", "emocion": "feliz"}],
            "camara": "acercar",
        },
    ]


def escena_despedida(rec):
    h1, h2, h3 = rec["heroes"]
    return [
        {
            "fondo": "cielo",
            "texto": "¿Cuál fue tu historia favorita? Escríbela en los comentarios, ¡me encanta leerlos!",
            "personajes": [{"id": h1, "x": 0.3, "accion": "celebrar"},
                           {"id": h2, "x": 0.5, "accion": "orar", "emocion": "feliz"},
                           {"id": h3, "x": 0.7, "accion": "celebrar"}],
            "efectos": [{"tipo": "luz"}],
            "camara": "fijo",
        },
        {
            "fondo": "cielo",
            "texto": "Si te gustó este video, dale me gusta, compártelo con tu familia "
                     "y suscríbete para más historias de la Biblia. ¡Dios te bendiga!",
            "personajes": [{"id": h2, "x": 0.5, "accion": "alabar", "emocion": "feliz"}],
            "efectos": [{"tipo": "luz"}, {"tipo": "brillo", "y": -600}],
            "rotulo": "¡SUSCRÍBETE!",
            "pausa": 1.5,
            "camara": "acercar",
        },
    ]


def base_extra(titulo):
    return {
        "titulo": titulo,
        "formato": "horizontal",
        "voz_narrador": "es_MX-claude-high",
        "velocidad_narrador": 1.1,
        "pausa_escenas": 0.3,
        "corte_seg": 3.0,
        "musica": "auto",
        "volumen_musica": 0.1,
        "efectos_sonido": True,
        "resaltar": ["BIBLIA", "DIOS", "JESÚS", "SUSCRÍBETE", "FAVORITA", "HÉROES"],
    }


def main():
    DESTINO.mkdir(exist_ok=True)
    for viejo in DESTINO.glob("*.json"):
        viejo.unlink()
    por_numero = {}
    for f in sorted(ORIGEN.glob("*.json")):
        num = int(f.name[:2])
        h = json.loads(f.read_text(encoding="utf-8"))
        h.update(AJUSTES)
        h["titulo"] = f"{h['titulo']} HD"
        (DESTINO / f.name).write_text(json.dumps(h, ensure_ascii=False, indent=1), encoding="utf-8")
        por_numero[num] = {"archivo": f.name, "video": h["titulo"], "titulo": h["titulo"][:-3]}

    lista = []
    for rec in RECOPILACIONES:
        intro = dict(base_extra(f"Intro {rec['id']}"), escenas=escena_presentacion(rec, 0))
        outro = dict(base_extra(f"Despedida {rec['id']}"), escenas=escena_despedida(rec))
        (DESTINO / f"intro_{rec['id']}.json").write_text(json.dumps(intro, ensure_ascii=False, indent=1), encoding="utf-8")
        (DESTINO / f"despedida_{rec['id']}.json").write_text(json.dumps(outro, ensure_ascii=False, indent=1), encoding="utf-8")
        lista.append({
            "titulo": rec["titulo"],
            "miniatura": rec["miniatura"],
            "intro": intro["titulo"],
            "despedida": outro["titulo"],
            "capitulos": [{"video": por_numero[n]["video"], "titulo": por_numero[n]["titulo"]}
                          for n in rec["historias"]],
        })
    (RAIZ / "recopilaciones.json").write_text(json.dumps(lista, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Listo: {len(por_numero)} historias horizontales + {len(lista) * 2} intros/despedidas "
          f"en {DESTINO.name}, y {len(lista)} recopilaciones en recopilaciones.json")


if __name__ == "__main__":
    main()
