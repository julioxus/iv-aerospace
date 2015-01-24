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

# Instalamos git para clonar nuestro repositorio
RUN apt-get install -y git
RUN git clone https://github.com/julioxus/iv-aerospace.git
RUN git submodule init
RUN git submodule sync
RUN git submodule update
RUN cd iv-aerospace
RUN chmod 755 run.sh
RUN bash run.sh
