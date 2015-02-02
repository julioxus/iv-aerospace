#!/bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "Debes tener permisos de administrador para ejecutar el script"

else
	echo "Instalando Virtualbox..."	
	apt-get install -y virtualbox

	echo "Instalando Vagrant..."
	apt-get install -y vagrant

	echo "Instalando Virtualbox-dkms..."
	apt-get install -y virtualbox-dkms

	echo "Creando máquina virtual ubuntu 14.04..."
	vagrant box add ubuntu https://github.com/kraksoft/vagrant-box-ubuntu/releases/download/14.04/ubuntu-14.04-amd64.box

	echo "Creando proyecto vagrant..."
	mkdir vagrant_project
	cp Vagrantfile vagrant_project

	echo "Lanzando la maquina virtual y provisionando..."
	vagrant up
	vagrant provision
fi
