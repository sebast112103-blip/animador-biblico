"""Video largo: Daniel en el foso de los leones, la historia completa."""
from base import S, P, gente, guardar

JOVEN = {"tunica": "#3f6fb5", "manto": "#d9c7a3"}
SABIO = {"tunica": "#f4f1ea", "manto": "#7a5c8a", "tocado": "turbante", "color_tocado": "#7a5c8a"}
VIEJO = {"barba": "#e8e4dc", "pelo": "#e8e4dc"}

# ---------- APERTURA EN FRÍO ----------
S("foso", "Una piedra enorme sella la entrada. Adentro, en la oscuridad, hay leones hambrientos que no han comido en días. Y un anciano acaba de ser arrojado ahí dentro.",
  [P("daniel", 0.5, **SABIO, **VIEJO, accion="orar"), P("leon1", 0.22, accion="rugir"), P("leon2", 0.8, mira="izquierda", accion="rugir")],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.45}, {"tipo": "temblor", "inicio": 0.7, "fin": 0.8}], camara="acercar_rapido", portada=True)
S("foso", "¿Su delito? Orar a Dios. ¿Qué pasó esa noche en el foso? Para entenderlo, tenemos que ir setenta años atrás.",
  [P("daniel", 0.5, **SABIO, **VIEJO, accion="orar")], efectos=[{"tipo": "oscuridad", "fuerza": 0.4}, {"tipo": "flash", "inicio": 0.85}], camara="acercar")

# ---------- 1. LLEVADO A BABILONIA ----------
S("ciudad", "Jerusalén había caído. El poderoso rey Nabucodonosor de Babilonia conquistó la ciudad y se llevó a los mejores jóvenes de Israel.",
  [P("soldado1", 0.3, objeto="lanza"), P("daniel", 0.55, **JOVEN, emocion="triste", accion="caminar", hasta=0.65)], [gente(0.75, 0.55, variante="soldados")],
  efectos=[{"tipo": "fuego", "x": 0.15, "tamano": 1.0}], rotulo="CAPÍTULO 1: CAUTIVOS", camara="paneo")
S("palacio", "Entre ellos estaba Daniel, un adolescente, junto con sus tres amigos: Sadrac, Mesac y Abed-nego. Lejos de su casa y de su familia.",
  [P("daniel", 0.3, **JOVEN, emocion="triste"), P("hermano1", 0.48, emocion="triste"), P("hermano2", 0.64, emocion="triste"), P("hombre2", 0.8, emocion="triste")],
  camara="acercar")
S("palacio", "El rey quería convertirlos en sabios de Babilonia. Les cambiaron el nombre, les enseñaron otra lengua... y les ofrecieron comida de la mesa del rey.",
  [P("enemigo1", 0.65, mira="izquierda", accion="ofrecer", emocion="feliz"), P("daniel", 0.35, **JOVEN)], [{"tipo": "mesa", "x": 0.5}, {"tipo": "panes_peces", "x": 0.5, "y": -40}],
  camara="fijo")
S("palacio", "Pero esa comida había sido ofrecida a los ídolos. Y Daniel decidió en su corazón no contaminarse, aunque eso le costara caro.",
  [P("daniel", 0.4, **JOVEN, accion="orar", emocion="valiente")], efectos=[{"tipo": "luz", "x": 0.4}], camara="acercar")
S("palacio", "Pruébanos diez días, pidió Daniel. Danos solo verduras y agua, y después compáranos con los demás.",
  [P("daniel", 0.35, **JOVEN, accion="ofrecer"), P("enemigo1", 0.68, mira="izquierda", emocion="sorprendido")], habla="daniel", camara="acercar")
S("palacio", "Y a los diez días, Daniel y sus amigos se veían más sanos y fuertes que todos los demás. Dios les dio sabiduría diez veces mayor que la de todos los magos del reino.",
  [P("daniel", 0.3, **JOVEN, emocion="feliz", accion="celebrar"), P("hermano1", 0.5, emocion="feliz"), P("hermano2", 0.68, emocion="feliz")],
  efectos=[{"tipo": "luz"}, {"tipo": "brillo"}], rotulo="10 DÍAS", camara="acercar")

