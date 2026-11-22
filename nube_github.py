#!/usr/bin/env python3
"""
NUBE GITHUB - sube el proyecto a GitHub, crea los videos alla y los descarga.

Uso (lo hacen los archivos .bat):
    python nube_github.py todo [cortos|largos|todos]   -> subir + crear + esperar + descargar
    python nube_github.py crear [cortos|largos|todos] [filtro]
    python nube_github.py descargar                     -> descarga los videos de la ultima ejecucion

La primera vez se abre una ventana de GitHub para iniciar sesion (la abre Git).
El programa nunca muestra ni guarda tu clave: la maneja el administrador de
credenciales de Git/Windows.
"""
import calendar
import io
import json
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
import zipfile
from pathlib import Path

for _f in (sys.stdout, sys.stderr):
    try:
        _f.reconfigure(errors="replace")
    except Exception:
        pass

RAIZ = Path(__file__).resolve().parent
REPO = "animador-biblico"
API = "https://api.github.com"
LOG = RAIZ / "github_log.txt"
PUBLICO = True   # publico = minutos y almacenamiento gratis ilimitados en GitHub Actions


def log(msg):
    print(msg, flush=True)
    with open(LOG, "a", encoding="utf-8") as f:
        f.write(time.strftime("%H:%M:%S ") + msg + "\n")


