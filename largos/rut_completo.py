"""Video largo: Rut, la historia completa."""
from base import S, P, gente, guardar

VIUDA = {"tunica": "#4a4a5a", "color_tocado": "#2a2a3a"}

# ---------- APERTURA EN FRÍO ----------
S("camino", "Lo perdió todo: su esposo, su casa y su país. Ahora camina por un camino polvoriento junto a una anciana viuda, sin dinero y sin nadie que las proteja.",
  [P("noemi", 0.4, accion="caminar", hasta=0.5, emocion="triste"), P("rut", 0.25, accion="caminar", hasta=0.35, emocion="triste")],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.2}], camara="acercar_rapido", portada=True)
S("camino", "Nadie habría apostado por ella. Pero una sola decisión la convirtió en la bisabuela del rey más famoso de Israel. Y todo empezó con hambre.",
  [P("rut", 0.5, emocion="valiente")], efectos=[{"tipo": "flash", "inicio": 0.85}], camara="acercar")

# ---------- 1. EL HAMBRE ----------
S("campo", "En los días en que los jueces gobernaban Israel, hubo un hambre terrible en la tierra. En Belén, que significa casa del pan, ya no había pan.",
  [P("hombre2", 0.4, accion="agacharse", emocion="triste")], [{"tipo": "canasta", "x": 0.6}], efectos=[{"tipo": "oscuridad", "fuerza": 0.2}], camara="paneo")
S("camino", "Un hombre llamado Elimelec tomó a su esposa Noemí y a sus dos hijos, Mahlón y Quelión, y se fueron a vivir a Moab, una tierra extranjera donde se adoraban otros dioses.",
  [P("hombre1", 0.35, accion="caminar", hasta=0.55), P("noemi", 0.22, accion="caminar", hasta=0.42, pelo=None), P("hermano1", 0.1, accion="caminar", hasta=0.3, escala=0.85)],
  camara="paneo")
S("campo", "Pensaban quedarse un tiempo. Pero se quedaron diez años. Allí murió Elimelec, y Noemí quedó viuda con sus dos hijos.",
  [P("noemi", 0.5, accion="arrodillarse", emocion="llorando", **VIUDA)], efectos=[{"tipo": "lluvia"}, {"tipo": "oscuridad", "fuerza": 0.3}], camara="acercar")
S("campo", "Sus hijos se casaron con dos muchachas moabitas: una se llamaba Orfa, y la otra se llamaba Rut. Por un tiempo, la casa volvió a tener alegría.",
  [P("hermano1", 0.25, emocion="feliz"), P("rut", 0.42, emocion="feliz"), P("hermano2", 0.6, emocion="feliz"), P("orfa", 0.77, emocion="feliz")], camara="paneo")
S("noche", "Pero entonces sucedió lo impensable. Los dos hijos de Noemí también murieron. Tres mujeres quedaron viudas, solas, en una tierra difícil.",
  [P("noemi", 0.3, **VIUDA, emocion="llorando", accion="arrodillarse"), P("rut", 0.5, **VIUDA, emocion="llorando"), P("orfa", 0.7, **VIUDA, emocion="llorando")],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.45}, {"tipo": "lluvia"}], camara="acercar")
