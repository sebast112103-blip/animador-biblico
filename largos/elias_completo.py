"""Video largo: Elías, la historia completa."""
from base import S, P, gente, guardar

EL = {"objeto": "cayado"}
ACAB = {"tocado": "corona", "manto": "#6a2a6a"}

# ---------- APERTURA EN FRÍO ----------
S("montana", "Cuatrocientos cincuenta profetas gritan, saltan y se cortan con cuchillos desde la mañana hasta la tarde. Y frente a ellos, un solo hombre los mira... y se burla.",
  [P("profeta_baal1", 0.25, accion="saltar", emocion="enojado"), P("profeta_baal2", 0.42, accion="alabar", emocion="enojado"), P("elias", 0.78, mira="izquierda", emocion="burlon", **EL)],
  [{"tipo": "altar", "x": 0.33}], camara="acercar_rapido", portada=True)
S("montana", "¿Qué pasó cuando ese hombre oró? ¿Y por qué después quiso morir? Esta es la historia de Elías, el profeta del fuego.",
  [P("elias", 0.5, emocion="valiente", **EL)], efectos=[{"tipo": "flash", "inicio": 0.85}], camara="acercar")

# ---------- 1. EL REY MALVADO ----------
S("palacio", "Israel estaba gobernado por Acab, el rey más malvado que había tenido hasta entonces. Se casó con Jezabel, una princesa extranjera que adoraba al dios Baal.",
  [P("acab", 0.45, **ACAB, emocion="burlon"), P("jezabel", 0.65, mira="izquierda", emocion="burlon")], [{"tipo": "trono", "x": 0.55, "profundidad": -30}],
  rotulo="CAPÍTULO 1: LA SEQUÍA", camara="paneo")
S("palacio", "Jezabel construyó templos para Baal, persiguió y mató a los profetas del Señor, y llevó a todo el pueblo a adorar ídolos.",
  [P("jezabel", 0.5, accion="senalar", emocion="enojado"), P("soldado1", 0.75, mira="izquierda", objeto="lanza")], efectos=[{"tipo": "oscuridad", "fuerza": 0.3}],
  camara="acercar")
S("palacio", "Baal era considerado el dios de la lluvia y de las cosechas. Y un día, un profeta desconocido llamado Elías se presentó ante el rey con un mensaje.",
  [P("elias", 0.3, **EL, accion="caminar", hasta=0.38, emocion="valiente"), P("acab", 0.72, mira="izquierda", **ACAB, emocion="sorprendido")], camara="paneo")
S("palacio", "¡Vive el Señor, Dios de Israel, que no habrá lluvia ni rocío en estos años, sino por mi palabra!",
  [P("elias", 0.4, **EL, accion="senalar", emocion="enojado")], habla="elias", efectos=[{"tipo": "temblor", "inicio": 0.6, "fin": 0.8}, {"tipo": "rayo", "inicio": 0.85}],
  camara="acercar_rapido")
S("desierto", "Y dejó de llover. Un mes, dos meses, un año... tres años y medio sin una sola gota. Los ríos se secaron y los campos se volvieron polvo. El supuesto dios de la lluvia no podía hacer nada.",
  [P("hombre2", 0.4, accion="agacharse", emocion="triste")], efectos=[{"tipo": "oscuridad", "fuerza": 0.15}], rotulo="3 AÑOS Y MEDIO", camara="alejar")

# ---------- 2. LOS CUERVOS Y LA VIUDA ----------
S("rocas", "Dios escondió a Elías junto a un arroyo llamado Querit. Y cada mañana y cada tarde, unos cuervos le traían pan y carne en el pico. Elías bebía del arroyo.",
  [P("elias", 0.45, **EL, accion="agacharse", emocion="feliz")], efectos=[{"tipo": "agua", "x": 0.6}, {"tipo": "brillo", "x": 0.55, "y": -500}],
  rotulo="CAPÍTULO 2: LA HARINA Y EL ACEITE", camara="acercar")