# ---------- 2. EL SUEÑO DEL REY ----------
S("palacio", "Una noche, el rey Nabucodonosor tuvo un sueño que lo dejó aterrado. Pero al despertar... no lo podía recordar.",
  [P("rey_dario", 0.5, accion="temblar", emocion="asustado", manto="#8a2a2a")], [{"tipo": "trono", "x": 0.55, "profundidad": -30}],
  efectos=[{"tipo": "rayo", "inicio": 0.3}], rotulo="CAPÍTULO 2: EL SUEÑO OLVIDADO", camara="acercar_rapido")
S("palacio", "Llamó a todos sus magos y les exigió algo imposible: Díganme qué soñé, y lo que significa. Si no, todos morirán.",
  [P("rey_dario", 0.65, mira="izquierda", accion="senalar", emocion="enojado", manto="#8a2a2a"), P("enemigo1", 0.3, accion="temblar", emocion="asustado")],
  habla="rey_dario", camara="acercar")
S("palacio", "Nadie en la tierra puede hacer eso, respondieron los magos temblando. Y el rey, furioso, ordenó matar a todos los sabios de Babilonia... incluyendo a Daniel.",
  [P("enemigo1", 0.3, accion="arrodillarse", emocion="asustado"), P("soldado1", 0.7, mira="izquierda", objeto="espada", emocion="enojado")],
  efectos=[{"tipo": "temblor", "inicio": 0.6, "fin": 0.75}], camara="paneo")
S("noche", "Daniel reunió a sus amigos y oraron toda la noche. Y Dios le reveló el misterio en una visión.",
  [P("daniel", 0.4, **JOVEN, accion="orar"), P("hermano1", 0.6, accion="orar")], efectos=[{"tipo": "luz", "x": 0.4}, {"tipo": "brillo", "y": -600}], camara="acercar")
S("palacio", "Ante el rey, Daniel dijo: Ningún sabio puede revelar esto. Pero hay un Dios en los cielos que revela los misterios.",
  [P("daniel", 0.35, **JOVEN, accion="senalar", emocion="valiente"), P("rey_dario", 0.7, mira="izquierda", manto="#8a2a2a", emocion="sorprendido")],
  habla="daniel", efectos=[{"tipo": "luz", "x": 0.35}], camara="acercar")
S("cielo", "Soñaste con una estatua gigante: cabeza de oro, pecho de plata, vientre de bronce y pies de hierro mezclado con barro. Y una piedra la hizo pedazos.",
  [], [{"tipo": "columna", "x": 0.5}], efectos=[{"tipo": "brillo"}, {"tipo": "temblor", "inicio": 0.75, "fin": 0.9}], camara="alejar")
