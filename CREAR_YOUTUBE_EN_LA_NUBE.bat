@echo off
chcp 65001 >nul
title Crear videos para YouTube en la nube (GitHub)
cd /d "%~dp0"
set "PATH=%PATH%;C:\Program Files\Git\cmd;%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Launcher"
set "PY="
py -3 --version >nul 2>nul && set "PY=py -3"
if not defined PY python --version >nul 2>nul && set "PY=python"
REM 1) Prepara las historias horizontales y las recopilaciones
%PY% construir_youtube.py
REM 2) Las sube a GitHub, crea los videos y las recopilaciones, y los descarga en videos\youtube
%PY% nube_github.py crear youtube
echo.
pause
