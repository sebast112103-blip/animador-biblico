"""Video largo: José, la historia completa (de esclavo a gobernador)."""
from base import S, P, gente, guardar

TUNICA = {"tunica": "#3f6fb5", "manto": "#d9a62e", "cinturon": "#c0392b"}      # túnica de colores
ESCLAVO = {"tunica": "#b8a888", "manto": None}
GOBERNADOR = {"tunica": "#f4f1ea", "manto": "#d9a62e", "tocado": "turbante", "color_tocado": "#d9a62e"}

# ---------- APERTURA EN FRÍO (lo más impactante primero) ----------
S("egipto", "Once hombres arrodillados ante el gobernador más poderoso de Egipto. No saben que ese hombre... es el hermano que ellos vendieron como esclavo.",
  [P("hermano1", 0.25, accion="arrodillarse", emocion="asustado"), P("hermano2", 0.42, accion="arrodillarse", emocion="asustado"),
   P("jose", 0.75, mira="izquierda", **GOBERNADOR, emocion="valiente")], [gente(0.35, 0.55, y=-140)],
  efectos=[{"tipo": "temblor", "inicio": 0.7, "fin": 0.8}], camara="acercar_rapido", portada=True)
S("egipto", "¿Se vengará de ellos... o hará algo que nadie se imagina? Para entenderlo, tenemos que volver veinte años atrás.",
  [P("jose", 0.5, **GOBERNADOR, emocion="triste")], efectos=[{"tipo": "flash", "inicio": 0.85}], camara="acercar")

# ---------- 1. EL HIJO FAVORITO ----------
S("campo", "José tenía diecisiete años y era el hijo favorito de su padre Jacob. Jacob lo amaba tanto, que le regaló una túnica de muchos colores.",
  [P("jose", 0.38, **TUNICA, emocion="feliz", accion="celebrar"), P("jacob", 0.65, mira="izquierda", accion="ofrecer", emocion="feliz")],
  rotulo="CAPÍTULO 1: EL HIJO FAVORITO", camara="acercar")
S("campo", "Pero sus diez hermanos mayores, al ver esa túnica, sentían celos. Tanto, que ya no podían ni hablarle con cariño.",
  [P("jose", 0.25, **TUNICA), P("hermano1", 0.6, mira="izquierda", emocion="enojado"), P("hermano2", 0.78, mira="izquierda", emocion="enojado")],
  camara="paneo")
S("noche", "Una noche, José tuvo un sueño muy extraño. Soñó que estaba en el campo atando manojos de trigo con sus hermanos...",
  [P("jose", 0.5, **TUNICA, accion="dormir")], efectos=[{"tipo": "brillo", "y": -500}], camara="acercar")
S("trigal", "Y de repente, su manojo se levantaba, y los manojos de sus hermanos se inclinaban ante el suyo.",
  [P("jose", 0.5, **TUNICA, emocion="sorprendido")], efectos=[{"tipo": "luz", "x": 0.5}], camara="acercar_rapido")
S("campo", "José, muy emocionado, les contó el sueño a sus hermanos. ¿Acaso piensas reinar sobre nosotros?, le dijeron furiosos.",
  [P("jose", 0.3, **TUNICA, accion="senalar", emocion="feliz"), P("hermano1", 0.65, mira="izquierda", emocion="enojado", accion="senalar")],
  habla="hermano1", camara="fijo")
S("noche", "Luego tuvo otro sueño: el sol, la luna y once estrellas se inclinaban ante él. Y desde ese día, sus hermanos lo odiaron todavía más.",
  [P("jose", 0.5, **TUNICA, emocion="sorprendido")], [{"tipo": "estrella", "x": 0.3, "y": -700}, {"tipo": "estrella", "x": 0.7, "y": -650}],
  efectos=[{"tipo": "brillo", "y": -600}], camara="acercar")
S("campo", "Lo que José no sabía es que esos sueños eran un mensaje de Dios. Pero antes de cumplirse, José iba a pasar por lo peor.",
  [P("jose", 0.5, **TUNICA)], efectos=[{"tipo": "oscuridad", "fuerza": 0.3}], camara="acercar")

