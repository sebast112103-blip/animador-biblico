@echo off
chcp 65001 >nul
cd /d "%~dp0"
REM Arrastra el archivo .json de la historia encima de este archivo.
if "%~1"=="" (
  echo Arrastra el archivo .json de la historia encima de este archivo.
  pause
  exit /b
)
set "PATH=%PATH%;%LOCALAPPDATA%\Microsoft\WinGet\Links;%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Python312\Scripts;%LOCALAPPDATA%\Programs\Python\Launcher"
set "PY="
py -3 --version >nul 2>nul && set "PY=py -3"
if not defined PY python --version >nul 2>nul && set "PY=python"
if not defined PY (
  echo Falta Python. Haz doble clic en INSTALAR.bat primero.
  pause
  exit /b
)
%PY% animador.py "%~1"
pause
