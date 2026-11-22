"""Video largo: Sansón, la historia completa."""
from base import S, P, gente, guardar

CIEGO = {"venda": True, "emocion": "triste"}

# ---------- APERTURA EN FRÍO ----------
S("templo", "Tres mil personas se burlan de él. Está ciego, encadenado entre dos columnas gigantes. Era el hombre más fuerte que jamás existió... y ahora es un esclavo.",
  [P("sanson", 0.5, accion="empujar", **CIEGO)], [{"tipo": "columna", "x": 0.3}, {"tipo": "columna", "x": 0.7}, gente(0.5, 0.55, y=-200, variante="soldados")],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.3}], camara="acercar_rapido", portada=True)
S("templo", "¿Cómo perdió su fuerza? ¿Y qué hizo en ese último momento? Para entenderlo, tenemos que ir al día en que un ángel anunció su nacimiento.",
  [P("sanson", 0.5, **CIEGO, accion="orar")], [{"tipo": "columna", "x": 0.3}, {"tipo": "columna", "x": 0.7}], efectos=[{"tipo": "flash", "inicio": 0.85}], camara="acercar")

# ---------- 1. UN NIÑO PROMETIDO ----------
S("campo", "En aquellos días, el pueblo de Israel había olvidado a Dios. Y durante cuarenta años, los filisteos los dominaban y los oprimían.",
  [P("filisteo1", 0.35, objeto="espada", emocion="burlon"), P("hombre2", 0.62, accion="agacharse", emocion="triste")], efectos=[{"tipo": "oscuridad", "fuerza": 0.25}],
  rotulo="CAPÍTULO 1: EL NIÑO PROMETIDO", camara="paneo")
S("campo", "Había un hombre llamado Manoa, de la tribu de Dan, cuya esposa no podía tener hijos. Un día, a ella se le apareció el ángel del Señor.",
  [P("mujer1", 0.4, emocion="sorprendido"), P("angel", 0.68, mira="izquierda")], efectos=[{"tipo": "luz", "x": 0.68}, {"tipo": "brillo", "x": 0.68}], camara="acercar")
S("campo", "Vas a tener un hijo, le dijo. Nunca se cortará el cabello, porque será nazareo, consagrado a Dios desde antes de nacer. Y él comenzará a liberar a Israel de los filisteos.",
  [P("angel", 0.6, mira="izquierda", accion="senalar"), P("mujer1", 0.35, accion="arrodillarse", emocion="feliz")], habla="angel", camara="fijo")
S("campo", "Manoa ofreció un sacrificio a Dios sobre una roca. Y cuando la llama subió hacia el cielo, el ángel subió dentro del fuego del altar. Manoa y su esposa cayeron rostro en tierra.",
  [P("hombre1", 0.3, accion="arrodillarse", emocion="sorprendido"), P("mujer1", 0.5, accion="arrodillarse", emocion="sorprendido")], [{"tipo": "altar", "x": 0.72}],
  efectos=[{"tipo": "fuego", "x": 0.72, "y": -120, "tamano": 1.4, "crece": True}, {"tipo": "brillo", "x": 0.72, "y": -600}], camara="acercar")
S("campo", "Y así nació Sansón. El niño creció, y el Señor lo bendecía. Su cabello largo era la señal de su promesa con Dios.",
  [P("sanson", 0.45, escala=0.8, emocion="feliz", accion="celebrar"), P("mujer1", 0.68, mira="izquierda", emocion="feliz")], efectos=[{"tipo": "luz"}], camara="acercar")

# ---------- 2. EL LEÓN ----------
S("camino", "Ya joven, Sansón bajó un día a la ciudad de Timnat. Y de repente, entre las viñas, un león joven salió rugiendo contra él.",
  [P("sanson", 0.3, accion="caminar", hasta=0.35), P("leon1", 0.75, mira="izquierda", accion="rugir")], efectos=[{"tipo": "temblor", "inicio": 0.6, "fin": 0.75}],
  rotulo="CAPÍTULO 2: LA FUERZA DE DIOS", camara="acercar_rapido")
