#!/bin/bash

#Borrar de manera recursiva los ficheros inutiles.

echo Directorio Raiz: $PWD
echo Procesando...

find $PWD -name '*.pyc' -delete

echo Listo!