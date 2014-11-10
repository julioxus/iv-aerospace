Instalación del sistema
========================

He utilizado una imagen de ubuntu 14.04 como sistema base para crear el entorno de desarrollo para la aplicación  en una máquina virtual.

Lo que instalaremos aquí será:

* Guest Additions (Para VirtualBox)
* Python
* Django
* Eclipse
* AppEngine para Eclipse
* Django para Eclipse
* 

**Secuencia de comandos para la instalación:**

sudo apt-get install python-pip python-dev build-essential
sudo pip install --upgrade pip
sudo pip install --upgrade virtualenv

sudo apt-get install python-setuptools build-essential

sudo pip install Django==1.7.1

sudo apt-get install openjdk-7-jdk openjdk-7-jre


**Creando lanzador de eclipse:**

Metemos la carpeta de eclipse en ~/.eclipse

Instalamos gnome-panel:

sudo apt-get install gnome-panel


Crear lanzador:

gnome-desktop-item-edit ~/Escritorio --create-new

Lo hacemos accesible al buscador metiéndolo en la carpeta applications:

sudo cp Escritorio/Eclipse.desktop /usr/share/applications

Ahora lo podemos añadir al panel lateral de Ubuntu arrastrando el icono de la aplicación.


**Configurando Eclipse:**

* Para instalar Pydev (Plugin para Django)

Vamos al menú Help -> Install y metemos el siguiente enlace en "Work with":

http://pydev.org/updates

[captura1](http://i.imgur.com/LDG0LAB.png)

E instalamos los paquetes que vienen por defecto


* Repetimos el proceso con Google AppEngine con este enlace:

https://dl.google.com/eclipse/plugin/4.4


![captura2](http://i.imgur.com/4Z7oqOo.png)


Descargamos el SDK de Python:

https://cloud.google.com/appengine/downloads#Google_App_Engine_SDK_for_Python

Extraemos la carpeta.

Al crear proyecto con pyDev Google AppEngine:

![captura3](http://i.imgur.com/wmYAdI2.png)


nos pide un directorio, le metemos el del SDK descargado