S("camino", "Sansón no tenía nada en las manos. Pero el Espíritu del Señor vino sobre él con poder... y despedazó al león como si fuera un cabrito.",
  [P("sanson", 0.45, accion="empujar", emocion="valiente"), P("leon1", 0.65, accion="caer")], efectos=[{"tipo": "flash", "inicio": 0.4}, {"tipo": "luz"}], camara="acercar_rapido")
S("camino", "Días después pasó por el mismo lugar, y vio que en el cuerpo del león... ¡unas abejas habían hecho un panal de miel!",
  [P("sanson", 0.45, accion="agacharse", emocion="sorprendido")], efectos=[{"tipo": "brillo", "x": 0.6}], camara="acercar")
S("palacio", "En su boda, Sansón les puso una adivinanza a treinta filisteos: Del que come salió comida, y del fuerte salió dulzura. Si la adivinan, les daré treinta trajes.",
  [P("sanson", 0.35, accion="senalar", emocion="burlon"), P("filisteo1", 0.6, mira="izquierda", emocion="sorprendido"), P("filisteo2", 0.78, mira="izquierda")],
  [{"tipo": "mesa", "x": 0.5}], habla="sanson", camara="acercar")
S("palacio", "Pero los filisteos amenazaron a su esposa, y ella le sacó la respuesta llorando. Sansón tuvo que pagar... y desde ese día, la guerra entre él y los filisteos no paró.",
  [P("sanson", 0.4, emocion="enojado"), P("filisteo1", 0.7, mira="izquierda", emocion="burlon")], camara="paneo")

# ---------- 3. UN EJÉRCITO DE UN SOLO HOMBRE ----------
S("trigal", "Una vez, Sansón atrapó trescientas zorras, les ató antorchas en la cola y las soltó en los trigales de los filisteos. Todo se quemó: el trigo, las viñas y los olivos.",
  [P("sanson", 0.25, accion="lanzar", emocion="enojado")], efectos=[{"tipo": "fuego", "x": 0.6, "tamano": 2.0, "crece": True}, {"tipo": "fuego", "x": 0.85, "tamano": 1.6, "crece": True}],
  rotulo="CAPÍTULO 3: UN EJÉRCITO DE UN HOMBRE", camara="paneo")
S("rocas", "Los filisteos mandaron un ejército para capturarlo. Y los mismos israelitas, por miedo, lo ataron con dos cuerdas nuevas y se lo entregaron.",
  [P("sanson", 0.45, accion="quieto", emocion="valiente"), P("hombre1", 0.25, emocion="asustado"), P("hombre2", 0.7, emocion="asustado")], camara="acercar")
S("valle", "Cuando los filisteos lo vieron atado, gritaron de alegría. Pero en ese momento, el Espíritu del Señor vino sobre Sansón...",
  [P("sanson", 0.5, emocion="valiente"), P("filisteo1", 0.75, mira="izquierda", accion="celebrar", emocion="burlon")], [gente(0.8, 0.55, variante="soldados")], camara="acercar_rapido")
S("valle", "...y las cuerdas se rompieron como hilos quemados. Tomó la quijada de un burro que estaba en el suelo... y con ella venció a mil soldados filisteos.",
  [P("sanson", 0.45, accion="levantar", emocion="enojado"), P("filisteo1", 0.7, accion="caer"), P("filisteo2", 0.85, accion="correr", hasta=1.0, emocion="asustado")],
  efectos=[{"tipo": "flash", "inicio": 0.2}, {"tipo": "temblor", "inicio": 0.3, "fin": 0.8}], rotulo="1000", camara="acercar_rapido")
