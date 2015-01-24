FROM ubuntu:latest
MAINTAINER iv-aerospace <ivaerospace2014@gmail.com>

#Instalar Python con todas las dependencias

RUN apt-get update
RUN apt-get -y install python python-setuptools build-essential python-dev
RUN apt-get install -y python-setuptools
RUN easy_install pip

# Instalar wget para descargar y zip para descomprimir

RUN apt-get install -y wget
RUN apt-get install -y zip

# Instalamos git para clonar nuestro repositorio y ejecutar el script que lanza la aplicación web.

RUN apt-get install -y git
RUN git clone https://github.com/julioxus/iv-aerospace.git
RUN cd iv-aerospace && \
git submodule init && \
git submodule sync && \
git submodule update && \
chmod 755 run.sh && \
bash run.sh



