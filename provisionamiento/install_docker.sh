#!/bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "Debes tener permisos de administrador para ejecutar el script"
else
	#Actualizar repositorios e instalar docker
	apt-get update

	if [[ $(dpkg-query -W -f='${Status}\n' docker.io) != 'install ok installed' ]]; then
		apt-get install -y docker.io
	fi

	#Ponemos docker como demonio del sistema
	docker -d &

	#Instalamos la imagen base del contenedor, en éste caso Ubuntu
	docker pull julioxus/iv-aerospace

	#Arrancamos el contenedor
	docker run -t -i julioxus/iv-aerospace /bin/bash
fi
