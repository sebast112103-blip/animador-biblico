"""Video largo: Noé y el arca, la historia completa."""
from base import S, P, gente, guardar

NOE = {}
VIEJO = {}

# ---------- APERTURA EN FRÍO ----------
S("tormenta", "Llueve sin parar desde hace días. El agua ya cubrió los árboles, las casas... y hasta las montañas. Solo una enorme barca de madera flota sobre el mundo entero.",
  [], [{"tipo": "arca", "x": 0.5, "escala": 1.1}], efectos=[{"tipo": "lluvia"}, {"tipo": "rayo", "inicio": 0.3}, {"tipo": "agua"}],
  camara="acercar_rapido", portada=True)
S("tormenta", "Adentro, un hombre de seiscientos años, su familia... y miles de animales. ¿Cómo llegaron ahí? Todo empezó con una orden de Dios que parecía una locura.",
  [P("noe", 0.5, accion="orar")], [{"tipo": "arca", "x": 0.5, "escala": 1.1, "profundidad": -100}], efectos=[{"tipo": "lluvia"}, {"tipo": "flash", "inicio": 0.85}], camara="acercar")

# ---------- 1. UN MUNDO PERDIDO ----------
S("ciudad", "Muchos años después de Adán y Eva, la tierra se había llenado de gente. Pero el corazón de las personas se llenó de maldad.",
  [P("enemigo1", 0.35, accion="empujar", emocion="enojado"), P("hombre2", 0.6, accion="caer", emocion="asustado")], [gente(0.75, 0.55)],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.3}], rotulo="CAPÍTULO 1: UN MUNDO PERDIDO", camara="paneo")
S("ciudad", "Había violencia en todas partes. Robaban, mentían, se lastimaban unos a otros... y nadie se acordaba de Dios.",
  [P("enemigo1", 0.4, accion="senalar", emocion="burlon"), P("enemigo2", 0.6, accion="lanzar", emocion="enojado")], efectos=[{"tipo": "fuego", "x": 0.85, "tamano": 0.8}], camara="acercar")
S("cielo", "La Biblia dice que a Dios le dolió en el corazón ver lo que la humanidad se había vuelto. Y decidió limpiar la tierra con un gran diluvio.",
  [], efectos=[{"tipo": "oscuridad", "fuerza": 0.35}, {"tipo": "rayo", "inicio": 0.6}], camara="alejar")
S("campo", "Pero había un hombre diferente. Se llamaba Noé. Era justo, honrado, y caminaba con Dios todos los días.",
  [P("noe", 0.5, accion="orar", emocion="feliz")], efectos=[{"tipo": "luz", "x": 0.5}], camara="acercar")
S("campo", "Noé era bisnieto de Enoc, aquel hombre tan cercano a Dios que un día Dios se lo llevó al cielo sin que muriera. Y su abuelo era Matusalén, el hombre que más años vivió en toda la Biblia: novecientos sesenta y nueve.",
  [P("noe", 0.4, emocion="feliz"), P("jacob", 0.65, mira="izquierda", barba="#e8e4dc", pelo="#e8e4dc", accion="abrazar")], camara="acercar")
S("campo", "Noé creció escuchando historias de un Dios que habla con los hombres. Y decidió que él también quería caminar con ese Dios, aunque nadie más lo hiciera.",
  [P("noe", 0.5, accion="caminar", hasta=0.6)], efectos=[{"tipo": "luz", "x": 0.6}], camara="paneo")