S("rocas", "Pero un día el arroyo también se secó. Y Dios le dijo: Ve a Sarepta. Allí le he ordenado a una viuda que te dé de comer.",
  [P("elias", 0.5, **EL, emocion="sorprendido")], efectos=[{"tipo": "luz", "x": 0.7}], camara="fijo")
S("ciudad", "En la entrada de la ciudad, Elías vio a una mujer recogiendo leña. Le pidió: Por favor, tráeme un poco de agua... y un pedazo de pan.",
  [P("elias", 0.3, **EL, accion="ofrecer"), P("mujer1", 0.65, mira="izquierda", accion="agacharse", tunica="#4a4a5a")], habla="elias", camara="acercar")
S("ciudad", "La mujer respondió llorando: No tengo pan. Solo me queda un puñado de harina y un poco de aceite. Estaba recogiendo leña para cocinar lo último... comerlo con mi hijo, y después morir.",
  [P("mujer1", 0.55, mira="izquierda", tunica="#4a4a5a", emocion="llorando"), P("nino", 0.72, mira="izquierda", emocion="triste")], habla="mujer1", camara="acercar")
S("ciudad", "Elías le dijo: No tengas miedo. Hazme primero a mí un pequeño pan. Porque así dice el Señor: la harina no se acabará y el aceite no faltará, hasta el día en que vuelva a llover.",
  [P("elias", 0.35, **EL, accion="senalar", emocion="feliz")], habla="elias", efectos=[{"tipo": "luz"}], camara="fijo")
S("ciudad", "¡Qué fe tuvo esa mujer! Le dio su última comida a un desconocido. Y desde ese día, cada vez que metía la mano en la vasija, había harina. Y en la jarra, siempre había aceite.",
  [P("mujer1", 0.45, accion="celebrar", emocion="feliz", tunica="#4a4a5a"), P("nino", 0.65, accion="saltar", emocion="feliz")], [{"tipo": "canasta", "x": 0.55}],
  efectos=[{"tipo": "brillo", "x": 0.55}], camara="acercar_rapido")
S("noche", "Tiempo después, el hijo de la viuda enfermó gravemente... y murió. La madre, desesperada, le gritó a Elías: ¿Viniste a mi casa para que muriera mi hijo?",
  [P("mujer1", 0.4, accion="arrodillarse", emocion="llorando", tunica="#4a4a5a"), P("elias", 0.68, mira="izquierda", **EL, emocion="triste")],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.45}], camara="acercar")
S("noche", "Elías tomó al niño en sus brazos, lo subió a su cuarto y clamó tres veces: Señor, Dios mío, te ruego que vuelva el alma de este niño a él.",
  [P("elias", 0.5, **EL, accion="orar", emocion="llorando"), P("nino", 0.68, accion="dormir")], efectos=[{"tipo": "oscuridad", "fuerza": 0.35}, {"tipo": "luz", "x": 0.6}],
  habla="elias", camara="acercar")
S("noche", "Y Dios escuchó. El niño volvió a respirar. Elías se lo devolvió a su madre y le dijo: Mira, tu hijo vive. Y ella dijo: Ahora sé que eres un hombre de Dios.",
  [P("nino", 0.45, accion="celebrar", emocion="feliz"), P("mujer1", 0.62, mira="izquierda", accion="abrazar", emocion="llorando", tunica="#4a4a5a")],
  efectos=[{"tipo": "luz"}, {"tipo": "brillo"}], camara="acercar_rapido")
