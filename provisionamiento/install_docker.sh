#!/bin/bash

#Actualizar repositorios e instalar docker
apt-get update
apt-get install -y docker.io

#Ponemos docker como demonio del sistema
docker -d &

#Instalamos la imagen base del contenedor, en éste caso Ubuntu
docker pull ubuntu

#Accedemos al contenedor y descargamos los scripts que instalarán las
#dependencias y ejecutarán la aplicación
sudo docker run -i -t ubuntu /bin/sh -c "apt-get install -y wget; wget https://raw.githubusercontent.com/julioxus/iv-aerospace/master/provisionamiento/install.sh; sh ./install.sh"

