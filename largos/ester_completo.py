"""Video largo: Ester, la historia completa."""
from base import S, P, gente, guardar

REINA = {"tocado": "corona"}

# ---------- APERTURA EN FRÍO ----------
S("palacio", "Si da un paso más, la matan. Una joven camina sola hacia el trono del hombre más poderoso del mundo. Nadie la llamó, y la ley es clara: quien entra sin ser invitado, muere.",
  [P("ester", 0.3, **REINA, accion="caminar", hasta=0.42, emocion="asustado"), P("rey_asuero", 0.78, mira="izquierda", emocion="enojado")],
  [{"tipo": "trono", "x": 0.82, "profundidad": -30}], efectos=[{"tipo": "oscuridad", "fuerza": 0.2}], camara="acercar_rapido", portada=True)
S("palacio", "Si el rey no levanta su cetro de oro, ella muere. Y si no se arriesga, muere todo su pueblo. ¿Cómo llegó una huérfana hasta aquí? Todo empezó con un rey muy poderoso.",
  [P("ester", 0.5, **REINA, emocion="valiente")], efectos=[{"tipo": "flash", "inicio": 0.85}], camara="acercar")

# ---------- 1. LA REINA DESOBEDIENTE ----------
S("palacio", "Hace unos dos mil quinientos años, el imperio persa gobernaba desde la India hasta Etiopía: ciento veintisiete provincias. Su rey se llamaba Asuero.",
  [P("rey_asuero", 0.5, accion="levantar", emocion="feliz")], [{"tipo": "trono", "x": 0.55, "profundidad": -30}], camara="alejar")
S("palacio", "Un día el rey hizo un banquete que duró ciento ochenta días, para mostrar sus riquezas. Y al final, ya alegre por el vino, mandó llamar a la reina Vasti para presumir su belleza ante todos.",
  [P("rey_asuero", 0.45, accion="celebrar", emocion="burlon")], [{"tipo": "mesa", "x": 0.6}, gente(0.75, 0.5)], camara="paneo")
S("palacio", "Pero la reina Vasti se negó a ir. El rey se enfureció, y sus consejeros le dijeron: Si no la castigas, todas las mujeres del reino desobedecerán a sus maridos. Y Vasti fue quitada de su puesto.",
  [P("rey_asuero", 0.6, mira="izquierda", accion="senalar", emocion="enojado"), P("hombre2", 0.35, accion="senalar")], efectos=[{"tipo": "temblor", "inicio": 0.4, "fin": 0.55}], camara="acercar")
S("palacio", "Entonces buscaron por todo el imperio a las jóvenes más hermosas para que el rey eligiera una nueva reina.",
  [P("criada", 0.3, accion="caminar", hasta=0.45), P("mujer1", 0.15, accion="caminar", hasta=0.3), P("ester", 0.0, accion="caminar", hasta=0.15)], camara="paneo")

# ---------- 2. LA HUÉRFANA ----------
S("ciudad", "En la capital, Susa, vivía un judío llamado Mardoqueo. Su pueblo había sido llevado cautivo desde Jerusalén años atrás. Y él había criado como a su propia hija a su prima huérfana: Hadasa, también llamada Ester.",
  [P("mardoqueo", 0.4, emocion="feliz"), P("ester", 0.6, mira="izquierda", emocion="feliz", tocado="velo")], rotulo="CAPÍTULO 1: LA HUÉRFANA", camara="acercar")
S("ciudad", "Ester era hermosa por fuera y por dentro. Cuando la llevaron al palacio, Mardoqueo le dio un consejo: No le digas a nadie que eres judía.",
  [P("mardoqueo", 0.4, accion="senalar", emocion="triste"), P("ester", 0.6, mira="izquierda", tocado="velo")], habla="mardoqueo", camara="fijo")
S("palacio", "Durante un año entero, las jóvenes recibieron tratamientos de belleza con perfumes y aceites. Y Ester se ganó el cariño de todos los que la conocían por su humildad.",
  [P("ester", 0.45, emocion="feliz"), P("criada", 0.65, mira="izquierda", accion="ofrecer", emocion="feliz")], efectos=[{"tipo": "brillo"}], rotulo="1 AÑO", camara="paneo")
