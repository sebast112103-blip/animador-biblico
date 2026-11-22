"""Video largo del dia: Moises, la historia completa (unos 10 minutos)."""
import json
from pathlib import Path

E = []


def S(fondo, texto, pers=(), cosas=None, efectos=None, **kw):
    e = {"fondo": fondo, "texto": texto, "personajes": list(pers)}
    if cosas:
        e["cosas"] = cosas
    if efectos:
        e["efectos"] = efectos
    e.update(kw)
    E.append(e)


def P(id, x, **kw):
    return {"id": id, "x": x, **kw}


def gente(x=0.5, esc=0.65, y=-160, prof=-70, **kw):
    return {"tipo": "multitud", "x": x, "escala": esc, "y": y, "profundidad": prof, **kw}


VARA = {"objeto": "cayado"}
PRINCIPE = {"tunica": "#f4f1ea", "manto": "#d9a62e", "tocado": "nemes", "color_tocado": "#d9a62e", "barba": None}
VIEJO = {"barba": "#e8e4dc", "pelo": "#e8e4dc"}

# ---------------- 1. ESCLAVOS EN EGIPTO ----------------
S("egipto", "Hace mucho tiempo, el pueblo de Israel vivía en Egipto. Al principio eran bienvenidos, pero con los años se multiplicaron tanto que el nuevo faraón tuvo miedo de ellos.",
  [P("faraon", 0.55, emocion="enojado", accion="senalar")], [{"tipo": "trono", "x": 0.6, "profundidad": -30}],
  rotulo="CAPÍTULO 1: ESCLAVOS", camara="acercar", portada=False)
S("egipto", "Así que los convirtió en esclavos. Los obligó a trabajar bajo el sol ardiente, fabricando ladrillos y construyendo ciudades enteras para él.",
  [P("hombre1", 0.25, accion="empujar", emocion="triste"), P("hombre2", 0.5, accion="agacharse", emocion="triste"),
   P("soldado1", 0.8, mira="izquierda", emocion="enojado", objeto="lanza")],
  [{"tipo": "piedra", "x": 0.36, "escala": 0.6}], camara="paneo")
S("egipto", "Pero mientras más los hacían sufrir, más crecía el pueblo. Y entonces el faraón dio una orden terrible.",
  [P("faraon", 0.5, accion="senalar", emocion="enojado")], [gente(0.5, 0.6, variante="soldados")],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.3}], camara="acercar_rapido")
S("palacio", "Ordenó que todos los bebés varones de los israelitas fueran lanzados al río Nilo.",
  [P("faraon", 0.62, accion="senalar", emocion="enojado", mira="izquierda"), P("soldado1", 0.3, objeto="lanza"), P("soldado2", 0.15, objeto="lanza")],
  [{"tipo": "trono", "x": 0.68, "profundidad": -30}], efectos=[{"tipo": "temblor", "inicio": 0.3, "fin": 0.5}], camara="fijo")
S("noche", "Imagínate el miedo de las familias hebreas. Cada noche temían escuchar los pasos de los soldados.",
  [P("mujer1", 0.4, emocion="asustado", accion="temblar"), P("hombre1", 0.6, emocion="asustado", mira="izquierda")], camara="acercar")

# ---------------- 2. EL BEBE EN EL RIO ----------------
S("noche", "En ese tiempo, una mujer llamada Jocabed tuvo un hermoso bebé. Y al verlo, decidió protegerlo a toda costa.",
  [P("jocabed", 0.45, accion="abrazar", emocion="feliz")], [{"tipo": "pesebre", "x": 0.6, "escala": 0.8}],
  rotulo="CAPÍTULO 2: EL BEBÉ DEL RÍO", camara="acercar")
S("noche", "Durante tres meses lo escondió en su casa. Pero el bebé crecía, y cada vez era más difícil ocultar su llanto.",
  [P("jocabed", 0.4, emocion="asustado", accion="agacharse"), P("miriam", 0.62, emocion="asustado", mira="izquierda")],
  [{"tipo": "pesebre", "x": 0.5, "escala": 0.8}], camara="fijo")