S("desierto", "Después de esa batalla, Sansón tenía tanta sed que sentía que iba a morir. Clamó a Dios, y Dios abrió una roca hueca, y de ella brotó agua. Sansón bebió, y recobró sus fuerzas.",
  [P("sanson", 0.4, accion="arrodillarse", emocion="triste")], [{"tipo": "rocas", "x": 0.65, "escala": 0.6}], efectos=[{"tipo": "agua", "x": 0.62}, {"tipo": "luz", "x": 0.62}], camara="acercar")
S("ciudad", "En otra ocasión, sus enemigos lo encerraron en la ciudad de Gaza. Pero a medianoche, Sansón arrancó las puertas de la ciudad con todo y postes... y se las llevó cargadas a la cima de un monte.",
  [P("sanson", 0.5, accion="levantar", emocion="valiente")], efectos=[{"tipo": "oscuridad", "fuerza": 0.4}, {"tipo": "temblor", "inicio": 0.5, "fin": 0.7}], camara="acercar")
S("cielo", "Pausa. ¿Cuál de las hazañas de Sansón te parece más increíble: el león, los mil soldados o las puertas de Gaza? Escríbelo en los comentarios.",
  [P("sanson", 0.5, accion="levantar", emocion="feliz")], efectos=[{"tipo": "luz"}], rotulo="¿CUÁL?", camara="fijo")
S("cielo", "Sansón fue juez de Israel durante veinte años. Pero tenía una debilidad... y sus enemigos estaban a punto de descubrirla.",
  [P("sanson", 0.5, emocion="feliz")], efectos=[{"tipo": "oscuridad", "fuerza": 0.3}], camara="acercar")

# ---------- 4. DALILA ----------
S("valle", "Sansón se enamoró de una mujer del valle de Sorec. Se llamaba Dalila.",
  [P("sanson", 0.4, emocion="feliz"), P("dalila", 0.62, mira="izquierda", emocion="feliz")], rotulo="CAPÍTULO 4: DALILA", camara="acercar")
S("valle", "Sansón había hecho un voto de no tocar nada impuro y de no cortarse el cabello. Pero poco a poco, fue jugando con su promesa... como si su fuerza fuera suya y no de Dios.",
  [P("sanson", 0.5, emocion="burlon")], efectos=[{"tipo": "oscuridad", "fuerza": 0.2}], camara="acercar")
S("palacio", "Los príncipes de los filisteos fueron a verla en secreto: Descubre de dónde viene su fuerza. Cada uno de nosotros te dará mil cien monedas de plata.",
  [P("filisteo1", 0.35, accion="ofrecer", emocion="burlon"), P("dalila", 0.65, mira="izquierda", emocion="sorprendido")], [{"tipo": "monedas", "x": 0.5}], habla="filisteo1", camara="acercar_rapido")
S("palacio", "Y Dalila aceptó. Esa noche le preguntó con dulzura: Sansón, dime, ¿de dónde viene tu gran fuerza?",
  [P("dalila", 0.4, accion="abrazar", emocion="feliz"), P("sanson", 0.62, mira="izquierda", emocion="feliz")], habla="dalila", camara="acercar")
S("palacio", "Sansón le mintió: Si me atan con siete cuerdas de arco nuevas, seré débil como cualquier hombre. Ella lo ató mientras dormía y gritó: ¡Sansón, los filisteos!",
  [P("sanson", 0.5, accion="dormir"), P("dalila", 0.75, mira="izquierda", accion="senalar", emocion="burlon")], habla="dalila", camara="fijo")
S("palacio", "Y Sansón rompió las cuerdas como si nada. Lo mismo pasó una segunda vez, y una tercera. Dalila estaba furiosa: ¡Me has engañado tres veces!",
  [P("sanson", 0.4, accion="levantar", emocion="burlon"), P("dalila", 0.68, mira="izquierda", emocion="enojado")], efectos=[{"tipo": "flash", "inicio": 0.2}], camara="acercar")
S("palacio", "¿Cómo puedes decir que me amas, si no confías en mí? Día tras día lo presionaba, hasta que Sansón se sintió morir de cansancio.",
  [P("dalila", 0.4, accion="senalar", emocion="llorando"), P("sanson", 0.65, mira="izquierda", emocion="triste")], habla="dalila", camara="acercar")
