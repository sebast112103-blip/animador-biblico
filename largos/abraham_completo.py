"""Video largo: Abraham, la historia completa."""
from base import S, P, gente, guardar

AB = {}
VIEJO = {"barba": "#e8e4dc", "pelo": "#e8e4dc"}
SARA_V = {"pelo": "#e8e4dc"}

# ---------- APERTURA EN FRÍO ----------
S("montana", "Un anciano sube una montaña con su único hijo. Lleva leña, fuego y un cuchillo. El muchacho pregunta: Padre, ¿dónde está el cordero? Y el anciano no sabe cómo responder.",
  [P("abraham", 0.45, **VIEJO, accion="caminar", hasta=0.55, emocion="triste"), P("isaac", 0.3, accion="caminar", hasta=0.4, escala=0.85)],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.2}], camara="acercar_rapido", portada=True)
S("montana", "¿Por qué Dios le pidió algo así? ¿Y qué pasó en la cima de esa montaña? Para entenderlo, tenemos que volver muchos años atrás, a una ciudad llamada Ur.",
  [P("abraham", 0.5, **VIEJO, emocion="triste")], efectos=[{"tipo": "flash", "inicio": 0.85}], camara="acercar")

# ---------- 1. EL LLAMADO ----------
S("ciudad", "Abram vivía en Ur de los caldeos, una de las ciudades más ricas y avanzadas del mundo antiguo. Tenía casa, familia, ganado y una vida cómoda.",
  [P("abraham", 0.4, emocion="feliz"), P("sara", 0.6, mira="izquierda", emocion="feliz")], [gente(0.75, 0.55)],
  rotulo="CAPÍTULO 1: EL LLAMADO", camara="paneo")
S("ciudad", "Pero en Ur la gente adoraba a muchos dioses: a la luna, al sol, a estatuas de piedra y de madera. Nadie conocía al Dios verdadero.",
  [P("hombre2", 0.4, accion="arrodillarse"), P("mujer1", 0.6, accion="orar")], [{"tipo": "columna", "x": 0.8, "escala": 0.7}], camara="acercar")
S("campo", "Un día, Dios le habló a Abram: Vete de tu tierra, de tu parentela y de la casa de tu padre, a la tierra que yo te mostraré.",
  [P("abraham", 0.45, emocion="sorprendido")], efectos=[{"tipo": "luz", "x": 0.7}, {"tipo": "brillo", "x": 0.7, "y": -600}], camara="acercar")
S("campo", "Y te haré una gran nación, te bendeciré, y engrandeceré tu nombre. En ti serán benditas todas las familias de la tierra.",
  [P("abraham", 0.45, accion="arrodillarse")], efectos=[{"tipo": "luz"}], camara="fijo")
S("campo", "Imagínate lo que Dios le estaba pidiendo: dejar todo lo que conocía, sin saber siquiera a dónde iba. No había mapa, no había dirección. Solo una promesa.",
  [P("abraham", 0.5, emocion="sorprendido", accion="temblar")], camara="acercar_rapido")
S("camino", "Y Abram obedeció. Tenía setenta y cinco años. Tomó a su esposa Sarai, a su sobrino Lot, a sus siervos y sus animales... y se puso en camino.",
  [P("abraham", 0.25, hasta=0.55, accion="caminar"), P("sara", 0.12, hasta=0.42, accion="caminar"), P("burro", 0.0, hasta=0.25, accion="caminar"), P("oveja1", 0.7)],
  camara="paneo")
S("desierto", "Caminaron cientos de kilómetros por el desierto, durante semanas, hasta llegar a la tierra de Canaán. Y ahí Dios le dijo: A tu descendencia daré esta tierra.",
  [P("abraham", 0.45, accion="levantar", emocion="feliz")], [{"tipo": "altar", "x": 0.68}], efectos=[{"tipo": "luz"}, {"tipo": "fuego", "x": 0.68, "y": -120, "tamano": 0.5}],
  camara="alejar")
