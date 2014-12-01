#!/bin/bash

# Descargar programas necesarios
apt-get install -y python
apt-get install -y curl
apt-get install -y wget
apt-get install -y zip
apt-get install -y git

if [ ! -d apps ]; then
	mkdir apps
fi

cd apps

# Descargar sdk de google app engine

if [ ! -d google_appengine ]; then
	wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.15.zip
	unzip -o google_appengine_1.9.15.zip
	rm google_appengine_1.9.15.zip
fi

# Descargar aplicación
if [ ! -d iv-aerospace ]; then
	git clone https://github.com/julioxus/iv-aerospace
fi

# Actualizamos repositorios
cd iv-aerospace
git pull
cd ..

# Terminamos de trabajar en el directorio de la aplicación
cd ..

RUNSCRIPT_PATH="/apps/iv-aerospace/Proyecto/HelloWorld"

# Añadir permisos de ejecución
chmod +x $RUNSCRIPT_PATH/run.sh

# Lanzar aplicación
sh $RUNSCRIPT_PATH/run.sh




