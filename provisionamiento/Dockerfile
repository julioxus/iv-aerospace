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

# Falta añadir DESCAGAR DE GOOGLE APP ENGINE

# Instalamos git para clonar nuestro repositorio
RUN apt-get install -y git
RUN git clone https://github.com/julioxus/iv-aerospace.git
RUN cd iv-aerospace
RUN ./run.sh
