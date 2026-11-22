"""Video largo: Jonás y el gran pez, la historia completa."""
from base import S, P, gente, guardar

# ---------- APERTURA EN FRÍO ----------
S("dentro_pez", "Oscuridad total. Algas enredadas en la cabeza. Un olor insoportable. Un hombre está vivo... dentro del estómago de un pez gigante.",
  [P("jonas", 0.5, accion="temblar", emocion="asustado")], efectos=[{"tipo": "oscuridad", "fuerza": 0.35}], camara="acercar_rapido", portada=True)
S("dentro_pez", "Lleva ahí tres días y tres noches. ¿Cómo llegó a ese lugar? Todo empezó cuando Dios le pidió algo... y él salió corriendo en dirección contraria.",
  [P("jonas", 0.5, accion="orar", emocion="llorando")], efectos=[{"tipo": "oscuridad", "fuerza": 0.35}, {"tipo": "flash", "inicio": 0.85}], camara="acercar")

# ---------- 1. LA ORDEN ----------
S("campo", "Jonás era un profeta de Israel. Un hombre que escuchaba la voz de Dios y llevaba sus mensajes al pueblo.",
  [P("jonas", 0.5, emocion="feliz")], efectos=[{"tipo": "luz", "x": 0.5}], rotulo="CAPÍTULO 1: LA ORDEN", camara="acercar")
S("campo", "Vivía en un pueblito de Galilea llamado Gat-hefer, muy cerca de donde siglos después crecería Jesús. Y ya había anunciado buenas noticias al rey de Israel, que se cumplieron tal como él dijo.",
  [P("jonas", 0.4, accion="senalar", emocion="feliz"), P("hombre1", 0.68, mira="izquierda", emocion="feliz")], camara="paneo")
S("campo", "Un día, Dios le habló: Levántate y ve a Nínive, la gran ciudad, y anúnciale que su maldad ha llegado hasta mí.",
  [P("jonas", 0.45, emocion="sorprendido")], efectos=[{"tipo": "luz", "x": 0.7}, {"tipo": "brillo", "x": 0.7, "y": -600}], camara="acercar")
S("ciudad", "Pero Nínive no era cualquier ciudad. Era la capital de Asiria, el imperio más cruel de su tiempo. Los enemigos más temidos de Israel.",
  [P("enemigo1", 0.35, objeto="espada", emocion="enojado"), P("enemigo2", 0.6, objeto="lanza", emocion="burlon")], [gente(0.5, 0.6, variante="soldados")],
  efectos=[{"tipo": "fuego", "x": 0.85, "tamano": 0.9}, {"tipo": "oscuridad", "fuerza": 0.3}], camara="paneo")
S("ciudad", "Los asirios conquistaban pueblos y trataban a los prisioneros con una crueldad terrible. Todo el mundo les tenía miedo.",
  [P("enemigo1", 0.4, accion="senalar", emocion="enojado"), P("hombre2", 0.65, accion="temblar", emocion="asustado")], camara="acercar")
S("campo", "Jonás pensó: ¿Ir a advertirles? ¿Y si se arrepienten y Dios los perdona? ¡No! Ellos merecen el castigo.",
  [P("jonas", 0.5, emocion="enojado", accion="senalar")], habla="jonas", camara="acercar_rapido")
S("camino", "Así que Jonás tomó una decisión. Se levantó... pero no fue hacia Nínive, que estaba al oriente. Huyó hacia el occidente, a Tarsis, lo más lejos posible.",
  [P("jonas", 0.6, accion="correr", hasta=0.05, mira="izquierda", emocion="asustado")], camara="paneo")

# ---------- 2. LA HUIDA ----------
S("mar", "Bajó al puerto de Jope, pagó su pasaje y se subió a un barco que salía hacia Tarsis. Quería huir de la presencia de Dios.",
  [P("jonas", 0.2, hasta=0.45, accion="caminar"), P("marinero1", 0.7, mira="izquierda")], [{"tipo": "barca", "x": 0.65, "escala": 1.0}],
  rotulo="CAPÍTULO 2: LA HUIDA", camara="paneo")
S("mar", "Tarsis estaba en el otro extremo del mar conocido, probablemente en lo que hoy es España. Era como decir: me voy al fin del mundo, donde Dios no me encuentre.",
  [P("jonas", 0.45, emocion="valiente"), P("marinero2", 0.72, mira="izquierda")], [{"tipo": "barca", "x": 0.6, "escala": 1.0, "profundidad": -100}], camara="alejar")
S("mar", "Una vez en alta mar, Jonás bajó a lo más profundo del barco, se acostó... y se quedó profundamente dormido.",
  [P("jonas", 0.5, accion="dormir")], [{"tipo": "barca", "x": 0.5, "escala": 1.0}], camara="acercar")
