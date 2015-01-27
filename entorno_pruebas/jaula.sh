#!/bin/bash

# Instalar debootstrap (para crear jaulas)
apt-get install debootstrap

# Crear la jaula
mkdir /home/jaulas
if [ ! -d /home/jaulas/jaula-iv/ ]; then
	if [ $(uname -m)  = "i686" ]; then  
		debootstrap --arch=i386 saucy /home/jaulas/jaula-iv/ http://archive.ubuntu.com/ubuntu
	else
		debootstrap --arch=amd64 trusty /home/jaulas/jaula-iv/ http://archive.ubuntu.com/ubuntu
	fi
fi

# Ejecutar la jaula usando el script automático de ejecución
# Cuando el script llegue al final tendremos la aplicación funcionando sin tener que tocar nada

#echo Copiando iv-aerospace en /home/jaulas/jaula-iv/ ...
cp -r ../../iv-aerospace /home/jaulas/jaula-iv/
cd /home/jaulas/jaula-iv/iv-aerospace/

# Damos permisos de ejecución al script de instalación
chmod +x run.sh

chroot /home/jaulas/jaula-iv/ $(cd iv-aerospace; ./run.sh)
