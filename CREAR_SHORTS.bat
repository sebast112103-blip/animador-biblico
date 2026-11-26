@echo off
chcp 65001 >nul
title Crear los Shorts en la nube (GitHub)
cd /d "%~dp0"
set "PATH=%PATH%;C:\Program Files\Git\cmd;%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Launcher"
set "PY="
py -3 --version >nul 2>nul && set "PY=py -3"
if not defined PY python --version >nul 2>nul && set "PY=python"
REM Crea en GitHub los Shorts de la carpeta historias_shorts
%PY% nube_github.py crear shorts
echo.
pause