S("cielo", "Pero había un problema enorme. Abram y Sarai no tenían hijos. Y Sarai no podía tenerlos. ¿Cómo iba a ser padre de una gran nación?",
  [P("abraham", 0.4), P("sara", 0.6, mira="izquierda", emocion="triste")], efectos=[{"tipo": "oscuridad", "fuerza": 0.25}], camara="acercar")

# ---------- 2. LOT ----------
S("campo", "Dios bendijo tanto a Abram y a Lot, que sus rebaños crecieron muchísimo. Tanto, que ya no cabían juntos, y sus pastores empezaron a pelear.",
  [P("pastor1", 0.35, accion="senalar", emocion="enojado"), P("pastor2", 0.6, mira="izquierda", emocion="enojado"), P("oveja1", 0.8), P("oveja2", 0.15)],
  rotulo="CAPÍTULO 2: EL SOBRINO", camara="paneo")
S("montana", "Abram, como buen tío, le dijo a Lot: No haya pleito entre nosotros, porque somos familia. Escoge tú primero. Si vas a la izquierda, yo iré a la derecha.",
  [P("abraham", 0.4, **{}, accion="senalar", emocion="feliz"), P("hombre2", 0.62, mira="izquierda")], habla="abraham", camara="acercar")
S("valle", "Lot miró a su alrededor y escogió lo mejor: el valle verde y lleno de agua, cerca de las ciudades de Sodoma y Gomorra. Abram se quedó con lo que sobró.",
  [P("hombre2", 0.4, accion="senalar", emocion="feliz")], [gente(0.75, 0.5)], camara="paneo")
S("noche", "Pero esa misma noche Dios le dijo a Abram: Levanta tus ojos y mira hacia el norte, el sur, el este y el oeste. Toda la tierra que ves, te la daré a ti para siempre.",
  [P("abraham", 0.5, accion="alabar", emocion="sorprendido")], [{"tipo": "estrella", "x": 0.3, "y": -650}, {"tipo": "estrella", "x": 0.7, "y": -700}],
  efectos=[{"tipo": "luz"}], camara="alejar")