S("cielo", "Si Dios está proveyendo para ti en medio de tu sequía, escribe en los comentarios: mi harina no se acaba.",
  [P("elias", 0.5, **EL, accion="alabar")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 3. EL DESAFÍO ----------
S("palacio", "Al tercer año, Dios envió a Elías de vuelta ante Acab. Cuando el rey lo vio, le gritó: ¿Eres tú el que trae la desgracia sobre Israel?",
  [P("acab", 0.65, mira="izquierda", **ACAB, accion="senalar", emocion="enojado"), P("elias", 0.32, **EL)], habla="acab", rotulo="CAPÍTULO 3: EL DESAFÍO", camara="acercar")
S("palacio", "No soy yo, respondió Elías. Eres tú, por abandonar al Señor y seguir a Baal. Ahora reúne a todo Israel en el monte Carmelo, y a los cuatrocientos cincuenta profetas de Baal.",
  [P("elias", 0.35, **EL, accion="senalar", emocion="valiente"), P("acab", 0.68, mira="izquierda", **ACAB, emocion="sorprendido")], habla="elias", camara="acercar_rapido")
S("montana", "Todo el pueblo subió al monte. Y Elías les habló: ¿Hasta cuándo van a estar indecisos? Si el Señor es Dios, síganlo. Y si Baal es dios, síganlo a él. Pero el pueblo no respondió ni una palabra.",
  [P("elias", 0.4, **EL, accion="levantar", emocion="valiente")], [gente(0.7, 0.6, y=250, profundidad=100)], habla="elias", camara="alejar")
S("montana", "Entonces propuso un desafío: Traigan dos bueyes. Ellos prepararán uno sobre la leña, y yo el otro. Pero nadie le pondrá fuego. El Dios que responda con fuego... ese es el Dios verdadero.",
  [P("elias", 0.5, **EL, accion="senalar")], [{"tipo": "altar", "x": 0.25}, {"tipo": "altar", "x": 0.78}], habla="elias", camara="paneo")
S("montana", "Y todo el pueblo respondió: ¡Bien dicho!",
  [], [gente(0.5, 0.6, y=280, profundidad=100)], efectos=[{"tipo": "temblor", "inicio": 0.2, "fin": 0.4}], camara="acercar_rapido")
S("cielo", "Pausa. Antes de ver qué pasó: ¿tú crees que Dios todavía responde con fuego hoy? Escribe sí o no en los comentarios.",
  [P("elias", 0.5, **EL, accion="senalar")], efectos=[{"tipo": "luz"}], rotulo="¿Y TÚ QUÉ CREES?", camara="fijo")

# ---------- 4. EL FUEGO ----------
S("montana", "Los profetas de Baal empezaron primero. Desde la mañana hasta el mediodía gritaban: ¡Baal, respóndenos! ¡Baal, respóndenos! Pero no hubo ninguna voz, ni nadie que respondiera.",
  [P("profeta_baal1", 0.3, accion="saltar", emocion="enojado"), P("profeta_baal2", 0.5, accion="alabar", emocion="enojado")], [{"tipo": "altar", "x": 0.4}],
  habla="profeta_baal1", rotulo="CAPÍTULO 4: FUEGO DEL CIELO", camara="paneo")
S("montana", "Al mediodía, Elías se burló de ellos: ¡Griten más fuerte! A lo mejor su dios está ocupado, o se fue de viaje... o está dormido y hay que despertarlo.",
  [P("elias", 0.75, mira="izquierda", **EL, accion="senalar", emocion="burlon"), P("profeta_baal1", 0.35, emocion="enojado")], habla="elias", camara="acercar")
S("montana", "Y ellos gritaban más fuerte y se cortaban con cuchillos, como era su costumbre, hasta que la sangre les corría. Pasó toda la tarde. Y no pasó nada.",
  [P("profeta_baal1", 0.3, accion="temblar", emocion="llorando"), P("profeta_baal2", 0.5, accion="arrodillarse", emocion="enojado")], [{"tipo": "altar", "x": 0.42}],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.2}], camara="acercar")
S("montana", "Entonces Elías llamó al pueblo. Reconstruyó el altar del Señor con doce piedras, una por cada tribu de Israel, cavó una zanja alrededor y puso la leña y el buey.",
  [P("elias", 0.45, **EL, accion="levantar")], [{"tipo": "altar", "x": 0.65}], camara="acercar")
