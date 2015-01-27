#!/bin/bash
 
if [[ $EUID -ne 0 ]]; then
        echo "Debes tener permisos de administrador para ejecutar el script"
else
 
        if [[ $(dpkg-query -W -f='${Status}\n' docker.io) != 'install ok installed' ]]; then
                #Actualizar repositorios e instalar docker
                apt-get update
                apt-get install -y docker.io
        fi
 
        cond=$(ps aux | grep docker | wc -l)
        #Ponemos docker como demonio del sistema
        if [ $cond -gt 1 ]; then
                while [ $cond -gt 1 ]; do
                        echo 'Matando demonio docker.io...'
			kill -9 `ps -ef|grep -v grep |grep docker | awk '{print $2}'`
                        cond=$(ps aux | grep docker | wc -l)
                done
        fi
 
        echo 'Iniciando demonio docker ...'
        docker -d &    
 
        #Instalamos la imagen base del contenedor, en éste caso Ubuntu
        docker pull julioxus/iv-aerospace
 
        #Arrancamos el contenedor
        docker run -t -i julioxus/iv-aerospace /bin/bash
fi