S("campo", "Y Noé halló gracia ante los ojos del Señor. En un mundo entero perdido... Dios encontró a uno fiel.",
  [P("noe", 0.5, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="fijo")

# ---------- 2. LA ORDEN ----------
S("campo", "Un día Dios le habló: Noé, voy a traer un diluvio de aguas sobre la tierra. Hazte un arca de madera.",
  [P("noe", 0.45, emocion="sorprendido")], efectos=[{"tipo": "luz", "x": 0.7}, {"tipo": "brillo", "x": 0.7, "y": -600}], rotulo="CAPÍTULO 2: LA ORDEN", camara="acercar")
S("campo", "Y le dio las medidas exactas: ciento cincuenta metros de largo, veinticinco de ancho y quince de alto. Con tres pisos, una ventana y una puerta.",
  [P("noe", 0.4, accion="senalar")], [{"tipo": "arca", "x": 0.7, "escala": 0.5}], efectos=[{"tipo": "brillo", "x": 0.7}], camara="acercar")
S("campo", "Era un barco más grande que un campo de fútbol. Y Noé vivía lejos del mar, en una tierra donde quizás nunca había visto llover así.",
  [P("noe", 0.5, emocion="sorprendido")], camara="alejar")
S("campo", "Y Dios le explicó por qué: Contigo estableceré mi pacto. Entrarás en el arca tú, tu esposa, tus hijos y las esposas de tus hijos. Y meterás animales de todas las especies, para que conserven la vida.",
  [P("noe", 0.45, accion="arrodillarse")], efectos=[{"tipo": "luz", "x": 0.7}, {"tipo": "brillo", "x": 0.7, "y": -600}], camara="acercar")
S("campo", "Imagina escuchar eso. Construir un barco gigante, sin herramientas modernas, sin máquinas, para una lluvia que nadie había visto jamás.",
  [P("noe", 0.5, emocion="sorprendido", accion="temblar")], camara="acercar_rapido")
S("cielo", "Algunos estudiosos creen que hasta ese momento la tierra se regaba con un vapor que subía del suelo. Si eso es cierto, Noé estaba preparándose para algo que nadie en la historia había visto: lluvia cayendo del cielo.",
  [P("noe", 0.5, emocion="sorprendido")], efectos=[{"tipo": "brillo", "y": -600}], camara="alejar")
S("campo", "Pero Noé no discutió, no puso excusas. La Biblia dice simplemente: Noé hizo todo lo que Dios le mandó.",
  [P("noe", 0.5, accion="levantar", emocion="valiente")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 3. CONSTRUYENDO ----------
S("campo", "Noé y sus tres hijos, Sem, Cam y Jafet, comenzaron a cortar árboles y a construir.",
  [P("noe", 0.25, accion="empujar"), P("hermano1", 0.45, accion="levantar"), P("hermano2", 0.62, accion="agacharse"), P("hombre2", 0.8, accion="empujar")],
  [{"tipo": "arbol", "x": 0.9}], rotulo="CAPÍTULO 3: LA BURLA", camara="paneo")
S("campo", "Día tras día, año tras año, golpe tras golpe. Muchos estudiosos creen que tardaron décadas en terminar el arca.",
  [P("noe", 0.4, accion="empujar"), P("hermano1", 0.6, accion="levantar")], [{"tipo": "arca", "x": 0.6, "escala": 0.8, "profundidad": -100}], camara="acercar")
S("campo", "Y la gente pasaba y se reía: ¡Miren al loco de Noé, construyendo un barco en medio de la tierra seca!",
  [P("enemigo1", 0.3, accion="senalar", emocion="burlon"), P("enemigo2", 0.48, emocion="burlon", accion="celebrar"), P("noe", 0.78, mira="izquierda", accion="empujar")],
  [{"tipo": "arca", "x": 0.75, "escala": 0.8, "profundidad": -100}], habla="enemigo1", camara="acercar_rapido")
S("campo", "Pasaban los años y el arca crecía. Noé cubrió la madera con brea por dentro y por fuera, para que no entrara ni una gota de agua. Y almacenó comida para su familia y para todos los animales.",
  [P("noe", 0.35, accion="agacharse"), P("hermano1", 0.55, accion="levantar")], [{"tipo": "arca", "x": 0.7, "escala": 0.9, "profundidad": -100}, {"tipo": "canasta", "x": 0.45}], camara="paneo")
S("campo", "Noé no solo construía. También les advertía: Viene un juicio. Arrepiéntanse y vuelvan a Dios. Pero nadie lo escuchó.",
  [P("noe", 0.4, accion="senalar", emocion="valiente"), P("enemigo1", 0.7, mira="izquierda", emocion="burlon")], habla="noe", camara="acercar")
S("cielo", "¿Alguna vez se burlaron de ti por tu fe? Escribe en los comentarios: Yo sigo construyendo. Porque lo que viene después lo cambia todo.",
  [P("noe", 0.5, accion="orar")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 4. LOS ANIMALES ----------
S("campo", "Cuando el arca estuvo lista, pasó algo que nadie esperaba. Desde todas las direcciones... empezaron a llegar animales.",
  [P("burro", 0.1, hasta=0.4, accion="caminar"), P("oveja1", 0.0, hasta=0.3, accion="caminar")], [{"tipo": "arca", "x": 0.7, "escala": 0.9, "profundidad": -100}],
  rotulo="CAPÍTULO 4: LOS ANIMALES", camara="paneo")
S("campo", "Llegaban de dos en dos, macho y hembra: leones, ovejas, burros, aves... Y de los animales limpios, siete parejas.",
  [P("leon1", 0.15, hasta=0.45, accion="caminar"), P("leon2", 0.05, hasta=0.32, accion="caminar"), P("oveja1", 0.55), P("oveja2", 0.62)],
  [{"tipo": "arca", "x": 0.82, "escala": 0.9, "profundidad": -100}], camara="acercar")
S("campo", "Nadie los arreaba. Era Dios mismo quien los traía. Y los que se burlaban miraban en silencio, sin entender lo que pasaba.",
  [P("enemigo1", 0.25, emocion="sorprendido"), P("gallo", 0.5, accion="caminar", hasta=0.6), P("carnero", 0.4, accion="caminar", hasta=0.55)],
  [{"tipo": "arca", "x": 0.8, "escala": 0.9, "profundidad": -100}], camara="paneo")
S("campo", "Entonces Dios le dijo a Noé: Entra en el arca, tú y toda tu familia. Dentro de siete días haré llover sobre la tierra.",
  [P("noe", 0.45, emocion="valiente"), P("mujer1", 0.6)], [{"tipo": "arca", "x": 0.7, "escala": 0.9, "profundidad": -100}], efectos=[{"tipo": "luz", "x": 0.7}], camara="acercar")
S("campo", "Ocho personas entraron: Noé, su esposa, sus tres hijos y sus esposas. Y la Biblia dice algo hermoso: Y el Señor cerró la puerta.",
  [P("noe", 0.4, accion="caminar", hasta=0.6), P("mujer1", 0.25, accion="caminar", hasta=0.45)], [{"tipo": "arca", "x": 0.7, "escala": 0.9, "profundidad": -100}],
  efectos=[{"tipo": "luz"}, {"tipo": "temblor", "inicio": 0.85, "fin": 0.95}], camara="acercar")

# ---------- 5. EL DILUVIO ----------
S("tormenta", "Siete días después, el cielo se oscureció. Se rompieron las fuentes del gran abismo, se abrieron las ventanas del cielo... y comenzó a llover.",
  [], [{"tipo": "arca", "x": 0.5, "escala": 0.9}], efectos=[{"tipo": "lluvia"}, {"tipo": "rayo", "inicio": 0.2}, {"tipo": "rayo", "inicio": 0.7}],
  rotulo="CAPÍTULO 5: EL DILUVIO", camara="acercar_rapido")
S("tormenta", "Los que se burlaban corrieron hacia el arca y golpearon la puerta. Pero la puerta ya estaba cerrada.",
  [P("enemigo1", 0.35, accion="correr", emocion="asustado", hasta=0.5), P("enemigo2", 0.2, accion="correr", emocion="asustado", hasta=0.35)],
  [{"tipo": "arca", "x": 0.75, "escala": 0.9, "profundidad": -100}], efectos=[{"tipo": "lluvia"}, {"tipo": "agua"}], camara="acercar")
S("mar_tormenta", "Llovió cuarenta días y cuarenta noches. El agua subió y subió, hasta cubrir las montañas más altas.",
  [], [{"tipo": "arca", "x": 0.5, "escala": 0.9}], efectos=[{"tipo": "lluvia"}, {"tipo": "rayo", "inicio": 0.5}], rotulo="40 DÍAS", camara="alejar")
S("mar_tormenta", "Afuera, toda la vida desapareció. Pero adentro del arca, Noé y su familia estaban a salvo, en la palma de la mano de Dios.",
  [P("noe", 0.4, accion="orar"), P("mujer1", 0.58, accion="orar")], efectos=[{"tipo": "lluvia"}, {"tipo": "luz", "x": 0.5}], camara="acercar")
S("mar_tormenta", "¿Cómo era la vida dentro del arca? Noé y su familia pasaban el día alimentando a los animales, limpiando, cuidando a los más pequeños... y orando juntos.",
  [P("noe", 0.3, accion="ofrecer"), P("oveja1", 0.5), P("mujer1", 0.7, accion="agacharse")], efectos=[{"tipo": "lluvia"}, {"tipo": "luz", "x": 0.4}], camara="acercar")
S("mar_tormenta", "Afuera se escuchaban los truenos y el golpe de las olas. Adentro, el rugido de los leones, el balido de las ovejas y el canto de los gallos.",
  [P("leon1", 0.3, accion="rugir"), P("gallo", 0.55, accion="saltar"), P("oveja2", 0.75)], efectos=[{"tipo": "rayo", "inicio": 0.4}, {"tipo": "temblor", "inicio": 0.4, "fin": 0.5}], camara="paneo")
S("mar", "Y entonces la lluvia se detuvo. Pero el agua tardó ciento cincuenta días en empezar a bajar. Cinco meses flotando, sin ver tierra.",
  [], [{"tipo": "arca", "x": 0.5, "escala": 0.9}], efectos=[{"tipo": "oscuridad", "fuerza": 0.15}], rotulo="150 DÍAS", camara="paneo")
S("cielo", "Dime en los comentarios: ¿cuál animal crees que fue el más difícil de cuidar dentro del arca? Yo creo que los leones.",
  [P("noe", 0.4, accion="senalar", emocion="feliz"), P("leon1", 0.68, mira="izquierda")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 6. LA PALOMA ----------
S("montana", "Hasta que un día, el arca chocó suavemente contra algo... ¡Se había detenido sobre los montes de Ararat!",
  [], [{"tipo": "arca", "x": 0.5, "escala": 0.8, "y": -250}], efectos=[{"tipo": "temblor", "inicio": 0.4, "fin": 0.55}], rotulo="CAPÍTULO 6: LA PALOMA", camara="acercar_rapido")
S("montana", "Noé abrió la ventana y soltó un cuervo, que iba y venía. Luego soltó una paloma... pero volvió, porque no encontró dónde posarse.",
  [P("noe", 0.45, accion="levantar")], efectos=[{"tipo": "brillo", "x": 0.6, "y": -600}], camara="acercar")
S("montana", "Siete días después la soltó otra vez. Y al atardecer, la paloma regresó... con una hoja verde de olivo en el pico.",
  [P("noe", 0.45, accion="celebrar", emocion="feliz")], efectos=[{"tipo": "brillo", "x": 0.55, "y": -500}, {"tipo": "luz"}], camara="acercar_rapido")
S("montana", "Imagina la alegría dentro del arca. Los hijos de Noé abrazándose, su esposa llorando de emoción, y Noé levantando esa hojita de olivo como el tesoro más grande del mundo.",
  [P("noe", 0.35, accion="levantar", emocion="feliz"), P("hermano1", 0.55, accion="celebrar", emocion="feliz"), P("mujer1", 0.72, accion="abrazar", emocion="llorando")], camara="acercar")
S("montana", "¡Había vida otra vez en la tierra! Y la tercera vez que la soltó, la paloma ya no volvió.",
  [P("noe", 0.4, accion="alabar", emocion="feliz"), P("mujer1", 0.6, accion="celebrar", emocion="feliz")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 7. EL ARCOÍRIS ----------
S("valle", "Después de más de un año dentro del arca, Dios dijo: Sal del arca. Y por fin, la puerta se abrió.",
  [P("noe", 0.3, accion="caminar", hasta=0.45, emocion="feliz"), P("mujer1", 0.15, accion="caminar", hasta=0.3)], [{"tipo": "arca", "x": 0.82, "escala": 0.8, "profundidad": -100}],
  rotulo="CAPÍTULO 7: LA PROMESA", camara="paneo")
S("valle", "Los animales salieron corriendo y volando en todas direcciones. La tierra estaba limpia, verde, nueva.",
  [P("leon1", 0.3, accion="correr", hasta=0.1), P("oveja1", 0.5, accion="saltar"), P("burro", 0.7, accion="correr", hasta=0.9), P("gallo", 0.6, accion="saltar")],
  efectos=[{"tipo": "luz"}], camara="alejar")
S("valle", "Lo primero que hizo Noé fue construir un altar y dar gracias a Dios.",
  [P("noe", 0.45, accion="arrodillarse")], [{"tipo": "altar", "x": 0.6}], efectos=[{"tipo": "fuego", "x": 0.6, "y": -120, "tamano": 0.6}, {"tipo": "luz"}], camara="acercar")
S("valle", "Y Dios hizo una promesa: Nunca más destruiré la tierra con un diluvio. Y como señal de esa promesa, puso su arco en las nubes.",
  [P("noe", 0.4, accion="alabar", emocion="sorprendido"), P("mujer1", 0.58, emocion="feliz")], efectos=[{"tipo": "arcoiris"}, {"tipo": "luz"}], camara="alejar")
S("valle", "Y Dios bendijo a Noé y a sus hijos: Sean fecundos, multiplíquense y llenen la tierra. De esas ocho personas que salieron del arca, volvió a llenarse el mundo entero.",
  [P("noe", 0.3, emocion="feliz", accion="abrazar"), P("hermano1", 0.48, emocion="feliz"), P("hermano2", 0.64, emocion="feliz"), P("mujer1", 0.8, emocion="feliz")],
  efectos=[{"tipo": "arcoiris"}], camara="paneo")
S("valle", "Por eso, cada vez que ves un arcoíris después de la lluvia, Dios te está recordando que él siempre cumple sus promesas.",
  [P("noe", 0.5, accion="senalar", emocion="feliz")], efectos=[{"tipo": "arcoiris"}, {"tipo": "brillo"}], camara="acercar")

# ---------- ENSEÑANZA Y FINAL ----------
S("cielo", "Noé obedeció cuando todos se burlaban, cuando no había ni una nube en el cielo, cuando nada tenía sentido.",
  [P("noe", 0.5, accion="orar")], efectos=[{"tipo": "luz"}], rotulo="ENSEÑANZA", camara="acercar")
S("cielo", "La fe no es ver la lluvia y luego construir. La fe es construir... antes de ver la primera gota.",
  [P("noe", 0.5, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "arcoiris"}], camara="fijo")
S("cielo", "¿Qué promesa de Dios estás esperando ver cumplida? Escríbela en los comentarios, y oremos juntos por ella.",
  [P("noe", 0.4, accion="senalar"), P("oveja1", 0.62)], efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "Suscríbete y activa la campanita, que mañana llega otra gran historia de la Biblia. ¡Dios te bendiga!",
  [P("noe", 0.5, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "arcoiris"}], rotulo="¡SUSCRÍBETE!", pausa=2.0, camara="acercar")

guardar("05_noe_la_historia_completa.json", "Noé y el Arca - La Historia Completa",
        "Todos se BURLABAN de él... hasta que empezó a LLOVER.",
        ["NOÉ", "ARCA", "DILUVIO", "LLUVIA", "ANIMALES", "PALOMA", "ARCOÍRIS", "PROMESA", "PUERTA"])