def git(*args, check=True):
    r = subprocess.run(["git", *args], cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if check and r.returncode != 0:
        log(f"[ERROR] git {' '.join(args)}: {r.stderr.strip()[-400:]}")
        sys.exit(1)
    return r.stdout.strip()


def credenciales():
    """Pide a Git las credenciales de github.com (abre la ventana de inicio de sesion si hace falta)."""
    log("Conectando con tu cuenta de GitHub (si se abre una ventana, inicia sesion y autoriza)...")
    r = subprocess.run(["git", "credential", "fill"], input="protocol=https\nhost=github.com\n\n",
                       capture_output=True, text=True, cwd=RAIZ)
    datos = dict(l.split("=", 1) for l in r.stdout.splitlines() if "=" in l)
    if not datos.get("password"):
        log("[ERROR] No se pudo iniciar sesion en GitHub.")
        sys.exit(1)
    # guardar para la proxima vez
    entrada = "".join(f"{k}={v}\n" for k, v in datos.items()) + "\n"
    subprocess.run(["git", "credential", "approve"], input=entrada, capture_output=True, text=True, cwd=RAIZ)
    return datos["password"]


def api(token, metodo, ruta, datos=None, aceptar=(200, 201, 204)):
    url = ruta if ruta.startswith("http") else API + ruta
    req = urllib.request.Request(url, method=metodo,
                                 data=json.dumps(datos).encode() if datos is not None else None)
    req.add_unredirected_header("Authorization", f"Bearer {token}")
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("X-GitHub-Api-Version", "2022-11-28")
    req.add_header("User-Agent", "animador-biblico")
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            cuerpo = r.read()
            return r.status, (json.loads(cuerpo) if cuerpo and r.headers.get_content_type() == "application/json" else cuerpo)
    except urllib.error.HTTPError as e:
        cuerpo = e.read().decode("utf-8", "replace")
        if e.code in aceptar:
            return e.code, cuerpo
        return e.code, cuerpo


def usuario(token):
    st, u = api(token, "GET", "/user")
    if st != 200:
        log(f"[ERROR] GitHub no acepto la sesion ({st}).")
        sys.exit(1)
    return u["login"]


def crear_repo(token, login):
    st, r = api(token, "GET", f"/repos/{login}/{REPO}")
    if st == 200:
        log(f"El repositorio {login}/{REPO} ya existe.")
        return
    st, r = api(token, "POST", "/user/repos", {
        "name": REPO, "private": not PUBLICO, "auto_init": False,
        "description": "Animador biblico 2D: historias de la Biblia en video para redes sociales"})
    if st not in (201,):
        log(f"[ERROR] No se pudo crear el repositorio ({st}): {str(r)[:300]}")
        sys.exit(1)
    log(f"Repositorio creado: https://github.com/{login}/{REPO}")


def subir(login):
    wf = RAIZ / ".github" / "workflows"
    wf.mkdir(parents=True, exist_ok=True)
    origen = RAIZ / "flujo_github" / "crear_videos.yml"
    if origen.exists():
        shutil.copy(origen, wf / "crear_videos.yml")
    if not (RAIZ / ".git").exists():
        git("init", "-b", "main")
    git("config", "user.name", login)
    git("config", "user.email", f"{login}@users.noreply.github.com")
    url = f"https://github.com/{login}/{REPO}.git"
    remotos = git("remote", check=False).split()
    if "origin" in remotos:
        git("remote", "set-url", "origin", url)
    else:
        git("remote", "add", "origin", url)
    git("add", "-A")
    if git("status", "--porcelain", check=False):
        git("commit", "-m", "Actualizar animador biblico")
    else:
        git("commit", "--allow-empty", "-m", "Animador biblico", check=False)
    log("Subiendo el proyecto a GitHub...")
    git("push", "-u", "origin", "main")
    log("Proyecto subido.")


def cancelar_pendientes(token, login):
    for estado in ("queued", "in_progress"):
        st, r = api(token, "GET", f"/repos/{login}/{REPO}/actions/runs?status={estado}&per_page=50")
        for run in (r.get("workflow_runs", []) if st == 200 else []):
            api(token, "POST", f"/repos/{login}/{REPO}/actions/runs/{run['id']}/cancel")
            log(f"Cancelada la ejecucion anterior #{run['run_number']}.")


def lanzar(token, login, carpeta, filtro=""):
    previa = ultima_ejecucion(token, login)
    previa_id = previa["id"] if previa else None
    ruta = f"/repos/{login}/{REPO}/actions/workflows/crear_videos.yml/dispatches"
    for intento in range(12):   # GitHub tarda unos segundos en registrar el flujo nuevo
        st, r = api(token, "POST", ruta, {"ref": "main", "inputs": {"carpeta": carpeta, "filtro": filtro}})
        if st == 204:
            log(f"Creacion de videos lanzada en la nube ({carpeta}).")
            return previa_id
        time.sleep(10)
    log(f"[ERROR] No se pudo lanzar la creacion ({st}): {str(r)[:300]}")
    sys.exit(1)


def ultima_ejecucion(token, login):
    st, r = api(token, "GET", f"/repos/{login}/{REPO}/actions/workflows/crear_videos.yml/runs?event=workflow_dispatch&per_page=1")
    if st == 200 and r.get("workflow_runs"):
        return r["workflow_runs"][0]
    return None


def esperar(token, login, previa_id="no-filtrar"):
    """Sigue la ejecucion mas nueva (si previa_id se da, espera una distinta a esa)."""
    log("Esperando a que GitHub cree los videos (revisa cada minuto)...")
    run = None
    for _ in range(30):
        run = ultima_ejecucion(token, login)
        if run and (previa_id == "no-filtrar" or run["id"] != previa_id):
            break
        run = None
        time.sleep(10)
    if not run:
        log("[ERROR] No encontre la ejecucion en GitHub.")
        sys.exit(1)
    log(f"Puedes verla aqui: {run['html_url']}")
    ultimo = ""
    while True:
        st, run = api(token, "GET", f"/repos/{login}/{REPO}/actions/runs/{run['id']}")
        hechos = total = 0
        pagina = 1
        while True:
            st2, j = api(token, "GET", f"/repos/{login}/{REPO}/actions/runs/{run['id']}/jobs?per_page=100&page={pagina}")
            if st2 != 200:
                break
            trabajos = [x for x in j.get("jobs", []) if x["name"].startswith("video")]
            total += len(trabajos)
            hechos += sum(1 for x in trabajos if x["status"] == "completed")
            if len(j.get("jobs", [])) < 100:
                break
            pagina += 1
        estado = f"  {hechos}/{total} videos terminados ({run['status']})"
        if estado != ultimo:
            log(estado)
            ultimo = estado
        if run["status"] == "completed":
            log(f"GitHub termino: {run['conclusion']}")
            return run
        time.sleep(60)


class ZipRemoto(io.RawIOBase):
    """Lee el zip de GitHub por partes (sin guardarlo entero en el disco)."""
    BLOQUE = 8 << 20

    def __init__(self, token, url_api, tam):
        self.token, self.url_api, self.tam = token, url_api, tam
        self.pos, self.buf_ini, self.buf = 0, 0, b""
        self.url = None

    def _enlace(self):
        # GitHub da un enlace temporal (dura poco): se pide de nuevo cuando caduca
        req = urllib.request.Request(self.url_api)
        req.add_unredirected_header("Authorization", f"Bearer {self.token}")
        req.add_header("User-Agent", "animador-biblico")
        req.add_header("Range", "bytes=0-0")
        with urllib.request.urlopen(req, timeout=120) as r:
            self.url = r.geturl()

    def _traer(self, ini, fin):
        for intento in range(6):
            try:
                if not self.url:
                    self._enlace()
                req = urllib.request.Request(self.url)
                req.add_header("Range", f"bytes={ini}-{fin - 1}")
                req.add_header("User-Agent", "animador-biblico")
                with urllib.request.urlopen(req, timeout=300) as r:
                    datos = r.read()
                if r.status == 206 and len(datos) == fin - ini:
                    return datos
                raise IOError(f"respuesta inesperada {r.status}")
            except Exception as ex:
                self.url = None
                if intento == 5:
                    raise
                time.sleep(3 + intento * 3)

    def readable(self):
        return True

    def seekable(self):
        return True

    def tell(self):
        return self.pos

    def seek(self, off, desde=0):
        self.pos = {0: off, 1: self.pos + off, 2: self.tam + off}[desde]
        return self.pos

    def read(self, n=-1):
        if n is None or n < 0:
            n = self.tam - self.pos
        n = min(n, self.tam - self.pos)
        if n <= 0:
            return b""
        fin_buf = self.buf_ini + len(self.buf)
        if not (self.buf_ini <= self.pos and self.pos + n <= fin_buf):
            ini = self.pos
            fin = min(self.tam, ini + max(n, self.BLOQUE))
            self.buf, self.buf_ini = self._traer(ini, fin), ini
        k = self.pos - self.buf_ini
        self.pos += n
        return self.buf[k:k + n]

    def readinto(self, b):
        d = self.read(len(b))
        b[:len(d)] = d
        return len(d)


def descargar(token, login, run=None):
    run = run or ultima_ejecucion(token, login)
    if not run:
        log("[ERROR] No hay ejecuciones en GitHub todavia.")
        sys.exit(1)
    st, r = api(token, "GET", f"/repos/{login}/{REPO}/actions/runs/{run['id']}/artifacts?per_page=100")
    arts = [a for a in r.get("artifacts", []) if a["name"] == "TODOS_LOS_VIDEOS"] if st == 200 else []
    if not arts:
        log("[ERROR] Esa ejecucion no tiene videos para descargar todavia.")
        sys.exit(1)
    # restos de descargas viejas (zip temporal que antes se guardaba entero)
    viejo = RAIZ / "videos" / "_nube.zip"
    if viejo.exists():
        viejo.unlink()
        log("Borre el archivo temporal de una descarga anterior (_nube.zip).")
    remoto = ZipRemoto(token, arts[0]["archive_download_url"], arts[0]["size_in_bytes"])
    with zipfile.ZipFile(io.BufferedReader(remoto, 1 << 20)) as z:
        nombres = z.namelist()
        tipo = z.read("_youtube.txt").decode().strip() if "_youtube.txt" in nombres else "nube"
        destino = RAIZ / "videos" / {"youtube": "youtube", "diario": "diarios"}.get(tipo, "nube")
        destino.mkdir(parents=True, exist_ok=True)
        miembros = [m for m in z.infolist() if not m.is_dir() and m.filename != "_youtube.txt"]
        faltan = [m for m in miembros
                  if not ((destino / m.filename).exists() and (destino / m.filename).stat().st_size == m.file_size)]
        necesita = sum(m.file_size for m in faltan)
        libre = shutil.disk_usage(destino).free
        log(f"Videos: {len(miembros)} ({len(miembros) - len(faltan)} ya estaban). "
            f"Por bajar: {necesita / 1e6:.0f} MB. Espacio libre en el disco: {libre / 1e6:.0f} MB.")
        if necesita + 50e6 > libre:
            log(f"[ERROR] No hay espacio suficiente en el disco. Libera al menos "
                f"{(necesita + 50e6 - libre) / 1e6:.0f} MB (vacia la Papelera, borra descargas viejas) y vuelve a intentar.")
            sys.exit(1)
        for i, m in enumerate(faltan, 1):
            log(f"  [{i}/{len(faltan)}] {m.filename} ({m.file_size / 1e6:.0f} MB)")
            tmp = destino / (m.filename + ".parcial")
            with z.open(m) as fuente, open(tmp, "wb") as f:
                shutil.copyfileobj(fuente, f, 1 << 20)
            tmp.replace(destino / m.filename)
    n = len(list(destino.glob("*.mp4")))
    log(f"LISTO: {n} videos en {destino}")


def main():
    accion = sys.argv[1] if len(sys.argv) > 1 else "todo"
    carpeta = sys.argv[2] if len(sys.argv) > 2 else "todos"
    filtro = sys.argv[3] if len(sys.argv) > 3 else ""
    if carpeta == "diario" and not filtro:
        # solo el siguiente video largo que todavia no se ha creado
        import re as _re
        # pendientes = historias largas que todavia no se han subido a YouTube
        pub = RAIZ / "historias_largas" / "_publicados.txt"
        hechos = set(pub.read_text(encoding="utf-8").split()) if pub.exists() else set()
        pendientes = []
        for f in sorted((RAIZ / "historias_largas").glob("*.json")):
            t = json.loads(f.read_text(encoding="utf-8")).get("titulo") or f.stem
            if _re.sub(r"[^\w-]+", "_", t).strip("_") not in hechos:
                pendientes.append(f.name.lower())
                log(f"Video pendiente: {t}")
        filtro = ",".join(pendientes)
        if not pendientes:
            log("Todos los videos largos ya estan creados. Pideme nuevas historias.")
            sys.exit(0)
    if shutil.which("git") is None:
        log("[ERROR] No encuentro Git. Instala Git para Windows: https://git-scm.com")
        sys.exit(1)
    token = credenciales()
    login = usuario(token)
    log(f"Sesion iniciada como: {login}")
    if accion == "todo":
        crear_repo(token, login)
        subir(login)
        t = lanzar(token, login, carpeta, filtro)
        run = esperar(token, login, t)
        descargar(token, login, run)
    elif accion == "subir":
        crear_repo(token, login)
        subir(login)
    elif accion == "crear":
        cancelar_pendientes(token, login)
        subir(login)
        t = lanzar(token, login, carpeta, filtro)
        run = esperar(token, login, t)
        if carpeta == "diario":
            # los videos largos quedan en GitHub (rama "publicar") y Claude los sube a YouTube:
            # no hace falta llenar el disco de la computadora
            log("LISTO: los videos del dia quedaron en GitHub, listos para subir a YouTube.")
        else:
            descargar(token, login, run)
    elif accion == "descargar":
        run = esperar(token, login)   # si todavia esta trabajando, espera; luego descarga
        descargar(token, login, run)
    else:
        print(__doc__)


if __name__ == "__main__":
    main()
