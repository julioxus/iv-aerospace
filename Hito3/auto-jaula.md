Montando nuestra aplicación en una jaula de manera automática
==============================================================

 
Para crear una jaula que automáticamente nos lance la aplicación he desarrollado los scripts:

* [install.sh](https://github.com/julioxus/iv-aerospace/blob/master/Hito3/install.sh): que instala todas las dependencias necesarias y ejecuta la aplicación llamando al otro script.

* [run.sh](https://github.com/julioxus/iv-aerospace/blob/master/Proyecto/HelloWorld/run.sh): que se encarga de ejecutar la aplicación haciendo uso de las dependencias previas instaladas.


Si queremos instalar una jaula y hacer uso de estos scripts tendremos que hacer lo siguiente:

```
# Instalar debootstrap (para crear jaulas)
$ sudo apt-get install debootstrap

# Crear la jaula
$ sudo mkdir /home/jaulas
$ sudo debootstrap --arch=amd64 trusty /home/jaulas/jaula-iv/ http://archive.ubuntu.com/ubuntu

# Descargar el script de instalación automática
$ wget https://raw.githubusercontent.com/julioxus/iv-aerospace/master/Hito3/install.sh

# Le damos permisos de ejecución
$ chmod +x install.sh

# Ejecutar la jaula usando el script automático de instalación y ejecución
# Cuando el script llegue al final tendremos la aplicación funcionando sin tener que tocar nada

./install.sh | sudo chroot /home/jaulas/saucy/

```
