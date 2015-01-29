#!/bin/bash

#Se avisa si no se tiene permisos de administrador para que el usuarios los ponga

if [[ $EUID -ne 0 ]]; then
	echo "Debes tener permisos de administrador para ejecutar el script"

else

	#Instala Ansible (y dependencias)
	
	if [[ $(dpkg-query -W -f='${Status}\n' python) != 'install ok installed' ]]; then
		apt-get install -y --force-yes python
	fi
	
	if [[ $(dpkg-query -W -f='${Status}\n' python-pip) != 'install ok installed' ]]; then
		apt-get install -y --force-yes python-pip
	fi

	echo 'Instalando herramienta ansible...'
	pip install paramiko PyYAML jinja2 httplib2 ansible
	
	# Gestiona la conexion ssh automaticamente
	
	echo 'Gestionando conexion ssh con Koding...'

	eval "$(ssh-agent -s)"

	chmod 400 secrets/koding.key

	ssh-add secrets/koding.key
	
	echo 'Desplegando...'

	#Añade el dominio a ansible_hosts

	printf "[koding]\nivaerospace.koding.io" > ~/ansible_hosts

	export ANSIBLE_HOSTS=~/ansible_hosts

	#Despliega la aplicación en Koding utilizado el playbook despliegue.yml

	ansible-playbook despliegue.yml

	echo 'Aplicacion correctamente desplegada'

fi