S("cielo", "¿Alguna vez intentaste huir de algo que sabías que debías hacer? Escribe en los comentarios: Yo también he huido. Porque lo que pasó después nos enseña mucho.",
  [P("jonas", 0.5, accion="dormir")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 3. LA TORMENTA ----------
S("mar_tormenta", "Pero no se puede huir de Dios. El Señor envió un viento tan fuerte sobre el mar, que la tormenta amenazaba con partir el barco en pedazos.",
  [], [{"tipo": "barca", "x": 0.5, "escala": 1.0}], efectos=[{"tipo": "lluvia"}, {"tipo": "rayo", "inicio": 0.3}, {"tipo": "temblor", "inicio": 0.2, "fin": 0.9}],
  rotulo="CAPÍTULO 3: LA TORMENTA", camara="acercar_rapido")
S("mar_tormenta", "Los marineros, aterrados, empezaron a gritar cada uno a su dios. Y tiraron la carga al mar para que el barco no se hundiera.",
  [P("marinero1", 0.35, accion="lanzar", emocion="asustado"), P("marinero2", 0.62, accion="orar", emocion="asustado")], [{"tipo": "barca", "x": 0.5, "escala": 1.0, "profundidad": -100}],
  efectos=[{"tipo": "lluvia"}, {"tipo": "rayo", "inicio": 0.6}], camara="acercar")
S("mar_tormenta", "El capitán bajó y encontró a Jonás dormido. ¿Cómo puedes dormir? ¡Levántate y clama a tu Dios! Quizás él tenga compasión de nosotros.",
  [P("marinero1", 0.35, accion="senalar", emocion="asustado"), P("jonas", 0.65, accion="dormir")], habla="marinero1", efectos=[{"tipo": "lluvia"}], camara="acercar")
S("mar_tormenta", "Los marineros echaron suertes para saber quién tenía la culpa de esa desgracia. Y la suerte cayó sobre Jonás.",
  [P("marinero1", 0.3, emocion="sorprendido"), P("marinero2", 0.5, emocion="sorprendido"), P("jonas", 0.75, mira="izquierda", emocion="asustado")],
  efectos=[{"tipo": "lluvia"}, {"tipo": "flash", "inicio": 0.7}], camara="acercar_rapido")
S("mar_tormenta", "¿Quién eres? ¿Qué has hecho?, le preguntaron. Y Jonás confesó: Soy hebreo. Temo al Señor, el Dios del cielo, que hizo el mar y la tierra... y estoy huyendo de él.",
  [P("jonas", 0.45, accion="arrodillarse", emocion="triste"), P("marinero1", 0.72, mira="izquierda", emocion="asustado")], habla="jonas", efectos=[{"tipo": "lluvia"}], camara="acercar")
S("mar_tormenta", "¿Qué hacemos contigo para que el mar se calme? Y Jonás respondió: Tírenme al mar. Yo sé que esta tormenta es por mi culpa.",
  [P("jonas", 0.5, accion="senalar", emocion="triste")], habla="jonas", efectos=[{"tipo": "lluvia"}, {"tipo": "rayo", "inicio": 0.7}], camara="acercar_rapido")
S("mar_tormenta", "Los marineros no querían hacerlo. Remaron con todas sus fuerzas hacia la orilla... pero el mar se embravecía cada vez más.",
  [P("marinero1", 0.35, accion="empujar", emocion="asustado"), P("marinero2", 0.6, accion="empujar", emocion="asustado")], [{"tipo": "barca", "x": 0.5, "escala": 1.0, "profundidad": -100}],
  efectos=[{"tipo": "lluvia"}, {"tipo": "temblor", "inicio": 0.1, "fin": 0.9}], camara="paneo")
S("mar_tormenta", "Al final, tomaron a Jonás... y lo lanzaron al mar.",
  [P("jonas", 0.5, accion="caer", emocion="asustado")], efectos=[{"tipo": "agua"}, {"tipo": "flash", "inicio": 0.5}], camara="acercar_rapido")
S("mar", "Y en ese mismo instante, el mar se calmó por completo. Los marineros, asombrados, adoraron al Dios de Jonás.",
  [P("marinero1", 0.4, accion="alabar", emocion="sorprendido"), P("marinero2", 0.6, accion="arrodillarse", emocion="sorprendido")], [{"tipo": "barca", "x": 0.5, "escala": 1.0, "profundidad": -100}],
  efectos=[{"tipo": "luz"}], camara="alejar")

# ---------- 4. EL GRAN PEZ ----------
S("mar", "Jonás se hundía en las profundidades. Las olas pasaban sobre su cabeza. Ya no había esperanza...",
  [P("jonas", 0.5, accion="caer", emocion="asustado")], efectos=[{"tipo": "oscuridad", "fuerza": 0.4}], rotulo="CAPÍTULO 4: EL GRAN PEZ", camara="acercar")
S("mar", "Pero Dios ya había preparado algo. De la oscuridad del océano apareció un pez enorme... y se tragó a Jonás de un solo bocado.",
  [], [{"tipo": "pez_gigante", "x": 0.5, "escala": 1.2}], efectos=[{"tipo": "agua"}, {"tipo": "temblor", "inicio": 0.5, "fin": 0.7}], camara="acercar_rapido")
S("dentro_pez", "Y ahí estaba Jonás, en el vientre del pez, vivo. Tres días y tres noches en la oscuridad.",
  [P("jonas", 0.5, accion="temblar", emocion="asustado")], efectos=[{"tipo": "oscuridad", "fuerza": 0.35}], rotulo="3 DÍAS", camara="acercar")
S("dentro_pez", "Imagínalo: sin luz, sin aire fresco, rodeado de agua y algas. Cada movimiento del pez lo sacudía de un lado a otro. Jonás pensó que ese sería su final.",
  [P("jonas", 0.5, accion="caer", emocion="asustado")], efectos=[{"tipo": "oscuridad", "fuerza": 0.4}, {"tipo": "temblor", "inicio": 0.3, "fin": 0.6}], camara="acercar_rapido")
S("dentro_pez", "Y en ese lugar, donde ya no podía huir de nada, Jonás hizo lo que debió hacer desde el principio: oró.",
  [P("jonas", 0.5, accion="arrodillarse", emocion="llorando")], efectos=[{"tipo": "oscuridad", "fuerza": 0.3}, {"tipo": "luz", "x": 0.5}], camara="acercar")
S("dentro_pez", "En mi angustia clamé al Señor, y él me respondió. Me echaste a lo profundo del mar, las aguas me rodearon... pero tú sacaste mi vida de la fosa.",
  [P("jonas", 0.5, accion="orar", emocion="llorando")], habla="jonas", efectos=[{"tipo": "luz", "x": 0.5}], camara="fijo")
S("dentro_pez", "Te ofreceré sacrificios con cantos de gratitud. Cumpliré lo que prometí. ¡La salvación viene del Señor!",
  [P("jonas", 0.5, accion="alabar", emocion="feliz")], habla="jonas", efectos=[{"tipo": "luz"}, {"tipo": "brillo"}], camara="acercar")
S("mar", "Entonces Dios le habló al pez... y el pez vomitó a Jonás en tierra seca.",
  [P("jonas", 0.4, accion="caer_de_cara", emocion="sorprendido")], [{"tipo": "pez_gigante", "x": 0.75, "escala": 0.9}], efectos=[{"tipo": "agua", "x": 0.6}, {"tipo": "flash", "inicio": 0.4}],
  camara="acercar_rapido")
S("cielo", "Pausa. Dime en los comentarios: ¿qué crees que sintió Jonás al ver la luz del sol otra vez?",
  [P("jonas", 0.5, accion="levantar", emocion="feliz")], efectos=[{"tipo": "luz"}], rotulo="¿QUÉ SINTIÓ?", camara="fijo")

# ---------- 5. NÍNIVE ----------
S("camino", "Por segunda vez, Dios le dijo a Jonás: Levántate y ve a Nínive. Y esta vez, Jonás obedeció.",
  [P("jonas", 0.15, hasta=0.6, accion="caminar", emocion="valiente")], efectos=[{"tipo": "luz", "x": 0.8}], rotulo="CAPÍTULO 5: NÍNIVE", camara="paneo")
S("ciudad", "Nínive era tan grande que se necesitaban tres días para recorrerla. Jonás entró y empezó a gritar por las calles:",
  [P("jonas", 0.4, accion="senalar", emocion="valiente")], [gente(0.65, 0.6)], camara="acercar")
S("ciudad", "¡Dentro de cuarenta días, Nínive será destruida!",
  [P("jonas", 0.5, accion="levantar", emocion="enojado")], [gente(0.5, 0.6, y=320, delante=True, profundidad=None)], habla="jonas",
  efectos=[{"tipo": "temblor", "inicio": 0.4, "fin": 0.6}], camara="acercar_rapido")
S("ciudad", "Imagina a un extranjero, con la piel blanqueada por los jugos del pez, gritando en medio de la ciudad más peligrosa del mundo. Jonás pudo haber sido apresado en ese mismo momento.",
  [P("jonas", 0.45, accion="senalar", emocion="valiente", piel="#f3e6d8"), P("enemigo1", 0.72, mira="izquierda", objeto="lanza", emocion="sorprendido")], camara="acercar")
S("ciudad", "Y entonces pasó algo increíble. La gente de Nínive le creyó a Dios. Dejaron de comer, se vistieron de luto, desde el más grande hasta el más pequeño.",
  [P("hombre2", 0.3, accion="arrodillarse", emocion="llorando"), P("mujer1", 0.5, accion="orar", emocion="llorando"), P("enemigo1", 0.7, accion="arrodillarse", emocion="triste")],
  camara="paneo")
S("palacio", "Hasta el rey de Nínive se levantó de su trono, se quitó su manto real, se sentó en ceniza, y ordenó a toda la ciudad: Clamen a Dios con todas sus fuerzas. ¿Quién sabe si Dios se arrepiente y nos perdona?",
  [P("rey_asuero", 0.5, accion="arrodillarse", emocion="llorando")], [{"tipo": "trono", "x": 0.7, "profundidad": -30}], habla="rey_asuero", camara="acercar")
S("ciudad", "Y Dios vio que se apartaron de su mal camino. Y tuvo compasión. No destruyó la ciudad. Más de ciento veinte mil personas fueron salvadas.",
  [P("hombre2", 0.35, accion="celebrar", emocion="feliz"), P("mujer1", 0.6, accion="alabar", emocion="feliz")], [gente(0.5, 0.55, y=-150)], efectos=[{"tipo": "luz"}, {"tipo": "brillo"}],
  camara="alejar")

# ---------- 6. EL ENOJO DE JONÁS ----------
S("desierto", "Cualquiera pensaría que Jonás estaría feliz. Pero no. Jonás se enojó muchísimo.",
  [P("jonas", 0.5, emocion="enojado", accion="temblar")], rotulo="CAPÍTULO 6: EL CORAZÓN DE DIOS", camara="acercar_rapido")
S("desierto", "¡Por esto huí a Tarsis!, le reclamó a Dios. Yo sabía que tú eres un Dios clemente y misericordioso, lento para la ira y lleno de amor.",
  [P("jonas", 0.5, accion="senalar", emocion="enojado")], habla="jonas", camara="acercar")
S("desierto", "Jonás salió de la ciudad y se sentó a esperar, por si acaso Dios la destruía. Hacía un calor terrible.",
  [P("jonas", 0.5, accion="agacharse", emocion="enojado")], camara="fijo")
S("desierto", "Dios hizo crecer una planta que le dio sombra. Jonás se puso muy contento con su planta.",
  [P("jonas", 0.45, emocion="feliz", accion="dormir")], [{"tipo": "arbol", "x": 0.55, "escala": 0.7}], efectos=[{"tipo": "brillo", "x": 0.55}], camara="acercar")
S("desierto", "Pero al día siguiente, Dios envió un gusano que secó la planta. Y con el sol y el viento caliente, Jonás deseó morirse.",
  [P("jonas", 0.45, emocion="llorando", accion="temblar")], efectos=[{"tipo": "oscuridad", "fuerza": 0.15}], camara="acercar")
S("desierto", "Entonces Dios le dijo: Tú tienes lástima de una planta que no sembraste y que vivió una sola noche.",
  [P("jonas", 0.5, emocion="sorprendido")], efectos=[{"tipo": "luz", "x": 0.7}, {"tipo": "brillo", "x": 0.7, "y": -600}], camara="acercar")
S("cielo", "¿Y no voy a tener yo compasión de Nínive, donde hay más de ciento veinte mil personas que no saben distinguir su derecha de su izquierda?",
  [], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="alejar")

# ---------- ENSEÑANZA Y FINAL ----------
S("cielo", "Jonás huyó de Dios, pero Dios no huyó de Jonás. Lo buscó en el barco, en el mar, y hasta en el vientre de un pez.",
  [P("jonas", 0.5, accion="orar")], efectos=[{"tipo": "luz"}], rotulo="ENSEÑANZA", camara="acercar")
S("cielo", "Y nos recuerda algo importante: el amor de Dios es más grande que nuestros enojos. Él quiere salvar incluso a los que nosotros creemos que no lo merecen.",
  [P("jonas", 0.5, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="fijo")
S("cielo", "Y algo más: Jesús dijo que así como Jonás estuvo tres días en el vientre del pez, él estaría tres días en la tumba antes de resucitar.",
  [P("jesus", 0.5, accion="ofrecer", emocion="feliz")], efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "¿Hay alguna Nínive en tu vida, alguien a quien te cuesta perdonar? Escríbelo en los comentarios. Y suscríbete, que mañana llega otra gran historia. ¡Dios te bendiga!",
  [P("jonas", 0.5, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="¡SUSCRÍBETE!", pausa=2.0, camara="acercar")

guardar("06_jonas_la_historia_completa.json", "Jonás y el Gran Pez - La Historia Completa",
        "Tres días VIVO dentro de un PEZ gigante... ¿cómo llegó ahí?",
        ["JONÁS", "NÍNIVE", "PEZ", "TORMENTA", "MAR", "TARSIS", "COMPASIÓN", "SEÑOR"])