S("montana", "Y luego hizo algo que nadie esperaba: Llenen cuatro cántaros de agua y échenla sobre el sacrificio. Otra vez. Y otra vez. Doce cántaros. El agua corría por todo el altar y llenó la zanja.",
  [P("hombre1", 0.45, accion="lanzar"), P("elias", 0.25, **EL, accion="senalar")], [{"tipo": "altar", "x": 0.68}], efectos=[{"tipo": "agua", "x": 0.68}],
  habla="elias", camara="acercar_rapido")
S("montana", "A la hora del sacrificio de la tarde, Elías se acercó y oró con calma: Señor, Dios de Abraham, de Isaac y de Israel, que se sepa hoy que tú eres Dios. Respóndeme, Señor, respóndeme.",
  [P("elias", 0.45, **EL, accion="orar")], [{"tipo": "altar", "x": 0.7}], habla="elias", efectos=[{"tipo": "luz", "x": 0.45}], camara="acercar")
S("montana", "¡Y entonces cayó fuego del cielo! Consumió el sacrificio, la leña, las piedras, el polvo... y hasta el agua de la zanja.",
  [P("elias", 0.35, **EL, accion="levantar", emocion="sorprendido")], [{"tipo": "altar", "x": 0.68}],
  efectos=[{"tipo": "rayo", "inicio": 0.05}, {"tipo": "flash", "inicio": 0.1}, {"tipo": "fuego", "x": 0.68, "y": -100, "tamano": 2.6, "crece": True}, {"tipo": "temblor", "inicio": 0.1, "fin": 0.6}],
  camara="acercar_rapido")
S("montana", "Todo el pueblo cayó de rodillas gritando: ¡El Señor es Dios! ¡El Señor es Dios!",
  [], [gente(0.5, 0.65, y=260, profundidad=100)], efectos=[{"tipo": "fuego", "x": 0.75, "y": -100, "tamano": 1.8}, {"tipo": "luz"}], habla="hombre1", camara="alejar")

# ---------- 5. LA LLUVIA ----------
S("montana", "Después, Elías subió a la cima del Carmelo, se postró en tierra con la cabeza entre las rodillas, y oró por lluvia. Y le dijo a su siervo: Sube y mira hacia el mar.",
  [P("elias", 0.4, **EL, accion="arrodillarse"), P("nino", 0.65, accion="caminar", hasta=0.75)], rotulo="CAPÍTULO 5: LA LLUVIA", camara="acercar")
S("montana", "No hay nada. Vuelve. Nada. Vuelve otra vez. Siete veces subió el siervo. Y a la séptima dijo: Veo una nube pequeña, como la palma de una mano, que sube del mar.",
  [P("nino", 0.6, accion="senalar", emocion="sorprendido"), P("elias", 0.35, **EL, accion="orar")], habla="nino", efectos=[{"tipo": "brillo", "x": 0.8, "y": -600}], camara="acercar_rapido")
S("tormenta", "En poco tiempo el cielo se oscureció con nubes y viento, y cayó una gran lluvia. Después de tres años y medio, la tierra volvió a beber.",
  [P("hombre2", 0.4, accion="celebrar", emocion="feliz"), P("mujer1", 0.6, accion="alabar", emocion="feliz")], efectos=[{"tipo": "lluvia"}, {"tipo": "rayo", "inicio": 0.3}],
  camara="alejar")

# ---------- 6. EL DESIERTO ----------
S("palacio", "Pero cuando Jezabel supo lo que había pasado, se puso furiosa. Le mandó un mensaje a Elías: Que los dioses me castiguen si mañana a esta hora no te he matado.",
  [P("jezabel", 0.5, accion="senalar", emocion="enojado")], [{"tipo": "trono", "x": 0.6, "profundidad": -30}], habla="jezabel", efectos=[{"tipo": "oscuridad", "fuerza": 0.3}],
  rotulo="CAPÍTULO 6: EL PROFETA CANSADO", camara="acercar_rapido")
