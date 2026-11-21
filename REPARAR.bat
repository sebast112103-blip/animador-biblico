@echo off
chcp 65001 >nul
title Reparando Animador Biblico
cd /d "%~dp0"
set "LOG=%~dp0reparar_log.txt"
echo Reparacion iniciada %date% %time% > "%LOG%"
set "PATH=%PATH%;%LOCALAPPDATA%\Microsoft\WinGet\Links;%LOCALAPPDATA%\Programs\Python\Python312;%LOCALAPPDATA%\Programs\Python\Python312\Scripts;%LOCALAPPDATA%\Programs\Python\Launcher"
set "PY="
py -3 --version >nul 2>nul && set "PY=py -3"
if not defined PY python --version >nul 2>nul && set "PY=python"
echo Python: %PY% >> "%LOG%"
echo ===== Instalando componente de Windows para Piper =====
%PY% -m pip install msvc-runtime >> "%LOG%" 2>&1
%PY% -c "import piper; print('PIPER OK')" >> "%LOG%" 2>&1
if errorlevel 1 (
  echo Instalando Visual C++ de Microsoft. Si Windows pregunta, responde SI.
  winget install -e --id Microsoft.VCRedist.2015+.x64 --accept-package-agreements --accept-source-agreements --silent >> "%LOG%" 2>&1
  %PY% -c "import piper; print('PIPER OK 2')" >> "%LOG%" 2>&1
)
echo ===== Prueba =====
%PY% -c "import animador, shutil; print('FFMPEG:', shutil.which('ffmpeg'))" >> "%LOG%" 2>&1
%PY% animador.py historias\02_david_y_goliat.json --vista >> "%LOG%" 2>&1
if errorlevel 1 (echo [ERROR] La prueba fallo >> "%LOG%") else (echo PRUEBA OK >> "%LOG%")
echo REPARACION TERMINADA >> "%LOG%"
echo ===== REPARACION TERMINADA =====
timeout /t 10