S("palacio", "Cuando llegó su turno, el rey se enamoró de Ester más que de todas las demás. Puso la corona real sobre su cabeza y la hizo reina en lugar de Vasti.",
  [P("ester", 0.42, **REINA, emocion="feliz"), P("rey_asuero", 0.65, mira="izquierda", accion="ofrecer", emocion="feliz")], [{"tipo": "trono", "x": 0.75, "profundidad": -30}],
  efectos=[{"tipo": "luz"}, {"tipo": "brillo"}], camara="acercar")
S("cielo", "Una huérfana extranjera se convirtió en reina del imperio más grande del mundo. Pero Dios no la puso ahí solo para que fuera feliz. La puso ahí con un propósito.",
  [P("ester", 0.5, **REINA, accion="orar")], efectos=[{"tipo": "luz"}], camara="acercar")
S("ciudad", "Mientras tanto, Mardoqueo, sentado a la puerta del palacio, escuchó a dos guardias planeando asesinar al rey. Se lo contó a Ester, ella avisó al rey, y los traidores fueron castigados. Y todo quedó escrito en el libro de las crónicas del rey.",
  [P("mardoqueo", 0.4, accion="senalar", emocion="sorprendido"), P("guardia1", 0.68, mira="izquierda", emocion="enojado", objeto="lanza")], camara="paneo")

# ---------- 3. AMÁN ----------
S("palacio", "Tiempo después, el rey nombró como primer ministro a un hombre llamado Amán. Y ordenó que todos se arrodillaran ante él cuando pasara.",
  [P("aman", 0.5, accion="levantar", emocion="burlon")], [gente(0.5, 0.55, y=320, delante=True, profundidad=None)], rotulo="CAPÍTULO 2: EL ENEMIGO", camara="acercar")
S("ciudad", "Todos se inclinaban... menos Mardoqueo. Él solo se arrodillaba ante Dios. Día tras día, Amán pasaba, y Mardoqueo se quedaba de pie.",
  [P("hombre1", 0.25, accion="arrodillarse"), P("hombre2", 0.4, accion="arrodillarse"), P("mardoqueo", 0.6, emocion="valiente"), P("aman", 0.85, mira="izquierda", emocion="enojado")],
  camara="paneo")
S("ciudad", "Amán se llenó de furia. Y cuando supo que Mardoqueo era judío, decidió que no bastaba con matarlo a él. Destruiría a todo su pueblo.",
  [P("aman", 0.5, accion="temblar", emocion="enojado")], efectos=[{"tipo": "oscuridad", "fuerza": 0.4}, {"tipo": "rayo", "inicio": 0.8}], camara="acercar_rapido")
S("palacio", "Echó suertes para escoger el día. Y luego le dijo al rey: Hay un pueblo esparcido por tu reino que no obedece tus leyes. Ordena que sean destruidos, y yo pagaré diez mil talentos de plata al tesoro real.",
  [P("aman", 0.38, accion="ofrecer", emocion="burlon"), P("rey_asuero", 0.68, mira="izquierda", emocion="sorprendido")], [{"tipo": "monedas", "x": 0.52}], habla="aman", camara="acercar")
S("palacio", "El rey, sin preguntar siquiera qué pueblo era, le dio su anillo para sellar la ley. Y se enviaron cartas a todas las provincias: en un solo día, el trece del mes de Adar, todos los judíos serían exterminados.",
  [P("rey_asuero", 0.6, mira="izquierda", accion="ofrecer"), P("aman", 0.35, accion="celebrar", emocion="burlon")], efectos=[{"tipo": "oscuridad", "fuerza": 0.35}], camara="acercar_rapido")
S("ciudad", "Cuando Mardoqueo se enteró, rasgó sus vestidos, se cubrió de ceniza y lloró a gritos en medio de la ciudad. Y en todas las provincias, los judíos ayunaban y lloraban.",
  [P("mardoqueo", 0.45, accion="arrodillarse", emocion="llorando", tunica="#5a5a5a"), P("mujer1", 0.68, accion="orar", emocion="llorando")], efectos=[{"tipo": "lluvia"}, {"tipo": "oscuridad", "fuerza": 0.3}],
  camara="acercar")

# ---------- 4. PARA ESTA HORA ----------
S("palacio", "Ester supo que Mardoqueo estaba de luto. Y él le mandó un mensaje: Ve ante el rey y pídele por la vida de tu pueblo.",
  [P("ester", 0.45, **REINA, emocion="asustado"), P("criada", 0.68, mira="izquierda", accion="ofrecer")], rotulo="CAPÍTULO 3: PARA ESTA HORA", camara="acercar")
