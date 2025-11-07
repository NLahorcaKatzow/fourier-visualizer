@echo off
chcp 65001 >nul
echo.
echo ========================================
echo  Compilando Visualizador de Fourier
echo ========================================
echo.

REM Verificar si Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Error: Python no está instalado o no está en el PATH
    echo Por favor, instala Python desde https://www.python.org
    pause
    exit /b 1
)

echo ✓ Python detectado
echo.

REM Instalar dependencias
echo Instalando dependencias...
pip install -r requirements.txt
if errorlevel 1 (
    echo ❌ Error al instalar las dependencias
    pause
    exit /b 1
)

echo ✓ Dependencias instaladas
echo.

REM Crear ejecutable
echo Creando ejecutable...
pyinstaller --onefile --windowed --name "Visualizador Fourier" --icon=fourier_icon.ico fourier_app.py

if errorlevel 1 (
    echo ⚠️  Error al crear el ejecutable (posiblemente falte el ícono)
    echo Intentando sin ícono...
    pyinstaller --onefile --windowed --name "Visualizador Fourier" fourier_app.py
)

echo.
echo ========================================
echo ✅ ¡Compilación completada!
echo ========================================
echo.
echo El ejecutable se encuentra en: dist\Visualizador Fourier.exe
echo.
pause

