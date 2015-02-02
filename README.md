
Proyecto para la asignatura Infraestructura Virtual - UGR Aerospace Program
============

![imagen](http://i.imgur.com/0WHT98c.jpg)
![imagen](http://i.imgur.com/UEC1ld2.jpg)
![imagen](http://i.imgur.com/MUYfaeA.png)

##Integrantes:##

* Julio Martínez Martínez-Checa
* Juan Francisco Rodríguez Vílchez
* Hans-Manuel Grenner Noguerón
* Óscar Sánchez Martínez
* Jose Antonio Plata Muñoz
* Miguel Martínez Castellanos
* Cristina Rosillo Arenas

##Aplicación desplegada en Google App Engine:##

[UGR Aerospace Program](http://ugraerospaceprogram.appspot.com/)

##Aplicación desplegada en Koding:##

[Koding](http://ivaerospace.koding.io/)

##Documentación:##

En la siguiente [enlace](https://github.com/julioxus/iv-aerospace/blob/master/doc/INDICE.md) puedes encontrar el indice a toda la información del proyecto.

##Para desplegar la aplicación en Koding:##

Ejecuta el script [despliegue_automatico_Koding.sh](https://github.com/julioxus/iv-aerospace/blob/master/despliegue_automatico_Koding.sh) y despliega la aplicación!

##Para desplegar la aplicación en Google App Engine:##

Ejecuta el script [despliegue_automatico_gae.sh](https://github.com/julioxus/iv-aerospace/blob/master/despliegue_automatico_gae.sh) y despliega la aplicación!

##Para instalar la aplicación en tu ordenador:##

Ejecuta el script [install.sh](https://github.com/julioxus/iv-aerospace/blob/master/install.sh) y la aplicación quedará instalada y ejecutándose por el puerto 80

##Para instalar la aplicación en una máquina virtual con vagrant y virtualbox

[Documentación de Vagrant](https://github.com/julioxus/iv-aerospace/blob/master/doc/documentacion_vagrant.md)

##Integración contínua con Shippable:##

Con cada commit la aplicación se desplegará de manera automática en Koding y en GAE gracias al script [shippale.yml](https://github.com/julioxus/iv-aerospace/blob/master/shippable.yml)


##Introducción a la aplicación:##

Nuestro grupo ha decidido trabajar en el UGR Aerospace program para desarrollar su infraestructura y plataforma. El motivo de trabajar en este proyecto es porque parte del equipo estabamos apuntados previamente al programa y nos parecía interesante participar en él.

Hemos utilizado la infraestructura de Google usando Google AppEngine para desarrollar la aplicación usando WebApp2 y NDB de Python como base de datos para almacenar en la Datastore.

**La aplicación dispone de:**

* Recepción y procesamiento de los datos según su tipo (podremos elegir entre temperatura, altura, velocidad del viento...).
* Procesamiento de dichos datos en gráficos a tiempo real.
* Recepción de coordenadas del robot Rober a tiempo real, siendo mostradas en un mapa de Google Maps.
* Almacenamiendo e interpretación de gráficos en tablas calculando sus medias.

Datos tenidos en cuenta en la aplicación:

* Los datos recibidos son heterogéneos, por lo tanto no todos se procesarán de la misma manera
* Dependiendo del tipo de dato, la actualización de estos será cada "x" tiempo.
* Dependiento del tipo de dato, se mostrarán en un determinado gráfico.



Nos hemos inscrito en el certamen de la OSL con nombre "UGR Aerospace Virtualization":

![inscripcion](http://i.imgur.com/fVNpRkx.png)