# ---------- 2. VENDIDO ----------
S("valle", "Un día, Jacob envió a José a buscar a sus hermanos, que cuidaban las ovejas lejos de casa.",
  [P("jose", 0.1, hasta=0.55, **TUNICA, accion="caminar", emocion="feliz"), P("oveja1", 0.8)],
  rotulo="CAPÍTULO 2: TRAICIONADO", camara="paneo")
S("valle", "Cuando lo vieron venir de lejos, dijeron: ¡Ahí viene el soñador! Vamos a matarlo, y veremos qué pasa con sus sueños.",
  [P("hermano1", 0.4, emocion="burlon", accion="senalar"), P("hermano2", 0.6, emocion="enojado")], habla="hermano1", camara="acercar_rapido")
S("desierto", "Le quitaron la túnica de colores y lo arrojaron a un pozo vacío, en medio del desierto.",
  [P("jose", 0.5, **ESCLAVO, accion="caer", emocion="llorando"), P("hermano1", 0.75, mira="izquierda", emocion="burlon")],
  efectos=[{"tipo": "temblor", "inicio": 0.4, "fin": 0.55}], camara="acercar")
S("desierto", "José gritaba y suplicaba desde el fondo del pozo. Pero sus hermanos se sentaron tranquilamente a comer.",
  [P("hermano1", 0.4, accion="agacharse", emocion="burlon"), P("hermano2", 0.62, accion="agacharse")],
  [{"tipo": "panes_peces", "x": 0.5}], camara="fijo")
S("desierto", "Entonces pasó una caravana de comerciantes rumbo a Egipto. Y uno de los hermanos tuvo una idea terrible.",
  [P("hombre1", 0.1, hasta=0.35, accion="caminar"), P("burro", 0.0, hasta=0.2, accion="caminar"), P("hermano1", 0.75, mira="izquierda", emocion="burlon")],
  camara="paneo")
S("desierto", "Vendieron a su propio hermano por veinte monedas de plata.",
  [P("jose", 0.38, **ESCLAVO, emocion="llorando", accion="temblar"), P("hermano1", 0.72, mira="izquierda", accion="ofrecer", emocion="burlon")],
  [{"tipo": "monedas", "x": 0.6, "escala": 0.8}], efectos=[{"tipo": "flash", "inicio": 0.6}], camara="acercar_rapido")
S("campo", "Luego mancharon la túnica con sangre de un cabrito y se la llevaron a su padre. Jacob creyó que una fiera había matado a José, y lloró por muchos días.",
  [P("jacob", 0.5, accion="arrodillarse", emocion="llorando")], efectos=[{"tipo": "lluvia"}, {"tipo": "oscuridad", "fuerza": 0.3}], camara="acercar")
