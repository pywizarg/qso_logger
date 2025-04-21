#!/bin/bash

# Verificar que se haya pasado un mensaje
if [ -z "$1" ]; then
  echo "Debes proporcionar un mensaje para el commit."
  exit 1
fi

# Agregar todos los cambios
git add .

# Hacer commit con el mensaje proporcionado
git commit -m "$1"

# Hacer push al repositorio remoto
git push origin main

echo "Cambios guardados y subidos exitosamente."
