"""Video largo: David y Goliat, la historia completa."""
from base import S, P, gente, guardar

PASTOR = {"objeto": "cayado"}
HONDA = {"objeto": "honda"}

# ---------- APERTURA EN FRÍO ----------
S("valle", "Un gigante de casi tres metros, cubierto de bronce. Frente a él, un muchacho sin armadura, con cinco piedras y una honda. Todo un ejército contiene la respiración.",
  [P("david", 0.3, **HONDA, emocion="valiente"), P("goliat", 0.72, mira="izquierda", emocion="burlon", objeto="lanza")],
  efectos=[{"tipo": "temblor", "inicio": 0.6, "fin": 0.75}], camara="acercar_rapido", portada=True)
S("valle", "¿Cómo terminó ese muchacho ahí? ¿Y qué pasó en los segundos siguientes? Quédate, porque esta historia empieza mucho antes, en un campo lleno de ovejas.",
  [P("david", 0.5, **HONDA, emocion="valiente")], efectos=[{"tipo": "flash", "inicio": 0.85}], camara="acercar")

# ---------- 1. EL PASTORCITO ----------
S("campo", "David era el más pequeño de los ocho hijos de Isaí, en el pueblo de Belén. Mientras sus hermanos eran fuertes y altos, a él le tocaba cuidar las ovejas.",
  [P("david", 0.45, **PASTOR, emocion="feliz"), P("oveja1", 0.65), P("oveja2", 0.8)], rotulo="CAPÍTULO 1: EL PASTORCITO", camara="paneo")
S("campo", "Pasaba días y noches en el campo, tocando su arpa y cantándole a Dios. Nadie lo veía... pero Dios sí lo veía.",
  [P("david", 0.5, **PASTOR, accion="alabar", emocion="feliz"), P("oveja1", 0.75)], efectos=[{"tipo": "luz", "x": 0.5}], camara="acercar")
S("campo", "Un día, un león atacó el rebaño y se llevó una oveja. David no huyó: corrió tras el león, le quitó la oveja de la boca... y lo venció.",
  [P("david", 0.35, **PASTOR, accion="correr", emocion="valiente"), P("leon1", 0.7, mira="izquierda", accion="rugir")],
  efectos=[{"tipo": "temblor", "inicio": 0.5, "fin": 0.6}, {"tipo": "flash", "inicio": 0.7}], camara="acercar_rapido")
S("campo", "Lo mismo hizo con un oso. David sabía que su fuerza no venía de sus brazos, sino de Dios. Y esa confianza lo prepararía para algo mucho más grande.",
  [P("david", 0.5, **PASTOR, accion="levantar", emocion="valiente")], efectos=[{"tipo": "luz"}], camara="acercar")

# ---------- 2. EL UNGIDO ----------
S("valle", "En ese tiempo, el rey de Israel era Saúl. Pero Saúl había desobedecido a Dios, y Dios buscaba un nuevo rey.",
  [P("saul", 0.5, emocion="enojado", tocado="corona")], rotulo="CAPÍTULO 2: EL ELEGIDO", camara="acercar")
S("campo", "Dios envió al profeta Samuel a la casa de Isaí. Uno de tus hijos será el próximo rey, le dijo.",
  [P("hombre1", 0.35, barba="#e8e4dc", pelo="#e8e4dc", tunica="#5a4a8a", accion="senalar"), P("jacob", 0.68, mira="izquierda", emocion="sorprendido")],
  habla="hombre1", camara="fijo")
S("campo", "Isaí le presentó a sus hijos mayores, uno por uno. Eran altos, fuertes y elegantes. Pero Dios le dijo a Samuel: No mires su apariencia.",
  [P("hermano1", 0.3, emocion="valiente"), P("hermano2", 0.48, emocion="valiente"), P("hombre1", 0.75, mira="izquierda", barba="#e8e4dc", pelo="#e8e4dc", tunica="#5a4a8a")],
  camara="paneo")
S("cielo", "El hombre mira lo que está delante de sus ojos, pero Dios mira el corazón.",
  [], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="1 SAMUEL 16:7", camara="acercar")