S("cielo", "Si alguna vez alguien cercano te traicionó, escribe en los comentarios: Dios ve mi dolor. Porque esta historia apenas comienza.",
  [P("jose", 0.5, **ESCLAVO, accion="orar", emocion="triste")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 3. ESCLAVO EN EGIPTO ----------
S("egipto", "En Egipto, José fue vendido otra vez, ahora a Potifar, el capitán de la guardia del faraón.",
  [P("jose", 0.35, **ESCLAVO, emocion="triste"), P("guardia1", 0.68, mira="izquierda", objeto="lanza", emocion="valiente")],
  rotulo="CAPÍTULO 3: ESCLAVO EN EGIPTO", camara="acercar")
S("egipto", "Pero José no se rindió. Trabajó con honestidad, y Dios lo bendecía en todo lo que hacía.",
  [P("jose", 0.45, **ESCLAVO, accion="empujar", emocion="valiente")], [{"tipo": "piedra", "x": 0.6, "escala": 0.6}],
  efectos=[{"tipo": "luz", "x": 0.45}], camara="paneo")
S("palacio", "Tanto, que Potifar lo puso a cargo de toda su casa y de todo lo que tenía.",
  [P("jose", 0.4, tunica="#e9e4d8", manto="#7a5c8a", emocion="feliz"), P("guardia1", 0.68, mira="izquierda", emocion="feliz")], camara="acercar")
S("palacio", "Pero la esposa de Potifar acusó falsamente a José de algo que él nunca hizo. Y Potifar, lleno de furia, le creyó a ella.",
  [P("criada", 0.3, accion="senalar", emocion="enojado"), P("jose", 0.55, tunica="#e9e4d8", emocion="asustado"),
   P("guardia1", 0.8, mira="izquierda", emocion="enojado")], efectos=[{"tipo": "temblor", "inicio": 0.6, "fin": 0.75}], camara="acercar_rapido")
S("prision", "Sin juicio y sin defensa, José fue encerrado en la cárcel del rey. Había hecho lo correcto... y aun así lo perdió todo otra vez.",
  [P("jose", 0.45, **ESCLAVO, accion="arrodillarse", emocion="llorando")], efectos=[{"tipo": "oscuridad", "fuerza": 0.35}], camara="acercar")
S("prision", "¿Por qué Dios permitía todo esto? José no lo entendía. Pero aun en la cárcel, Dios seguía con él.",
  [P("jose", 0.45, **ESCLAVO, accion="orar")], efectos=[{"tipo": "luz", "x": 0.6}], camara="fijo")

# ---------- 4. LOS SUEÑOS EN LA CÁRCEL ----------
S("prision", "En la prisión, el jefe de la cárcel confió en José y lo puso a cargo de los demás presos.",
  [P("jose", 0.4, **ESCLAVO, emocion="valiente", accion="senalar"), P("hombre1", 0.65, mira="izquierda"), P("hombre2", 0.82, mira="izquierda")],
  rotulo="CAPÍTULO 4: LOS SUEÑOS", camara="paneo")
S("prision", "Un día llegaron dos presos muy importantes: el copero y el panadero del faraón. Y una mañana, los dos amanecieron muy tristes.",
  [P("hombre1", 0.35, emocion="triste"), P("hombre2", 0.6, emocion="triste"), P("jose", 0.82, mira="izquierda", **ESCLAVO)], camara="acercar")
S("prision", "Tuvimos un sueño, y no hay nadie que nos diga qué significa, le dijeron. Y José respondió: Las interpretaciones pertenecen a Dios. Cuéntenmelos.",
  [P("hombre1", 0.35, emocion="triste"), P("jose", 0.65, mira="izquierda", **ESCLAVO, accion="senalar", emocion="valiente")], habla="jose", camara="fijo")
S("prision", "Al copero le dijo: En tres días el faraón te devolverá tu puesto. Pero al panadero le dio una noticia muy triste.",
  [P("hombre1", 0.35, accion="celebrar", emocion="feliz"), P("hombre2", 0.6, accion="temblar", emocion="asustado")], camara="acercar")
S("prision", "Y todo pasó exactamente como José dijo. Antes de que el copero saliera, José le pidió: Acuérdate de mí cuando estés con el faraón.",
  [P("jose", 0.4, **ESCLAVO, accion="ofrecer", emocion="triste"), P("hombre1", 0.65, mira="izquierda", emocion="feliz")], habla="jose", camara="acercar")
S("prision", "Pero el copero... se olvidó de él. Y José pasó dos años más en la cárcel.",
  [P("jose", 0.5, **ESCLAVO, accion="dormir")], efectos=[{"tipo": "oscuridad", "fuerza": 0.45}], rotulo="2 AÑOS DESPUÉS", camara="alejar")

# ---------- 5. ANTE EL FARAÓN ----------
S("palacio", "Hasta que una noche, el mismísimo faraón tuvo dos sueños que lo dejaron temblando.",
  [P("faraon", 0.5, accion="temblar", emocion="asustado")], [{"tipo": "trono", "x": 0.55, "profundidad": -30}],
  rotulo="CAPÍTULO 5: EL SUEÑO DEL FARAÓN", efectos=[{"tipo": "rayo", "inicio": 0.3}], camara="acercar_rapido")
S("campo", "Soñó que del río salían siete vacas gordas y hermosas. Y detrás, siete vacas flacas y feas... que se comían a las gordas.",
  [P("burro", 0.3), P("oveja1", 0.5), P("oveja2", 0.7)], efectos=[{"tipo": "oscuridad", "fuerza": 0.25}], camara="paneo")
S("trigal", "Luego soñó con siete espigas llenas de trigo, que eran tragadas por siete espigas secas y quemadas por el viento.",
  [], efectos=[{"tipo": "fuego", "x": 0.6, "tamano": 0.8}, {"tipo": "oscuridad", "fuerza": 0.2}], camara="acercar")
S("palacio", "Ninguno de los sabios de Egipto pudo explicarlo. Y en ese momento, el copero se acordó de José.",
  [P("faraon", 0.65, mira="izquierda", emocion="enojado"), P("hombre1", 0.35, accion="senalar", emocion="sorprendido")], habla="hombre1", camara="acercar")
S("palacio", "Sacaron a José de la cárcel, lo afeitaron, le dieron ropa nueva y lo llevaron ante el hombre más poderoso del mundo.",
  [P("jose", 0.1, hasta=0.35, tunica="#e9e4d8", accion="caminar", emocion="asustado"), P("faraon", 0.72, mira="izquierda")],
  [{"tipo": "trono", "x": 0.78, "profundidad": -30}], camara="paneo")
S("palacio", "Me dicen que tú sabes interpretar sueños, le dijo el faraón. Y José respondió: No soy yo. Es Dios quien te dará la respuesta.",
  [P("jose", 0.35, tunica="#e9e4d8", accion="senalar", emocion="valiente"), P("faraon", 0.72, mira="izquierda", emocion="sorprendido")],
  habla="jose", efectos=[{"tipo": "luz", "x": 0.35}], camara="acercar")
S("palacio", "Los dos sueños son uno solo: vendrán siete años de mucha abundancia, y después siete años de un hambre terrible.",
  [P("jose", 0.4, tunica="#e9e4d8", accion="levantar", emocion="valiente")], efectos=[{"tipo": "brillo"}], habla="jose", camara="acercar_rapido")
S("palacio", "Guarda la quinta parte de cada cosecha durante los años buenos, y así Egipto no morirá de hambre.",
  [P("jose", 0.35, tunica="#e9e4d8", accion="ofrecer"), P("faraon", 0.7, mira="izquierda", emocion="feliz")], habla="jose", camara="fijo")
S("palacio", "El faraón quedó impresionado. ¿Dónde vamos a encontrar a alguien como este, que tiene el espíritu de Dios?",
  [P("faraon", 0.5, accion="senalar", emocion="feliz")], [{"tipo": "trono", "x": 0.55, "profundidad": -30}], habla="faraon", camara="acercar")
S("egipto", "Y ese mismo día, el esclavo que había pasado años en la cárcel se convirtió en el gobernador de todo Egipto. Solo el faraón estaba por encima de él.",
  [P("jose", 0.4, **GOBERNADOR, accion="alabar", emocion="feliz"), P("faraon", 0.72, mira="izquierda", emocion="feliz")],
  [gente(0.5, 0.6, y=-150, variante="egipcios")], efectos=[{"tipo": "luz"}, {"tipo": "brillo"}], camara="acercar")
S("cielo", "José tenía treinta años. Trece años de dolor... y en un solo día, Dios cambió su historia. ¿Estás esperando tu día? Escribe: Mi día va a llegar.",
  [P("jose", 0.5, **GOBERNADOR, accion="orar")], efectos=[{"tipo": "luz"}], rotulo="13 AÑOS", camara="fijo")

# ---------- 6. EL HAMBRE ----------
S("trigal", "Durante siete años, José guardó trigo en enormes almacenes por todo Egipto. Tanto, que dejaron de contarlo.",
  [P("jose", 0.5, **GOBERNADOR, accion="senalar")], [{"tipo": "canasta", "x": 0.7}], rotulo="CAPÍTULO 6: EL HAMBRE", camara="paneo")
S("desierto", "Y luego llegó el hambre, tal como Dios había dicho. No solo en Egipto, sino en todas las tierras de alrededor.",
  [P("hombre2", 0.4, accion="agacharse", emocion="triste"), P("mujer1", 0.6, emocion="triste")], efectos=[{"tipo": "oscuridad", "fuerza": 0.3}], camara="acercar")
S("campo", "Allá en Canaán, el anciano Jacob les dijo a sus hijos: He oído que en Egipto hay trigo. Vayan y compren comida, para que no muramos.",
  [P("jacob", 0.62, mira="izquierda", accion="senalar", emocion="triste", barba="#e8e4dc", pelo="#e8e4dc"), P("hermano1", 0.35), P("nino", 0.2, emocion="triste")],
  habla="jacob", camara="acercar")
S("campo", "Pero Jacob no dejó ir a Benjamín, el hermano menor. Tenía miedo de perderlo como había perdido a José.",
  [P("jacob", 0.55, accion="abrazar", emocion="triste", barba="#e8e4dc", pelo="#e8e4dc"), P("nino", 0.35, emocion="triste")], camara="fijo")

# ---------- 7. EL REENCUENTRO ----------
S("egipto", "Y así llegamos al momento del principio: los diez hermanos, inclinados hasta el suelo ante el gobernador de Egipto.",
  [P("hermano1", 0.25, accion="arrodillarse"), P("hermano2", 0.42, accion="arrodillarse"), P("jose", 0.75, mira="izquierda", **GOBERNADOR)],
  rotulo="CAPÍTULO 7: EL REENCUENTRO", camara="acercar")
S("egipto", "El sueño de José se estaba cumpliendo. Él los reconoció enseguida... pero ellos no lo reconocieron a él.",
  [P("jose", 0.5, **GOBERNADOR, emocion="sorprendido")], efectos=[{"tipo": "flash", "inicio": 0.5}], camara="acercar_rapido")
S("egipto", "José les habló con dureza: ¡Ustedes son espías! Quería saber si sus hermanos habían cambiado, o si seguían siendo los mismos de antes.",
  [P("jose", 0.6, mira="izquierda", **GOBERNADOR, accion="senalar", emocion="enojado"), P("hermano1", 0.3, accion="temblar", emocion="asustado")],
  habla="jose", camara="acercar")
S("egipto", "Les exigió que trajeran a Benjamín. Y cuando volvieron con él, José escondió su copa de plata en el saco del muchacho.",
  [P("nino", 0.35, emocion="sorprendido"), P("jose", 0.7, mira="izquierda", **GOBERNADOR)], [{"tipo": "monedas", "x": 0.5}], camara="paneo")
S("egipto", "Los guardias encontraron la copa. Benjamín se quedará aquí como mi esclavo, dijo José. Era la prueba final.",
  [P("guardia1", 0.25, objeto="lanza"), P("nino", 0.45, accion="temblar", emocion="llorando"), P("jose", 0.75, mira="izquierda", **GOBERNADOR, emocion="valiente")],
  efectos=[{"tipo": "temblor", "inicio": 0.5, "fin": 0.65}], camara="acercar_rapido")
S("egipto", "Entonces Judá, el mismo hermano que años antes propuso venderlo, se arrodilló: Por favor, déjeme a mí como esclavo en lugar del muchacho.",
  [P("hermano1", 0.4, accion="arrodillarse", emocion="llorando"), P("jose", 0.72, mira="izquierda", **GOBERNADOR, emocion="sorprendido")],
  habla="hermano1", camara="acercar")
S("egipto", "Sus hermanos habían cambiado. Y José ya no pudo contenerse más. Mandó salir a todos los egipcios... y se echó a llorar a gritos.",
  [P("jose", 0.5, **GOBERNADOR, emocion="llorando", accion="temblar")], camara="acercar")
S("egipto", "¡Yo soy José, su hermano, el que ustedes vendieron!",
  [P("jose", 0.5, **GOBERNADOR, accion="levantar", emocion="llorando")], habla="jose",
  efectos=[{"tipo": "flash", "inicio": 0.2}, {"tipo": "luz"}], camara="acercar_rapido")
S("egipto", "Los hermanos quedaron paralizados de miedo. Pero José les dijo: No se angustien. Ustedes pensaron hacerme mal, pero Dios lo convirtió en bien, para salvar muchas vidas.",
  [P("hermano1", 0.32, accion="abrazar", emocion="llorando"), P("jose", 0.6, mira="izquierda", **GOBERNADOR, accion="abrazar", emocion="llorando")],
  habla="jose", camara="fijo")
S("egipto", "Y abrazó a Benjamín, y besó a cada uno de sus hermanos, llorando con ellos.",
  [P("nino", 0.38, accion="abrazar", emocion="llorando"), P("jose", 0.58, mira="izquierda", **GOBERNADOR, accion="abrazar", emocion="feliz"),
   P("hermano2", 0.8, mira="izquierda", emocion="llorando")], efectos=[{"tipo": "luz"}], camara="acercar")

# ---------- 8. EL PADRE ----------
S("campo", "Cuando los hermanos volvieron a Canaán y le dijeron a Jacob: ¡José está vivo, y es gobernador de Egipto!, el anciano no lo podía creer.",
  [P("jacob", 0.6, mira="izquierda", emocion="sorprendido", barba="#e8e4dc", pelo="#e8e4dc"), P("hermano1", 0.35, accion="celebrar", emocion="feliz")],
  rotulo="CAPÍTULO 8: EL ABRAZO", camara="acercar_rapido")
S("egipto", "Jacob viajó a Egipto con toda su familia. Y cuando José vio a su padre, corrió hacia él, lo abrazó... y lloró sobre su cuello por largo rato.",
  [P("jose", 0.35, **GOBERNADOR, accion="abrazar", emocion="llorando"), P("jacob", 0.58, mira="izquierda", accion="abrazar", emocion="llorando", barba="#e8e4dc", pelo="#e8e4dc")],
  efectos=[{"tipo": "luz"}, {"tipo": "brillo"}], camara="acercar")
S("valle", "Después de veintidós años separados, la familia volvió a estar unida. Y Dios los cuidó en Egipto durante todo el tiempo del hambre.",
  [P("jacob", 0.3, barba="#e8e4dc", pelo="#e8e4dc", emocion="feliz"), P("jose", 0.5, **GOBERNADOR, emocion="feliz", accion="celebrar"),
   P("nino", 0.65, accion="celebrar"), P("hermano1", 0.8, emocion="feliz")], efectos=[{"tipo": "arcoiris"}], camara="paneo")

# ---------- ENSEÑANZA Y FINAL ----------
S("cielo", "El pozo, la esclavitud y la cárcel no eran el final de la historia de José. Eran el camino hacia el palacio.",
  [P("jose", 0.5, **GOBERNADOR, accion="orar")], efectos=[{"tipo": "luz"}], rotulo="ENSEÑANZA", camara="acercar")
S("cielo", "Lo que otros hacen para hacerte daño, Dios lo puede convertir en bien. Y el perdón no cambia el pasado... pero sí cambia el futuro.",
  [P("jose", 0.5, **GOBERNADOR, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="fijo")
S("cielo", "¿Tú habrías perdonado a tus hermanos como José? Respóndeme en los comentarios, que leo cada uno.",
  [P("jose", 0.4, **GOBERNADOR, accion="senalar"), P("nino", 0.62, mira="izquierda", accion="celebrar")], efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "Y si esta historia te tocó el corazón, suscríbete y activa la campanita. Mañana te espera otra gran historia de la Biblia. ¡Dios te bendiga!",
  [P("jose", 0.5, **GOBERNADOR, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}],
  rotulo="¡SUSCRÍBETE!", pausa=2.0, camara="acercar")

guardar("02_jose_la_historia_completa.json", "José - De Esclavo a Gobernador",
        "Lo VENDIERON sus propios hermanos... y terminó gobernando EGIPTO.",
        ["JOSÉ", "EGIPTO", "FARAÓN", "HERMANOS", "SUEÑO", "PERDÓN", "BENJAMÍN", "JACOB"])
