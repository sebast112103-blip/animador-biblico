"""Video largo: La Navidad, parte 1 - El anuncio."""
from base import S, P, gente, guardar

VIEJO = {"barba": "#e8e4dc", "pelo": "#e8e4dc"}

# ---------- APERTURA EN FRÍO ----------
S("noche", "Una joven de Nazaret está sola en su casa. Tiene unos quince años. Y de repente, la habitación se llena de luz... y un ángel le dice: ¡Alégrate, muy favorecida! El Señor está contigo.",
  [P("maria", 0.4, emocion="asustado", accion="temblar"), P("angel", 0.72, mira="izquierda", accion="ofrecer")],
  efectos=[{"tipo": "luz", "x": 0.72}, {"tipo": "brillo", "x": 0.72}, {"tipo": "flash", "inicio": 0.1}], camara="acercar_rapido", portada=True)
S("noche", "Lo que ese ángel estaba por anunciarle cambiaría la historia del mundo para siempre. Esta es la primera parte de la verdadera historia de la Navidad.",
  [P("maria", 0.5, emocion="sorprendido")], efectos=[{"tipo": "luz"}, {"tipo": "flash", "inicio": 0.85}], rotulo="LA NAVIDAD · PARTE 1", camara="acercar")

# ---------- 1. EL SILENCIO ----------
S("cielo", "Durante cuatrocientos años, Dios no envió ningún profeta a su pueblo. Cuatrocientos años de silencio. El último mensaje del Antiguo Testamento había sido una promesa: Dios enviaría un mensajero para preparar el camino.",
  [], efectos=[{"tipo": "oscuridad", "fuerza": 0.35}], rotulo="CAPÍTULO 1: 400 AÑOS DE SILENCIO", camara="alejar")
S("ciudad", "Israel ya no era un reino libre. Ahora lo gobernaba el poderoso Imperio Romano, y en Judea reinaba Herodes, un rey cruel y desconfiado.",
  [P("soldado1", 0.35, objeto="lanza", casco=True), P("soldado2", 0.6, objeto="lanza", casco=True)], [gente(0.8, 0.5, variante="soldados")], camara="paneo")
S("ciudad", "El pueblo esperaba al Mesías, el Salvador prometido. Muchos creían que vendría como un rey guerrero para expulsar a los romanos. Nadie imaginaba cómo iba a llegar en realidad.",
  [P("hombre1", 0.4, accion="orar"), P("mujer1", 0.6, accion="orar")], efectos=[{"tipo": "luz", "x": 0.5}], camara="acercar")

# ---------- 2. ZACARÍAS ----------
S("templo", "En esos días vivía un sacerdote llamado Zacarías, con su esposa Elisabet. Los dos eran justos delante de Dios. Pero tenían una tristeza: no tenían hijos, y ya eran ancianos.",
  [P("zacarias", 0.4, emocion="triste"), P("elisabet", 0.6, mira="izquierda", emocion="triste")], rotulo="CAPÍTULO 2: EL SACERDOTE", camara="acercar")
S("templo", "Había miles de sacerdotes en Israel, y se sorteaba quién entraría al templo a ofrecer el incienso. Muchos nunca tenían esa oportunidad en toda su vida. Y ese día, la suerte cayó sobre Zacarías.",
  [P("zacarias", 0.5, accion="caminar", hasta=0.6, emocion="feliz")], [gente(0.2, 0.5)], camara="paneo")
S("templo", "Mientras afuera el pueblo oraba, Zacarías entró solo al lugar santo. Y junto al altar del incienso... estaba un ángel.",
  [P("zacarias", 0.35, accion="temblar", emocion="asustado"), P("angel", 0.7, mira="izquierda")], [{"tipo": "altar", "x": 0.55}],
  efectos=[{"tipo": "fuego", "x": 0.55, "y": -120, "tamano": 0.4}, {"tipo": "luz", "x": 0.7}, {"tipo": "brillo", "x": 0.7}], camara="acercar_rapido")
