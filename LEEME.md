# Animador Bíblico 2D: gratis, sin créditos

Escribes la historia en un archivo `.json` y el programa crea un **video animado vertical (9:16)**
con personajes estilo doodle, voz narrada, bocas que se mueven al hablar y subtítulos
palabra por palabra. Sirve para TikTok, Reels, YouTube Shorts y Facebook.

## Instalación (solo la primera vez)

**Windows**
1. Instala Python desde https://www.python.org/downloads/ y marca **"Add Python to PATH"**.
2. Abre "Símbolo del sistema" y escribe: `winget install ffmpeg`
3. Entra a esta carpeta y escribe: `pip install -r requirements.txt`
4. Cierra la ventana y abre una nueva.

**Mac**
1. Instala Homebrew (https://brew.sh) y luego: `brew install python ffmpeg`
2. En esta carpeta: `pip3 install -r requirements.txt`

La voz en off usa **Piper**, un programa de voz de código abierto y gratuito. La primera vez que usas una voz,
el programa la descarga sola (unos 60–110 MB, por eso necesitas internet esa vez) y la guarda en la carpeta `voces/`.
Después funciona **sin internet y sin límites**.

## Crear un video

- **Windows, la forma fácil:** arrastra cualquier historia de la carpeta `historias` encima de `CREAR_VIDEO.bat`.
  La primera vez tarda un poco más porque descarga las voces.
- **Desde la terminal:** `python animador.py historias/02_david_y_goliat.json`

El video queda en la carpeta `videos/`, junto con una imagen de portada.

**Para publicar todos los días:** guarda varias historias en la carpeta `historias/` y haz doble clic en
`CREAR_TODOS.bat` (o `python animador.py --todas`). Crea los videos de todas las historias que todavía no
tengan video y se salta las que ya lo tienen. Puedes dejarlo trabajando de noche.
Un video de 1 minuto tarda entre 3 y 6 minutos en crearse.

- `--borrador`: crea una versión rápida en baja calidad para revisarla.
- `--sin-voz`: crea el video sin narración, para probar.

## Crear historias nuevas (lo fácil)

Pídele a Claude:

> Escribe la historia de **[Zaqueo]** en el mismo formato que este archivo
> 02_david_y_goliat.json (te lo pego abajo). Que dure unos 60 segundos (10–12 escenas), con un
> gancho fuerte al inicio, narración emocionante en español y una pregunta final para comentarios.
> Usa solo los fondos, acciones, emociones, efectos y objetos de la lista del LEEME.

Guarda la respuesta como `historias/21_zaqueo.json` y crea el video.

## Crear los videos GRATIS en la nube (GitHub Actions)

Las computadoras gratuitas de GitHub crean los videos **todos al mismo tiempo**, sin usar tu computadora.

1. Entra a tu repositorio en github.com → pestaña **Actions** → **Crear videos** → botón **Run workflow**.
2. Elige qué crear:
   - `cortos`: las 80 versiones de 10, 15, 20 y 30 segundos
   - `largos`: las 20 historias completas
   - `todos`: ambas
   - En **filtro** puedes poner, por ejemplo, `30s` (solo las de 30 segundos), `noe` o `05_`.
3. Espera entre 15 y 30 minutos. Al terminar, abre la ejecución y descarga **TODOS_LOS_VIDEOS** (abajo, en "Artifacts").

**Historias nuevas:** si subes o cambias un archivo en `historias/` o `historias_cortas/`, GitHub crea ese video solo.

## Videos cortos (10, 15, 20 y 30 segundos)
Están en `historias_cortas/`. Están pensados para ganar seguidores:
- La narración empieza con una pregunta gancho y tiene un ritmo más rápido.
- Barra de progreso arriba, palabras que saltan y rótulos con rebote.
- Efectos de sonido y música de fondo generados por el programa (sin derechos de autor).
- Las de 10 y 15 segundos terminan en suspenso con "Sígueme", para que la gente busque la historia completa.
- Las de 20 y 30 segundos terminan con una pregunta para comentar (SÍ/NO, AMÉN…): eso hace que el algoritmo las muestre a más personas.

**Idea de publicación:** sube primero el corto de 15 segundos y, horas después, el video largo de la misma historia.

## Revisar antes de crear (vista previa rápida)
`python animador.py historias/01_noe_y_el_arca.json --vista`
crea en segundos una imagen con un cuadro de cada escena, para revisar la historia sin esperar el video completo.

## Personajes compartidos
`personajes.json` guarda a todos los personajes: Jesús, María, Moisés, Pedro, ángeles, leones y los demás.
Así se ven **iguales en todos los videos**. Si cambias a alguien ahí (por ejemplo, el color del manto de Jesús),
cambia en todas las historias. Una historia también puede definir sus propios personajes.

## Referencia del formato

**Historia (arriba del archivo)**
- `titulo`, `gancho` (texto de los primeros 3 segundos), `final` (texto de los últimos 3 segundos)
- `resaltar`: palabras que siempre salen en amarillo
- `voz_narrador`, `velocidad_narrador` (1 = normal)
- `musica`: `"auto"` (música generada por el programa), la ruta a un mp3 sin derechos de autor, o `null`; `volumen_musica`: 0.1
- `efectos_sonido`: true/false; `barra_progreso`: true/false
- `tamano_personajes`: 1.4 por defecto

**Personajes** (en `personajes.json` o en la historia)
- `tipo`: `persona`, `oveja`, `leon`, `cerdo`, `carnero`, `gallo`, `burro`
- `piel`, `pelo`, `barba`, `tunica`, `manto`, `cinturon`: colores tipo `"#5b8fd6"` (o `null` para quitarlo)
- `pelo_largo`, `armadura`, `aureola`, `alas`, `venda`: true/false
- `tocado`: `corona`, `casco`, `velo`, `turbante`, `nemes` (faraón) o `null`; `color_tocado`
- `objeto`: `cayado`, `honda`, `lanza`, `espada`, `escudo`, `tablas`, `pan`, `lampara`
- `escala`: tamaño
- `voz`: `{ "nombre": "es_MX-ald-medium", "tono": -3, "velocidad": 0.95 }`

**Escenas**
- `texto`: lo que se narra o se dice
- `habla`: id del personaje que habla (se le mueve la boca y usa su voz, aunque no esté en pantalla)
- `rotulo`: texto grande en amarillo durante la escena ("40 DÍAS", "3 VECES"…)
- `fondo`: `valle`, `campo`, `desierto`, `mar`, `mar_tormenta`, `mar_rojo`, `montana`, `jardin`, `ciudad`,
  `palacio`, `templo`, `egipto`, `prision`, `foso`, `establo`, `trigal`, `dentro_pez`, `camino`, `patio`,
  `noche`, `cielo`, `tormenta`, o **tu propia imagen** (`"fondos/arca.jpg"`)
- `camara`: `fijo`, `acercar`, `alejar`, `acercar_rapido`, `paneo`; `foco_x`: 0–1
- `personajes`: lista con
  - `id`, `x` (0 = izquierda, 1 = derecha), `hasta` (para moverse), `mira`: `derecha`/`izquierda`, `y`, `profundidad`
  - `accion`: `quieto`, `caminar`, `correr`, `saltar`, `celebrar`, `alabar`, `orar`, `arrodillarse`, `agacharse`,
    `senalar`, `ofrecer`, `abrazar`, `levantar` (la vara), `empujar`, `temblar`, `lanzar`, `caer`, `caer_de_cara`,
    `dormir`, `rugir` (animales)
  - `emocion`: `neutral`, `feliz`, `triste`, `llorando`, `enojado`, `asustado`, `sorprendido`, `valiente`, `burlon`
  - cualquier rasgo solo para esa escena: `"venda": true`, `"pelo_largo": false`, `"objeto": "honda"`, `"escala": 0.8`…
  - `entra_en` / `sale_en`: segundo en que aparece o desaparece
- `cosas` (objetos): `arca`, `barca`, `pez_gigante`, `altar`, `pesebre`, `tumba`, `piedra`, `columna`, `canasta`,
  `panes_peces`, `multitud`, `trono`, `estrella`, `mesa`, `monedas`, `arbol`, `rocas`, `cruz_vacia`
  - con `x`, `y`, `escala`, `mira`, `hasta`, `delante` (delante de los personajes), `balanceo` (flota), `sube`
  - especiales: arca `puerta`; barca `vela`; pez `abierta`; pesebre `bebe`/`aureola`; piedra `girar` (rueda);
    columna `caer`; multitud `variante`: `pueblo`, `soldados`, `egipcios`
- `efectos`: `luz` (`x`), `brillo`, `proyectil` (`de`, `a`), `temblor`, `flash`, `lluvia`, `rayo`, `oscuridad` (`fuerza`),
  `fuego` (`x`, `y`, `tamano`, `crece`), `agua` (`nivel`, `hasta`), `arcoiris`, `abrir_mar`, `cerrar_mar`;
  con `inicio`/`fin` de 0 a 1 dentro de la escena
- `portada`: true para guardar esa escena como miniatura
- `pausa`, `duracion`, `duracion_min`: control del tiempo

## Voces en español (Piper, gratis y de código abierto)
| Voz | Tipo |
|---|---|
| `es_MX-claude-high` | hombre, México, la más natural (narrador por defecto) |
| `es_MX-ald-medium` | hombre, México |
| `es_ES-davefx-medium` | hombre, España (con `tono` -5 sirve para un gigante o un villano) |
| `es_AR-daniela-high` | mujer, Argentina (para María, Ester, Rut…) |
| `es_ES-sharvard-medium` | España |

Con `tono` y `velocidad` una misma voz sirve para varios personajes: un niño (+4), un anciano (-2 y 0.9), un gigante (-5).
Puedes escuchar todas las voces en https://rhasspy.github.io/piper-samples/

**Opcional:** si prefieres las voces de Microsoft por internet, instala `pip install edge-tts` y usa nombres
como `"es-MX-JorgeNeural"` o `"es-DO-EmilioNeural"`. El programa reconoce solo qué motor usar.

## Consejos para que se haga viral
- Gancho de pregunta en los primeros 3 segundos: "¿Cómo un NIÑO venció a un GIGANTE?"
- Entre 45 y 75 segundos, con escenas cortas (4–6 segundos) y mucho movimiento.
- Termina con una pregunta personal ("¿Qué gigante necesitas vencer hoy?"): genera comentarios.
- Si citas versículos textuales, usa la Reina-Valera 1909 (dominio público) o cuenta la historia con tus palabras.

## Videos horizontales para YouTube (recopilaciones)

Doble clic en **CREAR_YOUTUBE_EN_LA_NUBE.bat**. Hace todo solo:

1. `construir_youtube.py` crea en `historias_youtube` la versión horizontal (1920x1080) de cada historia,
   más una bienvenida y una despedida para cada recopilación.
2. GitHub crea los videos y los une en recopilaciones largas (`recopilar.py`).
3. Se descargan en `videos\youtube`:
   - `Recopilacion_*.mp4` – los videos largos listos para subir a YouTube.
   - `Recopilacion_*_miniatura.jpg` – la miniatura (1280x720).
   - `Recopilacion_*_descripcion.txt` – título, descripción y capítulos con sus minutos (cópialos en YouTube).
   - `*_HD.mp4` – cada historia sola, en horizontal.

Para cambiar qué historias van en cada recopilación, edita la lista `RECOPILACIONES` al principio de `construir_youtube.py`.
