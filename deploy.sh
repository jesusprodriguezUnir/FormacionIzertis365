#!/bin/bash
# Script para publicar en GitHub

# Variables
GITHUB_USER="tu_usuario_github"
REPO_NAME="FormacionIzertis365"

# Agregar remote
git remote add origin https://github.com/$GITHUB_USER/$REPO_NAME.git

# Renombrar rama a main (opcional pero recomendado)
git branch -M main

# Push al repositorio
git push -u origin main

echo "✓ Repositorio publicado en: https://github.com/$GITHUB_USER/$REPO_NAME"