S("campo", "Entonces Jocabed tomó una canasta, la cubrió con brea para que no le entrara agua, y puso al niño adentro.",
  [P("jocabed", 0.4, accion="ofrecer", emocion="triste")], [{"tipo": "canasta", "x": 0.58, "escala": 0.9}], camara="acercar")
S("mar", "Con el corazón roto, dejó la canasta entre los juncos, a la orilla del río Nilo. Solo podía confiar en Dios.",
  [P("jocabed", 0.3, accion="orar", emocion="llorando")], [{"tipo": "canasta", "x": 0.6, "escala": 0.8, "y": 120}], camara="acercar")
S("mar", "Su hija Miriam se quedó escondida a lo lejos, observando qué pasaría con su hermanito.",
  [P("miriam", 0.18, accion="agacharse", emocion="asustado")], [{"tipo": "canasta", "x": 0.62, "escala": 0.8, "y": 120}],
  camara="paneo")
S("mar", "Y en ese momento llegó al río nada menos que la hija del faraón, con sus criadas, para bañarse.",
  [P("princesa", 0.15, hasta=0.45, accion="caminar"), P("criada", 0.05, hasta=0.3, accion="caminar")],
  [{"tipo": "canasta", "x": 0.68, "escala": 0.8, "y": 120}], camara="acercar")
S("mar", "Cuando vio la canasta, la abrió... y encontró al bebé llorando.",
  [P("princesa", 0.5, accion="agacharse", emocion="sorprendido")], [{"tipo": "canasta", "x": 0.63, "escala": 0.8, "y": 120}],
  efectos=[{"tipo": "brillo", "x": 0.63}], camara="acercar_rapido")
S("mar", "Este es uno de los niños de los hebreos, dijo con ternura. Y su corazón se llenó de compasión.",
  [P("princesa", 0.5, accion="abrazar", emocion="feliz")], habla="princesa", camara="acercar")
S("mar", "Miriam corrió valientemente y le preguntó: ¿Quiere que le busque una mujer hebrea para que cuide al niño?",
  [P("miriam", 0.3, accion="correr", hasta=0.4), P("princesa", 0.65, mira="izquierda", accion="abrazar")], habla="miriam", camara="fijo")
S("campo", "Y adivina a quién buscó Miriam. ¡A su propia madre! Así Jocabed pudo criar a su hijo, y además le pagaban por hacerlo.",
  [P("jocabed", 0.4, accion="abrazar", emocion="llorando"), P("miriam", 0.62, accion="celebrar", emocion="feliz")],
  efectos=[{"tipo": "luz"}], camara="acercar")
S("palacio", "Cuando el niño creció, fue llevado al palacio. La princesa lo adoptó como su hijo y le puso por nombre Moisés, que significa sacado de las aguas.",
  [P("moises", 0.45, emocion="feliz", **PRINCIPE, escala=0.8), P("princesa", 0.65, mira="izquierda", emocion="feliz")],
  [{"tipo": "trono", "x": 0.8, "profundidad": -30}], camara="acercar")
S("cielo", "Dios había salvado al niño que un día salvaría a todo su pueblo. Escribe en los comentarios: Dios tiene un plan para mí.",
  [P("moises", 0.5, **PRINCIPE, escala=0.8, accion="alabar")], efectos=[{"tipo": "luz"}], camara="fijo")

# ---------------- 3. HUIDA AL DESIERTO ----------------
S("palacio", "Moisés creció como un príncipe de Egipto. Tenía riquezas, educación y poder. Pero nunca olvidó que era hebreo.",
  [P("moises", 0.45, **PRINCIPE, emocion="valiente")], [{"tipo": "trono", "x": 0.7, "profundidad": -30}],
  rotulo="CAPÍTULO 3: LA HUIDA", camara="paneo")
S("egipto", "Un día salió a ver a sus hermanos y vio a un capataz egipcio golpeando a un esclavo hebreo.",
  [P("hombre1", 0.6, accion="caer", emocion="llorando"), P("soldado1", 0.78, mira="izquierda", accion="lanzar", emocion="enojado"),
   P("moises", 0.2, **PRINCIPE, emocion="sorprendido")], efectos=[{"tipo": "temblor", "inicio": 0.4, "fin": 0.55}], camara="acercar")
