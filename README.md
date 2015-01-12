
Proyecto para la asignatura Infraestructura Virtual - UGR Aerospace Program
============

![imagen](http://i.imgur.com/0WHT98c.jpg)
![imagen](http://i.imgur.com/dDb4A9D.png)

##Integrantes:##

* Julio Martínez Martínez-Checa
* Juan Francisco Rodríguez Vílchez
* Hans-Manuel Grenner Noguerón
* Óscar Sánchez Martínez
* Jose Antonio Plata Muñoz
* Miguel Martínez Castellano
* Cristina Rosillo Arenas

##Objetivos a conseguir con la aplicación:##

Nuestro grupo ha decidido trabajar en el UGR Aerospace program para desarrollar su infraestructura y plataforma. El motivo de trabajar en este proyecto es porque parte del equipo estábamos apuntados previamente al programa y nos parece interesante participar en él.

Vamos a usar la infraestructura de Google usando AppEngine para desarrollar la aplicación y Google Drive para almacenar los documentos para que sean colaborativos.

La aplicación debe contar con las siguientes funcionalidades:

* Servidor de streaming de vídeo para la cámara del robot.
* Visualización gráfica, y/o procesamiento de datos.
* Un blog en Wordpress (migración)
* Un chat para comunicarse
* Foros
* Almacenar datos en Google Drive
* Más funcionalidades por determinar.

##Documentación:##

En la siguiente [Wiki](https://github.com/julioxus/iv-aerospace/wiki/Wiki) puedes encontrar toda la información del proyecto.

##Creación de un entorno de pruebas para la aplicación.:##

+ **Creación de un entorno de pruebas para la aplicación**: Las técnicas de virtualización que hemos usado han sido tanto el contenedor Docker como la jaula. Sin embargo, hemos utilizado sobretodo la jaula más que el contenedor.
Todos los procesos de creación de entornos de pruebas están automatizados mediante scripts. Aquí explicamos brevemente lo realizado en ambos casos:

    * **Contenedor Docker:** El [script](https://github.com/julioxus/iv-aerospace/blob/master/doc/install_docker.sh) se encargará de instalar Docker, ejecutarlo como un demonio e instalar la imagen que vamos a utilizar, Ubuntu en nuestro caso.
Finalmente accederá al contenedor descargando y lanzando otro [script](https://github.com/julioxus/iv-aerospace/blob/master/doc/install.sh) también automatizado para la instalación de la aplicación y la ejecutará.

    * **Jaula:** El [script jaula.sh](https://github.com/julioxus/iv-aerospace/blob/master/doc/jaula.sh) instalará debootstrap y crear el directorio destino para la jaula, instalará en función de nuestra arquitectura una jaula de 32 o 64 bits, ubuntu saucy o trusty respectivamente. A continuación se descargará el [script install.sh](https://github.com/julioxus/iv-aerospace/blob/master/doc/install.sh) que instalará y ejecutará la aplicación.

+ **Testeo de la aplicacion**: Al ser por ahora una página html simple, sólo hemos comprobado que funciona correctamente con "curl" como se muestra en esta [explicación](https://github.com/julioxus/iv-aerospace/blob/master/doc/test_disponibilidad.md). Por otro lado, nos hemos informado sobre el testeo en Django a través de diferentes fuentes y hemos añadido un [resumen explicativo](https://github.com/julioxus/iv-aerospace/blob/master/doc/testing_tools_django.md) sobre el testeo con Django para cuando avancemos en los próximos días, poder realizarlo correctamente.

+ **Progreso global del proyecto**: Hoy, día 15/12/2014,hemos tenido en clase una reunión con Samuel y JJ para detallar como iba a ser el proyecto. Finalmente, nos ha quedado claro lo que tenemos que hacer. En la wiki de nuestro proyecto se explica las conclusiones obtenidas en dicha reunión y los puntos en los cuales, nos vamos a basar para desarrollar nuestra aplicación.

Por otro lado, tenemos lista la [estructura de directorios](https://github.com/julioxus/iv-aerospace/tree/master/workspace/guestbook) necesarios para integrar Django con Google App Engine por lo que podemos trabajar comodamente en el desarrollo de la aplicación. Por ahora solo está compuesta de imágenes con Jquery y algo mínimo de código, pero la estructura es la correcta.


Nos hemos inscrito en el certamen de la OSL con nombre "UGR Aerospace Virtualization":

![inscripcion](http://i.imgur.com/fVNpRkx.png)