S("campo", "¿No tienes más hijos?, preguntó Samuel. Bueno, queda el más pequeño, pero está cuidando las ovejas.",
  [P("hombre1", 0.35, barba="#e8e4dc", pelo="#e8e4dc", tunica="#5a4a8a", emocion="sorprendido"), P("jacob", 0.65, mira="izquierda")], camara="fijo")
S("campo", "Cuando David llegó, Dios dijo: Es él. Y Samuel derramó aceite sobre su cabeza. El pastorcito que nadie tomaba en cuenta... sería el futuro rey de Israel.",
  [P("david", 0.55, **PASTOR, accion="arrodillarse"), P("hombre1", 0.35, barba="#e8e4dc", pelo="#e8e4dc", tunica="#5a4a8a", accion="ofrecer")],
  efectos=[{"tipo": "luz", "x": 0.55}, {"tipo": "brillo", "x": 0.55}], camara="acercar")
S("cielo", "Si alguna vez te sentiste invisible, escribe en los comentarios: Dios mira mi corazón.",
  [P("david", 0.5, **PASTOR, accion="orar")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------- 3. EL ARPISTA DEL REY ----------
S("palacio", "Mientras tanto, en el palacio, el rey Saúl estaba atormentado. Tenía noches de angustia y ataques de furia que nadie podía calmar.",
  [P("saul", 0.5, tocado="corona", accion="temblar", emocion="asustado")], [{"tipo": "trono", "x": 0.55, "profundidad": -30}],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.4}], rotulo="CAPÍTULO 3: EL ARPISTA DEL REY", camara="acercar")
S("palacio", "Sus siervos le dijeron: Busquemos a alguien que toque el arpa. Y uno de ellos respondió: Conozco a un joven de Belén, hijo de Isaí, que toca muy bien. Y el Señor está con él.",
  [P("hombre2", 0.35, accion="senalar"), P("saul", 0.68, mira="izquierda", tocado="corona", emocion="triste")], habla="hombre2", camara="fijo")
S("palacio", "Así, el pastorcito llegó al palacio del rey. Y cada vez que Saúl se angustiaba, David tocaba su arpa... y la paz volvía al corazón del rey.",
  [P("david", 0.35, accion="alabar", emocion="feliz"), P("saul", 0.68, mira="izquierda", tocado="corona", emocion="feliz")],
  efectos=[{"tipo": "luz", "x": 0.35}, {"tipo": "brillo", "x": 0.35}], camara="acercar")
S("palacio", "Saúl le tomó tanto cariño, que lo nombró su escudero. Lo que el rey no sabía es que ese joven sería el que ocuparía su trono.",
  [P("david", 0.4, objeto="escudo", emocion="valiente"), P("saul", 0.68, mira="izquierda", tocado="corona")], camara="acercar")
S("campo", "Después David volvió a casa a cuidar las ovejas de su padre. Pero muy pronto, una guerra lo cambiaría todo.",
  [P("david", 0.3, hasta=0.6, accion="caminar", **PASTOR), P("oveja1", 0.75)], efectos=[{"tipo": "oscuridad", "fuerza": 0.2}], camara="paneo")

# ---------- 3. EL GIGANTE ----------
S("valle", "Años después, los filisteos declararon la guerra a Israel. Los dos ejércitos se acamparon en dos montes, con un valle en medio.",
  [], [gente(0.25, 0.6, variante="soldados"), gente(0.75, 0.6, variante="soldados")], rotulo="CAPÍTULO 4: EL GIGANTE", camara="alejar")
S("valle", "Y de entre los filisteos salió un guerrero enorme: Goliat de Gat. Su armadura pesaba más de cincuenta kilos, y la punta de su lanza era de hierro.",
  [P("goliat", 0.55, accion="caminar", hasta=0.6, objeto="lanza", emocion="enojado")], efectos=[{"tipo": "temblor", "inicio": 0.1, "fin": 0.9}], camara="acercar")
