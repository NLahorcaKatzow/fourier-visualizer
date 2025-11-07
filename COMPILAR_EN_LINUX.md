# 🐧 Compilar para Linux

## Requisitos Previos

### Distribuciones Soportadas

✅ Ubuntu 20.04+
✅ Debian 10+
✅ Fedora 33+
✅ CentOS 8+
✅ Arch Linux
✅ macOS 10.14+
✅ Otras distribuciones con Python 3.8+

### Requisitos del Sistema

```
Python 3.8 o superior
pip3 (gestor de paquetes Python)
git (opcional, para clonar el repo)
~500 MB de espacio en disco
```

---

## Instalación de Dependencias

### Ubuntu/Debian

```bash
# Actualizar lista de paquetes
sudo apt update

# Instalar Python 3 y pip
sudo apt install python3 python3-pip

# Instalar dependencias del sistema (para PyQt6)
sudo apt install python3-dev libgl1-mesa-glx libxkbcommon-x11-0

# Para gráficas (opcional, pero recomendado)
sudo apt install python3-tk
```

### Fedora/RHEL/CentOS

```bash
# Instalar Python 3 y pip
sudo dnf install python3 python3-pip

# Instalar dependencias del sistema
sudo dnf install python3-devel mesa-libGL libxkbcommon-x11
```

### Arch Linux

```bash
# Instalar Python y pip
sudo pacman -S python python-pip

# Instalar dependencias
sudo pacman -S base-devel mesa
```

### macOS

```bash
# Instalar Homebrew si no lo tienes
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Python 3
brew install python3

# pip3 se instala con Python 3 automáticamente
```

---

## Compilación Paso a Paso

### Opción 1: Usar el Script (Recomendado)

```bash
# 1. Navega a la carpeta del proyecto
cd ~/ruta/a/fourier-visualizer

# 2. Dale permisos de ejecución al script
chmod +x build.sh

# 3. Ejecuta el script
./build.sh

# 4. El ejecutable estará en:
# dist/Visualizador_Fourier
```

### Opción 2: Manual (Paso a Paso)

```bash
# 1. Navega a la carpeta
cd ~/ruta/a/fourier-visualizer

# 2. Instala pip (si no lo tienes)
sudo apt install python3-pip  # Ubuntu/Debian
sudo dnf install python3-pip  # Fedora
sudo pacman -S python-pip     # Arch

# 3. Instala las dependencias
pip3 install -r requirements.txt

# 4. Compila con PyInstaller
pyinstaller --onefile --windowed --name "Visualizador_Fourier" fourier_app.py

# 5. El ejecutable estará en:
# dist/Visualizador_Fourier
```

---

## Ejecutar la Aplicación

### Después de Compilar

```bash
# Opción 1: Desde la carpeta
./dist/Visualizador_Fourier

# Opción 2: Crear un alias (opcional)
alias fourier='~/ruta/a/fourier-visualizer/dist/Visualizador_Fourier'
fourier

# Opción 3: Crear un lanzador (opcional)
# Ver sección "Crear Lanzador" más abajo
```

---

## Crear Lanzador de Escritorio (Opcional)

### Para GNOME/Ubuntu

```bash
# 1. Crea el archivo del lanzador
nano ~/.local/share/applications/fourier.desktop

# 2. Copia el contenido de abajo y pega (Ctrl+O, Enter, Ctrl+X)
# Reemplaza /ruta/al/fourier con tu ruta real

[Desktop Entry]
Version=1.0
Type=Application
Name=Visualizador Fourier
Comment=Visualiza Series de Fourier
Exec=/ruta/al/fourier/dist/Visualizador_Fourier
Icon=utilities-terminal
Terminal=false
Categories=Education;Science;Mathematics;

# 3. Guarda (Ctrl+O, Enter)
# 4. Sale (Ctrl+X)

# 5. Ahora debería aparecer en tu menú de aplicaciones
```

### Para KDE/Fedora

```bash
# Similar a GNOME, pero la ruta es:
~/.config/share/applications/fourier.desktop
```

### Para Arch/i3/openbox

```bash
# Coloca el archivo en:
~/.local/share/applications/fourier.desktop
```

---

## Solución de Problemas

### ❌ "Python no encontrado"

```bash
# Verifica que Python 3 está instalado
python3 --version

# Si no funciona, instálalo:
sudo apt install python3  # Ubuntu/Debian
sudo dnf install python3  # Fedora
```

### ❌ "pip3 no encontrado"

```bash
# Instala pip3
sudo apt install python3-pip  # Ubuntu/Debian
sudo dnf install python3-pip  # Fedora
```

### ❌ "Error: ModuleNotFoundError"

```bash
# Asegúrate de instalar requirements.txt
pip3 install -r requirements.txt

# Si persiste, intenta actualizar pip
pip3 install --upgrade pip
```

### ❌ "Error de PyQt6"

