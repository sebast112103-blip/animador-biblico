"""Video largo: Salomón, la historia completa."""
from base import S, P, gente, guardar

REY = {"tocado": "corona"}

# ---------- APERTURA EN FRÍO ----------
S("palacio", "¡Traigan una espada y partan al bebé en dos! Eso ordenó el rey. Dos mujeres decían ser la madre del mismo niño, y no había testigos ni pruebas.",
  [P("mujer1", 0.25, accion="senalar", emocion="enojado"), P("madre2", 0.42, accion="senalar", emocion="llorando"), P("salomon", 0.75, mira="izquierda", **REY, accion="levantar")],
  [{"tipo": "trono", "x": 0.8, "profundidad": -30}], camara="acercar_rapido", portada=True)
S("palacio", "¿De verdad iba a hacerlo? Este es el rey más sabio que ha existido. Hoy verás cómo llegó al trono, lo que construyó... y cómo terminó.",
  [P("salomon", 0.5, **REY, emocion="valiente")], efectos=[{"tipo": "flash", "inicio": 0.85}], camara="acercar")

# ---------- 1. EL NUEVO REY ----------
S("valle", "Pero antes, hubo una traición. Adonías, otro hijo de David, se proclamó rey a escondidas. Hizo una gran fiesta, invitó a los generales y a los príncipes... y no invitó a Salomón.",
  [P("hermano1", 0.45, tocado="corona", accion="celebrar", emocion="burlon")], [gente(0.75, 0.5), {"tipo": "mesa", "x": 0.3}], camara="paneo")
S("palacio", "El profeta Natán y Betsabé, la madre de Salomón, corrieron a avisarle al anciano rey David: ¿No juraste que nuestro hijo Salomón reinaría después de ti? Ahora Adonías se ha hecho rey.",
  [P("mujer1", 0.35, accion="senalar", emocion="asustado"), P("hombre1", 0.55, barba="#e8e4dc", pelo="#e8e4dc"), P("david", 0.78, mira="izquierda", tocado="corona", barba="#e8e4dc", pelo="#e8e4dc", emocion="sorprendido")],
  habla="mujer1", camara="acercar")
S("ciudad", "David reaccionó de inmediato. Ordenó que montaran a Salomón en su propia mula, lo llevaran al río Gihón y lo ungieran rey. Y el pueblo tocó trompetas y gritó: ¡Viva el rey Salomón! La fiesta de Adonías terminó en un instante.",
  [P("salomon", 0.5, accion="levantar", emocion="feliz", tocado="corona")], [gente(0.5, 0.6, y=320, delante=True, profundidad=None)], efectos=[{"tipo": "luz"}], camara="alejar")
S("palacio", "El rey David ya era muy anciano. Y antes de morir, eligió como sucesor a su hijo Salomón, el hijo que tuvo con Betsabé.",
  [P("david", 0.38, tocado="corona", barba="#e8e4dc", pelo="#e8e4dc", accion="ofrecer"), P("salomon", 0.62, mira="izquierda", emocion="sorprendido")],
  [{"tipo": "trono", "x": 0.2, "profundidad": -30}], camara="acercar")
S("palacio", "David le dio sus últimos consejos: Yo voy por el camino de todos los mortales. Esfuérzate y sé valiente. Guarda los mandamientos del Señor, y te irá bien en todo lo que hagas.",
  [P("david", 0.4, tocado="corona", barba="#e8e4dc", pelo="#e8e4dc", accion="senalar", emocion="triste"), P("salomon", 0.62, mira="izquierda")], habla="david", camara="fijo")
S("palacio", "Salomón era muy joven, quizás de unos veinte años. Y de pronto tenía que gobernar a un pueblo enorme, con enemigos alrededor y una gran responsabilidad.",
  [P("salomon", 0.5, **REY, emocion="asustado")], [{"tipo": "trono", "x": 0.55, "profundidad": -30}], camara="acercar")

# ---------- 2. EL SUEÑO ----------
S("noche", "Una noche, en Gabaón, Dios se le apareció en un sueño y le hizo una oferta increíble: Pídeme lo que quieras, y yo te lo daré.",
  [P("salomon", 0.5, **REY, accion="dormir")], efectos=[{"tipo": "luz", "x": 0.7}, {"tipo": "brillo", "x": 0.7, "y": -600}], rotulo="CAPÍTULO 1: PÍDEME LO QUE QUIERAS", camara="acercar")
