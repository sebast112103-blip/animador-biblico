@echo off
chcp 65001 >nul
title Creando videos - Animador Biblico
cd /d "%~dp0"
REM Crea los videos de TODAS las historias de la carpeta "historias" que aun no tengan video.
set "PATH=%PATH%;%LOCALAPPDATA%\Microsoft\WinGet\Links;%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Python312\Scripts;%LOCALAPPDATA%\Programs\Python\Launcher"
set "PY="
py -3 --version >nul 2>nul && set "PY=py -3"
if not defined PY python --version >nul 2>nul && set "PY=python"
if not defined PY (
  echo Falta Python. Haz doble clic en INSTALAR.bat primero.
  pause
  exit /b
)
%PY% animador.py --todas
echo.
echo ===== LISTO: revisa la carpeta "videos" =====
pause