S("cielo", "Si alguna vez perdiste a alguien que amabas, escribe en los comentarios: Dios sana mi corazón. Porque esta historia no termina en el dolor.",
  [P("rut", 0.5, accion="orar", **VIUDA)], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 2. LA DECISIÓN ----------
S("camino", "Un día Noemí escuchó que Dios había visitado a su pueblo y que en Belén volvía a haber pan. Y decidió regresar a casa.",
  [P("noemi", 0.45, **VIUDA, emocion="sorprendido")], efectos=[{"tipo": "luz", "x": 0.8}], rotulo="CAPÍTULO 1: LA DECISIÓN", camara="acercar")
S("camino", "Orfa y Rut salieron con ella. Pero en el camino, Noemí se detuvo y les dijo: Vuelvan a la casa de sus madres. Ustedes son jóvenes, pueden casarse otra vez. Yo ya no tengo nada que darles.",
  [P("noemi", 0.5, **VIUDA, accion="senalar", emocion="triste"), P("rut", 0.3, **VIUDA), P("orfa", 0.72, mira="izquierda", **VIUDA)], habla="noemi", camara="acercar")
S("camino", "Las tres lloraron abrazadas. Orfa besó a su suegra, se despidió... y regresó a Moab.",
  [P("orfa", 0.6, accion="abrazar", emocion="llorando", **VIUDA), P("noemi", 0.4, accion="abrazar", emocion="llorando", **VIUDA)], camara="acercar")
S("camino", "Pero Rut se quedó abrazada a Noemí y no la soltó. Mira, tu cuñada se ha vuelto a su pueblo y a sus dioses. Vete tú también con ella.",
  [P("rut", 0.4, accion="abrazar", emocion="llorando", **VIUDA), P("noemi", 0.58, mira="izquierda", emocion="triste", **VIUDA)], habla="noemi", camara="fijo")
S("camino", "Y entonces Rut dijo una de las frases más hermosas de toda la Biblia:",
  [P("rut", 0.5, emocion="valiente", **VIUDA)], efectos=[{"tipo": "luz", "x": 0.5}], camara="acercar_rapido")
S("cielo", "No me pidas que te deje. A donde tú vayas, iré yo. Donde tú vivas, viviré. Tu pueblo será mi pueblo, y tu Dios será mi Dios.",
  [P("rut", 0.5, accion="orar", emocion="llorando", **VIUDA)], habla="rut", efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="RUT 1:16", camara="acercar")
S("camino", "Rut lo estaba dejando todo: su tierra, su familia, sus costumbres, y cualquier esperanza de volver a casarse. Lo dejaba por amor a una anciana... y por el Dios de Israel.",
  [P("rut", 0.4, **VIUDA, accion="caminar", hasta=0.55), P("noemi", 0.25, **VIUDA, accion="caminar", hasta=0.4)], camara="paneo")
S("cielo", "Pausa. ¿Tú habrías hecho lo mismo que Rut, o lo que hizo Orfa? Respóndeme con sinceridad en los comentarios.",
  [P("rut", 0.4, **VIUDA), P("orfa", 0.62, mira="izquierda", **VIUDA)], efectos=[{"tipo": "luz"}], rotulo="¿RUT U ORFA?", camara="fijo")

# ---------- 3. BELÉN ----------
S("ciudad", "Cuando llegaron a Belén, toda la ciudad se conmovió. ¿No es esta Noemí?, decían las mujeres. Pero ella respondió: No me llamen Noemí, que significa agradable. Llámenme Mara, que significa amarga.",
  [P("noemi", 0.45, **VIUDA, emocion="llorando"), P("mujer1", 0.68, mira="izquierda", emocion="sorprendido")], [gente(0.8, 0.5)], habla="noemi",
  rotulo="CAPÍTULO 2: EL CAMPO DE BOOZ", camara="acercar")
S("ciudad", "Me fui llena, y el Señor me ha hecho volver vacía. Noemí estaba tan herida que no podía ver que a su lado caminaba una gran bendición: Rut.",
  [P("noemi", 0.4, **VIUDA, emocion="triste"), P("rut", 0.6, mira="izquierda", **VIUDA, emocion="triste")], camara="fijo")
S("trigal", "Llegaron justo al comienzo de la cosecha de la cebada. Y la ley de Dios decía que los pobres podían recoger las espigas que se les caían a los segadores.",
  [P("hombre1", 0.3, accion="agacharse"), P("hombre2", 0.55, accion="levantar")], camara="paneo")
S("trigal", "Rut le dijo a Noemí: Déjame ir al campo a recoger espigas, detrás de alguien que me trate con bondad. Y fue a trabajar bajo el sol, para que las dos pudieran comer.",
  [P("rut", 0.5, **VIUDA, accion="agacharse", emocion="valiente")], camara="acercar")
S("trigal", "No era un trabajo fácil. Había que caminar todo el día agachada bajo el sol, buscando espiga por espiga entre la paja. Y como era extranjera, muchos la miraban con desconfianza.",
  [P("rut", 0.45, **VIUDA, accion="agacharse", emocion="triste"), P("hombre2", 0.75, mira="izquierda", emocion="burlon")], camara="paneo")
S("trigal", "Y por casualidad, aunque en la Biblia nada es casualidad, llegó a un campo que pertenecía a un hombre llamado Booz, pariente de Elimelec.",
  [P("rut", 0.35, **VIUDA, accion="agacharse"), P("booz", 0.7, mira="izquierda", accion="caminar", hasta=0.62)], efectos=[{"tipo": "brillo", "x": 0.7}], camara="acercar")
S("trigal", "Booz era un hombre rico, respetado y temeroso de Dios. Cuando llegó, saludó a sus trabajadores: El Señor esté con ustedes. Y ellos respondieron: El Señor te bendiga.",
  [P("booz", 0.45, accion="levantar", emocion="feliz"), P("hombre1", 0.7, mira="izquierda", emocion="feliz")], habla="booz", camara="paneo")
S("trigal", "Entonces Booz vio a Rut y preguntó: ¿De quién es esa joven? Es la moabita que vino con Noemí, le dijeron. Ha trabajado desde la mañana sin descansar.",
  [P("booz", 0.6, mira="izquierda", emocion="sorprendido"), P("rut", 0.25, **VIUDA, accion="agacharse")], camara="acercar")

# ---------- 4. LA BONDAD DE BOOZ ----------
S("trigal", "Booz se acercó a Rut y le dijo: Hija mía, no vayas a otro campo. Quédate aquí con mis criadas. Ya ordené que nadie te moleste. Y cuando tengas sed, bebe del agua de mis trabajadores.",
  [P("booz", 0.55, mira="izquierda", accion="ofrecer", emocion="feliz"), P("rut", 0.35, **VIUDA, emocion="sorprendido")], habla="booz",
  rotulo="CAPÍTULO 3: UN HOMBRE BUENO", camara="acercar")
S("trigal", "Rut se inclinó hasta el suelo: ¿Por qué me tratas con tanta bondad, si soy una extranjera?",
  [P("rut", 0.4, **VIUDA, accion="arrodillarse", emocion="llorando"), P("booz", 0.62, mira="izquierda")], habla="rut", camara="acercar_rapido")
S("trigal", "Y Booz respondió: Me han contado todo lo que hiciste por tu suegra. Que el Señor, bajo cuyas alas has venido a refugiarte, te recompense.",
  [P("booz", 0.55, mira="izquierda", accion="senalar", emocion="feliz"), P("rut", 0.35, **VIUDA)], habla="booz", efectos=[{"tipo": "luz"}], camara="fijo")
S("trigal", "A la hora de comer, Booz la invitó a su mesa. Y en secreto les dijo a sus trabajadores: Dejen caer espigas a propósito, para que ella recoja más.",
  [P("booz", 0.4, accion="senalar", emocion="burlon"), P("hombre1", 0.65, mira="izquierda", accion="agacharse", emocion="feliz")], [{"tipo": "panes_peces", "x": 0.55}],
  camara="paneo")
S("noche", "Esa noche Rut llegó a casa con casi veinte kilos de cebada. Noemí no lo podía creer. ¿Dónde trabajaste hoy? En el campo de un hombre llamado Booz.",
  [P("rut", 0.4, **VIUDA, accion="ofrecer", emocion="feliz"), P("noemi", 0.62, mira="izquierda", **VIUDA, emocion="sorprendido")], [{"tipo": "canasta", "x": 0.5}],
  camara="acercar")
S("noche", "Rut le contó todo: cómo Booz la protegió, cómo le dio agua y comida, y cómo le pidió que se quedara en su campo hasta el final de la cosecha. Noemí escuchaba con los ojos muy abiertos.",
  [P("rut", 0.4, **VIUDA, accion="senalar", emocion="feliz"), P("noemi", 0.62, mira="izquierda", **VIUDA, emocion="sorprendido")], camara="fijo")
S("noche", "¡Booz! ¡Bendito sea el Señor! Ese hombre es nuestro pariente. Es uno de nuestros redentores. Por primera vez en años, Noemí volvió a sonreír.",
  [P("noemi", 0.5, **VIUDA, accion="celebrar", emocion="feliz")], habla="noemi", efectos=[{"tipo": "luz"}], camara="acercar_rapido")

# ---------- 5. EL REDENTOR ----------
S("cielo", "En Israel existía una ley especial: cuando un hombre moría sin hijos, un pariente cercano podía casarse con la viuda, recuperar sus tierras y darle descendencia. A ese pariente se le llamaba redentor.",
  [P("booz", 0.5, emocion="valiente")], efectos=[{"tipo": "luz"}], rotulo="CAPÍTULO 4: EL REDENTOR", camara="acercar")
S("trigal", "Durante semanas, Rut trabajó en el campo de Booz, primero en la cosecha de la cebada y después en la del trigo. Y cada noche volvía a casa con comida para ella y para Noemí.",
  [P("rut", 0.4, **VIUDA, accion="levantar", emocion="feliz")], [{"tipo": "canasta", "x": 0.55}], camara="paneo")
S("noche", "Al final de la cosecha, Noemí le dio a Rut un consejo. Rut se arregló, fue de noche al lugar donde Booz cuidaba el grano, y se acostó a sus pies.",
  [P("booz", 0.6, accion="dormir"), P("rut", 0.4, accion="agacharse", emocion="asustado")], efectos=[{"tipo": "oscuridad", "fuerza": 0.4}], camara="acercar")
S("noche", "A medianoche Booz despertó sobresaltado. ¿Quién eres? Soy Rut, tu sierva. Extiende tu manto sobre mí, porque tú eres mi redentor.",
  [P("booz", 0.6, mira="izquierda", emocion="sorprendido"), P("rut", 0.38, accion="arrodillarse")], habla="rut", efectos=[{"tipo": "oscuridad", "fuerza": 0.35}],
  camara="acercar_rapido")
S("noche", "Booz respondió con ternura: Bendita seas, hija mía. No has buscado a los jóvenes, ni ricos ni pobres. Todo mi pueblo sabe que eres una mujer virtuosa.",
  [P("booz", 0.55, mira="izquierda", accion="ofrecer", emocion="feliz"), P("rut", 0.38, emocion="feliz")], habla="booz", efectos=[{"tipo": "luz", "x": 0.5}], camara="fijo")
S("noche", "Pero hay un problema: existe otro pariente más cercano que yo. Él tiene el primer derecho. Mañana resolveré este asunto, te lo prometo.",
  [P("booz", 0.5, emocion="triste")], habla="booz", efectos=[{"tipo": "oscuridad", "fuerza": 0.3}], camara="acercar")

# ---------- 6. LA PUERTA DE LA CIUDAD ----------
S("noche", "Antes del amanecer, Booz le llenó el manto con seis medidas de cebada. No vuelvas a tu suegra con las manos vacías, le dijo. Y Noemí, al verlo, sonrió: Ese hombre no descansará hasta resolverlo hoy mismo.",
  [P("booz", 0.6, mira="izquierda", accion="ofrecer"), P("rut", 0.38, emocion="feliz")], [{"tipo": "canasta", "x": 0.48}], efectos=[{"tipo": "oscuridad", "fuerza": 0.25}], camara="acercar")
S("ciudad", "A la mañana siguiente, Booz se sentó a la puerta de la ciudad, donde se hacían los tratos. Cuando pasó el otro pariente, lo llamó delante de diez ancianos como testigos.",
  [P("booz", 0.35), P("hombre2", 0.6, mira="izquierda"), P("jacob", 0.82, mira="izquierda", barba="#e8e4dc", pelo="#e8e4dc")], [gente(0.7, 0.5)],
  rotulo="CAPÍTULO 5: EL TRATO", camara="paneo")
S("ciudad", "Noemí vende el terreno de Elimelec. ¿Quieres comprarlo? Sí, lo compro, dijo el hombre. Pero hay algo más: el que compre el terreno, también debe casarse con Rut la moabita.",
  [P("booz", 0.4, accion="senalar"), P("hombre2", 0.62, mira="izquierda", emocion="sorprendido")], habla="booz", camara="acercar")
S("ciudad", "Entonces no puedo, respondió el pariente. Arruinaría mi propia herencia. Cómpralo tú. Y se quitó la sandalia y se la dio a Booz, que era la forma de cerrar un trato en Israel.",
  [P("hombre2", 0.55, mira="izquierda", accion="ofrecer", emocion="triste"), P("booz", 0.35, emocion="feliz")], habla="hombre2", camara="acercar_rapido")
S("ciudad", "Y Booz declaró ante todo el pueblo: Hoy ustedes son testigos de que tomo a Rut la moabita como mi esposa. Y todos respondieron: ¡Somos testigos! ¡Que el Señor la bendiga!",
  [P("booz", 0.5, accion="levantar", emocion="feliz")], [gente(0.5, 0.55, y=320, delante=True, profundidad=None)], habla="booz", efectos=[{"tipo": "luz"}], camara="alejar")

# ---------- 7. LA RECOMPENSA ----------
S("valle", "Booz y Rut se casaron. Y Dios les dio un hijo. La extranjera viuda y sin esperanza ahora tenía un esposo que la amaba, un hogar y un hijo.",
  [P("rut", 0.4, accion="abrazar", emocion="feliz"), P("booz", 0.6, mira="izquierda", accion="abrazar", emocion="feliz")], [{"tipo": "pesebre", "x": 0.5, "escala": 0.7}],
  efectos=[{"tipo": "luz"}, {"tipo": "arcoiris"}], rotulo="CAPÍTULO 6: LA RECOMPENSA", camara="acercar")
S("valle", "Las mujeres de Belén le dijeron a Noemí: Bendito sea el Señor, que no te dejó sin redentor. Tu nuera, que te ama, vale más para ti que siete hijos.",
  [P("noemi", 0.45, accion="abrazar", emocion="llorando"), P("mujer1", 0.68, mira="izquierda", emocion="feliz")], habla="mujer1", camara="paneo")
S("valle", "Y Noemí tomó al niño en sus brazos y lo cuidó como a su propio hijo. La mujer que se llamó a sí misma amarga, volvió a ser feliz.",
  [P("noemi", 0.5, accion="abrazar", emocion="feliz")], [{"tipo": "pesebre", "x": 0.62, "escala": 0.6}], efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "Al niño lo llamaron Obed. Obed fue el padre de Isaí. E Isaí fue el padre de... David, el pastorcito que venció a Goliat y llegó a ser el gran rey de Israel.",
  [P("david", 0.5, accion="alabar", emocion="feliz", tocado="corona")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="acercar_rapido")
S("cielo", "Y de la familia de David, mil años después, nacería en Belén el Hijo de Dios: Jesús. Rut, la extranjera que todo lo dejó, aparece con su nombre en la genealogía de Jesús.",
  [P("jesus", 0.5, accion="ofrecer", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="fijo")

# ---------- ENSEÑANZA Y FINAL ----------
S("cielo", "Booz es una imagen de Jesús: nuestro Redentor. Él pagó el precio para rescatarnos, nos dio un hogar y una familia, aunque éramos extranjeros sin esperanza.",
  [P("booz", 0.4, emocion="feliz"), P("jesus", 0.62, mira="izquierda", emocion="feliz")], efectos=[{"tipo": "luz"}], rotulo="ENSEÑANZA", camara="acercar")
S("cielo", "Rut nos enseña que la lealtad y la bondad nunca pasan desapercibidas para Dios. Una decisión de amor puede cambiar la historia de muchas generaciones.",
  [P("rut", 0.5, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="fijo")
S("cielo", "¿Quién ha sido una Rut en tu vida, alguien que se quedó contigo en el peor momento? Etiquétalo o escribe su nombre en los comentarios.",
  [P("rut", 0.4, accion="abrazar"), P("noemi", 0.6, mira="izquierda", accion="abrazar", emocion="feliz")], efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "Suscríbete y activa la campanita, que mañana llega otra gran historia de la Biblia. ¡Dios te bendiga!",
  [P("rut", 0.5, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="¡SUSCRÍBETE!", pausa=2.0, camara="acercar")

guardar("09_rut_la_historia_completa.json", "Rut - Una Historia de Amor y Lealtad",
        "Lo perdió TODO... y terminó en la familia de un REY.",
        ["RUT", "NOEMÍ", "BOOZ", "BELÉN", "REDENTOR", "DAVID", "JESÚS", "LEALTAD"],
        personajes={"orfa": {"tunica": "#b85a6a", "tocado": "velo", "color_tocado": "#8a3a4a", "pelo": None}},
        miniatura={"texto": ["LO PERDIÓ", "TODO..."], "sello": "Y DIOS LA RESTAURÓ",
                   "escena": {"fondo": "trigal", "personajes": [
                       {"id": "rut", "x": 0.62, "accion": "agacharse", "emocion": "llorando", "escala": 1.3},
                       {"id": "booz", "x": 0.85, "mira": "izquierda", "accion": "ofrecer", "emocion": "feliz", "escala": 1.3}],
                       "efectos": [{"tipo": "luz", "x": 0.7}, {"tipo": "brillo", "x": 0.7}]}})