```bash
# Instala dependencias del sistema
sudo apt install libgl1-mesa-glx libxkbcommon-x11-0  # Ubuntu/Debian
sudo dnf install mesa-libGL libxkbcommon-x11         # Fedora
```

### ❌ "La app no se abre"

```bash
# Verifica permisos
chmod +x dist/Visualizador_Fourier

# Ejecuta desde terminal para ver errores
./dist/Visualizador_Fourier
```

### ❌ "Error: Build failed"

```bash
# Limpia y recompila
rm -rf build dist *.spec

# Actualiza PyInstaller
pip3 install --upgrade pyinstaller

# Recompila
python3 -m pyinstaller --onefile --windowed --name "Visualizador_Fourier" fourier_app.py
```

---

## Ejecutar Desde el Código Fuente

Si no quieres compilar, puedes ejecutar directamente:

```bash
# Instala dependencias
pip3 install -r requirements.txt

# Ejecuta directamente
python3 fourier_app.py
```

**Ventajas:**
- Más rápido
- No requiere compilación
- Puedes editar el código

**Desventajas:**
- Necesita Python instalado
- Más lento al iniciar
- No es un ejecutable

---

## Distribución

### Compartir Ejecutable

```bash
# El ejecutable está en:
dist/Visualizador_Fourier

# Puedes:
# 1. Copiarlo a otros usuarios (misma distro)
# 2. Comprimir: tar -czf Visualizador_Fourier.tar.gz dist/
# 3. Compartir por email, USB, etc.

# Para ejecutar en otra máquina:
./Visualizador_Fourier
```

### Crear Paquete Instalable (Avanzado)

Para distribuciones específicas, puedes crear:
- `.deb` para Debian/Ubuntu
- `.rpm` para Fedora/RHEL
- AUR para Arch Linux

Consulta la documentación de PyInstaller y empaquetadores para tu distribución.

---

## Compilación Multi-Plataforma

### Desde Windows para Linux

```bash
# Usando WSL 2 (Windows Subsystem for Linux)
# 1. Instala WSL 2 en Windows
# 2. Instala una distribución Linux (ej: Ubuntu)
# 3. Sigue los pasos de compilación normales en WSL

# Desde PowerShell:
wsl

# Luego en WSL:
cd /mnt/c/Users/usuario/Documents/fourier-visualizer
./build.sh
```

### Desde Linux para Windows

No es posible compilar para Windows desde Linux fácilmente con PyInstaller.
Solución: Usa la rama de Windows o compila en Windows.

### Desde Linux para macOS

Difícil sin macOS físico. Opción: Compila en macOS.

---

## Tamaño y Rendimiento

### Tamaño del Ejecutable

```
Linux (sin comprimir): ~70-80 MB
Linux (comprimido):    ~20-30 MB
```

### Rendimiento

Esperado igual que en Windows:
- Carga: 3-5 segundos
- Interactividad: tiempo real
- Memoria: ~200-300 MB en uso

---

## Actualizar la Aplicación

Para actualizar a una nueva versión:

```bash
# Descarga/obtén la nueva versión
cd ~/ruta/nueva

# Compila
chmod +x build.sh
./build.sh

# El nuevo ejecutable está en dist/
```

---

## Crear Script de Actualización Automática

```bash
#!/bin/bash
# update_fourier.sh

echo "Actualizando Visualizador de Fourier..."

# Descarga actualización (ejemplo con git)
git pull origin main

# Recompila
./build.sh

echo "✅ Actualización completada"
./dist/Visualizador_Fourier
```

---

## Soporte Multi-Usuario

Para instalar para todos los usuarios:

```bash
# Copia el ejecutable a /usr/local/bin
sudo cp dist/Visualizador_Fourier /usr/local/bin/

# Ahora cualquiera puede ejecutar desde terminal
Visualizador_Fourier

# O copiar el .desktop a compartido
sudo cp fourier.desktop /usr/share/applications/
```

---

## Tips Finales

💡 **Tip 1:** Compila en la misma distro donde usarás
```
Ubuntu → compila en Ubuntu
Fedora → compila en Fedora
```

💡 **Tip 2:** Crea un alias para facilitar
```bash
alias fourier='~/path/to/dist/Visualizador_Fourier'
```

💡 **Tip 3:** Usa pantalla de inicio customizada
```bash
# En el .desktop:
Icon=/ruta/a/icono.png
```

💡 **Tip 4:** Crea un launcher con temas
```bash
# El lanzador hereda temas del sistema
```

---

## Conclusión

**En Linux tienes varias opciones:**

1. ✅ **Compilar** (recomendado para distribución)
2. ✅ **Ejecutar desde código** (rápido para desarrollo)
3. ✅ **Crear lanzador** (para comodidad)

**Todo funciona perfectamente en Linux** 🐧✨

---

Para más ayuda:
- Ver: `README.md`
- Ver: `LEEME_PRIMERO.txt`
- Terminal: `./dist/Visualizador_Fourier --help`