S("templo", "No temas, Zacarías, porque tu oración ha sido escuchada. Tu esposa Elisabet te dará un hijo, y le pondrás por nombre Juan. Irá delante del Señor para preparar a su pueblo.",
  [P("angel", 0.65, mira="izquierda", accion="senalar"), P("zacarias", 0.35, emocion="sorprendido")], habla="angel", camara="acercar")
S("templo", "Pero Zacarías dudó: ¿Cómo sabré que esto es cierto? Yo soy viejo, y mi esposa también.",
  [P("zacarias", 0.4, accion="ofrecer", emocion="sorprendido")], habla="zacarias", camara="fijo")
S("templo", "Y el ángel le respondió: Yo soy Gabriel, que estoy delante de Dios. Fui enviado para darte esta buena noticia. Pero como no creíste mis palabras, quedarás mudo hasta el día en que esto suceda.",
  [P("angel", 0.6, mira="izquierda", accion="levantar", emocion="valiente"), P("zacarias", 0.35, accion="temblar", emocion="asustado")], habla="angel",
  efectos=[{"tipo": "temblor", "inicio": 0.75, "fin": 0.9}], camara="acercar_rapido")
S("templo", "Afuera, el pueblo se preguntaba por qué tardaba tanto. Cuando por fin salió, Zacarías no podía hablar. Solo hacía señas. Y todos entendieron que había visto una visión.",
  [P("zacarias", 0.4, accion="senalar", emocion="sorprendido")], [gente(0.75, 0.55)], camara="paneo")