S("valle", "¡Elijan a un hombre que pelee conmigo! Si me vence, seremos sus esclavos. Pero si yo lo venzo, ustedes serán nuestros esclavos.",
  [P("goliat", 0.5, accion="senalar", objeto="lanza", emocion="burlon")], habla="goliat", camara="acercar_rapido")
S("valle", "Durante cuarenta días, mañana y tarde, Goliat salía a desafiar a Israel. Y nadie, ni siquiera el rey Saúl, se atrevía a enfrentarlo.",
  [P("soldado1", 0.35, accion="temblar", emocion="asustado"), P("saul", 0.6, tocado="corona", emocion="asustado")], rotulo="40 DÍAS", camara="paneo")

# ---------- 4. EL VALIENTE ----------
S("camino", "Un día, Isaí envió a David a llevar comida a sus hermanos, que estaban en el ejército.",
  [P("david", 0.15, hasta=0.55, accion="caminar", emocion="feliz")], [{"tipo": "canasta", "x": 0.3}], rotulo="CAPÍTULO 5: ¿QUIÉN ES ESE FILISTEO?", camara="paneo")
S("valle", "Justo cuando llegó, escuchó los gritos de Goliat burlándose del Dios de Israel. Y vio a todos los soldados huir de miedo.",
  [P("david", 0.3, emocion="sorprendido"), P("goliat", 0.75, mira="izquierda", accion="senalar", emocion="burlon", objeto="lanza")], habla="goliat", camara="acercar")
S("valle", "¿Quién es este filisteo para desafiar a los ejércitos del Dios vivo?, preguntó David indignado.",
  [P("david", 0.45, accion="senalar", emocion="enojado")], habla="david", camara="acercar_rapido")
S("valle", "Su hermano mayor se enojó: ¿Qué haces aquí? Solo viniste a ver la batalla. Pero David no se dejó desanimar.",
  [P("hermano1", 0.65, mira="izquierda", emocion="enojado", accion="senalar"), P("david", 0.35, emocion="valiente")], habla="hermano1", camara="fijo")
S("palacio", "Lo llevaron ante el rey Saúl. Y David le dijo: Nadie tenga miedo de ese gigante. Yo iré a pelear contra él.",
  [P("david", 0.35, emocion="valiente", accion="senalar"), P("saul", 0.7, mira="izquierda", tocado="corona", emocion="sorprendido")], habla="david", camara="acercar")
S("palacio", "Saúl casi se ríe. Tú no puedes. Eres solo un muchacho, y él es guerrero desde su juventud.",
  [P("saul", 0.55, tocado="corona", emocion="burlon", accion="senalar")], habla="saul", camara="acercar")
S("campo", "Pero David le contó lo del león y el oso. El Señor que me libró de las garras del león, me librará también de este filisteo.",
  [P("david", 0.45, **PASTOR, accion="levantar", emocion="valiente"), P("leon1", 0.75, mira="izquierda", accion="caer")], efectos=[{"tipo": "luz"}], camara="acercar")
S("palacio", "Saúl le dio su propia armadura y su espada. Pero David apenas podía caminar con ella. No estoy acostumbrado, dijo, y se la quitó.",
  [P("david", 0.5, armadura=True, objeto="espada", accion="temblar", emocion="sorprendido")], camara="fijo")
S("mar", "En su lugar, bajó al arroyo y eligió cinco piedras lisas. Las guardó en su bolsa de pastor... y tomó su honda.",
  [P("david", 0.45, accion="agacharse", **HONDA)], [{"tipo": "rocas", "x": 0.6, "escala": 0.5}], camara="acercar")
S("cielo", "Pausa. Antes de ver la batalla, dime en los comentarios: ¿cuál es el gigante que estás enfrentando hoy?",
  [P("david", 0.5, **HONDA, accion="senalar")], efectos=[{"tipo": "luz"}], rotulo="¿Y TU GIGANTE?", camara="fijo")

# ---------- 5. LA BATALLA ----------
S("valle", "David caminó hacia el valle. Cuando Goliat lo vio, soltó una carcajada: ¿Soy acaso un perro, para que vengas contra mí con palos?",
  [P("david", 0.2, hasta=0.35, accion="caminar", **HONDA), P("goliat", 0.75, mira="izquierda", accion="senalar", emocion="burlon", objeto="lanza")],
  rotulo="CAPÍTULO 6: LA BATALLA", habla="goliat", camara="paneo")
