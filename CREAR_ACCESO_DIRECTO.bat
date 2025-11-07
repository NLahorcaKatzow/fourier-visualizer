@echo off
chcp 65001 >nul
setlocal enabledelayedexpansion

echo.
echo ========================================
echo  Creando acceso directo en Escritorio
echo ========================================
echo.

REM Obtener ruta del usuario
for /f "tokens=*" %%a in ('echo %USERPROFILE%') do set userprofile=%%a

REM Definir rutas
set rutaApp=%cd%\dist\Visualizador Fourier.exe
set rutaEscritorio=!userprofile!\Desktop
set rutaAcceso=!rutaEscritorio!\Visualizador Fourier.lnk

REM Verificar que el exe existe
if not exist "%rutaApp%" (
    echo ❌ Error: No se encontró el ejecutable
    echo.
    echo Asegúrate de ejecutar build.bat primero
    pause
    exit /b 1
)

echo ✓ Ejecutable encontrado: %rutaApp%
echo.

REM Crear acceso directo usando PowerShell
echo Creando acceso directo en el escritorio...
echo.

powershell -Command "$WshShell = New-Object -ComObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%rutaAcceso%'); $Shortcut.TargetPath = '%rutaApp%'; $Shortcut.WorkingDirectory = '%cd%\dist'; $Shortcut.Description = 'Visualizador de Series de Fourier'; $Shortcut.Save()" 2>nul

if exist "%rutaAcceso%" (
    echo.
    echo ========================================
    echo ✅ ¡Acceso directo creado exitosamente!
    echo ========================================
    echo.
    echo Ubicación: %rutaEscritorio%\Visualizador Fourier.lnk
    echo.
    echo Ahora puedes hacer doble clic en el acceso directo del escritorio
    echo para abrir la aplicación rápidamente.
    echo.
) else (
    echo.
    echo ⚠️  No se pudo crear el acceso directo automáticamente
    echo.
    echo Alternativa manual:
    echo  1. Abre: dist\
    echo  2. Botón derecho en: Visualizador Fourier.exe
    echo  3. Selecciona: Enviar a ^> Escritorio ^(crear acceso directo^)
    echo.
)

pause