S("palacio", "El rey cayó de rodillas: ¡Verdaderamente tu Dios es Dios de dioses! Y nombró a Daniel jefe de todos los sabios de Babilonia.",
  [P("rey_dario", 0.6, mira="izquierda", accion="arrodillarse", manto="#8a2a2a", emocion="sorprendido"), P("daniel", 0.35, **SABIO, emocion="feliz")],
  efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "Si crees que Dios puede revelar lo que nadie más entiende, escribe en los comentarios: Dios tiene la respuesta.",
  [P("daniel", 0.5, **SABIO, accion="orar")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 3. EL HORNO DE FUEGO ----------
S("valle", "Pero el orgullo del rey creció. Mandó construir una estatua de oro de casi treinta metros, y ordenó que todos se arrodillaran ante ella.",
  [], [{"tipo": "columna", "x": 0.5, "escala": 1.2}, gente(0.5, 0.6, y=250, profundidad=100)], rotulo="CAPÍTULO 3: EL HORNO DE FUEGO", camara="alejar")
S("valle", "Cuando sonó la música, todo el pueblo se inclinó... excepto tres jóvenes. Los amigos de Daniel permanecieron de pie.",
  [P("hermano1", 0.35, emocion="valiente"), P("hermano2", 0.5, emocion="valiente"), P("hombre2", 0.65, emocion="valiente")], [gente(0.5, 0.55, y=320, delante=True, profundidad=None)],
  camara="acercar_rapido")
S("palacio", "El rey, rojo de ira, les dio una última oportunidad: Si no se arrodillan, serán echados en un horno de fuego ardiendo. ¿Y qué dios los librará de mi mano?",
  [P("rey_dario", 0.6, mira="izquierda", accion="senalar", manto="#8a2a2a", emocion="enojado")], habla="rey_dario", camara="acercar")
S("palacio", "Ellos respondieron: Nuestro Dios puede librarnos. Y si no lo hace... de todas maneras no adoraremos tu estatua.",
  [P("hermano1", 0.3, emocion="valiente", accion="senalar"), P("hermano2", 0.46, emocion="valiente"), P("hombre2", 0.62, emocion="valiente")],
  habla="hermano1", efectos=[{"tipo": "luz"}], camara="fijo")
S("noche", "Furioso, el rey ordenó calentar el horno siete veces más de lo normal. El fuego era tan intenso que mató a los soldados que los arrojaron.",
  [P("soldado1", 0.25, accion="caer", emocion="asustado")], efectos=[{"tipo": "fuego", "x": 0.6, "tamano": 2.2, "crece": True}, {"tipo": "temblor", "inicio": 0.3, "fin": 0.9}],
  camara="acercar_rapido")
S("noche", "Pero entonces el rey miró dentro del horno y se levantó de un salto: ¿No echamos a tres hombres? ¡Yo veo cuatro, caminando en medio del fuego! Y el cuarto parece un hijo de los dioses.",
  [P("hermano1", 0.4, accion="caminar", hasta=0.45), P("hermano2", 0.55), P("hombre2", 0.7), P("angel", 0.85)],
  efectos=[{"tipo": "fuego", "x": 0.6, "tamano": 2.4}, {"tipo": "luz", "x": 0.85}, {"tipo": "brillo", "x": 0.85}], camara="acercar")
S("valle", "Salieron del horno sin una sola quemadura. Ni siquiera olían a humo. Y el rey tuvo que reconocer que no hay otro Dios que pueda salvar así.",
  [P("hermano1", 0.3, accion="celebrar", emocion="feliz"), P("hermano2", 0.48, accion="alabar", emocion="feliz"), P("hombre2", 0.66, accion="celebrar", emocion="feliz")],
  efectos=[{"tipo": "luz"}], camara="paneo")

S("palacio", "Aun así, Nabucodonosor volvió a llenarse de orgullo. Paseando por su palacio dijo: ¿No es esta la gran Babilonia que yo construí con mi poder y para mi gloria?",
  [P("rey_dario", 0.5, accion="levantar", manto="#8a2a2a", emocion="burlon")], habla="rey_dario", camara="paneo")
S("campo", "Y en ese mismo instante perdió la razón. Durante siete años vivió en el campo como un animal, comiendo hierba como los bueyes, con el pelo largo como plumas de águila.",
  [P("rey_dario", 0.5, accion="agacharse", manto="#8a2a2a", emocion="noqueado", pelo_largo=True), P("burro", 0.75, mira="izquierda")],
  efectos=[{"tipo": "lluvia"}], rotulo="7 AÑOS", camara="acercar")
S("cielo", "Hasta que un día levantó los ojos al cielo, y Dios le devolvió la razón y su reino. Y el rey más poderoso del mundo escribió: Ahora yo alabo al Rey del cielo, porque él puede humillar a los soberbios.",
  [P("rey_dario", 0.5, accion="alabar", manto="#8a2a2a", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="acercar")

# ---------- 4. LA ESCRITURA EN LA PARED ----------
S("palacio", "Pasaron los años y los reyes. Ahora gobernaba Belsasar, que hizo una gran fiesta y usó las copas sagradas del templo de Dios para emborracharse.",
  [P("enemigo2", 0.5, accion="celebrar", emocion="burlon", tocado="corona")], [{"tipo": "mesa", "x": 0.5}, {"tipo": "monedas", "x": 0.4, "y": -40}],
  rotulo="CAPÍTULO 4: LA MANO MISTERIOSA", camara="paneo")
S("palacio", "De repente, apareció una mano... y empezó a escribir en la pared del palacio. El rey se puso pálido y le temblaban las rodillas.",
  [P("enemigo2", 0.4, accion="temblar", emocion="asustado", tocado="corona")], efectos=[{"tipo": "brillo", "x": 0.7, "y": -600}, {"tipo": "oscuridad", "fuerza": 0.35}],
  camara="acercar_rapido")
S("palacio", "Llamaron a Daniel, ya anciano. Y él leyó: Mene, Mene, Tekel, Uparsin. Dios ha contado tu reino y le ha puesto fin. Fuiste pesado en la balanza... y fuiste hallado falto.",
  [P("daniel", 0.35, **SABIO, **VIEJO, accion="senalar", emocion="valiente"), P("enemigo2", 0.7, mira="izquierda", tocado="corona", emocion="asustado")],
  habla="daniel", camara="acercar")
S("noche", "Esa misma noche, los ejércitos de los medos y los persas entraron en Babilonia. Y el imperio cayó.",
  [], [gente(0.5, 0.65, variante="soldados", y=-120)], efectos=[{"tipo": "fuego", "x": 0.3, "tamano": 1.2}, {"tipo": "temblor", "inicio": 0.2, "fin": 0.8}], camara="paneo")

# ---------- 5. LA TRAMPA ----------
S("palacio", "El nuevo rey, Darío, puso a Daniel como uno de los tres hombres más importantes del reino. Y pensaba ponerlo sobre todos.",
  [P("rey_dario", 0.65, mira="izquierda", emocion="feliz"), P("daniel", 0.35, **SABIO, **VIEJO, emocion="feliz")], [{"tipo": "trono", "x": 0.72, "profundidad": -30}],
  rotulo="CAPÍTULO 5: LA TRAMPA", camara="acercar")
S("palacio", "Pero los otros gobernadores le tenían envidia. Buscaron algún error en Daniel... y no encontraron nada. Era un hombre fiel y honesto.",
  [P("enemigo1", 0.4, emocion="enojado"), P("enemigo2", 0.6, emocion="burlon")], camara="acercar")
S("palacio", "Entonces dijeron: Solo podremos acusarlo por algo relacionado con su Dios. Y prepararon una trampa.",
  [P("enemigo1", 0.4, accion="senalar", emocion="burlon"), P("enemigo2", 0.6, mira="izquierda", emocion="burlon")], habla="enemigo1", efectos=[{"tipo": "oscuridad", "fuerza": 0.3}], camara="acercar_rapido")
S("palacio", "Convencieron al rey de firmar una ley: durante treinta días, nadie podía orar a ningún dios ni hombre, solo al rey. Y quien desobedeciera, sería echado al foso de los leones.",
  [P("enemigo1", 0.3, accion="ofrecer"), P("rey_dario", 0.65, mira="izquierda", emocion="feliz")], [{"tipo": "trono", "x": 0.7, "profundidad": -30}], camara="fijo")
S("noche", "Daniel supo de la ley. Y aun así, fue a su casa, abrió las ventanas hacia Jerusalén, y se arrodilló a orar tres veces al día, como siempre lo había hecho.",
  [P("daniel", 0.45, **SABIO, **VIEJO, accion="arrodillarse")], efectos=[{"tipo": "luz", "x": 0.45}], camara="acercar")
S("noche", "Sus enemigos lo estaban espiando. ¡Lo atrapamos!",
  [P("enemigo1", 0.75, mira="izquierda", accion="senalar", emocion="burlon"), P("daniel", 0.3, **SABIO, **VIEJO, accion="orar")], habla="enemigo1", camara="acercar_rapido")
S("palacio", "El rey Darío se dio cuenta de que lo habían engañado. Trató hasta el atardecer de salvar a Daniel. Pero la ley de los medos y persas no se podía cambiar.",
  [P("rey_dario", 0.5, accion="temblar", emocion="triste")], efectos=[{"tipo": "oscuridad", "fuerza": 0.25}], camara="acercar")
S("cielo", "Antes de ver qué pasó en el foso, dime en los comentarios: ¿tú habrías cerrado la ventana para orar a escondidas?",
  [P("daniel", 0.5, **SABIO, **VIEJO, accion="orar")], efectos=[{"tipo": "luz"}], rotulo="¿Y TÚ?", camara="fijo")

# ---------- 6. EL FOSO ----------
S("foso", "Arrojaron a Daniel al foso. Y antes de sellar la piedra, el rey le dijo: El Dios a quien tú sirves siempre... él te libre.",
  [P("daniel", 0.5, **SABIO, **VIEJO, accion="caer"), P("leon1", 0.2, accion="rugir"), P("leon2", 0.82, mira="izquierda", accion="rugir")],
  habla="rey_dario", efectos=[{"tipo": "oscuridad", "fuerza": 0.45}, {"tipo": "temblor", "inicio": 0.5, "fin": 0.65}], rotulo="CAPÍTULO 6: EL FOSO", camara="acercar_rapido")
S("palacio", "Esa noche, el rey no comió. No quiso música. Y no pudo dormir.",
  [P("rey_dario", 0.5, accion="temblar", emocion="triste")], efectos=[{"tipo": "oscuridad", "fuerza": 0.5}], camara="acercar")
S("foso", "Mientras tanto, en el foso, los leones se acercaron a Daniel... rugiendo...",
  [P("daniel", 0.5, **SABIO, **VIEJO, accion="orar"), P("leon1", 0.3, accion="caminar", hasta=0.36), P("leon2", 0.72, mira="izquierda", accion="caminar", hasta=0.66)],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.5}], camara="acercar_rapido")
S("foso", "...pero de pronto, una luz llenó la cueva. Dios envió a su ángel, y cerró la boca de los leones.",
  [P("angel", 0.5), P("daniel", 0.32, **SABIO, **VIEJO, accion="orar"), P("leon1", 0.15, accion="dormir"), P("leon2", 0.82, accion="dormir")],
  efectos=[{"tipo": "luz", "x": 0.5}, {"tipo": "brillo", "x": 0.5}, {"tipo": "flash", "inicio": 0.1}], camara="acercar")
S("foso", "Los leones se echaron a su lado como gatitos. Y Daniel pasó la noche entera... sin un solo rasguño.",
  [P("daniel", 0.5, **SABIO, **VIEJO, accion="dormir"), P("leon1", 0.3, accion="dormir"), P("leon2", 0.7, accion="dormir")], efectos=[{"tipo": "luz"}], camara="alejar")
S("foso", "Al amanecer, el rey corrió al foso y gritó con angustia: ¡Daniel! ¿Tu Dios ha podido librarte de los leones?",
  [P("rey_dario", 0.5, accion="correr", hasta=0.55, emocion="asustado")], habla="rey_dario", camara="acercar_rapido")
S("foso", "Y desde adentro se oyó una voz: ¡Oh rey, vive para siempre! Mi Dios envió a su ángel y cerró la boca de los leones.",
  [P("daniel", 0.5, **SABIO, **VIEJO, accion="alabar", emocion="feliz"), P("leon1", 0.25, accion="dormir")], habla="daniel", efectos=[{"tipo": "luz"}], camara="acercar")
S("palacio", "El rey se llenó de alegría y mandó sacar a Daniel. Y los que habían preparado la trampa... recibieron el castigo que querían para él.",
  [P("rey_dario", 0.6, mira="izquierda", accion="abrazar", emocion="feliz"), P("daniel", 0.35, **SABIO, **VIEJO, accion="abrazar", emocion="feliz")], camara="paneo")
S("palacio", "Y Darío escribió a todas las naciones: Que todos teman al Dios de Daniel, porque él es el Dios viviente, que salva y hace maravillas.",
  [P("rey_dario", 0.5, accion="levantar", emocion="feliz")], [gente(0.5, 0.55, y=320, delante=True, profundidad=None)], efectos=[{"tipo": "luz"}, {"tipo": "brillo"}], camara="acercar")

# ---------- ENSEÑANZA Y FINAL ----------
S("cielo", "Daniel no oró para salir del foso. Oró antes de entrar. Su fe no dependía de lo que pasara, sino de quién era su Dios.",
  [P("daniel", 0.5, **SABIO, **VIEJO, accion="orar")], efectos=[{"tipo": "luz"}], rotulo="ENSEÑANZA", camara="acercar")
S("cielo", "A veces Dios no te saca del foso... te acompaña dentro de él, y cierra la boca de los leones.",
  [P("daniel", 0.5, **SABIO, **VIEJO, accion="alabar", emocion="feliz"), P("leon1", 0.75, accion="dormir")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="fijo")
S("cielo", "¿Qué momento te impactó más: el horno de fuego, la mano en la pared o el foso? Escríbelo en los comentarios.",
  [P("daniel", 0.4, **SABIO, **VIEJO, accion="senalar"), P("leon1", 0.65, mira="izquierda")], efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "Suscríbete y activa la campanita, que mañana viene otra gran historia de la Biblia. ¡Dios te bendiga!",
  [P("daniel", 0.5, **SABIO, **VIEJO, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}],
  rotulo="¡SUSCRÍBETE!", pausa=2.0, camara="acercar")

guardar("04_daniel_la_historia_completa.json", "Daniel - El Foso de los Leones",
        "Lo arrojaron a los LEONES por orar a DIOS... esto fue lo que pasó.",
        ["DANIEL", "LEONES", "FOSO", "REY", "BABILONIA", "HORNO", "FUEGO", "ÁNGEL", "ORAR", "DARÍO"])