S("palacio", "Pero Ester respondió con miedo: Todo el mundo sabe que quien entra ante el rey sin ser llamado, muere. Y el rey no me ha llamado en treinta días.",
  [P("ester", 0.5, **REINA, accion="temblar", emocion="asustado")], habla="ester", camara="acercar_rapido")
S("ciudad", "Y Mardoqueo le respondió con una de las frases más poderosas de la Biblia:",
  [P("mardoqueo", 0.5, emocion="valiente", tunica="#5a5a5a")], efectos=[{"tipo": "luz", "x": 0.5}], camara="acercar")
S("cielo", "No pienses que por estar en el palacio te vas a salvar. Si te quedas callada, la ayuda vendrá de otra parte. ¿Y quién sabe si para esta hora has llegado al reino?",
  [P("mardoqueo", 0.5, accion="senalar", tunica="#5a5a5a")], habla="mardoqueo", efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="ESTER 4:14", camara="fijo")
S("palacio", "Ester se quedó en silencio mucho tiempo. Pensó en su pueblo, en Mardoqueo que la había criado, en las familias que serían destruidas. Y entendió que su corona no era un premio, sino una responsabilidad.",
  [P("ester", 0.5, **REINA, emocion="triste", accion="orar")], efectos=[{"tipo": "oscuridad", "fuerza": 0.2}], camara="acercar")
S("palacio", "Ester respiró hondo y tomó una decisión: Reúne a todos los judíos de Susa y ayunen por mí tres días. Yo y mis criadas haremos lo mismo. Y después iré ante el rey. Y si perezco... que perezca.",
  [P("ester", 0.5, **REINA, accion="levantar", emocion="valiente")], habla="ester", efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "Tal vez estás donde estás, en tu trabajo, tu escuela o tu familia, para un momento como este. Si lo crees, escribe en los comentarios: para esta hora.",
  [P("ester", 0.5, **REINA, accion="orar")], efectos=[{"tipo": "luz"}], rotulo="PARA ESTA HORA", camara="fijo")

# ---------- 5. EL CETRO ----------
S("noche", "Durante tres días y tres noches, Ester no comió ni bebió. En el palacio, sus criadas oraban con ella. Y en las casas de Susa, miles de judíos clamaban a Dios por su reina.",
  [P("ester", 0.4, **REINA, accion="arrodillarse"), P("criada", 0.62, accion="orar")], efectos=[{"tipo": "oscuridad", "fuerza": 0.35}, {"tipo": "luz", "x": 0.4}], rotulo="3 DÍAS DE AYUNO", camara="paneo")
S("palacio", "Al tercer día, Ester se puso su vestido real y entró al patio interior del palacio. El silencio era total. Todos esperaban a ver qué haría el rey.",
  [P("ester", 0.32, **REINA, accion="caminar", hasta=0.45, emocion="asustado"), P("rey_asuero", 0.78, mira="izquierda", emocion="sorprendido")],
  [{"tipo": "trono", "x": 0.82, "profundidad": -30}, gente(0.2, 0.5)], rotulo="CAPÍTULO 4: EL CETRO DE ORO", camara="acercar")
S("palacio", "Y cuando el rey la vio... sonrió, y extendió hacia ella el cetro de oro. Ester se acercó y tocó la punta del cetro. Estaba viva.",
  [P("rey_asuero", 0.7, mira="izquierda", accion="ofrecer", emocion="feliz"), P("ester", 0.48, **REINA, accion="ofrecer", emocion="feliz")], [{"tipo": "trono", "x": 0.82, "profundidad": -30}],
  efectos=[{"tipo": "luz"}, {"tipo": "brillo"}], camara="acercar_rapido")
S("palacio", "¿Qué te pasa, reina Ester? ¿Qué deseas? Hasta la mitad del reino te daré. Pero Ester fue sabia. No pidió nada todavía. Solo invitó al rey y a Amán a un banquete.",
  [P("rey_asuero", 0.65, mira="izquierda", accion="senalar", emocion="feliz"), P("ester", 0.4, **REINA, emocion="feliz")], habla="rey_asuero", camara="fijo")
