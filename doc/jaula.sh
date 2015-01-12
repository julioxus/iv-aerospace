#!/bin/bash

# Instalar debootstrap (para crear jaulas)
apt-get install debootstrap

# Crear la jaula
mkdir /home/jaulas

if [ $(uname -m)  = "i686" ]; then  
	debootstrap --arch=i386 saucy /home/jaulas/jaula-iv/ http://archive.ubuntu.com/ubuntu
else
	debootstrap --arch=amd64 trusty /home/jaulas/jaula-iv/ http://archive.ubuntu.com/ubuntu
fi

# Descargar el script de instalación automática
wget https://raw.githubusercontent.com/julioxus/iv-aerospace/master/Hito3/install.sh

# Le damos permisos de ejecución
chmod +x install.sh

# Ejecutar la jaula usando el script automático de instalación y ejecución
# Cuando el script llegue al final tendremos la aplicación funcionando sin tener que tocar nada

chroot /home/jaulas/jaula-iv/ < install.sh 
