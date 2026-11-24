"""Video largo: Samuel, la historia completa."""
from base import S, P, gente, guardar

NINO = {"escala": 0.72}
VIEJO = {"barba": "#e8e4dc", "pelo": "#e8e4dc"}

# ---------- APERTURA EN FRÍO ----------
S("noche", "Medianoche en el templo. Un niño duerme junto al arca de Dios. Y de repente, una voz lo llama por su nombre: ¡Samuel! ¡Samuel!",
  [P("samuel", 0.5, **NINO, accion="dormir")], efectos=[{"tipo": "oscuridad", "fuerza": 0.4}, {"tipo": "luz", "x": 0.7}, {"tipo": "brillo", "x": 0.7}],
  camara="acercar_rapido", portada=True)
S("noche", "No es el sacerdote. No es nadie en el templo. Es Dios mismo hablándole a un niño. ¿Por qué a él? Para entenderlo, tenemos que conocer primero a su madre.",
  [P("samuel", 0.5, **NINO, emocion="sorprendido")], efectos=[{"tipo": "oscuridad", "fuerza": 0.3}, {"tipo": "flash", "inicio": 0.85}], camara="acercar")

# ---------- 1. LA ORACIÓN DE ANA ----------
S("campo", "Había un hombre llamado Elcana que tenía dos esposas: Penina y Ana. Penina tenía hijos e hijas. Pero Ana... no podía tener hijos.",
  [P("hombre1", 0.5, emocion="feliz"), P("mujer1", 0.3, emocion="burlon"), P("ana", 0.72, mira="izquierda", emocion="triste"), P("nino", 0.15, escala=0.7)],
  rotulo="CAPÍTULO 1: LAS LÁGRIMAS DE ANA", camara="paneo")
S("campo", "En aquel tiempo, no tener hijos era visto como una vergüenza. Y Penina se burlaba de Ana todos los días, año tras año, hasta hacerla llorar.",
  [P("mujer1", 0.4, accion="senalar", emocion="burlon"), P("ana", 0.65, mira="izquierda", accion="temblar", emocion="llorando")], habla="mujer1", camara="acercar")
S("campo", "Elcana la amaba mucho y le decía: Ana, ¿por qué lloras? ¿Por qué no comes? ¿No soy yo para ti mejor que diez hijos? Pero el dolor de Ana no se iba.",
  [P("hombre1", 0.4, accion="abrazar", emocion="triste"), P("ana", 0.6, mira="izquierda", emocion="llorando")], habla="hombre1", camara="fijo")
S("templo", "Cada año la familia subía a adorar al templo de Silo. Y un año, Ana entró sola, se arrodilló... y le abrió su corazón a Dios con amargura.",
  [P("ana", 0.5, accion="arrodillarse", emocion="llorando")], efectos=[{"tipo": "luz", "x": 0.5}], camara="acercar")
S("templo", "Señor, si te acuerdas de mí y me das un hijo varón, yo te lo dedicaré a ti todos los días de su vida.",
  [P("ana", 0.5, accion="orar", emocion="llorando")], habla="ana", efectos=[{"tipo": "luz"}], camara="acercar")
S("templo", "Oraba en silencio. Solo se movían sus labios. Y el sacerdote Elí, que estaba sentado a la puerta, pensó que estaba borracha. ¿Hasta cuándo vas a estar ebria? ¡Deja el vino!",
  [P("eli", 0.7, mira="izquierda", accion="senalar", emocion="enojado"), P("ana", 0.4, accion="orar", emocion="llorando")], habla="eli", camara="acercar_rapido")
S("templo", "No, señor mío, respondió Ana. No he bebido vino. Soy una mujer con el corazón destrozado, y estaba derramando mi alma delante del Señor.",
  [P("ana", 0.4, accion="ofrecer", emocion="llorando"), P("eli", 0.68, mira="izquierda", emocion="sorprendido")], habla="ana", camara="fijo")
S("templo", "Entonces Elí le dijo con ternura: Vete en paz, y que el Dios de Israel te conceda lo que le has pedido. Y Ana se fue... y ya no estaba triste.",
  [P("eli", 0.62, mira="izquierda", accion="ofrecer", emocion="feliz"), P("ana", 0.38, emocion="feliz")], habla="eli", efectos=[{"tipo": "luz"}, {"tipo": "brillo"}], camara="acercar")