S("ciudad", "Amán salió del banquete feliz y orgulloso. Pero al ver a Mardoqueo que otra vez no se inclinaba, se llenó de rabia. Su esposa le aconsejó: Construye una horca de veinte metros, y mañana pídele al rey que cuelguen ahí a Mardoqueo.",
  [P("aman", 0.4, emocion="enojado", accion="senalar"), P("mujer1", 0.65, mira="izquierda", emocion="burlon")], efectos=[{"tipo": "oscuridad", "fuerza": 0.3}], camara="acercar")

# ---------- 6. LA NOCHE SIN SUEÑO ----------
S("noche", "Pero esa misma noche, el rey no podía dormir. Y pidió que le leyeran el libro de las crónicas del reino.",
  [P("rey_asuero", 0.5, accion="temblar", emocion="triste")], efectos=[{"tipo": "oscuridad", "fuerza": 0.4}], rotulo="CAPÍTULO 5: UNA NOCHE SIN SUEÑO", camara="acercar")
S("noche", "Y justo leyeron la parte en que Mardoqueo había salvado la vida del rey. ¿Qué recompensa recibió este hombre? Ninguna, majestad.",
  [P("rey_asuero", 0.6, mira="izquierda", emocion="sorprendido"), P("hombre1", 0.35, accion="senalar")], habla="hombre1", camara="acercar_rapido")
S("palacio", "En ese momento, Amán llegó muy temprano para pedir la muerte de Mardoqueo. Pero antes de que hablara, el rey le preguntó: ¿Qué debo hacer por el hombre a quien quiero honrar?",
  [P("aman", 0.35, emocion="feliz"), P("rey_asuero", 0.68, mira="izquierda", accion="senalar")], habla="rey_asuero", camara="acercar")
S("palacio", "Amán pensó: ¿A quién querrá honrar el rey sino a mí? Y respondió: Que lo vistan con el manto real, lo suban al caballo del rey y lo paseen por la ciudad gritando: ¡Así se hace con el hombre a quien el rey quiere honrar!",
  [P("aman", 0.45, accion="celebrar", emocion="burlon")], habla="aman", camara="paneo")
S("palacio", "¡Muy bien! Date prisa y hazlo así... con Mardoqueo el judío.",
  [P("rey_asuero", 0.6, mira="izquierda", accion="senalar", emocion="feliz"), P("aman", 0.35, emocion="sorprendido", accion="temblar")], habla="rey_asuero",
  efectos=[{"tipo": "flash", "inicio": 0.4}], camara="acercar_rapido")
S("ciudad", "Y Amán tuvo que pasear por toda la ciudad a su peor enemigo, gritando su honor. Volvió a casa humillado, con la cabeza cubierta.",
  [P("mardoqueo", 0.45, manto="#8a2a6a", emocion="feliz"), P("aman", 0.25, accion="senalar", emocion="triste")], [gente(0.75, 0.5)], camara="paneo")
S("cielo", "Pausa. Dios no aparece ni una sola vez nombrado en el libro de Ester... pero ¿lo ves trabajando detrás de cada detalle? Escribe en los comentarios: Dios está en los detalles.",
  [P("ester", 0.5, **REINA, accion="senalar")], efectos=[{"tipo": "luz"}], rotulo="DIOS EN LOS DETALLES", camara="fijo")

# ---------- 7. EL BANQUETE ----------
S("palacio", "Esa misma tarde llegaron los mensajeros del rey a buscar a Amán para el segundo banquete. Él no sabía que iba directo hacia su final.",
  [P("aman", 0.45, accion="caminar", hasta=0.6, emocion="triste"), P("guardia1", 0.25, accion="caminar", hasta=0.4, objeto="lanza")], camara="paneo")
S("palacio", "En el segundo banquete, el rey volvió a preguntar: ¿Cuál es tu petición, reina Ester? Y ella por fin habló:",
  [P("rey_asuero", 0.5, mira="izquierda"), P("ester", 0.3, **REINA), P("aman", 0.75, mira="izquierda", emocion="feliz")], [{"tipo": "mesa", "x": 0.5}],
  rotulo="CAPÍTULO 6: LA VERDAD", camara="acercar")
S("palacio", "Oh rey, te pido mi vida y la vida de mi pueblo. Porque hemos sido vendidos para ser destruidos, asesinados y exterminados.",
  [P("ester", 0.4, **REINA, accion="arrodillarse", emocion="llorando")], habla="ester", camara="acercar_rapido")