S("cielo", "Imagina que Dios te dice eso a ti. ¿Qué pedirías? ¿Dinero? ¿Salud? ¿Fama? Piénsalo un segundo... y escríbelo en los comentarios antes de ver qué pidió Salomón.",
  [P("salomon", 0.5, **REY, emocion="sorprendido")], efectos=[{"tipo": "luz"}], rotulo="¿QUÉ PEDIRÍAS TÚ?", camara="fijo")
S("noche", "Salomón respondió: Señor, yo soy como un niño pequeño. No sé cómo gobernar. Dame un corazón entendido para juzgar a tu pueblo y para distinguir entre el bien y el mal.",
  [P("salomon", 0.5, **REY, accion="arrodillarse")], habla="salomon", efectos=[{"tipo": "luz", "x": 0.7}], camara="acercar")
S("cielo", "A Dios le agradó mucho esa petición. Y le dijo: Porque no pediste larga vida, ni riquezas, ni la muerte de tus enemigos, sino sabiduría, te daré un corazón sabio como nunca hubo ni habrá otro igual.",
  [], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="alejar")
S("cielo", "Y además te daré lo que no pediste: riquezas y gloria, más que a cualquier rey de tu tiempo.",
  [P("salomon", 0.5, **REY, accion="alabar", emocion="feliz")], [{"tipo": "monedas", "x": 0.7}], efectos=[{"tipo": "luz"}, {"tipo": "brillo"}], camara="acercar")

# ---------- 3. LAS DOS MADRES ----------
S("palacio", "Poco después, llegaron ante el rey dos mujeres con un bebé. La primera dijo: Majestad, las dos vivimos en la misma casa y las dos tuvimos un hijo con tres días de diferencia.",
  [P("mujer1", 0.3, accion="senalar", emocion="llorando"), P("madre2", 0.48, emocion="enojado"), P("salomon", 0.78, mira="izquierda", **REY)],
  [{"tipo": "trono", "x": 0.82, "profundidad": -30}], habla="mujer1", rotulo="CAPÍTULO 2: EL JUICIO", camara="paneo")
S("palacio", "Una noche, el hijo de ella murió. Y mientras yo dormía, cambió los bebés: puso a su hijo muerto en mis brazos y se llevó al mío.",
  [P("mujer1", 0.4, accion="temblar", emocion="llorando")], habla="mujer1", efectos=[{"tipo": "oscuridad", "fuerza": 0.3}], camara="acercar")
S("palacio", "¡Mentira!, gritó la otra. ¡El niño vivo es mío, y el muerto es el tuyo! Y empezaron a discutir delante del rey.",
  [P("madre2", 0.4, accion="senalar", emocion="enojado"), P("mujer1", 0.6, mira="izquierda", accion="senalar", emocion="enojado")], habla="madre2", camara="acercar_rapido")
S("palacio", "El rey escuchó en silencio. Y luego dijo: Traigan una espada. Partan al niño vivo en dos, y den una mitad a cada una.",
  [P("salomon", 0.5, **REY, accion="senalar"), P("guardia1", 0.75, mira="izquierda", objeto="espada")], habla="salomon", efectos=[{"tipo": "temblor", "inicio": 0.7, "fin": 0.85}], camara="acercar")
S("palacio", "La verdadera madre gritó con desesperación: ¡No, por favor! ¡Denle el niño a ella, pero no lo maten! Pero la otra dijo: Ni para mí ni para ti. ¡Que lo partan!",
  [P("mujer1", 0.35, accion="arrodillarse", emocion="llorando"), P("madre2", 0.58, emocion="burlon")], habla="mujer1", camara="acercar_rapido")
S("palacio", "Entonces Salomón levantó la mano: Denle el niño a la primera. No lo maten. Ella es su madre. Una madre de verdad prefiere perder a su hijo antes que verlo morir.",
  [P("salomon", 0.6, **REY, accion="levantar", emocion="feliz"), P("mujer1", 0.38, accion="abrazar", emocion="llorando")], [{"tipo": "pesebre", "x": 0.42, "escala": 0.6}],
  habla="salomon", efectos=[{"tipo": "luz"}], camara="acercar")
S("ciudad", "Todo Israel se enteró de esa sentencia, y respetaron al rey, porque vieron que tenía la sabiduría de Dios para hacer justicia.",
  [], [gente(0.5, 0.6, y=-120)], efectos=[{"tipo": "luz"}], camara="alejar")

