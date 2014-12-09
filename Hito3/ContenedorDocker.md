**Encapsulando nuestra aplicación en un contenedor Docker

Para realizarlo todo de forma automática se ha creado un script "[install_docker.sh]()", que se encargará de instalar la herramienta y de realizar las configuraciones necesarias. El script principal  
A continuación podemos ver el contenido de dicho script:

...
	#Actualizar los repositorios del sistem dockera
	> sudo apt-get update

	#Instalar docker (para crear el contenedor)
	> sudo apt-get install docker.io

	#Demonizamos docker
	> sudo docker -d &

	#A continuación nos descargaremos la imagen base que vamos a uitlizar, en éste caso es la de Ubuntu
	> sudo docker pull ubuntu

	#Accederemos al contenedor y  descargaremos algunos paquetes y el script que se encargará de instalar las dependencias y de ejecutar de forma automática la aplicación
	> sudo docker run -i -t ubuntu /bin/sh -c "apt-get install -y wget; wget https://raw.githubusercontent.com/julioxus/iv-aerospace/master/Hito3/install.sh; sh ./install.sh"

...