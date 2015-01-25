#!/bin/bash

# Variables
APPENGINE_SERVER="google_appengine/dev_appserver.py"

# Descargar programas necesarios
if [[ $(dpkg-query -W -f='${Status}\n' python) != 'install ok installed' ]]; then
	apt-get install -y --force-yes python
fi
if [[ $(dpkg-query -W -f='${Status}\n' curl) != 'install ok installed' ]]; then
	apt-get install -y --force-yes curl
fi
if [[ $(dpkg-query -W -f='${Status}\n' wget) != 'install ok installed' ]]; then
	apt-get install -y --force-yes wget
fi

# Lanzar aplicación (con autoconfirmación)

echo y | python $APPENGINE_SERVER src --storage_path=database &

if [ $(curl localhost:8080 | wc -l) > 2 ]; then
        echo  '\n LA WEB FUNCIONA!!! \n'
else
        echo "\n LA WEB NO FUNCIONA :S \n"
fi
