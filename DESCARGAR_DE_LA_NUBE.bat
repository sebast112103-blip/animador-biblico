@echo off
chcp 65001 >nul
title Descargar videos de la nube (GitHub)
cd /d "%~dp0"
set "PATH=%PATH%;C:\Program Files\Git\cmd;%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Launcher"
set "PY="
py -3 --version >nul 2>nul && set "PY=py -3"
if not defined PY python --version >nul 2>nul && set "PY=python"
%PY% nube_github.py descargar
echo.
pause