S("egipto", "Lleno de rabia, Moisés atacó al egipcio y lo mató. Luego, asustado, escondió el cuerpo en la arena.",
  [P("moises", 0.45, **PRINCIPE, accion="empujar", emocion="enojado"), P("soldado1", 0.65, accion="caer_de_cara", mira="izquierda")],
  efectos=[{"tipo": "flash", "inicio": 0.2}], camara="acercar_rapido")
S("palacio", "Pero la noticia llegó a oídos del faraón, y este ordenó que buscaran a Moisés para matarlo.",
  [P("faraon", 0.55, accion="senalar", emocion="enojado")], [gente(0.5, 0.6, variante="soldados")], camara="acercar")
S("desierto", "Moisés tuvo que huir. Dejó atrás el palacio, la riqueza y todo lo que conocía, y escapó al desierto.",
  [P("moises", 0.1, hasta=0.7, accion="correr", emocion="asustado", manto="#8a5a3a", tocado="turbante")], camara="paneo")
S("desierto", "Caminó durante días bajo el sol, hasta llegar a una tierra llamada Madián.",
  [P("moises", 0.2, hasta=0.6, accion="caminar", emocion="triste", manto="#8a5a3a", tocado="turbante")], camara="alejar")
S("campo", "Allí se casó, formó una familia y se convirtió en pastor de ovejas. Pasaron cuarenta largos años.",
  [P("moises", 0.4, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a"), P("oveja1", 0.6), P("oveja2", 0.75)],
  rotulo="40 AÑOS DESPUÉS", camara="acercar")
S("campo", "Mientras tanto, en Egipto, el pueblo seguía sufriendo y clamaba a Dios día y noche. Y Dios escuchó su clamor.",
  [P("hombre1", 0.35, accion="orar", emocion="llorando"), P("mujer1", 0.6, accion="orar", emocion="llorando")],
  efectos=[{"tipo": "luz", "x": 0.5}], camara="acercar", fondo_override=None)

# ---------------- 4. LA ZARZA ARDIENTE ----------------
S("montana", "Un día, mientras cuidaba las ovejas cerca del monte de Dios, Moisés vio algo increíble.",
  [P("moises", 0.3, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="caminar", hasta=0.4), P("oveja1", 0.15)],
  rotulo="CAPÍTULO 4: LA ZARZA", camara="paneo")
S("montana", "Una zarza ardía en fuego... pero no se consumía. Las llamas no la quemaban.",
  [], [{"tipo": "arbol", "x": 0.55, "escala": 0.6}], efectos=[{"tipo": "fuego", "x": 0.55, "tamano": 1.4}, {"tipo": "brillo", "x": 0.55}],
  camara="acercar_rapido", portada=True)
S("montana", "Cuando Moisés se acercó para mirar, una voz lo llamó desde el fuego: ¡Moisés, Moisés!",
  [P("moises", 0.3, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", emocion="sorprendido")],
  [{"tipo": "arbol", "x": 0.62, "escala": 0.6}], efectos=[{"tipo": "fuego", "x": 0.62, "tamano": 1.4}, {"tipo": "temblor", "inicio": 0.5, "fin": 0.65}],
  camara="acercar")
S("montana", "No te acerques. Quítate las sandalias, porque el lugar donde estás es tierra santa. Yo soy el Dios de tus padres.",
  [P("moises", 0.3, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="arrodillarse", emocion="asustado")],
  [{"tipo": "arbol", "x": 0.62, "escala": 0.6}], efectos=[{"tipo": "fuego", "x": 0.62, "tamano": 1.4}, {"tipo": "luz", "x": 0.62}],
  camara="fijo")
S("montana", "He visto el sufrimiento de mi pueblo en Egipto. Ve, porque yo te envío al faraón para que saques a mi pueblo de allí.",
  [P("moises", 0.3, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="arrodillarse")],
  [{"tipo": "arbol", "x": 0.62, "escala": 0.6}], efectos=[{"tipo": "fuego", "x": 0.62, "tamano": 1.4}], camara="acercar")
S("montana", "Pero Moisés tuvo miedo. ¿Quién soy yo para ir ante el faraón? Ni siquiera sé hablar bien.",
  [P("moises", 0.35, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="temblar", emocion="asustado")],
  [{"tipo": "arbol", "x": 0.65, "escala": 0.6}], efectos=[{"tipo": "fuego", "x": 0.65, "tamano": 1.2}], habla="moises", camara="acercar")
S("montana", "Y Dios le respondió: Yo estaré contigo. Tu hermano Aarón hablará por ti.",
  [P("moises", 0.35, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", emocion="sorprendido")],
  [{"tipo": "arbol", "x": 0.65, "escala": 0.6}], efectos=[{"tipo": "fuego", "x": 0.65, "tamano": 1.2}, {"tipo": "brillo", "x": 0.65}],
  camara="fijo")
S("cielo", "¿Alguna vez sentiste que no eras capaz? Dios no llama a los preparados; Dios prepara a los que llama.",
  [P("moises", 0.5, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="orar")], efectos=[{"tipo": "luz"}],
  rotulo="RECUERDA", camara="acercar")

# ---------------- 5. ANTE EL FARAON ----------------
S("desierto", "Así que Moisés volvió a Egipto con su vara en la mano. En el camino se encontró con su hermano Aarón.",
  [P("moises", 0.2, hasta=0.4, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="caminar"),
   P("aaron", 0.75, mira="izquierda", accion="abrazar", emocion="feliz")],
  rotulo="CAPÍTULO 5: DEJA IR A MI PUEBLO", camara="acercar")
S("palacio", "Juntos entraron al palacio y se pararon frente al hombre más poderoso del mundo.",
  [P("moises", 0.2, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a"), P("aaron", 0.35),
   P("faraon", 0.72, mira="izquierda", emocion="burlon")], [{"tipo": "trono", "x": 0.78, "profundidad": -30}], camara="paneo")
S("palacio", "Así dice el Señor, Dios de Israel: ¡Deja ir a mi pueblo!",
  [P("moises", 0.3, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="senalar", emocion="valiente"),
   P("faraon", 0.72, mira="izquierda", emocion="enojado")], [{"tipo": "trono", "x": 0.78, "profundidad": -30}],
  habla="moises", efectos=[{"tipo": "temblor", "inicio": 0.6, "fin": 0.75}], camara="acercar_rapido")
S("palacio", "El faraón se rió. ¿Quién es ese Dios para que yo le obedezca? No conozco a tu Dios, y no dejaré ir a Israel.",
  [P("faraon", 0.55, accion="senalar", emocion="burlon")], [{"tipo": "trono", "x": 0.6, "profundidad": -30}], habla="faraon", camara="acercar")
S("egipto", "Y en lugar de escuchar, hizo el trabajo de los esclavos aún más duro. Ahora tendrían que buscar su propia paja para los ladrillos.",
  [P("hombre1", 0.3, accion="agacharse", emocion="llorando"), P("hombre2", 0.55, accion="empujar", emocion="triste"),
   P("soldado1", 0.82, mira="izquierda", objeto="lanza", emocion="enojado")], camara="paneo")
S("egipto", "El pueblo estaba furioso con Moisés. Y Moisés, triste, le preguntó a Dios por qué todo había empeorado.",
  [P("moises", 0.35, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="orar", emocion="triste"),
   P("hombre1", 0.65, mira="izquierda", accion="senalar", emocion="enojado")], camara="acercar")
S("cielo", "Pero Dios le dijo: Ahora verás lo que haré. Con mano poderosa los sacaré de Egipto.",
  [P("moises", 0.5, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", emocion="sorprendido")],
  efectos=[{"tipo": "luz"}, {"tipo": "rayo", "inicio": 0.6}], camara="acercar_rapido")

# ---------------- 6. LAS PLAGAS ----------------
S("mar", "Entonces comenzaron las diez plagas. Primero, Moisés golpeó el río con su vara... y el agua se convirtió en sangre.",
  [P("moises", 0.3, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="levantar")],
  efectos=[{"tipo": "agua"}, {"tipo": "flash", "inicio": 0.55}, {"tipo": "oscuridad", "fuerza": 0.25}],
  rotulo="CAPÍTULO 6: LAS DIEZ PLAGAS", camara="acercar")
S("egipto", "Los peces murieron y nadie podía beber. Luego vinieron millones de ranas que invadieron las casas, las camas y hasta los hornos.",
  [P("hombre2", 0.35, accion="saltar", emocion="asustado"), P("criada", 0.6, accion="temblar", emocion="asustado")], camara="paneo")
S("egipto", "Después llegaron los piojos, y luego nubes de moscas que cubrían todo Egipto.",
  [P("soldado1", 0.4, accion="temblar", emocion="asustado"), P("soldado2", 0.62, accion="agacharse", emocion="asustado")],
  efectos=[{"tipo": "lluvia"}], camara="acercar")
S("campo", "Los animales de los egipcios enfermaron, y la gente se llenó de llagas dolorosas.",
  [P("burro", 0.4, accion="caer"), P("hombre2", 0.65, emocion="llorando", accion="agacharse")],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.2}], camara="fijo")
S("tormenta", "Entonces cayó del cielo un granizo terrible, mezclado con fuego, como nunca se había visto.",
  [P("soldado1", 0.4, accion="correr", emocion="asustado", hasta=0.7)],
  efectos=[{"tipo": "lluvia"}, {"tipo": "rayo", "inicio": 0.2}, {"tipo": "rayo", "inicio": 0.6}, {"tipo": "fuego", "x": 0.25, "tamano": 0.8}],
  camara="acercar_rapido")
S("egipto", "Luego llegaron las langostas y se comieron todo lo verde que quedaba en los campos.",
  [P("hombre2", 0.45, accion="temblar", emocion="llorando")], [gente(0.5, 0.55, variante="egipcios")],
  efectos=[{"tipo": "lluvia"}, {"tipo": "oscuridad", "fuerza": 0.3}], camara="paneo")
S("noche", "Y la novena plaga fue una oscuridad tan espesa que durante tres días nadie podía ver a nadie... excepto en las casas de los israelitas, donde había luz.",
  [P("mujer1", 0.65, emocion="feliz")], efectos=[{"tipo": "oscuridad", "fuerza": 0.7}, {"tipo": "luz", "x": 0.65}], camara="acercar")
S("palacio", "Cada vez que llegaba una plaga, el faraón prometía dejarlos ir. Pero cuando la plaga terminaba, su corazón se endurecía otra vez.",
  [P("faraon", 0.5, accion="temblar", emocion="asustado")], [{"tipo": "trono", "x": 0.55, "profundidad": -30}],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.3}], camara="acercar")
S("cielo", "Pausa un momento. ¿Cuántas oportunidades le dio Dios al faraón? Escribe el número en los comentarios.",
  [P("moises", 0.5, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="senalar")], efectos=[{"tipo": "luz"}],
  rotulo="¿CUÁNTAS?", camara="fijo")

# ---------------- 7. LA PASCUA ----------------
S("noche", "Entonces Dios anunció la última plaga, la más terrible de todas: esa noche morirían todos los primogénitos de Egipto.",
  [P("moises", 0.5, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", emocion="triste")],
  efectos=[{"tipo": "oscuridad", "fuerza": 0.5}, {"tipo": "rayo", "inicio": 0.7}], rotulo="CAPÍTULO 7: LA PASCUA", camara="acercar")
S("noche", "Pero Dios dio una instrucción a su pueblo: cada familia debía sacrificar un cordero y pintar con su sangre los marcos de sus puertas.",
  [P("hombre1", 0.35, accion="levantar"), P("oveja1", 0.6)], efectos=[{"tipo": "luz", "x": 0.35}], camara="acercar")
S("noche", "Esa noche cenaron de pie, con las sandalias puestas y listos para salir. A esta cena la llamaron la Pascua.",
  [P("hombre1", 0.3), P("mujer1", 0.5), P("nino", 0.68)], [{"tipo": "mesa", "x": 0.5}, {"tipo": "panes_peces", "x": 0.5, "y": -40}],
  camara="paneo")
S("noche", "A la medianoche, el ángel de la muerte pasó por Egipto. Pero cuando veía la sangre en una puerta, pasaba de largo.",
  [P("angel", 0.5, accion="caminar", hasta=0.7)], efectos=[{"tipo": "oscuridad", "fuerza": 0.55}, {"tipo": "brillo", "x": 0.5}], camara="paneo")
S("palacio", "En el palacio se escuchó un grito de dolor. Hasta el hijo del faraón había muerto.",
  [P("faraon", 0.5, accion="arrodillarse", emocion="llorando")], efectos=[{"tipo": "oscuridad", "fuerza": 0.4}], camara="acercar")
S("palacio", "Destrozado, el faraón llamó a Moisés en plena noche: ¡Váyanse! ¡Salgan de mi país, ustedes y todo su pueblo!",
  [P("faraon", 0.65, mira="izquierda", accion="senalar", emocion="llorando"), P("moises", 0.3, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a")],
  habla="faraon", camara="acercar_rapido")
S("cielo", "Siglos después, Jesús sería llamado el Cordero de Dios. Su sangre también nos protege y nos da libertad.",
  [P("jesus", 0.5, accion="ofrecer", emocion="feliz")], efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="acercar")

# ---------------- 8. EL MAR ROJO ----------------
S("desierto", "Y así, después de cuatrocientos treinta años, más de seiscientos mil hombres, con sus mujeres y niños, salieron de Egipto.",
  [P("moises", 0.3, hasta=0.6, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="caminar")],
  [gente(0.25, 0.65, hasta=0.5)], rotulo="CAPÍTULO 8: EL MAR ROJO", camara="paneo")
S("cielo", "De día, Dios los guiaba con una columna de nube. Y de noche, con una columna de fuego que les daba luz.",
  [P("moises", 0.35, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="alabar")],
  efectos=[{"tipo": "fuego", "x": 0.65, "tamano": 1.6}, {"tipo": "luz", "x": 0.65}], camara="acercar")
S("palacio", "Pero en Egipto, el faraón se arrepintió de haberlos dejado ir. ¿Quién va a trabajar para nosotros ahora?",
  [P("faraon", 0.5, accion="senalar", emocion="enojado")], [{"tipo": "trono", "x": 0.55, "profundidad": -30}], habla="faraon", camara="acercar")
S("egipto", "Reunió seiscientos carros de guerra y a todo su ejército, y salió a perseguirlos.",
  [P("faraon", 0.7, mira="izquierda", accion="senalar", emocion="enojado")], [gente(0.45, 0.75, variante="soldados", y=-130)],
  efectos=[{"tipo": "temblor", "inicio": 0.2, "fin": 0.9}], camara="paneo")
S("mar", "Los israelitas llegaron a la orilla del mar Rojo. Y al voltear, vieron al ejército egipcio acercándose. Estaban atrapados.",
  [P("hombre1", 0.3, accion="temblar", emocion="asustado"), P("mujer1", 0.6, mira="izquierda", accion="temblar", emocion="asustado")],
  [gente(0.5, 0.75, y=330, delante=True, profundidad=None)], camara="acercar_rapido")
S("mar", "¿No había tumbas en Egipto, que nos trajiste a morir al desierto?, le gritaban a Moisés.",
  [P("hombre1", 0.35, accion="senalar", emocion="enojado"), P("moises", 0.65, mira="izquierda", **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a")],
  habla="hombre1", camara="fijo")
S("mar", "Pero Moisés respondió: ¡No tengan miedo! Quédense quietos y vean la salvación que el Señor hará hoy por ustedes.",
  [P("moises", 0.5, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="senalar", emocion="valiente")],
  habla="moises", efectos=[{"tipo": "luz"}], camara="acercar")
S("mar_rojo", "Entonces Moisés extendió su vara sobre el mar...",
  [P("moises", 0.5, accion="levantar", profundidad=120, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a")],
  [gente(0.5, 0.8, y=330, profundidad=200)], efectos=[{"tipo": "abrir_mar", "inicio": 0.99, "fin": 1}], camara="acercar")
S("mar_rojo", "Y un viento fuerte sopló toda la noche. ¡Las aguas se dividieron como dos murallas, y apareció un camino de tierra seca en medio del mar!",
  [P("moises", 0.5, accion="levantar", profundidad=120, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a")],
  [gente(0.5, 0.8, y=330, profundidad=200)], efectos=[{"tipo": "abrir_mar", "inicio": 0.05, "fin": 0.7}, {"tipo": "temblor", "inicio": 0.1, "fin": 0.6}],
  camara="acercar_rapido", portada=False)
S("mar_rojo", "Todo el pueblo cruzó caminando entre las paredes de agua, sin mojarse los pies.",
  [], [gente(0.5, 0.45, y=0, sube=-250, profundidad=0)], camara="acercar")
S("mar_rojo", "Los egipcios entraron detrás de ellos. Pero cuando el último israelita llegó a la otra orilla, Moisés volvió a extender su mano...",
  [], [gente(0.5, 0.4, variante="soldados", y=80, sube=-120, profundidad=0)], camara="fijo")
S("mar_rojo", "Y las aguas se cerraron con un estruendo, cubriendo a todo el ejército del faraón.",
  [], efectos=[{"tipo": "cerrar_mar", "inicio": 0.1, "fin": 0.8}, {"tipo": "temblor", "inicio": 0.3, "fin": 0.7}, {"tipo": "flash", "inicio": 0.75}],
  camara="acercar_rapido")
S("valle", "Ese día el pueblo vio el gran poder de Dios. Miriam tomó una pandereta, y todas las mujeres cantaron y bailaron de alegría.",
  [P("miriam", 0.35, accion="celebrar", emocion="feliz", escala=1.0), P("mujer1", 0.55, accion="celebrar", emocion="feliz"),
   P("moises", 0.75, mira="izquierda", **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="alabar")],
  efectos=[{"tipo": "luz"}, {"tipo": "arcoiris"}], camara="paneo")

# ---------------- 9. EN EL DESIERTO ----------------
S("desierto", "Pero el viaje no fue fácil. En el desierto no había comida, y el pueblo comenzó a quejarse otra vez.",
  [P("hombre1", 0.4, accion="agacharse", emocion="triste"), P("mujer1", 0.6, emocion="triste")],
  rotulo="CAPÍTULO 9: EL DESIERTO", camara="acercar")
S("desierto", "Y Dios hizo llover pan del cielo. Cada mañana el suelo amanecía cubierto de maná, un pan dulce como la miel.",
  [P("nino", 0.4, accion="celebrar", emocion="feliz"), P("mujer1", 0.6, accion="agacharse", emocion="feliz")],
  [{"tipo": "panes_peces", "x": 0.5}], efectos=[{"tipo": "brillo"}, {"tipo": "luz"}], camara="acercar")
S("rocas", "Cuando tuvieron sed, Dios le dijo a Moisés que golpeara una roca. ¡Y de la roca brotó agua fresca para todos!",
  [P("moises", 0.35, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="levantar")],
  efectos=[{"tipo": "agua", "x": 0.6}, {"tipo": "flash", "inicio": 0.4}], camara="acercar_rapido")

# ---------------- 10. EL MONTE SINAI ----------------
S("montana", "Tres meses después, llegaron al monte Sinaí. Y el monte se llenó de humo, truenos y relámpagos, porque Dios descendió sobre él.",
  [], [gente(0.5, 0.65, y=250, profundidad=100)], efectos=[{"tipo": "rayo", "inicio": 0.2}, {"tipo": "rayo", "inicio": 0.65}, {"tipo": "temblor", "inicio": 0.2, "fin": 0.9}, {"tipo": "fuego", "x": 0.5, "y": -500, "tamano": 1.2}],
  rotulo="CAPÍTULO 10: LOS DIEZ MANDAMIENTOS", camara="alejar")
S("montana", "Moisés subió solo a la montaña, y allí Dios le entregó dos tablas de piedra con los Diez Mandamientos, escritos por su propio dedo.",
  [P("moises", 0.5, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="levantar")],
  efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -500}], camara="acercar")
S("montana", "Amarás a Dios sobre todas las cosas, honrarás a tu padre y a tu madre, no mentirás, no robarás... Leyes para vivir en amor con Dios y con los demás.",
  [P("moises", 0.5, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="ofrecer")], efectos=[{"tipo": "luz"}], camara="fijo")
S("valle", "Durante cuarenta años, Moisés guió al pueblo por el desierto, hasta llevarlos a las puertas de la tierra prometida.",
  [P("moises", 0.3, hasta=0.6, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="caminar")], [gente(0.2, 0.6, hasta=0.45)],
  camara="paneo")
S("montana", "Desde lo alto de un monte, ya anciano, Moisés pudo contemplar esa tierra hermosa que Dios había prometido a su pueblo.",
  [P("moises", 0.4, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", emocion="feliz")], efectos=[{"tipo": "luz", "x": 0.7}, {"tipo": "arcoiris"}],
  camara="alejar")

# ---------------- ENSEÑANZA Y FINAL ----------------
S("cielo", "Moisés fue el bebé que debía morir en el río, el príncipe que huyó, el pastor que tenía miedo de hablar.",
  [P("moises", 0.5, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="orar")], efectos=[{"tipo": "luz"}],
  rotulo="ENSEÑANZA", camara="acercar")
S("cielo", "Y aun así, Dios lo usó para liberar a millones de personas. Porque cuando Dios te llama, no importa tu pasado ni tus miedos.",
  [P("moises", 0.5, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="alabar", emocion="feliz")],
  efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], camara="fijo")
S("cielo", "¿Qué parte de la historia te gustó más: el bebé en el río, las plagas o el mar abierto? Escríbelo en los comentarios.",
  [P("moises", 0.35, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="senalar"), P("miriam", 0.65, mira="izquierda", accion="celebrar")],
  efectos=[{"tipo": "luz"}], camara="acercar")
S("cielo", "Y si te gustó este video, suscríbete y activa la campanita. Cada día hay una nueva historia de la Biblia. ¡Dios te bendiga!",
  [P("moises", 0.5, **VARA, **VIEJO, tocado="turbante", manto="#8a5a3a", accion="alabar", emocion="feliz")],
  efectos=[{"tipo": "luz"}, {"tipo": "brillo", "y": -600}], rotulo="¡SUSCRÍBETE!", pausa=2.0, camara="acercar")

for e in E:
    e.pop("fondo_override", None)
    for c in e.get("cosas", []):
        if c.get("profundidad", 0) is None:
            c.pop("profundidad")

historia = {
    "titulo": "Moisés - La Historia Completa",
    "gancho": "¿Cómo un BEBÉ abandonado en un río llegó a partir el MAR en dos?",
    "final": "",
    "formato": "horizontal",
    "voz_narrador": "es_MX-claude-high",
    "velocidad_narrador": 1.1,
    "pausa_escenas": 0.35,
    "corte_seg": 3.0,
    "musica": "auto",
    "volumen_musica": 0.1,
    "efectos_sonido": True,
    "barra_progreso": False,
    "resaltar": ["MOISÉS", "DIOS", "FARAÓN", "EGIPTO", "MAR", "PUEBLO", "PLAGA", "PASCUA", "CORDERO", "JESÚS", "COMENTARIOS", "SUSCRÍBETE"],
    "personajes": {
        "jocabed": {"tunica": "#7a5c8a", "tocado": "velo", "color_tocado": "#4a3a6a", "pelo": None, "voz": {"nombre": "es_AR-daniela-high"}},
        "miriam": {"tunica": "#d98a4a", "tocado": "velo", "color_tocado": "#b85a2a", "pelo": None, "escala": 0.8, "voz": {"nombre": "es_AR-daniela-high", "tono": 2}},
        "princesa": {"tunica": "#f4f1ea", "manto": "#3fa0a0", "tocado": "corona", "pelo": "#1a1410", "pelo_largo": True, "piel": "#c89a70", "voz": {"nombre": "es_AR-daniela-high", "tono": -1}},
        "aaron": {"tunica": "#5a6a9a", "manto": "#8a5a3a", "barba": "#cfcac0", "pelo": "#cfcac0", "tocado": "turbante", "color_tocado": "#e9e4d8"},
    },
    "escenas": E,
}
out = Path(__file__).resolve().parent.parent / "historias_largas" / "01_moises_la_historia_completa.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(historia, ensure_ascii=False, indent=1), encoding="utf-8")
w = sum(len(e["texto"].split()) for e in E)
print(f"{out.name}: {len(E)} escenas, {w} palabras, ~{w / 145:.1f} min")
