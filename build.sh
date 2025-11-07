#!/bin/bash

# Script de compilación para Linux
# Visualizador de Series de Fourier v3.1

echo "=========================================="
echo "  Compilando para Linux"
echo "  Visualizador de Fourier v3.1"
echo "=========================================="
echo ""

# Verificar si Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 no está instalado"
    echo "Por favor, instala Python 3.8 o superior"
    echo ""
    echo "En Ubuntu/Debian:"
    echo "  sudo apt update"
    echo "  sudo apt install python3 python3-pip"
    echo ""
    echo "En Fedora/RHEL:"
    echo "  sudo dnf install python3 python3-pip"
    echo ""
    echo "En macOS:"
    echo "  brew install python3"
    exit 1
fi

echo "✓ Python detectado: $(python3 --version)"
echo ""

# Verificar pip
if ! command -v pip3 &> /dev/null; then
    echo "❌ Error: pip3 no está instalado"
    echo "Instálalo con: sudo apt install python3-pip"
    exit 1
fi

echo "✓ pip3 detectado"
echo ""

# Instalar dependencias
echo "Instalando dependencias..."
pip3 install --upgrade pip setuptools wheel

echo ""
echo "Instalando paquetes requeridos..."
pip3 install -r requirements.txt

if [ $? -ne 0 ]; then
    echo "❌ Error al instalar dependencias"
    exit 1
fi

echo "✓ Dependencias instaladas"
echo ""

# Crear ejecutable
echo "Compilando aplicación..."
pyinstaller --onefile --windowed --name "Visualizador_Fourier" fourier_app.py

if [ $? -ne 0 ]; then
    echo "❌ Error al compilar"
    exit 1
fi

echo ""
echo "=========================================="
echo "✅ ¡Compilación completada!"
echo "=========================================="
echo ""
echo "El ejecutable se encuentra en:"
echo "  dist/Visualizador_Fourier"
echo ""
echo "Para ejecutar:"
echo "  ./dist/Visualizador_Fourier"
echo ""
echo "O simplemente:"
echo "  ./dist/Visualizador_Fourier"
echo ""

