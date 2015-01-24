FROM ubuntu:latest
MAINTAINER iv-aerospace <ivaerospace2014@gmail.com>

#Instalar Python con todas las dependencias

RUN apt-get update
RUN apt-get -y install python python-setuptools build-essential python-dev
RUN apt-get install -y python-setuptools
RUN easy_install pip

#Instalar frameworks necesarios para GAE

RUN pip install webapp2
RUN pip install jinja2

# Instalar wget para descargar y zip para descomprimir

RUN apt-get install -y wget
RUN apt-get install -y zip


# Descargamos el sdk de Google App Engine
RUN wget https://storage.googleapis.com/appengine-sdks/featured/google_appengine_1.9.17.zip --no-check-certificate

# Descomprimimos el fichero descargado, ya tendremos disponible el SDK
RUN unzip google_appengine_1.9.17.zip


# Instalamos git para clonar nuestro repositorio
RUN apt-get install -y git
RUN git clone https://github.com/julioxus/iv-aerospace.git
RUN cd iv-aerospace
RUN ./run.sh