S("valle", "¡Ven acá, y daré tu carne a las aves del cielo!",
  [P("goliat", 0.55, accion="rugir", objeto="lanza", emocion="enojado")], habla="goliat", efectos=[{"tipo": "temblor", "inicio": 0.2, "fin": 0.5}], camara="acercar_rapido")
S("valle", "Y David respondió con una voz que todo el valle escuchó: Tú vienes contra mí con espada y lanza. Pero yo vengo contra ti en el nombre del Señor.",
  [P("david", 0.4, **HONDA, accion="senalar", emocion="valiente")], habla="david", efectos=[{"tipo": "luz", "x": 0.4}], camara="acercar")
S("valle", "¡Hoy toda la tierra sabrá que hay Dios en Israel! Porque la batalla es del Señor.",
  [P("david", 0.45, **HONDA, accion="levantar", emocion="valiente")], habla="david", efectos=[{"tipo": "brillo"}, {"tipo": "rayo", "inicio": 0.8}], camara="acercar_rapido")
S("valle", "Goliat avanzó con paso pesado. Y David, en vez de huir... ¡corrió hacia él!",
  [P("goliat", 0.75, mira="izquierda", accion="caminar", hasta=0.65, objeto="lanza", emocion="enojado"),
   P("david", 0.15, hasta=0.4, accion="correr", objeto="girar_honda", emocion="valiente")], efectos=[{"tipo": "temblor", "inicio": 0.1, "fin": 0.9}], camara="paneo")
S("valle", "Metió la mano en su bolsa, sacó una piedra, la puso en la honda... y la lanzó con todas sus fuerzas.",
  [P("david", 0.35, objeto="lanzo", accion="lanzar", emocion="valiente"), P("goliat", 0.72, mira="izquierda", objeto="lanza")],
  efectos=[{"tipo": "proyectil", "inicio": 0.55, "fin": 0.85}], camara="acercar_rapido")
S("valle", "La piedra voló por el aire y se clavó justo en la frente del gigante.",
  [P("goliat", 0.6, mira="izquierda", emocion="noqueado", accion="temblar")], efectos=[{"tipo": "flash", "inicio": 0.3}, {"tipo": "temblor", "inicio": 0.3, "fin": 0.5}], camara="acercar_rapido")
S("valle", "Goliat se tambaleó... y cayó de cara al suelo, con un estruendo que hizo temblar el valle entero.",
  [P("goliat", 0.6, mira="izquierda", accion="caer_de_cara", emocion="noqueado")], efectos=[{"tipo": "temblor", "inicio": 0.5, "fin": 0.8}], camara="acercar")
S("valle", "Un pastorcito, sin espada y sin armadura, había vencido al guerrero más temido de su tiempo.",
  [P("david", 0.35, accion="levantar", emocion="valiente", **HONDA), P("goliat", 0.7, accion="caer_de_cara", emocion="noqueado")], efectos=[{"tipo": "luz"}], camara="alejar")
S("valle", "Al ver a su campeón derrotado, los filisteos huyeron. Y el ejército de Israel salió tras ellos gritando de alegría.",
  [P("soldado1", 0.3, accion="celebrar", emocion="feliz"), P("soldado2", 0.5, accion="correr", emocion="feliz")], [gente(0.75, 0.55, variante="soldados", hasta=0.95)], camara="paneo")

# ---------- 6. DEL CAMPO AL TRONO ----------
S("palacio", "Ese día, David se volvió el héroe de todo Israel. Las mujeres salían a las calles cantando y bailando en su honor.",
  [P("david", 0.4, emocion="feliz", accion="alabar"), P("mujer1", 0.65, accion="celebrar", emocion="feliz")], rotulo="CAPÍTULO 7: EL FUTURO REY", camara="acercar")