S("cielo", "El que cede con generosidad nunca pierde con Dios. Si crees eso, escribe en los comentarios: Dios es mi recompensa.",
  [P("abraham", 0.5, accion="orar")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 3. LAS ESTRELLAS ----------
S("noche", "Pasaron los años y el hijo no llegaba. Una noche Abram le dijo a Dios con tristeza: ¿De qué me sirve todo lo que me das, si no tengo hijos?",
  [P("abraham", 0.5, **VIEJO, emocion="triste", accion="arrodillarse")], rotulo="CAPÍTULO 3: LAS ESTRELLAS", camara="acercar")
S("noche", "Entonces Dios lo llevó afuera y le dijo: Mira al cielo y cuenta las estrellas, si es que puedes contarlas. Así será tu descendencia.",
  [P("abraham", 0.45, **VIEJO, accion="levantar", emocion="sorprendido")],
  [{"tipo": "estrella", "x": 0.2, "y": -700}, {"tipo": "estrella", "x": 0.4, "y": -760}, {"tipo": "estrella", "x": 0.65, "y": -690}, {"tipo": "estrella", "x": 0.85, "y": -740}],
  efectos=[{"tipo": "brillo", "y": -650}], camara="alejar")
S("noche", "Y la Biblia dice algo muy importante: Abram creyó a Dios, y Dios se lo contó por justicia. No tenía pruebas. Solo tenía la palabra de Dios. Y eso le bastó.",
  [P("abraham", 0.5, **VIEJO, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}], camara="acercar")
S("campo", "Pero Sarai se cansó de esperar. Le dijo a Abram: Toma a mi sierva Agar; quizás tenga un hijo por medio de ella. Y así nació Ismael.",
  [P("sara", 0.35, **SARA_V, accion="senalar", emocion="triste"), P("criada", 0.6), P("abraham", 0.8, mira="izquierda", **VIEJO)], camara="paneo")
S("campo", "Pero ese no era el plan de Dios. Y en vez de traer alegría, trajo celos, peleas y lágrimas a la familia. Cuando tratamos de adelantar los tiempos de Dios, las cosas se complican.",
  [P("sara", 0.35, **SARA_V, emocion="enojado"), P("criada", 0.65, mira="izquierda", emocion="llorando")], efectos=[{"tipo": "oscuridad", "fuerza": 0.2}], camara="acercar")

# ---------- 4. NOMBRES NUEVOS ----------
S("cielo", "Cuando Abram tenía noventa y nueve años, Dios se le apareció otra vez: Yo soy el Dios Todopoderoso. Ya no te llamarás Abram, sino Abraham, que significa padre de muchas naciones.",
  [P("abraham", 0.5, **VIEJO, accion="arrodillarse", emocion="sorprendido")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}],
  rotulo="CAPÍTULO 4: LA RISA", camara="acercar")
S("cielo", "Y a Sarai la llamarás Sara, que significa princesa. Porque de ella nacerá un hijo, y será madre de naciones y de reyes.",
  [P("sara", 0.5, **SARA_V, emocion="sorprendido")], efectos=[{"tipo": "luz"}], camara="fijo")
S("desierto", "Un día de mucho calor, Abraham estaba sentado a la puerta de su tienda, cuando vio a tres hombres parados frente a él. Corrió a recibirlos y les preparó comida.",
  [P("abraham", 0.35, **VIEJO, accion="correr", hasta=0.45), P("angel", 0.68, mira="izquierda"), P("hombre1", 0.82, mira="izquierda", tunica="#f4f1ea")],
  camara="paneo")
S("desierto", "Uno de ellos le dijo: El año que viene, por este tiempo, Sara tu mujer tendrá un hijo.",
  [P("angel", 0.6, mira="izquierda", accion="senalar"), P("abraham", 0.35, **VIEJO, emocion="sorprendido")], habla="angel", camara="acercar")
S("desierto", "Sara estaba escuchando detrás de la tienda... y se rió por dentro. ¿Yo, a mis noventa años, voy a tener un hijo?",
  [P("sara", 0.5, **SARA_V, emocion="burlon", accion="celebrar")], habla="sara", camara="acercar_rapido")
S("desierto", "Y el Señor preguntó: ¿Por qué se ha reído Sara? ¿Hay algo que sea imposible para Dios?",
  [P("angel", 0.5, accion="senalar")], efectos=[{"tipo": "luz"}, {"tipo": "brillo"}], habla="angel", camara="acercar")
S("cielo", "Esa pregunta es para ti también. ¿Hay algo imposible para Dios? Respóndela en los comentarios. Yo ya sé mi respuesta.",
  [P("abraham", 0.5, **VIEJO, accion="senalar", emocion="feliz")], efectos=[{"tipo": "luz"}], rotulo="¿HAY ALGO IMPOSIBLE?", camara="fijo")

S("desierto", "Antes de irse, los visitantes miraron hacia Sodoma. Y Dios le contó a Abraham que iba a juzgar esa ciudad, porque su maldad era terrible. Allí vivía Lot, su sobrino.",
  [P("angel", 0.65, mira="izquierda", accion="senalar"), P("abraham", 0.38, **VIEJO, emocion="asustado")], efectos=[{"tipo": "oscuridad", "fuerza": 0.25}], camara="acercar")
S("desierto", "Entonces Abraham se acercó y se atrevió a negociar con Dios: ¿Destruirás al justo junto con el malvado? Si hay cincuenta justos en la ciudad, ¿no la perdonarás?",
  [P("abraham", 0.45, **VIEJO, accion="ofrecer", emocion="valiente")], habla="abraham", camara="acercar")
S("desierto", "Y Dios respondió: Si encuentro cincuenta justos, perdonaré a toda la ciudad. ¿Y si son cuarenta y cinco? ¿Y si son treinta? ¿Y veinte? ¿Y si solo hay diez?",
  [P("abraham", 0.45, **VIEJO, accion="arrodillarse", emocion="triste")], efectos=[{"tipo": "luz", "x": 0.7}], camara="fijo")
S("desierto", "Y Dios le dijo: Por amor a diez, no la destruiré. Pero ni siquiera había diez justos en Sodoma.",
  [P("abraham", 0.5, **VIEJO, emocion="triste")], efectos=[{"tipo": "oscuridad", "fuerza": 0.3}], camara="acercar")
S("ciudad", "A la mañana siguiente cayó fuego y azufre del cielo sobre Sodoma y Gomorra. Pero antes, los ángeles sacaron a Lot y a sus hijas de la mano y los pusieron a salvo. Dios había escuchado la oración de Abraham.",
  [P("hombre2", 0.3, accion="correr", hasta=0.08, emocion="asustado"), P("angel", 0.45, accion="correr", hasta=0.2)],
  efectos=[{"tipo": "fuego", "x": 0.7, "tamano": 2.2, "crece": True}, {"tipo": "fuego", "x": 0.9, "tamano": 1.8, "crece": True}, {"tipo": "temblor", "inicio": 0.3, "fin": 0.9}],
  camara="acercar_rapido")
S("cielo", "Tus oraciones por tu familia sí cuentan. Abraham oró por Lot, y Lot fue salvado. Escribe el nombre de alguien de tu familia por quien estás orando.",
  [P("abraham", 0.5, **VIEJO, accion="orar")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 5. ISAAC ----------
S("campo", "Y tal como Dios lo prometió, un año después, Sara dio a luz un hijo. Abraham tenía cien años, y Sara noventa.",
  [P("sara", 0.45, **SARA_V, accion="abrazar", emocion="feliz"), P("abraham", 0.65, mira="izquierda", **VIEJO, accion="celebrar", emocion="feliz")],
  [{"tipo": "pesebre", "x": 0.55, "escala": 0.7}], efectos=[{"tipo": "luz"}, {"tipo": "brillo"}], rotulo="CAPÍTULO 5: EL HIJO DE LA PROMESA", camara="acercar")
S("campo", "Le pusieron por nombre Isaac, que significa risa. Y Sara dijo: Dios me ha hecho reír, y todos los que lo oigan se reirán conmigo.",
  [P("sara", 0.4, **SARA_V, accion="celebrar", emocion="feliz"), P("abraham", 0.6, **VIEJO, accion="alabar", emocion="feliz")], habla="sara", camara="paneo")
S("campo", "Veinticinco años esperando. Veinticinco años de promesas que parecían imposibles. Pero Dios nunca llega tarde.",
  [P("isaac", 0.45, escala=0.7, accion="saltar", emocion="feliz"), P("abraham", 0.65, mira="izquierda", **VIEJO, emocion="feliz")], efectos=[{"tipo": "luz"}], camara="acercar")
S("campo", "Isaac creció, y era la alegría de sus padres. Abraham le enseñaba a cuidar las ovejas, a orar y a confiar en el Dios que había hecho posible su nacimiento. Abraham lo amaba con todo su corazón.",
  [P("isaac", 0.4, escala=0.85, emocion="feliz"), P("abraham", 0.6, **VIEJO, accion="abrazar", emocion="feliz")], camara="fijo")

# ---------- 6. LA PRUEBA ----------
S("noche", "Pero un día, Dios probó a Abraham. Le dijo: Toma a tu hijo, tu único hijo Isaac, a quien amas, y ve a la tierra de Moriah. Allí ofrécelo en sacrificio sobre uno de los montes.",
  [P("abraham", 0.5, **VIEJO, accion="temblar", emocion="asustado")], efectos=[{"tipo": "oscuridad", "fuerza": 0.4}, {"tipo": "rayo", "inicio": 0.8}],
  rotulo="CAPÍTULO 6: LA PRUEBA", camara="acercar_rapido")
S("noche", "¿Cómo podía Dios pedirle eso? Isaac era el hijo de la promesa. Sin Isaac, no habría gran nación. No tenía sentido.",
  [P("abraham", 0.5, **VIEJO, accion="arrodillarse", emocion="llorando")], efectos=[{"tipo": "oscuridad", "fuerza": 0.4}], camara="acercar")
S("camino", "Pero Abraham se levantó muy temprano, preparó el burro, cortó la leña y salió con Isaac y dos siervos. Caminaron tres días.",
  [P("abraham", 0.3, hasta=0.55, **VIEJO, accion="caminar"), P("isaac", 0.18, hasta=0.42, accion="caminar", escala=0.85), P("burro", 0.05, hasta=0.28, accion="caminar")],
  rotulo="3 DÍAS", camara="paneo")
S("montana", "Al tercer día vio el monte a lo lejos. Les dijo a los siervos: Quédense aquí. El muchacho y yo iremos a adorar... y volveremos a ustedes.",
  [P("abraham", 0.4, **VIEJO, accion="senalar"), P("hombre1", 0.65, mira="izquierda"), P("isaac", 0.25, escala=0.85)], habla="abraham", camara="acercar")
S("montana", "¿Te diste cuenta? Dijo: volveremos. Abraham creía que, pasara lo que pasara, Dios cumpliría su promesa. Aunque tuviera que resucitar a Isaac.",
  [P("abraham", 0.5, **VIEJO, emocion="valiente")], efectos=[{"tipo": "luz"}], camara="fijo")
S("montana", "Isaac cargaba la leña, y Abraham llevaba el fuego y el cuchillo. Y entonces Isaac preguntó: Padre, aquí está el fuego y la leña... pero ¿dónde está el cordero?",
  [P("isaac", 0.35, accion="caminar", hasta=0.42, escala=0.85, emocion="sorprendido"), P("abraham", 0.6, **VIEJO, accion="caminar", hasta=0.65, emocion="triste")],
  habla="isaac", camara="acercar")
S("montana", "Y Abraham respondió: Dios proveerá el cordero, hijo mío.",
  [P("abraham", 0.5, **VIEJO, emocion="llorando", accion="abrazar"), P("isaac", 0.32, escala=0.85, accion="abrazar")], habla="abraham", camara="acercar_rapido")

# ---------- 7. DIOS PROVEE ----------
S("montana", "En la cima, Abraham construyó un altar, acomodó la leña... y ató a su hijo sobre el altar. Isaac no se resistió. Confió en su padre.",
  [P("abraham", 0.5, **VIEJO, accion="levantar", emocion="llorando"), P("isaac", 0.68, accion="dormir", escala=0.85)], [{"tipo": "altar", "x": 0.68}],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.3}], rotulo="CAPÍTULO 7: DIOS PROVEERÁ", camara="acercar")
S("montana", "Abraham levantó el cuchillo con la mano temblando...",
  [P("abraham", 0.5, **VIEJO, accion="levantar", emocion="llorando", objeto="espada")], efectos=[{"tipo": "temblor", "inicio": 0.3, "fin": 0.9}], camara="acercar_rapido")
S("montana", "¡Abraham! ¡Abraham! Era el ángel del Señor llamándolo desde el cielo. ¡No le hagas nada al muchacho! Ya sé que temes a Dios, porque no me negaste a tu único hijo.",
  [P("angel", 0.75, mira="izquierda", accion="senalar"), P("abraham", 0.45, **VIEJO, emocion="sorprendido")], habla="angel",
  efectos=[{"tipo": "flash", "inicio": 0.05}, {"tipo": "luz", "x": 0.75}, {"tipo": "brillo", "x": 0.75}], camara="acercar")
S("montana", "Abraham alzó los ojos... y vio un carnero atrapado por los cuernos en un arbusto. Dios había provisto el cordero.",
  [P("carnero", 0.72, accion="temblar"), P("abraham", 0.4, **VIEJO, emocion="feliz", accion="senalar")], [{"tipo": "arbol", "x": 0.75, "escala": 0.5}],
  efectos=[{"tipo": "luz", "x": 0.72}], camara="acercar_rapido")
S("montana", "Desató a Isaac, lo abrazó con todas sus fuerzas, y ofreció el carnero en su lugar. Y llamó a ese lugar: Jehová Jireh, que significa el Señor proveerá.",
  [P("abraham", 0.45, **VIEJO, accion="abrazar", emocion="llorando"), P("isaac", 0.62, mira="izquierda", accion="abrazar", escala=0.85, emocion="feliz")],
  [{"tipo": "altar", "x": 0.82}], efectos=[{"tipo": "fuego", "x": 0.82, "y": -120, "tamano": 0.6}, {"tipo": "luz"}], rotulo="JEHOVÁ JIREH", camara="acercar")
S("cielo", "Y el ángel repitió la promesa: Por cuanto has hecho esto, multiplicaré tu descendencia como las estrellas del cielo y como la arena del mar.",
  [P("abraham", 0.5, **VIEJO, accion="alabar", emocion="feliz")], [{"tipo": "estrella", "x": 0.3, "y": -700}, {"tipo": "estrella", "x": 0.7, "y": -720}],
  efectos=[{"tipo": "brillo", "y": -650}], camara="alejar")

# ---------- 8. EL CORDERO ----------
S("cielo", "Siglos después, en ese mismo monte de Moriah se construyó Jerusalén. Y muy cerca de ahí, otro Padre entregó a su único Hijo.",
  [P("jesus", 0.5, accion="ofrecer", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="CAPÍTULO 8: EL CORDERO DE DIOS", camara="acercar")
S("cielo", "Isaac fue salvado porque un carnero murió en su lugar. Y nosotros somos salvados porque Jesús, el Cordero de Dios, murió en el nuestro. Esta vez, Dios no detuvo el cuchillo.",
  [P("jesus", 0.5, accion="alabar")], [{"tipo": "cruz_vacia", "x": 0.75, "escala": 0.6}], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- ENSEÑANZA Y FINAL ----------
S("cielo", "Abraham es llamado el padre de la fe. No porque nunca dudó, sino porque siguió confiando cuando no entendía nada.",
  [P("abraham", 0.5, **VIEJO, accion="orar")], efectos=[{"tipo": "luz"}], rotulo="ENSEÑANZA", camara="acercar")
S("cielo", "Hoy millones de personas en el mundo lo consideran su padre en la fe. Las estrellas que no podía contar... somos nosotros.",
  [P("abraham", 0.5, **VIEJO, accion="alabar", emocion="feliz")], [{"tipo": "estrella", "x": 0.25, "y": -700}, {"tipo": "estrella", "x": 0.75, "y": -720}],
  efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="alejar")
S("cielo", "¿Qué promesa de Dios llevas años esperando? Escríbela en los comentarios. Si Dios cumplió a Abraham a los cien años, también puede cumplirte a ti.",
  [P("abraham", 0.4, **VIEJO, accion="senalar"), P("sara", 0.62, mira="izquierda", **SARA_V, emocion="feliz")], efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "Suscríbete y activa la campanita, que mañana llega otra gran historia de la Biblia. ¡Dios te bendiga!",
  [P("abraham", 0.5, **VIEJO, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="¡SUSCRÍBETE!", pausa=2.0, camara="acercar")

guardar("08_abraham_la_historia_completa.json", "Abraham - El Padre de la Fe",
        "Dios le pidió lo que más amaba... ¿lo entregaría?",
        ["ABRAHAM", "SARA", "ISAAC", "PROMESA", "ESTRELLAS", "CORDERO", "PROVEERÁ", "FE"],
        miniatura={"texto": ["LA PRUEBA", "MÁS DIFÍCIL"],
                   "escena": {"fondo": "montana", "personajes": [
                       {"id": "abraham", "x": 0.62, "accion": "levantar", "emocion": "llorando", "barba": "#e8e4dc", "pelo": "#e8e4dc", "escala": 1.3},
                       {"id": "angel", "x": 0.86, "mira": "izquierda", "accion": "senalar", "escala": 1.2}],
                       "cosas": [{"tipo": "altar", "x": 0.74}], "efectos": [{"tipo": "luz", "x": 0.86}, {"tipo": "brillo", "x": 0.86}]}})