# ---------- 4. EL TEMPLO ----------
S("ciudad", "Salomón se hizo famoso. Escribió tres mil proverbios y más de mil canciones. Sabía de plantas, de animales, de aves y de peces. Gente de todas las naciones venía a escucharlo.",
  [P("salomon", 0.45, **REY, accion="senalar", emocion="feliz")], [gente(0.75, 0.5)], rotulo="CAPÍTULO 3: LA CASA DE DIOS", camara="paneo")
S("cielo", "Muchos de esos proverbios están en tu Biblia. Por ejemplo: Fíate del Señor de todo tu corazón, y no te apoyes en tu propia prudencia.",
  [P("salomon", 0.5, **REY, accion="orar")], efectos=[{"tipo": "luz"}], rotulo="PROVERBIOS 3:5", camara="fijo")
S("templo", "Pero su obra más grande fue cumplir el sueño de su padre David: construir el templo de Dios en Jerusalén.",
  [P("salomon", 0.45, **REY, accion="levantar")], efectos=[{"tipo": "luz"}], camara="alejar")
S("palacio", "Salomón le pidió ayuda a su amigo Hiram, rey de Tiro. Hiram le envió los mejores cedros del Líbano por el mar, atados como balsas. Y Salomón le pagaba cada año con trigo y aceite.",
  [P("salomon", 0.38, **REY, accion="ofrecer"), P("rey_asuero", 0.65, mira="izquierda", emocion="feliz")], [{"tipo": "arbol", "x": 0.85}], camara="paneo")
S("templo", "Durante siete años trabajaron miles de obreros. Usaron piedras enormes, madera de cedro del Líbano y lo cubrieron todo por dentro con oro puro. Ni siquiera se escuchaba un martillo en el lugar, porque las piedras llegaban ya cortadas.",
  [P("hombre1", 0.3, accion="empujar"), P("hombre2", 0.5, accion="levantar")], [{"tipo": "piedra", "x": 0.4, "escala": 0.6}, {"tipo": "columna", "x": 0.75}], rotulo="7 AÑOS", camara="paneo")
S("templo", "El día de la dedicación, los sacerdotes llevaron el arca del pacto al lugar santísimo. Y cuando los músicos empezaron a alabar a Dios...",
  [P("salomon", 0.5, **REY, accion="alabar")], [gente(0.5, 0.55, y=320, delante=True, profundidad=None)], camara="acercar")
S("templo", "...una nube llenó el templo. La gloria de Dios era tan fuerte que los sacerdotes no podían quedarse de pie para servir.",
  [P("salomon", 0.5, **REY, accion="arrodillarse", emocion="sorprendido")], efectos=[{"tipo": "luz"}, {"tipo": "brillo"}, {"tipo": "flash", "inicio": 0.1}], camara="acercar_rapido")
S("templo", "Salomón oró de rodillas, con las manos extendidas al cielo: Señor, ni los cielos de los cielos te pueden contener, ¡cuánto menos esta casa! Pero escucha las oraciones de tu pueblo cuando oren hacia este lugar.",
  [P("salomon", 0.5, **REY, accion="orar")], habla="salomon", efectos=[{"tipo": "luz"}], camara="fijo")
S("templo", "Y al terminar de orar, cayó fuego del cielo y consumió el sacrificio. Todo el pueblo se postró y adoró diciendo: Porque él es bueno, y su misericordia es para siempre.",
  [], [{"tipo": "altar", "x": 0.5}, gente(0.5, 0.55, y=320, delante=True, profundidad=None)], efectos=[{"tipo": "fuego", "x": 0.5, "y": -100, "tamano": 2.2, "crece": True}, {"tipo": "luz"}],
  camara="alejar")

# ---------- 5. LA REINA DE SABÁ ----------
S("desierto", "La fama de Salomón llegó hasta tierras muy lejanas. Y la reina de Sabá viajó más de dos mil kilómetros con una gran caravana de camellos cargados de especias, oro y piedras preciosas.",
  [P("reina_saba", 0.45, accion="caminar", hasta=0.55), P("burro", 0.25, accion="caminar", hasta=0.35)], [{"tipo": "monedas", "x": 0.7}], rotulo="CAPÍTULO 4: LA REINA DE SABÁ", camara="paneo")
