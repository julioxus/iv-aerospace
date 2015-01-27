#!/bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "Debes tener permisos de administrador para ejecutar el script"

else

	echo 'Instalando aplicación...'

	if [ ! -d /usr/local/bin/iv-aerospace ]; then
		echo 'Copiando archivos en el sistema...'
		cp -r . /usr/local/bin/iv-aerospace
	fi

	sudo cp ivaerospace /etc/init.d

	sudo update-rc.d ivaerospace defaults
	sudo service ivaerospace start

	echo '¡Listo!'

fi