S("desierto", "Y el mismo hombre que vio caer fuego del cielo... tuvo miedo y huyó. Caminó un día entero por el desierto, se sentó bajo un arbusto y le pidió a Dios: Basta ya, Señor. Quítame la vida.",
  [P("elias", 0.45, **EL, accion="arrodillarse", emocion="llorando")], [{"tipo": "arbol", "x": 0.62, "escala": 0.6}], habla="elias", camara="acercar")
S("desierto", "Elías estaba agotado, deprimido, sin fuerzas. Y se quedó dormido. Pero Dios no lo regañó. Le envió un ángel que lo tocó y le dijo: Levántate y come.",
  [P("elias", 0.45, **EL, accion="dormir"), P("angel", 0.7, mira="izquierda", accion="ofrecer")], [{"tipo": "panes_peces", "x": 0.58}],
  efectos=[{"tipo": "luz", "x": 0.7}], camara="acercar")
S("desierto", "Junto a su cabeza había un pan cocido sobre piedras calientes y una jarra de agua. Comió, bebió, y volvió a dormir. Y el ángel volvió: Come, porque el camino es largo para ti.",
  [P("elias", 0.45, **EL, accion="agacharse", emocion="sorprendido"), P("angel", 0.7, mira="izquierda")], efectos=[{"tipo": "brillo", "x": 0.58}], habla="angel", camara="fijo")
S("cielo", "A veces lo más espiritual que puedes hacer es descansar y comer. Dios cuida tu cuerpo y tu ánimo, no solo tu fe. Si estás cansado, escribe: Dios renueva mis fuerzas.",
  [P("elias", 0.5, **EL, accion="orar")], efectos=[{"tipo": "luz"}], camara="acercar")

# ---------- 7. EL SILBO APACIBLE ----------
S("montana", "Con la fuerza de esa comida, Elías caminó cuarenta días hasta el monte Horeb, el monte de Dios. Y allí entró en una cueva.",
  [P("elias", 0.3, **EL, accion="caminar", hasta=0.55)], rotulo="CAPÍTULO 7: LA VOZ SUAVE", camara="paneo")
S("tormenta", "Dios le dijo: Sal y ponte en el monte, porque voy a pasar. Y vino un viento tan fuerte que rompía las rocas... pero Dios no estaba en el viento.",
  [P("elias", 0.45, **EL, accion="temblar", emocion="asustado")], efectos=[{"tipo": "lluvia"}, {"tipo": "temblor", "inicio": 0.1, "fin": 0.9}], camara="acercar_rapido")
S("montana", "Después vino un terremoto... pero Dios no estaba en el terremoto. Y después un fuego... pero Dios no estaba en el fuego.",
  [P("elias", 0.45, **EL, accion="temblar", emocion="asustado")], efectos=[{"tipo": "temblor", "inicio": 0.0, "fin": 0.5}, {"tipo": "fuego", "x": 0.75, "tamano": 1.6}], camara="acercar")
