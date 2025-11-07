# 🍎 Compilar para macOS

## Requisitos

```
macOS 10.14 (Mojave) o superior
Xcode Command Line Tools
Python 3.8 o superior
pip3
```

---

## Instalación Rápida

### Opción 1: Homebrew (Recomendado)

```bash
# 1. Instala Homebrew si no lo tienes
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# 2. Instala Python 3
brew install python3

# 3. Verifica
python3 --version
pip3 --version
```

### Opción 2: Desde python.org

```bash
# Descarga desde: https://www.python.org/downloads/macos/
# Instala haciendo doble clic en el instalador
# Verifica en terminal:
python3 --version
```

---

## Compilación

### Paso 1: Descargar o Clonar

```bash
# Opción A: Si tienes git
git clone <url_del_repo>
cd fourier-visualizer

# Opción B: Descargar ZIP
# 1. Descarga
# 2. Descomprime
# 3. Abre terminal en esa carpeta
```

### Paso 2: Instalar Dependencias

```bash
# Actualiza pip
pip3 install --upgrade pip

# Instala dependencias
pip3 install -r requirements.txt
```

### Paso 3: Compilar

```bash
# Opción A: Usar script (crea uno basado en build.sh)
chmod +x build.sh
./build.sh

# Opción B: Manual
pyinstaller --onefile --windowed --name "Visualizador_Fourier" fourier_app.py
```

### Paso 4: Encontrar el Ejecutable

```bash
# El ejecutable está en:
dist/Visualizador_Fourier

# Para ejecutar:
./dist/Visualizador_Fourier
```

---

## Crear App Bundle para macOS

Para crear una app nativa de macOS (.app):

```bash
# Opción mejorada de compilación
pyinstaller --onefile \
  --windowed \
  --name "Visualizador Fourier" \
  --icon=icono.icns \
  fourier_app.py
```

Esto crea: `dist/Visualizador Fourier.app`

---

## Código de Firma (Opcional pero Recomendado)

Si quieres distribuir:

```bash
# 1. Obtén certificado de desarrollador de Apple
# 2. Firma la app
codesign -s - ./dist/"Visualizador Fourier.app"

# 3. Verifica
codesign -v ./dist/"Visualizador Fourier.app"
```

---

## Crear Instalador DMG

Para distribución profesional:

```bash
# 1. Crea carpeta
mkdir -p dist/dmg
cp -r dist/"Visualizador Fourier.app" dist/dmg/

# 2. Crea symlink de Applications
ln -s /Applications dist/dmg/Applications

# 3. Crea DMG
hdiutil create -volname "Visualizador Fourier" \
  -srcfolder dist/dmg \
  -ov -format UDZO \
  dist/Visualizador_Fourier.dmg
```

---

## Ejecutar desde el Código Fuente

Si prefieres no compilar:

```bash
# Instala dependencias
pip3 install -r requirements.txt

# Ejecuta
python3 fourier_app.py
```

---

## Solución de Problemas

### ❌ "Python no encontrado"

```bash
# Instala Python 3
brew install python3

# O descarga de python.org
```

### ❌ "Gatekeeper bloquea la app"

```bash
# Abre la app
open ./dist/Visualizador_Fourier.app

# O en Preferencias de Seguridad: permite apps de desarrolladores desconocidos
```

### ❌ "El ícono no aparece"

```bash
# El icono por defecto de PyInstaller se usará
# Para un ícono personalizado, crea un archivo .icns y usa:
pyinstaller --icon=custom.icns ...
```

### ❌ "Errores de M1/M2 (Apple Silicon)"

```bash
# Asegúrate de usar Python universal
python3 -c "import platform; print(platform.machine())"
# Debería mostrar: arm64 (para M1/M2)

# Si tienes x86_64, instala versión ARM64 de Python
```

---

## Tips para macOS

💡 **Tip 1:** Crear alias en terminal

```bash
# Agrega a ~/.zprofile o ~/.bash_profile
alias fourier='~/path/to/Visualizador_Fourier'

# Luego:
fourier
```

💡 **Tip 2:** Crear acceso directo en Dock

```bash
# Abre Finder
# Navega a dist/Visualizador_Fourier.app
# Arrastra a Dock
```

💡 **Tip 3:** Automatizar con AppleScript

```applescript
# Crea un script que lance la app automáticamente
tell application "Visualizador Fourier" to activate
```

---

## Distribución en macOS

### Para Usuarios Locales

```bash
# Copia la app
cp -r dist/"Visualizador Fourier.app" ~/Applications/

# O crea DMG (ver arriba)
```

### Para Distribución General

1. Crea DMG (ver arriba)
2. Sube a servidor
3. Los usuarios descargan y abren

---

## Notarización de Apple (Para App Store)

```bash
# Para publicar en App Store, necesitas:
# 1. Developer Account de Apple
# 2. Certificado de firma
# 3. Notarización

xcrun altool --notarize-app \
  -f dist/Visualizador_Fourier.dmg \
  --primary-bundle-id com.tu-nombre.fourier \
  -u tu-email@apple.com \
  -p tu-password
```

---

## Requisitos Mínimos macOS

```
macOS 10.14+ (Mojave)
Para M1/M2: macOS 11.0+
512 MB RAM mínimo
200 MB espacio en disco
```

---

## Verificación Final

```bash
# 1. Verifica que se abre
./dist/Visualizador_Fourier

# 2. Prueba funcionalidades
# - Pan (click + arrastra)
# - Zoom (rueda)
# - Triggers (checkbox)

# 3. Cierra correctamente
# - Cmd+Q
```

---

## Comparación: Compilado vs Interpretado

| Aspecto | Compilado | Interpretado |
|--------|-----------|--------------|
| Tamaño | 70+ MB | - |
| Velocidad inicio | 3-5 seg | Más rápido |
| Instalación | Solo copiar | Necesita Python |
| Distribución | Fácil | Compleja |

---

## Conclusión

**En macOS:**
- ✅ Compilación sencilla con Homebrew
- ✅ Ejecutable nativo (.app)
- ✅ Distribución profesional (DMG)
- ✅ Compatible con M1/M2

**¡Funciona perfecto en macOS!** 🍎✨

---

Para más ayuda:
- Ver: `README.md`
- Ver: `COMPILAR_EN_LINUX.md` (pasos similares)