S("palacio", "Venía a probarlo con preguntas difíciles. Y Salomón respondió todas. No hubo ninguna que no supiera contestar.",
  [P("reina_saba", 0.35, accion="senalar", emocion="sorprendido"), P("salomon", 0.68, mira="izquierda", **REY, accion="ofrecer", emocion="feliz")], camara="acercar")
S("palacio", "Cuando vio su sabiduría, el palacio, la comida, sus siervos y el templo, la reina se quedó sin aliento: Ni siquiera me contaron la mitad. Tu sabiduría supera todo lo que había oído. Bendito sea el Señor tu Dios.",
  [P("reina_saba", 0.4, accion="alabar", emocion="sorprendido")], habla="reina_saba", efectos=[{"tipo": "luz"}], camara="acercar_rapido")
S("palacio", "En Jerusalén la plata llegó a ser tan común como las piedras. Salomón fue el rey más rico y más sabio de toda la tierra.",
  [P("salomon", 0.5, **REY, accion="levantar", emocion="feliz")], [{"tipo": "monedas", "x": 0.3}, {"tipo": "monedas", "x": 0.75}], efectos=[{"tipo": "brillo"}], camara="paneo")

# ---------- 6. EL CORAZÓN DIVIDIDO ----------
S("palacio", "Tenía miles de caballos y carros de guerra, flotas de barcos que traían oro, plata, marfil y monos de tierras lejanas. Cada día, su palacio consumía toneladas de comida. Nunca nadie había vivido con tanto lujo.",
  [P("salomon", 0.45, **REY, accion="celebrar", emocion="feliz")], [{"tipo": "mesa", "x": 0.7}, {"tipo": "monedas", "x": 0.28}], camara="paneo")
S("palacio", "Pero aquí viene la parte que muchos no conocen. Dios había advertido que el rey no debía multiplicar esposas, ni caballos, ni oro. Y Salomón hizo las tres cosas.",
  [P("salomon", 0.5, **REY, emocion="burlon")], efectos=[{"tipo": "oscuridad", "fuerza": 0.25}], rotulo="CAPÍTULO 5: EL CORAZÓN DIVIDIDO", camara="acercar")
S("palacio", "Tuvo setecientas esposas y trescientas concubinas, muchas de ellas de pueblos que adoraban otros dioses. Y cuando envejeció, ellas desviaron su corazón.",
  [P("salomon", 0.45, **REY, barba="#e8e4dc", pelo="#e8e4dc"), P("mujer1", 0.68, mira="izquierda", emocion="burlon")], [gente(0.85, 0.45)], camara="paneo")
S("montana", "El hombre que construyó el templo de Dios... terminó construyendo altares para ídolos en los montes de Jerusalén.",
  [P("salomon", 0.45, **REY, barba="#e8e4dc", pelo="#e8e4dc", accion="arrodillarse", emocion="triste")], [{"tipo": "altar", "x": 0.68}, {"tipo": "columna", "x": 0.85, "escala": 0.6}],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.4}], camara="acercar")
S("cielo", "Dios se enojó con Salomón, y le anunció que después de su muerte el reino se dividiría. Y así pasó: Israel se partió en dos reinos que nunca volvieron a unirse.",
  [], efectos=[{"tipo": "oscuridad", "fuerza": 0.4}, {"tipo": "rayo", "inicio": 0.5}, {"tipo": "temblor", "inicio": 0.5, "fin": 0.7}], camara="alejar")
S("campo", "Un día, el profeta Ahías encontró a un joven siervo de Salomón llamado Jeroboam. Tomó su manto nuevo, lo rompió en doce pedazos y le dijo: Toma diez para ti. Dios le quitará el reino a la casa de Salomón y te dará diez tribus.",
  [P("hombre1", 0.38, barba="#e8e4dc", pelo="#e8e4dc", accion="ofrecer"), P("hermano2", 0.62, mira="izquierda", emocion="sorprendido")], habla="hombre1", camara="acercar")
S("palacio", "Salomón reinó cuarenta años en Jerusalén. Y cuando murió, su hijo Roboam tomó el trono... y en poco tiempo el reino se partió, tal como Dios lo había dicho.",
  [P("salomon", 0.5, **REY, barba="#e8e4dc", pelo="#e8e4dc", accion="dormir")], efectos=[{"tipo": "oscuridad", "fuerza": 0.35}], rotulo="40 AÑOS", camara="acercar")