S("palacio", "El rey se levantó furioso: ¿Quién es? ¿Dónde está el que se ha atrevido a hacer esto? Y Ester señaló: ¡El enemigo es este malvado Amán!",
  [P("rey_asuero", 0.5, accion="levantar", emocion="enojado"), P("ester", 0.3, **REINA, accion="senalar", emocion="valiente"), P("aman", 0.75, mira="izquierda", accion="temblar", emocion="asustado")],
  habla="ester", efectos=[{"tipo": "temblor", "inicio": 0.6, "fin": 0.8}, {"tipo": "flash", "inicio": 0.65}], camara="acercar_rapido")
S("palacio", "Amán fue condenado y colgado en la misma horca que había preparado para Mardoqueo. Y el rey le entregó a Ester toda la casa de Amán, y a Mardoqueo le dio su anillo. Ahora él era el primer ministro.",
  [P("mardoqueo", 0.45, manto="#8a2a6a", emocion="feliz"), P("rey_asuero", 0.68, mira="izquierda", accion="ofrecer", emocion="feliz")], efectos=[{"tipo": "luz"}], camara="paneo")
S("ciudad", "La ley del rey no se podía anular. Pero se escribió una nueva ley: los judíos podrían defenderse. Y el día que debía ser de muerte, se convirtió en un día de victoria.",
  [P("hombre1", 0.35, accion="celebrar", emocion="feliz"), P("mujer1", 0.55, accion="alabar", emocion="feliz"), P("mardoqueo", 0.75, emocion="feliz")], [gente(0.5, 0.5, y=-150)],
  efectos=[{"tipo": "luz"}, {"tipo": "brillo"}], camara="alejar")
S("ciudad", "Desde entonces, cada año, el pueblo judío celebra la fiesta de Purim, para recordar cómo Dios cambió el luto en alegría a través de una joven valiente.",
  [P("ester", 0.4, **REINA, accion="celebrar", emocion="feliz"), P("mardoqueo", 0.6, manto="#8a2a6a", accion="alabar", emocion="feliz")], efectos=[{"tipo": "arcoiris"}], rotulo="PURIM", camara="paneo")

# ---------- ENSEÑANZA Y FINAL ----------
S("cielo", "Ester no nació reina. Era huérfana, extranjera y tenía miedo. Pero cuando llegó su hora, fue valiente. El valor no es no tener miedo, sino obedecer a Dios aunque lo tengas.",
  [P("ester", 0.5, **REINA, accion="orar")], efectos=[{"tipo": "luz"}], rotulo="ENSEÑANZA", camara="acercar")
S("cielo", "Y aunque no lo veas, Dios está moviendo las piezas: una noche sin sueño, un libro leído en la página exacta, un cetro levantado a tiempo.",
  [P("ester", 0.5, **REINA, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="fijo")
S("cielo", "¿Cuál fue tu momento favorito: el cetro de oro, la noche del rey o la caída de Amán? Escríbelo en los comentarios.",
  [P("ester", 0.4, **REINA, accion="senalar"), P("mardoqueo", 0.62, mira="izquierda", emocion="feliz")], efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "Suscríbete y activa la campanita, que mañana llega otra gran historia de la Biblia. ¡Dios te bendiga!",
  [P("ester", 0.5, **REINA, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="¡SUSCRÍBETE!", pausa=2.0, camara="acercar")

guardar("11_ester_la_historia_completa.json", "Ester - La Reina Valiente",
        "Si entraba sin permiso, MORÍA.",
        ["ESTER", "MARDOQUEO", "AMÁN", "REY", "CETRO", "REINA", "PUEBLO", "HORA"],
        personajes={"mardoqueo": {"tunica": "#3f5a8a", "manto": "#d9c7a3", "barba": "#cfcac0", "pelo": "#cfcac0", "tocado": "turbante", "color_tocado": "#e9e4d8"}},
        miniatura={"texto": ["SI ENTRABA", "MORÍA"],
                   "escena": {"fondo": "palacio", "personajes": [
                       {"id": "ester", "x": 0.6, "accion": "caminar", "emocion": "asustado", "tocado": "corona", "escala": 1.3},
                       {"id": "rey_asuero", "x": 0.86, "mira": "izquierda", "emocion": "enojado", "escala": 1.3}],
                       "cosas": [{"tipo": "trono", "x": 0.88, "profundidad": -30}], "efectos": [{"tipo": "oscuridad", "fuerza": 0.2}, {"tipo": "luz", "x": 0.6}]}})