S("cielo", "Si tienes una petición que llevas años pidiéndole a Dios, escríbela en los comentarios. Ana nos enseña que vale la pena seguir orando.",
  [P("ana", 0.5, accion="orar")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 2. EL NIÑO PRESTADO ----------
S("campo", "Y Dios se acordó de Ana. Al año siguiente nació un niño, y ella le puso por nombre Samuel, que significa porque se lo pedí a Dios.",
  [P("ana", 0.45, accion="abrazar", emocion="feliz"), P("hombre1", 0.65, mira="izquierda", accion="celebrar", emocion="feliz")], [{"tipo": "pesebre", "x": 0.52, "escala": 0.7}],
  efectos=[{"tipo": "luz"}, {"tipo": "brillo"}], rotulo="CAPÍTULO 2: UN NIÑO PARA DIOS", camara="acercar")
S("campo", "Ana lo cuidó y lo amamantó con todo su amor. Pero ella no había olvidado su promesa.",
  [P("ana", 0.45, accion="abrazar", emocion="feliz"), P("samuel", 0.6, **NINO, emocion="feliz")], camara="fijo")
S("templo", "Cuando Samuel tenía unos tres años, Ana lo llevó al templo de Silo, ante el sacerdote Elí. ¿Se acuerda de mí? Yo soy la mujer que oraba aquí. Por este niño oraba, y el Señor me lo concedió.",
  [P("ana", 0.35, accion="ofrecer", emocion="llorando"), P("samuel", 0.5, **NINO), P("eli", 0.72, mira="izquierda", **VIEJO, emocion="sorprendido")], habla="ana", camara="acercar")
S("templo", "Por eso yo ahora se lo entrego al Señor. Todos los días de su vida será del Señor.",
  [P("ana", 0.4, accion="abrazar", emocion="llorando"), P("samuel", 0.55, **NINO, accion="abrazar")], habla="ana", efectos=[{"tipo": "luz"}], camara="acercar_rapido")
S("templo", "Imagina lo que le costó a Ana. Esperó años por ese hijo... y lo entregó a Dios. Y cada año le cosía una pequeña túnica nueva y se la llevaba cuando subía al templo.",
  [P("ana", 0.4, accion="ofrecer", emocion="feliz"), P("samuel", 0.58, **NINO, emocion="feliz", tunica="#3f6fb5")], camara="fijo")
S("cielo", "Y Dios la bendijo todavía más: Ana tuvo después tres hijos más y dos hijas. Nadie le gana a Dios en generosidad.",
  [P("ana", 0.5, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="acercar")

# ---------- 3. LOS HIJOS DE ELÍ ----------
S("templo", "Así, el pequeño Samuel se quedó a vivir en el templo. Aprendió a encender las lámparas, a abrir las puertas cada mañana y a servir al anciano Elí. Y la Biblia dice que el niño crecía delante del Señor.",
  [P("samuel", 0.45, **NINO, accion="levantar", emocion="feliz"), P("eli", 0.7, mira="izquierda", **VIEJO, emocion="feliz")], efectos=[{"tipo": "luz", "x": 0.45}], camara="paneo")
S("templo", "Samuel creció en el templo, sirviendo a Dios junto a Elí. Pero en ese mismo templo había un gran problema: los hijos de Elí, Ofni y Finees.",
  [P("samuel", 0.4, **NINO, accion="levantar"), P("hermano1", 0.65, emocion="burlon"), P("hermano2", 0.82, emocion="burlon")], rotulo="CAPÍTULO 3: UN TEMPLO CORRUPTO", camara="paneo")
S("templo", "Eran sacerdotes, pero no conocían a Dios. Robaban las mejores ofrendas, trataban con desprecio a la gente y hacían cosas terribles dentro del templo.",
  [P("hermano1", 0.4, accion="senalar", emocion="burlon"), P("hombre2", 0.65, mira="izquierda", emocion="triste")], [{"tipo": "altar", "x": 0.25}], efectos=[{"tipo": "oscuridad", "fuerza": 0.3}],
  camara="acercar")
S("templo", "Elí lo sabía. Los regañaba con palabras, pero nunca hizo nada para detenerlos. Y en esos días la palabra del Señor escaseaba. Dios casi no hablaba a su pueblo.",
  [P("eli", 0.5, **VIEJO, emocion="triste", accion="senalar")], efectos=[{"tipo": "oscuridad", "fuerza": 0.3}], camara="fijo")

# ---------- 4. LA VOZ EN LA NOCHE ----------
S("noche", "Una noche, Samuel dormía en el templo, cerca del arca de Dios. La lámpara del santuario todavía estaba encendida. Y una voz lo llamó: ¡Samuel!",
  [P("samuel", 0.5, **NINO, accion="dormir")], efectos=[{"tipo": "oscuridad", "fuerza": 0.4}, {"tipo": "brillo", "x": 0.7}], rotulo="CAPÍTULO 4: LA VOZ EN LA NOCHE", camara="acercar")
S("noche", "Samuel se levantó corriendo y fue donde Elí: ¡Aquí estoy! ¿Me llamaste? No te llamé, hijo. Vuelve a acostarte.",
  [P("samuel", 0.4, **NINO, accion="correr", hasta=0.5), P("eli", 0.72, mira="izquierda", **VIEJO, accion="dormir")], habla="samuel", efectos=[{"tipo": "oscuridad", "fuerza": 0.35}], camara="paneo")
S("noche", "Pasó otra vez. Y otra vez. Tres veces. Y a la tercera, Elí entendió: era Dios quien llamaba al niño.",
  [P("eli", 0.55, **VIEJO, emocion="sorprendido"), P("samuel", 0.35, **NINO, emocion="sorprendido")], efectos=[{"tipo": "oscuridad", "fuerza": 0.35}], camara="acercar_rapido")
S("noche", "Le dijo: Ve y acuéstate. Y si te vuelve a llamar, responde: Habla, Señor, que tu siervo escucha.",
  [P("eli", 0.6, mira="izquierda", **VIEJO, accion="senalar"), P("samuel", 0.38, **NINO)], habla="eli", camara="fijo")
S("noche", "Y el Señor vino, se quedó allí, y llamó como las otras veces: ¡Samuel, Samuel! Y el niño respondió:",
  [P("samuel", 0.5, **NINO, accion="arrodillarse")], efectos=[{"tipo": "oscuridad", "fuerza": 0.3}, {"tipo": "luz", "x": 0.7}, {"tipo": "brillo", "x": 0.7}], camara="acercar")
S("cielo", "Habla, Señor, que tu siervo escucha.",
  [P("samuel", 0.5, **NINO, accion="orar")], habla="samuel", efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="1 SAMUEL 3:10", camara="acercar_rapido")
S("noche", "Pero el mensaje era muy difícil: Dios iba a juzgar a la casa de Elí por la maldad de sus hijos. A la mañana siguiente, Samuel tenía miedo de contárselo.",
  [P("samuel", 0.45, **NINO, emocion="asustado")], efectos=[{"tipo": "oscuridad", "fuerza": 0.3}], camara="acercar")
S("templo", "Elí le insistió: No me ocultes nada. Y Samuel le dijo todo. Elí bajó la cabeza: Él es el Señor. Que haga lo que bien le parezca.",
  [P("samuel", 0.38, **NINO, emocion="triste"), P("eli", 0.62, mira="izquierda", **VIEJO, emocion="triste")], habla="eli", camara="fijo")
S("cielo", "Pausa. ¿Cuándo fue la última vez que le dijiste a Dios: habla, que te escucho? Escribe en los comentarios: Habla, Señor.",
  [P("samuel", 0.5, **NINO, accion="senalar")], efectos=[{"tipo": "luz"}], rotulo="HABLA, SEÑOR", camara="fijo")

# ---------- 5. EL ARCA PERDIDA ----------
S("valle", "Poco tiempo después, los filisteos atacaron a Israel. Los hijos de Elí llevaron el arca de Dios a la batalla, como si fuera un amuleto de buena suerte.",
  [P("hermano1", 0.4, accion="levantar", emocion="burlon"), P("hermano2", 0.58)], [gente(0.8, 0.55, variante="soldados")], rotulo="CAPÍTULO 5: EL ARCA PERDIDA", camara="paneo")
S("valle", "Pero Dios no se deja usar. Israel perdió la batalla, los dos hijos de Elí murieron, y los filisteos se llevaron el arca de Dios.",
  [P("filisteo1", 0.5, accion="celebrar", emocion="burlon"), P("hermano1", 0.25, accion="caer")], efectos=[{"tipo": "fuego", "x": 0.85, "tamano": 1.2}, {"tipo": "temblor", "inicio": 0.3, "fin": 0.6}],
  camara="acercar_rapido")
S("templo", "Cuando el anciano Elí escuchó que el arca había sido capturada, cayó de su silla hacia atrás... y murió. Así se cumplió la palabra que Dios le había dado a Samuel.",
  [P("eli", 0.5, **VIEJO, accion="caer", emocion="asustado")], efectos=[{"tipo": "oscuridad", "fuerza": 0.4}], camara="acercar")
S("templo", "Y desde entonces, todo Israel, desde Dan hasta Beerseba, supo que Samuel era un verdadero profeta del Señor. Ninguna de sus palabras caía a tierra sin cumplirse.",
  [P("samuel", 0.5, emocion="valiente", tunica="#f4f1ea", manto="#3f5a8a")], [gente(0.5, 0.55, y=320, delante=True, profundidad=None)], efectos=[{"tipo": "luz"}], camara="alejar")

S("ciudad", "Mientras tanto, el arca de Dios causaba desastres en las ciudades filisteas. La pusieron en el templo de su dios Dagón, y a la mañana siguiente la estatua de Dagón estaba tirada en el suelo, de cara frente al arca.",
  [P("filisteo1", 0.4, accion="temblar", emocion="asustado")], [{"tipo": "columna", "x": 0.65, "caer": True, "caer_desde": 0, "caer_hasta": 0.01}], camara="acercar")
S("ciudad", "Asustados, después de siete meses los filisteos la devolvieron a Israel en una carreta tirada por dos vacas, cargada de regalos de oro.",
  [P("burro", 0.3, accion="caminar", hasta=0.55)], [{"tipo": "monedas", "x": 0.45}], camara="paneo")
S("valle", "Veinte años después, Samuel reunió a todo el pueblo en Mizpa y les dijo: Si de verdad quieren volver a Dios, quiten los ídolos y sirvan solo al Señor. Y el pueblo lo hizo. Ayunaron y confesaron: Hemos pecado contra el Señor.",
  [P("samuel", 0.4, tunica="#f4f1ea", manto="#3f5a8a", accion="levantar")], [gente(0.7, 0.55, y=250, profundidad=100)], habla="samuel", camara="alejar")
S("tormenta", "Los filisteos aprovecharon para atacar. Pero mientras Samuel ofrecía un sacrificio y oraba, Dios tronó desde el cielo con un estruendo tan grande que el ejército enemigo huyó en desorden.",
  [P("samuel", 0.4, tunica="#f4f1ea", manto="#3f5a8a", accion="orar")], [gente(0.78, 0.55, variante="soldados", hasta=1.0)],
  efectos=[{"tipo": "rayo", "inicio": 0.2}, {"tipo": "rayo", "inicio": 0.5}, {"tipo": "temblor", "inicio": 0.2, "fin": 0.7}], camara="acercar_rapido")
S("valle", "Samuel tomó una piedra, la puso como recuerdo y la llamó Ebenezer, que significa hasta aquí nos ayudó el Señor.",
  [P("samuel", 0.45, tunica="#f4f1ea", manto="#3f5a8a", accion="levantar", emocion="feliz")], [{"tipo": "rocas", "x": 0.65, "escala": 0.5}], efectos=[{"tipo": "luz"}], rotulo="EBENEZER", camara="acercar")
S("cielo", "Mira tu vida y escribe en los comentarios: Hasta aquí me ayudó el Señor. Porque si te ayudó hasta hoy, te ayudará mañana.",
  [P("samuel", 0.5, tunica="#f4f1ea", manto="#3f5a8a", accion="orar")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 6. QUEREMOS UN REY ----------
S("ciudad", "Samuel guió al pueblo durante muchos años como juez y profeta. Pero cuando envejeció, los ancianos de Israel vinieron a pedirle algo: Danos un rey, como tienen todas las naciones.",
  [P("samuel", 0.35, **VIEJO, tunica="#f4f1ea", manto="#3f5a8a", emocion="triste"), P("jacob", 0.65, mira="izquierda", **VIEJO, accion="senalar")], [gente(0.82, 0.5)],
  habla="jacob", rotulo="CAPÍTULO 6: QUEREMOS UN REY", camara="acercar")
S("noche", "A Samuel le dolió mucho. Pero Dios le dijo: No te han rechazado a ti. Me han rechazado a mí como su rey. Dales lo que piden, pero adviérteles lo que eso les costará.",
  [P("samuel", 0.5, **VIEJO, tunica="#f4f1ea", manto="#3f5a8a", accion="orar", emocion="triste")], efectos=[{"tipo": "luz", "x": 0.7}], camara="fijo")
S("ciudad", "Samuel les advirtió: Un rey tomará a sus hijos para su ejército, a sus hijas para su palacio, y la décima parte de sus cosechas. Un día clamarán por causa del rey que eligieron. Pero el pueblo insistió: ¡No! Queremos un rey.",
  [P("samuel", 0.35, **VIEJO, tunica="#f4f1ea", manto="#3f5a8a", accion="senalar", emocion="triste")], [gente(0.72, 0.55, y=-150)], habla="samuel", camara="acercar")
S("campo", "Dios eligió a un joven alto y apuesto de la tribu de Benjamín: Saúl. Samuel derramó aceite sobre su cabeza y lo ungió como el primer rey de Israel.",
  [P("samuel", 0.35, **VIEJO, tunica="#f4f1ea", manto="#3f5a8a", accion="ofrecer"), P("saul", 0.6, accion="arrodillarse")], efectos=[{"tipo": "luz", "x": 0.6}, {"tipo": "brillo", "x": 0.6}],
  camara="acercar")
S("valle", "Al principio Saúl fue humilde. Pero con el tiempo se llenó de orgullo y desobedeció a Dios una y otra vez. Y Samuel tuvo que decirle: Obedecer vale más que los sacrificios.",
  [P("samuel", 0.35, **VIEJO, tunica="#f4f1ea", manto="#3f5a8a", accion="senalar", emocion="enojado"), P("saul", 0.65, mira="izquierda", tocado="corona", emocion="asustado")],
  habla="samuel", camara="acercar_rapido")
S("campo", "Entonces Dios envió a Samuel a Belén, a la casa de Isaí. Y allí, entre ocho hermanos, Dios eligió al más pequeño: un pastorcito llamado David. Pero esa historia ya la conoces.",
  [P("samuel", 0.4, **VIEJO, tunica="#f4f1ea", manto="#3f5a8a", accion="ofrecer"), P("david", 0.62, accion="arrodillarse", objeto="cayado")], efectos=[{"tipo": "luz", "x": 0.62}],
  camara="acercar")

# ---------- ENSEÑANZA Y FINAL ----------
S("cielo", "Samuel fue el último juez de Israel y el profeta que ungió a sus dos primeros reyes. Y todo empezó con las lágrimas de una madre y la respuesta sencilla de un niño.",
  [P("samuel", 0.5, **NINO, accion="orar")], efectos=[{"tipo": "luz"}], rotulo="ENSEÑANZA", camara="acercar")
S("cielo", "Dios sigue hablando hoy. No siempre con una voz en la noche, pero sí en su Palabra y en tu corazón. La pregunta es si estamos dispuestos a decir: Habla, Señor, que tu siervo escucha.",
  [P("samuel", 0.4, **NINO, accion="alabar", emocion="feliz"), P("ana", 0.6, mira="izquierda", accion="abrazar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="fijo")
S("cielo", "¿Qué te tocó más: la oración de Ana o la voz que llamó a Samuel? Cuéntamelo en los comentarios.",
  [P("ana", 0.4, accion="senalar"), P("samuel", 0.58, **NINO, emocion="feliz")], efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "Suscríbete y activa la campanita, que mañana llega otra gran historia de la Biblia. ¡Dios te bendiga!",
  [P("samuel", 0.5, **NINO, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="¡SUSCRÍBETE!", pausa=2.0, camara="acercar")

guardar("12_samuel_la_historia_completa.json", "Samuel - El Niño que Escuchó a Dios",
        "Dios le habló a un NIÑO en medio de la noche...",
        ["SAMUEL", "ANA", "ELÍ", "SEÑOR", "ESCUCHA", "ARCA", "REY", "SAÚL"],
        personajes={"samuel": {"tunica": "#e9e4d8", "pelo": "#5a3a1a", "barba": None},
                    "ana": {"tunica": "#7a5c8a", "tocado": "velo", "color_tocado": "#4a3a6a", "pelo": None, "voz": {"nombre": "es_AR-daniela-high"}},
                    "eli": {"tunica": "#f4f1ea", "manto": "#3f5a8a", "tocado": "turbante", "color_tocado": "#e9e4d8", "barba": "#e8e4dc", "pelo": "#e8e4dc"}},
        miniatura={"texto": ["DIOS LE", "HABLÓ"], "sello": "A UN NIÑO",
                   "escena": {"fondo": "noche", "personajes": [
                       {"id": "samuel", "x": 0.66, "accion": "arrodillarse", "emocion": "sorprendido", "escala": 1.1}],
                       "efectos": [{"tipo": "luz", "x": 0.82}, {"tipo": "brillo", "x": 0.82}, {"tipo": "oscuridad", "fuerza": 0.25}]}})