S("palacio", "Y al final... le contó todo su corazón. Nunca se ha pasado navaja por mi cabeza. Si me cortan el cabello, mi fuerza se irá.",
  [P("sanson", 0.5, accion="agacharse", emocion="triste")], habla="sanson", efectos=[{"tipo": "oscuridad", "fuerza": 0.35}], camara="acercar_rapido")
S("noche", "Dalila supo que esta vez era verdad. Lo hizo dormir sobre sus rodillas... y llamó a un hombre que le cortó las siete trenzas.",
  [P("sanson", 0.45, accion="dormir"), P("dalila", 0.65, mira="izquierda", emocion="burlon"), P("filisteo2", 0.82, mira="izquierda", objeto="espada")],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.5}], camara="acercar")
S("noche", "¡Sansón, los filisteos sobre ti! Él se despertó, pensando: Saldré como las otras veces. Pero no sabía que el Señor ya se había apartado de él.",
  [P("sanson", 0.5, accion="temblar", emocion="sorprendido", pelo_largo=False)], habla="dalila", efectos=[{"tipo": "oscuridad", "fuerza": 0.45}, {"tipo": "temblor", "inicio": 0.3, "fin": 0.5}], camara="acercar_rapido")

# ---------- 5. ESCLAVO ----------
S("prision", "Los filisteos lo atraparon fácilmente. Le sacaron los ojos, lo llevaron a Gaza, lo ataron con cadenas de bronce... y lo pusieron a moler grano en la cárcel, como un animal.",
  [P("sanson", 0.5, accion="empujar", **CIEGO, pelo_largo=False)], [{"tipo": "piedra", "x": 0.68, "escala": 0.8}], efectos=[{"tipo": "oscuridad", "fuerza": 0.4}],
  rotulo="CAPÍTULO 5: CAÍDO", camara="acercar")
S("prision", "El hombre más fuerte del mundo, el juez de Israel... ahora era un prisionero ciego, dando vueltas a una piedra de molino día tras día.",
  [P("sanson", 0.5, accion="caminar", hasta=0.55, **CIEGO, pelo_largo=False)], [{"tipo": "piedra", "x": 0.7, "escala": 0.8}], efectos=[{"tipo": "oscuridad", "fuerza": 0.4}], camara="alejar")
S("prision", "Pero la Biblia guarda un pequeño detalle lleno de esperanza: el cabello de su cabeza comenzó a crecer otra vez.",
  [P("sanson", 0.5, **CIEGO, accion="orar")], efectos=[{"tipo": "luz", "x": 0.5}], camara="acercar")
