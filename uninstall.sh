#!/bin/bash

if [[ $EUID -ne 0 ]]; then
	echo "Debes tener permisos de administrador para ejecutar el script"

else

	echo 'Desinstalando aplicación...'

	if [ ! -d /usr/local/bin/iv-aerospace ]; then
		echo 'El programa ya está desinstalado'
	else
		rm -rf /usr/local/bin/iv-aerospace
		rm /etc/init.d/ivaerospace
	fi

	echo '¡Listo!'

fi
