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

echo y | python $APPENGINE_SERVER  src --host=0.0.0.0 --port=80 --admin_port=8080 --storage_path=database &
