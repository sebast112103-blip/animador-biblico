@echo off
chcp 65001 >nul
title Instalando Animador Biblico
cd /d "%~dp0"
set "LOG=%~dp0instalacion_log.txt"
echo Instalacion iniciada %date% %time% > "%LOG%"
set "PATH=%PATH%;%LOCALAPPDATA%\Microsoft\WinGet\Links;%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Python312\Scripts;%LOCALAPPDATA%\Programs\Python\Launcher"
set "PY="
py -3 --version >nul 2>nul && set "PY=py -3"
if not defined PY python --version >nul 2>nul && set "PY=python"
echo.
echo ===== 1/3 Python =====
if defined PY (
  echo Python ya esta instalado.
) else (
  echo Instalando Python 3.12... puede tardar unos minutos.
  winget install -e --id Python.Python.3.12 --scope user --accept-package-agreements --accept-source-agreements --silent >> "%LOG%" 2>&1
  py -3 --version >nul 2>nul && set "PY=py -3"
  if not defined PY if exist "%LOCALAPPDATA%\Programs\Python\Python312\python.exe" set "PY=%LOCALAPPDATA%\Programs\Python\Python312\python.exe"
)
if not defined PY (
  echo [ERROR] No se pudo instalar Python. >> "%LOG%"
  echo [ERROR] No se pudo instalar Python. Revisa instalacion_log.txt
  goto fin
)
echo Python: %PY% >> "%LOG%"
echo.
echo ===== 2/3 ffmpeg =====
ffmpeg -version >nul 2>nul
if errorlevel 1 (
  echo Instalando ffmpeg... puede tardar unos minutos.
  winget install -e --id Gyan.FFmpeg --accept-package-agreements --accept-source-agreements --silent >> "%LOG%" 2>&1
) else (
  echo ffmpeg ya esta instalado.
)
ffmpeg -version >nul 2>nul
if errorlevel 1 (echo [ERROR] ffmpeg no quedo disponible >> "%LOG%") else (echo ffmpeg OK >> "%LOG%")
echo.
echo ===== 3/3 Librerias (Piper, Pillow, NumPy) =====
%PY% -m pip install --upgrade pip >> "%LOG%" 2>&1
%PY% -m pip install -r requirements.txt >> "%LOG%" 2>&1
if errorlevel 1 (
  echo [ERROR] Fallo la instalacion de librerias >> "%LOG%"
  echo [ERROR] Fallo la instalacion de librerias. Revisa instalacion_log.txt
  goto fin
)
%PY% -c "import piper, PIL, numpy; print('LIBRERIAS OK')" >> "%LOG%" 2>&1
echo.
echo ===== Prueba rapida =====
%PY% animador.py historias\02_david_y_goliat.json --vista >> "%LOG%" 2>&1
if errorlevel 1 (echo [ERROR] La prueba fallo >> "%LOG%") else (echo PRUEBA OK >> "%LOG%")
echo INSTALACION TERMINADA >> "%LOG%"
echo.
echo ===== INSTALACION TERMINADA =====
:fin
echo Fin %date% %time% >> "%LOG%"
timeout /t 15