S("campo", "Y poco tiempo después, tal como Dios dijo, la anciana Elisabet quedó embarazada. Ella decía con alegría: El Señor me ha quitado mi vergüenza.",
  [P("elisabet", 0.45, accion="alabar", emocion="feliz"), P("zacarias", 0.65, mira="izquierda", emocion="feliz")], efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "Zacarías oró por un hijo durante años... y quizás ya había dejado de pedirlo. Pero Dios no se había olvidado. Si sigues esperando una respuesta, escribe: Dios escucha mi oración.",
  [P("zacarias", 0.5, accion="orar")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 3. MARÍA ----------
S("ciudad", "Seis meses después, Dios envió al mismo ángel Gabriel a un pueblito pequeño y sin importancia de Galilea: Nazaret.",
  [P("angel", 0.5)], [gente(0.8, 0.4)], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="CAPÍTULO 3: LA JOVEN DE NAZARET", camara="alejar")
S("ciudad", "Nazaret era tan pequeño que ni siquiera aparece mencionado en el Antiguo Testamento. Tenía unas pocas casas de piedra y gente humilde que trabajaba la tierra. Algunos decían: ¿De Nazaret puede salir algo bueno?",
  [P("hombre2", 0.35, accion="agacharse"), P("mujer1", 0.6, accion="levantar")], camara="paneo")
S("ciudad", "Allí vivía una joven llamada María, comprometida para casarse con un carpintero llamado José, que era descendiente del rey David.",
  [P("maria", 0.4, emocion="feliz"), P("jose_carpintero", 0.62, mira="izquierda", emocion="feliz")], camara="acercar")
S("campo", "José trabajaba con sus manos la madera y la piedra. María, como las jóvenes de su tiempo, ayudaba en casa y esperaba el día de su boda. Eran personas sencillas. Nadie se fijaba en ellos.",
  [P("jose_carpintero", 0.38, accion="empujar"), P("maria", 0.65, accion="levantar", emocion="feliz")], [{"tipo": "piedra", "x": 0.25, "escala": 0.5}], camara="fijo")
S("noche", "El ángel entró donde estaba María y le dijo: ¡Alégrate, muy favorecida! El Señor está contigo. Y María se turbó mucho, preguntándose qué significaba ese saludo.",
  [P("maria", 0.4, emocion="asustado"), P("angel", 0.7, mira="izquierda", accion="ofrecer")], habla="angel", efectos=[{"tipo": "luz", "x": 0.7}], camara="acercar")
S("noche", "No temas, María, porque has hallado gracia delante de Dios. Concebirás y darás a luz un hijo, y le pondrás por nombre Jesús.",
  [P("angel", 0.65, mira="izquierda", accion="senalar"), P("maria", 0.38, emocion="sorprendido")], habla="angel", efectos=[{"tipo": "luz"}, {"tipo": "brillo"}], camara="acercar_rapido")
S("cielo", "Él será grande, y será llamado Hijo del Altísimo. Dios le dará el trono de David su padre, y su reino no tendrá fin.",
  [], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], habla="angel", camara="alejar")
S("noche", "María preguntó: ¿Cómo será esto, si nunca he estado con un hombre? Y el ángel respondió: El Espíritu Santo vendrá sobre ti, y el poder del Altísimo te cubrirá con su sombra. Por eso el niño será llamado Hijo de Dios.",
  [P("maria", 0.4, accion="ofrecer", emocion="sorprendido"), P("angel", 0.68, mira="izquierda", accion="levantar")], habla="angel", camara="fijo")
S("noche", "Y le dio una señal: Tu parienta Elisabet, la que llamaban estéril, ya está en su sexto mes. Porque para Dios no hay nada imposible.",
  [P("angel", 0.6, mira="izquierda", accion="senalar", emocion="feliz")], habla="angel", efectos=[{"tipo": "luz"}], camara="acercar")
S("noche", "Piensa en lo que esto significaba para María. Una joven embarazada antes de casarse podía ser rechazada, avergonzada... e incluso apedreada. Decir que sí podía costarle todo.",
  [P("maria", 0.5, emocion="triste", accion="temblar")], efectos=[{"tipo": "oscuridad", "fuerza": 0.3}], camara="acercar")
S("cielo", "Y aun así, María respondió: Aquí está la sierva del Señor. Hágase conmigo conforme a tu palabra.",
  [P("maria", 0.5, accion="arrodillarse", emocion="valiente")], habla="maria", efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="LUCAS 1:38", camara="acercar_rapido")
S("cielo", "Pausa. ¿Qué crees que habrías respondido tú en el lugar de María? Escríbelo con sinceridad en los comentarios.",
  [P("maria", 0.5, accion="orar")], efectos=[{"tipo": "luz"}], rotulo="¿Y TÚ?", camara="fijo")

# ---------- 4. LA VISITA ----------
S("camino", "María se levantó y fue de prisa a las montañas de Judea, a visitar a Elisabet. Fue un viaje de varios días.",
  [P("maria", 0.25, accion="caminar", hasta=0.6, emocion="feliz")], rotulo="CAPÍTULO 4: EL ENCUENTRO", camara="paneo")
S("campo", "Cuando entró en la casa y saludó a Elisabet, el bebé que Elisabet llevaba en su vientre saltó de alegría. Y Elisabet, llena del Espíritu Santo, exclamó:",
  [P("maria", 0.4, accion="abrazar", emocion="feliz"), P("elisabet", 0.6, mira="izquierda", accion="abrazar", emocion="sorprendido")], efectos=[{"tipo": "luz"}, {"tipo": "brillo"}],
  camara="acercar_rapido")
S("campo", "¡Bendita tú entre las mujeres, y bendito el fruto de tu vientre! ¿Y quién soy yo para que la madre de mi Señor venga a visitarme? Dichosa tú, que creíste.",
  [P("elisabet", 0.55, mira="izquierda", accion="alabar", emocion="feliz"), P("maria", 0.35, emocion="feliz")], habla="elisabet", camara="acercar")
S("cielo", "Y María cantó una canción de alabanza que hoy se conoce como el Magníficat: Mi alma engrandece al Señor, y mi espíritu se alegra en Dios mi Salvador, porque miró la humildad de su sierva.",
  [P("maria", 0.5, accion="alabar", emocion="feliz")], habla="maria", efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="fijo")
S("cielo", "Derribó a los poderosos de sus tronos, y exaltó a los humildes. A los hambrientos llenó de bienes, y a los ricos los despidió vacíos.",
  [P("maria", 0.5, accion="levantar", emocion="feliz")], habla="maria", efectos=[{"tipo": "luz"}], camara="acercar")
S("campo", "María se quedó con Elisabet unos tres meses. Dos mujeres, una muy joven y otra anciana, esperando juntas dos milagros.",
  [P("maria", 0.4, emocion="feliz"), P("elisabet", 0.6, mira="izquierda", emocion="feliz")], rotulo="3 MESES", camara="paneo")

# ---------- 5. JUAN ----------
S("campo", "Cuando llegó el tiempo, Elisabet dio a luz un hijo. Los vecinos y parientes celebraron con ella. Y al octavo día querían llamarlo Zacarías, como su padre.",
  [P("elisabet", 0.4, accion="abrazar", emocion="feliz"), P("mujer1", 0.62, mira="izquierda", accion="celebrar", emocion="feliz")], [{"tipo": "pesebre", "x": 0.5, "escala": 0.6}],
  rotulo="CAPÍTULO 5: SU NOMBRE ES JUAN", camara="acercar")
S("campo", "Pero Elisabet dijo: No. Se llamará Juan. ¿Juan? Nadie en tu familia se llama así. Y le preguntaron por señas a Zacarías.",
  [P("elisabet", 0.38, accion="senalar"), P("hombre1", 0.62, mira="izquierda", emocion="sorprendido")], habla="elisabet", camara="fijo")
S("campo", "Zacarías pidió una tablilla y escribió: Su nombre es Juan. Y en ese mismo instante, su boca se abrió... ¡y volvió a hablar! Lo primero que hizo fue alabar a Dios.",
  [P("zacarias", 0.5, accion="alabar", emocion="feliz")], habla="zacarias", efectos=[{"tipo": "luz"}, {"tipo": "brillo"}, {"tipo": "flash", "inicio": 0.4}], camara="acercar_rapido")
S("cielo", "Y Zacarías, lleno del Espíritu Santo, profetizó: Bendito el Señor Dios de Israel, que ha visitado y redimido a su pueblo. Y tú, niño, serás llamado profeta del Altísimo, porque irás delante del Señor para preparar sus caminos.",
  [P("zacarias", 0.5, accion="levantar", emocion="feliz")], habla="zacarias", efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="acercar")
S("campo", "Todos los vecinos se llenaron de asombro y se preguntaban: ¿Qué llegará a ser este niño? Ese niño crecería y sería Juan el Bautista, el que prepararía el camino para Jesús.",
  [P("hombre1", 0.35, emocion="sorprendido"), P("mujer1", 0.55, emocion="sorprendido"), P("zacarias", 0.78, mira="izquierda", emocion="feliz")], camara="paneo")

S("desierto", "El niño Juan crecía y se fortalecía en espíritu. Y años más tarde vivió en el desierto, vestido con pelo de camello, comiendo langostas y miel silvestre, hasta el día en que comenzó a predicar.",
  [P("discipulo1", 0.5, tunica="#8a6a3a", pelo_largo=True, emocion="valiente")], efectos=[{"tipo": "luz"}], camara="alejar")

# ---------- 6. JOSÉ ----------
S("noche", "Mientras tanto, María regresó a Nazaret. Y José descubrió que estaba embarazada. Imagina lo que sintió: confusión, tristeza... traición.",
  [P("jose_carpintero", 0.5, emocion="triste", accion="temblar")], efectos=[{"tipo": "oscuridad", "fuerza": 0.35}], rotulo="CAPÍTULO 6: EL SUEÑO DE JOSÉ", camara="acercar")
S("noche", "Había soñado con formar un hogar con ella. Había preparado la casa, ahorrado, trabajado duro. Y ahora todo parecía derrumbarse. Por la ley, José tenía derecho a denunciarla públicamente.",
  [P("jose_carpintero", 0.5, accion="agacharse", emocion="llorando")], efectos=[{"tipo": "oscuridad", "fuerza": 0.35}], camara="acercar")
S("noche", "José era un hombre justo y no quería avergonzarla en público. Así que decidió terminar el compromiso en secreto.",
  [P("jose_carpintero", 0.5, accion="orar", emocion="triste")], efectos=[{"tipo": "oscuridad", "fuerza": 0.35}], camara="fijo")
S("noche", "Pero esa noche, mientras dormía, un ángel se le apareció en sueños: José, hijo de David, no temas recibir a María como tu esposa. Lo que hay en ella es obra del Espíritu Santo.",
  [P("jose_carpintero", 0.4, accion="dormir"), P("angel", 0.68, mira="izquierda", accion="ofrecer")], habla="angel", efectos=[{"tipo": "luz", "x": 0.68}, {"tipo": "brillo", "x": 0.68}],
  camara="acercar")
S("noche", "Dará a luz un hijo, y le pondrás por nombre Jesús, porque él salvará a su pueblo de sus pecados.",
  [P("angel", 0.55, accion="senalar")], habla="angel", efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="acercar_rapido")
S("campo", "Cuando José despertó, hizo exactamente lo que el ángel le dijo. Recibió a María como su esposa, y decidió cuidar y proteger a ese niño como si fuera suyo.",
  [P("jose_carpintero", 0.4, accion="abrazar", emocion="feliz"), P("maria", 0.6, mira="izquierda", accion="abrazar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "arcoiris"}], camara="acercar")
S("cielo", "Y así se cumplía lo que el profeta Isaías había escrito setecientos años antes: La virgen concebirá y dará a luz un hijo, y lo llamarán Emanuel, que significa Dios con nosotros.",
  [], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="EMANUEL", camara="alejar")

# ---------- FINAL CON ADELANTO ----------
S("cielo", "Zacarías dudó, María creyó, José obedeció. Tres personas sencillas que dijeron sí a Dios, y prepararon el camino para la noche más importante de la historia.",
  [P("zacarias", 0.3), P("maria", 0.5, emocion="feliz"), P("jose_carpintero", 0.7, emocion="feliz")], efectos=[{"tipo": "luz"}], rotulo="ENSEÑANZA", camara="paneo")
S("noche", "Pero todavía faltaba un viaje largo, una orden del emperador, una ciudad sin lugar... y un pesebre. Eso lo verás en la Parte 2 de la Navidad.",
  [P("maria", 0.4, accion="caminar", hasta=0.55), P("jose_carpintero", 0.25, accion="caminar", hasta=0.4), P("burro", 0.1, accion="caminar", hasta=0.25)],
  [{"tipo": "estrella", "x": 0.75, "y": -700}], efectos=[{"tipo": "brillo", "x": 0.75, "y": -700}], rotulo="PRÓXIMAMENTE: PARTE 2", camara="paneo")
S("cielo", "Suscríbete y activa la campanita para no perderte la Parte 2. Y escribe en los comentarios: ¡Emanuel, Dios con nosotros! ¡Dios te bendiga!",
  [P("maria", 0.5, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="¡SUSCRÍBETE!", pausa=2.0, camara="acercar")

guardar("14_navidad_parte1_el_anuncio.json", "La Navidad - Parte 1 - El Anuncio",
        "Un ángel visitó a una joven de NAZARET... y todo cambió.",
        ["MARÍA", "JOSÉ", "GABRIEL", "ÁNGEL", "JESÚS", "ELISABET", "ZACARÍAS", "JUAN", "EMANUEL", "NAVIDAD"],
        personajes={"zacarias": {"tunica": "#f4f1ea", "manto": "#3f5a8a", "tocado": "turbante", "color_tocado": "#e9e4d8", "barba": "#e8e4dc", "pelo": "#e8e4dc"},
                    "elisabet": {"tunica": "#8a6a8a", "tocado": "velo", "color_tocado": "#5a4a6a", "pelo": None, "voz": {"nombre": "es_AR-daniela-high", "tono": -3}}},
        miniatura={"texto": ["EL ÁNGEL", "LE DIJO..."], "sello": "NAVIDAD · PARTE 1",
                   "escena": {"fondo": "noche", "personajes": [
                       {"id": "maria", "x": 0.6, "emocion": "sorprendido", "escala": 1.3},
                       {"id": "angel", "x": 0.85, "mira": "izquierda", "accion": "ofrecer", "escala": 1.35}],
                       "efectos": [{"tipo": "luz", "x": 0.85}, {"tipo": "brillo", "x": 0.85}]}})