S("montana", "Y después del fuego, se escuchó un susurro suave y apacible. Elías se cubrió el rostro con su manto... porque supo que Dios estaba ahí.",
  [P("elias", 0.5, **EL, accion="arrodillarse")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="acercar")
S("montana", "Dios le habló con ternura, le dio nuevas tareas y le dijo algo que lo consoló: No estás solo. Todavía hay siete mil en Israel que no se han arrodillado ante Baal.",
  [P("elias", 0.5, **EL, emocion="feliz")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 8. EL CARRO DE FUEGO ----------
S("campo", "Dios le dio un compañero: Eliseo, un joven que estaba arando el campo. Elías le echó su manto encima, y Eliseo lo dejó todo para seguirlo.",
  [P("elias", 0.35, **EL, accion="ofrecer"), P("discipulo1", 0.62, mira="izquierda", emocion="sorprendido")], rotulo="CAPÍTULO 8: EL CARRO DE FUEGO", camara="acercar")
S("mar", "Años después, Elías y Eliseo llegaron al río Jordán. Elías golpeó el agua con su manto... y el río se abrió en dos para que pasaran.",
  [P("elias", 0.45, **EL, accion="levantar"), P("discipulo1", 0.28)], efectos=[{"tipo": "agua"}, {"tipo": "flash", "inicio": 0.5}], camara="acercar_rapido")
S("valle", "Mientras caminaban conversando, de repente apareció un carro de fuego con caballos de fuego que los separó.",
  [P("elias", 0.55, **EL, emocion="sorprendido"), P("discipulo1", 0.3, emocion="asustado")], efectos=[{"tipo": "fuego", "x": 0.55, "tamano": 2.2, "crece": True}, {"tipo": "temblor", "inicio": 0.3, "fin": 0.8}],
  camara="acercar_rapido")
S("cielo", "Y Elías subió al cielo en un torbellino. Sin morir. Solo dos personas en toda la Biblia fueron llevadas así: Enoc... y Elías.",
  [P("elias", 0.5, **EL, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}, {"tipo": "fuego", "x": 0.5, "y": 120, "tamano": 1.0}], camara="alejar")

# ---------- ENSEÑANZA Y FINAL ----------
S("cielo", "Elías fue un hombre como nosotros: valiente un día, y asustado al siguiente. Pero oró, y el cielo se cerró. Volvió a orar, y el cielo dio lluvia.",
  [P("elias", 0.5, **EL, accion="orar")], efectos=[{"tipo": "luz"}], rotulo="ENSEÑANZA", camara="acercar")
S("cielo", "Dios no solo está en el fuego y en los milagros grandes. También está en el susurro suave, en el pan del camino, y en el ángel que te dice: levántate y come.",
  [P("elias", 0.5, **EL, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="fijo")
S("cielo", "¿Qué parte te impactó más: la viuda, el fuego del Carmelo o el carro de fuego? Cuéntame en los comentarios.",
  [P("elias", 0.4, **EL, accion="senalar"), P("discipulo1", 0.62, mira="izquierda")], efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "Suscríbete y activa la campanita, que mañana llega otra gran historia de la Biblia. ¡Dios te bendiga!",
  [P("elias", 0.5, **EL, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="¡SUSCRÍBETE!", pausa=2.0, camara="acercar")

guardar("10_elias_la_historia_completa.json", "Elías - El Profeta del Fuego",
        "450 profetas contra UNO solo... y cayó FUEGO del cielo.",
        ["ELÍAS", "BAAL", "ACAB", "JEZABEL", "FUEGO", "LLUVIA", "CARMELO", "SEÑOR"],
        personajes={"acab": {"tunica": "#6a2a6a", "manto": "#d9a62e", "tocado": "corona", "barba": "#3a2a1a"},
                    "jezabel": {"tunica": "#8a1a3a", "manto": "#d9a62e", "tocado": "corona", "pelo": "#1a1410", "pelo_largo": True,
                                "voz": {"nombre": "es_AR-daniela-high", "tono": -2}}},
        miniatura={"texto": ["¡FUEGO", "DEL CIELO!"],
                   "escena": {"fondo": "montana", "personajes": [
                       {"id": "elias", "x": 0.6, "accion": "levantar", "emocion": "valiente", "objeto": "cayado", "escala": 1.3}],
                       "cosas": [{"tipo": "altar", "x": 0.82}],
                       "efectos": [{"tipo": "fuego", "x": 0.82, "y": -100, "tamano": 2.6}, {"tipo": "rayo", "inicio": 0.4}, {"tipo": "luz", "x": 0.8}]}})