S("cielo", "Pausa. ¿Cómo crees que el hombre más sabio del mundo terminó así? Deja tu opinión en los comentarios.",
  [P("salomon", 0.5, **REY, barba="#e8e4dc", pelo="#e8e4dc", emocion="triste")], efectos=[{"tipo": "luz"}], rotulo="¿CÓMO PASÓ?", camara="fijo")

# ---------- 7. VANIDAD DE VANIDADES ----------
S("cielo", "Al final de su vida, Salomón escribió el libro de Eclesiastés. Lo había tenido todo: sabiduría, riquezas, placeres, fama. Y su conclusión fue: Vanidad de vanidades, todo es vanidad.",
  [P("salomon", 0.5, **REY, barba="#e8e4dc", pelo="#e8e4dc", accion="orar", emocion="triste")], efectos=[{"tipo": "luz"}], rotulo="CAPÍTULO 6: LA CONCLUSIÓN", camara="acercar")
S("cielo", "Y terminó con este consejo: El fin de todo el discurso es este: teme a Dios y guarda sus mandamientos, porque esto es el todo del hombre.",
  [P("salomon", 0.5, **REY, barba="#e8e4dc", pelo="#e8e4dc", accion="senalar")], habla="salomon", efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="ECLESIASTÉS 12:13", camara="fijo")

# ---------- ENSEÑANZA Y FINAL ----------
S("cielo", "Salomón nos enseña dos cosas. Primero: la sabiduría de Dios vale más que todo el oro del mundo, y Dios la da a quien se la pide.",
  [P("salomon", 0.5, **REY, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}], rotulo="ENSEÑANZA", camara="acercar")
S("cielo", "Y segundo: no importa cómo empieces, sino cómo termines. Un corazón dividido puede perder lo que tanto le costó construir. Por eso, cuida tu corazón cada día.",
  [P("salomon", 0.5, **REY, accion="orar")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="fijo")
S("cielo", "Y recuerda tu respuesta del principio. Si Dios te dijera hoy pídeme lo que quieras, ¿seguirías pidiendo lo mismo? Cuéntame en los comentarios.",
  [P("salomon", 0.4, **REY, accion="senalar"), P("reina_saba", 0.62, mira="izquierda", emocion="feliz")], efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "Suscríbete y activa la campanita, que mañana llega otra gran historia de la Biblia. ¡Dios te bendiga!",
  [P("salomon", 0.5, **REY, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="¡SUSCRÍBETE!", pausa=2.0, camara="acercar")

guardar("13_salomon_la_historia_completa.json", "Salomón - El Rey Más Sabio",
        "¿Partiría al BEBÉ en dos?",
        ["SALOMÓN", "SABIDURÍA", "TEMPLO", "REY", "DAVID", "SABÁ", "CORAZÓN", "SEÑOR"],
        personajes={"salomon": {"tunica": "#f4f1ea", "manto": "#7a2a8a", "tocado": "corona", "barba": "#3a2a1a", "pelo": "#3a2a1a"},
                    "madre2": {"tunica": "#8a6a3a", "tocado": "velo", "color_tocado": "#5a4a2a", "pelo": None, "voz": {"nombre": "es_AR-daniela-high", "tono": -2}},
                    "reina_saba": {"tunica": "#d9a62e", "manto": "#1a6a6a", "tocado": "corona", "piel": "#8a5a3a", "pelo": "#1a1410", "pelo_largo": True,
                                   "voz": {"nombre": "es_AR-daniela-high", "tono": -1}}},
        miniatura={"texto": ["¡PARTAN", "AL NIÑO!"], "sello": "EL REY MÁS SABIO",
                   "escena": {"fondo": "palacio", "personajes": [
                       {"id": "mujer1", "x": 0.55, "accion": "arrodillarse", "emocion": "llorando", "escala": 1.2},
                       {"id": "salomon", "x": 0.75, "mira": "izquierda", "accion": "levantar", "tocado": "corona", "escala": 1.3},
                       {"id": "guardia1", "x": 0.92, "mira": "izquierda", "objeto": "espada", "emocion": "enojado", "escala": 1.3}],
                       "cosas": [{"tipo": "trono", "x": 0.75, "profundidad": -30}], "efectos": [{"tipo": "luz", "x": 0.75}]}})