S("palacio", "Pero no todo fue fácil. El rey Saúl sintió celos de él, y durante años David tuvo que huir y esconderse en cuevas.",
  [P("saul", 0.6, tocado="corona", emocion="enojado", accion="senalar"), P("david", 0.25, accion="correr", hasta=0.05, emocion="asustado")], camara="acercar")
S("rocas", "Una vez, Saúl entró solo en una cueva para descansar. No sabía que David y sus hombres estaban escondidos al fondo, en la oscuridad.",
  [P("saul", 0.65, tocado="corona", accion="dormir")], efectos=[{"tipo": "oscuridad", "fuerza": 0.55}], camara="acercar")
S("rocas", "¡Es tu oportunidad!, le susurraron sus hombres. Dios te entregó a tu enemigo. David se acercó en silencio, con un cuchillo en la mano...",
  [P("david", 0.35, accion="agacharse", objeto="espada", emocion="valiente"), P("saul", 0.7, tocado="corona", accion="dormir")],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.5}], camara="acercar_rapido")
S("rocas", "...pero solo cortó un pedacito del manto del rey. No tocaré al ungido del Señor, dijo. David prefirió perdonar antes que vengarse.",
  [P("david", 0.4, accion="ofrecer", emocion="triste"), P("saul", 0.7, mira="izquierda", tocado="corona", emocion="llorando")],
  habla="david", efectos=[{"tipo": "luz", "x": 0.4}], camara="acercar")
S("rocas", "Aun así, David nunca dejó de confiar en Dios. En esos años difíciles escribió muchos de los salmos que hoy leemos en la Biblia.",
  [P("david", 0.5, accion="orar")], efectos=[{"tipo": "luz", "x": 0.5}], camara="acercar")
S("cielo", "El Señor es mi pastor, nada me faltará. Esas palabras las escribió el mismo pastorcito que venció al gigante.",
  [P("david", 0.5, **PASTOR, accion="alabar", emocion="feliz"), P("oveja1", 0.72)], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="SALMO 23", camara="fijo")
S("palacio", "Y finalmente, tal como Dios había prometido, David fue coronado rey de Israel. El rey más amado de toda su historia.",
  [P("david", 0.5, tocado="corona", manto="#b8302a", accion="alabar", emocion="feliz")], [{"tipo": "trono", "x": 0.55, "profundidad": -30}, gente(0.5, 0.55, y=200, delante=True, profundidad=None)],
  efectos=[{"tipo": "luz"}, {"tipo": "brillo"}], camara="acercar")
S("cielo", "Y de su familia, muchos años después, nacería en Belén alguien todavía más grande: Jesús, el Hijo de David.",
  [P("jesus", 0.5, accion="ofrecer", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="acercar")

# ---------- ENSEÑANZA Y FINAL ----------
S("cielo", "David no venció por ser el más grande, ni el más fuerte. Venció porque sabía que su Dios era más grande que su gigante.",
  [P("david", 0.5, **HONDA, accion="orar")], efectos=[{"tipo": "luz"}], rotulo="ENSEÑANZA", camara="acercar")
S("cielo", "No le digas a Dios lo grande que es tu gigante. Dile a tu gigante lo grande que es tu Dios.",
  [P("david", 0.5, **HONDA, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="fijo")
S("cielo", "¿Qué parte te gustó más: el león, la piedra o la caída del gigante? Cuéntamelo en los comentarios.",
  [P("david", 0.4, **HONDA, accion="senalar"), P("oveja1", 0.62)], efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "Suscríbete y activa la campanita, porque mañana llega otra gran historia de la Biblia. ¡Dios te bendiga!",
  [P("david", 0.5, **HONDA, accion="alabar", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}],
  rotulo="¡SUSCRÍBETE!", pausa=2.0, camara="acercar")

guardar("03_david_y_goliat_la_historia_completa.json", "David y Goliat - La Historia Completa",
        "Un MUCHACHO con una honda contra un GIGANTE de tres metros.",
        ["DAVID", "GOLIAT", "GIGANTE", "SAÚL", "PIEDRA", "HONDA", "ISRAEL", "SEÑOR", "REY"])
