#!/bin/bash
	
if [[ $(dpkg-query -W -f='${Status}\n' python) != 'install ok installed' ]]; then
	apt-get install -y --force-yes python
fi
	
if [[ $(dpkg-query -W -f='${Status}\n' python-pip) != 'install ok installed' ]]; then
	apt-get install -y --force-yes python-pip
fi

#Iniciamos los módulos de GAE

git submodule init && \
git submodule sync && \
git submodule update

#Desplegamos la aplicación

google_appengine/appcfg.py --oauth2  --oauth2_credential_file=secrets/.appcfg_oauth2_tokens update src/
