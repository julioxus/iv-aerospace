#!/bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "Debes tener permisos de administrador para ejecutar el script"

else
	echo "Instalando Virtualbox..."	
	apt-get install -y virtualbox

	echo "Instalando wget..."
	apt-get install -y wget

	echo "Instalando Vagrant..."
	wget https://dl.bintray.com/mitchellh/vagrant/vagrant_1.7.2_x86_64.deb
	dpkg -i vagrant_1.7.2_x86_64.deb

	echo "Instalando Virtualbox-dkms..."
	apt-get install -y virtualbox-dkms

	echo "Creando máquina virtual Debian..."
	vagrant box add debian https://dl.dropboxusercontent.com/u/197673519/debian-7.2.0.box

	echo "Creando proyecto vagrant..."
	mkdir vagrant_project
	vagrant init debian
	cp Vagrantfile vagrant_project

	echo "Lanzando la maquina virtual y provisionando..."
	vagrant up
	vagrant provision
fi