S("cielo", "Si alguna vez sentiste que arruinaste todo, escribe en los comentarios: Dios no ha terminado conmigo. Porque esta historia todavía no termina.",
  [P("sanson", 0.5, **CIEGO, accion="orar")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 6. EL ÚLTIMO ACTO ----------
S("templo", "Un día, los filisteos hicieron una gran fiesta en el templo de su dios Dagón. ¡Nuestro dios nos entregó a Sansón!, cantaban.",
  [], [{"tipo": "columna", "x": 0.3}, {"tipo": "columna", "x": 0.7}, gente(0.5, 0.65, y=-150, variante="soldados")], efectos=[{"tipo": "fuego", "x": 0.5, "y": -300, "tamano": 0.8}],
  rotulo="CAPÍTULO 6: EL ÚLTIMO ACTO", camara="alejar")
S("templo", "Traigan a Sansón para que nos divierta. Y lo sacaron de la cárcel para burlarse de él delante de todos. El templo estaba lleno, y en el techo había unas tres mil personas más.",
  [P("sanson", 0.5, **CIEGO, accion="caminar", hasta=0.5), P("filisteo1", 0.25, accion="senalar", emocion="burlon"), P("filisteo2", 0.8, mira="izquierda", accion="celebrar", emocion="burlon")],
  [{"tipo": "columna", "x": 0.35, "profundidad": -60}, {"tipo": "columna", "x": 0.65, "profundidad": -60}], camara="paneo")
S("templo", "Sansón le pidió al muchacho que lo guiaba: Déjame tocar las columnas que sostienen el templo, para apoyarme en ellas.",
  [P("nino", 0.3, emocion="triste"), P("sanson", 0.5, **CIEGO)], [{"tipo": "columna", "x": 0.38}, {"tipo": "columna", "x": 0.62}], habla="sanson", camara="acercar")
S("templo", "Y entonces Sansón oró: Señor, acuérdate de mí. Dame fuerzas solo una vez más.",
  [P("sanson", 0.5, **CIEGO, accion="orar")], [{"tipo": "columna", "x": 0.38}, {"tipo": "columna", "x": 0.62}], habla="sanson", efectos=[{"tipo": "luz", "x": 0.5}], camara="acercar")
S("templo", "Puso una mano en cada columna... empujó con todas sus fuerzas... y gritó: ¡Muera yo con los filisteos!",
  [P("sanson", 0.5, accion="empujar", **CIEGO)], [{"tipo": "columna", "x": 0.38, "caer": True, "mira": "izquierda", "caer_desde": 0.55, "caer_hasta": 0.95}, {"tipo": "columna", "x": 0.62, "caer": True, "caer_desde": 0.55, "caer_hasta": 0.95}],
  efectos=[{"tipo": "temblor", "inicio": 0.3, "fin": 1.0}, {"tipo": "luz"}], camara="acercar_rapido")
S("templo", "Las columnas cedieron... y el templo entero se vino abajo sobre los príncipes y sobre todo el pueblo que estaba ahí.",
  [], [{"tipo": "columna", "x": 0.3, "caer": True, "mira": "izquierda", "caer_desde": 0, "caer_hasta": 0.01}, {"tipo": "columna", "x": 0.7, "caer": True, "caer_desde": 0, "caer_hasta": 0.01}, {"tipo": "rocas", "x": 0.5, "escala": 0.9}],
  efectos=[{"tipo": "temblor", "inicio": 0.0, "fin": 0.8}, {"tipo": "flash", "inicio": 0.3}, {"tipo": "oscuridad", "fuerza": 0.4}], camara="alejar")
S("cielo", "En su muerte, Sansón venció a más enemigos que en toda su vida. Dios escuchó su última oración.",
  [P("sanson", 0.5, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="acercar")

# ---------- ENSEÑANZA Y FINAL ----------
S("cielo", "La fuerza de Sansón nunca estuvo en su cabello. Estaba en su promesa con Dios. El cabello solo era la señal.",
  [P("sanson", 0.5, accion="orar")], efectos=[{"tipo": "luz"}], rotulo="ENSEÑANZA", camara="acercar")
S("cielo", "Y aunque Sansón falló muchas veces, Dios lo escuchó cuando volvió a él con humildad. Mientras haya vida, nunca es tarde para decir: Señor, acuérdate de mí.",
  [P("sanson", 0.5, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="fijo")
S("cielo", "¿Qué crees que fue lo que más debilitó a Sansón: Dalila, su orgullo o haberse alejado de Dios? Respóndeme en los comentarios.",
  [P("sanson", 0.4, accion="senalar"), P("dalila", 0.65, mira="izquierda")], efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "Suscríbete y activa la campanita, que mañana llega otra gran historia de la Biblia. ¡Dios te bendiga!",
  [P("sanson", 0.5, accion="levantar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="¡SUSCRÍBETE!", pausa=2.0, camara="acercar")

guardar("07_sanson_la_historia_completa.json", "Sansón - La Historia Completa",
        "El hombre más FUERTE del mundo... perdió todo por un SECRETO.",
        ["SANSÓN", "DALILA", "FILISTEOS", "FUERZA", "CABELLO", "LEÓN", "COLUMNAS", "SEÑOR"])
