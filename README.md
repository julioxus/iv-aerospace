
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

##Objetivos a conseguir con la aplicación:##

Nuestro grupo ha decidido trabajar en el UGR Aerospace program para desarrollar su infraestructura y plataforma. El motivo de trabajar en este proyecto es porque parte del equipo estabamos apuntados previamente al programa y nos parecía interesante participar en él.

Vamos a usar la infraestructura de Google usando AppEngine para desarrollar la aplicación usando WebApp2 y NDB de Python como base de datos.

**Objetivos:**

* Recepción y procesamiento de los datos.
* Streaming de vídeo.
* Simular y elegir el formato según el tipo de dato (podremos elegir entre temperatura, altura, velocidad del viento...)
* Procesamiento de las imágenes (gráficos).
* 
**Se ha decidido suprimir al streaming ya que se consideró como un proyecto independiente.**

Datos a tener en cuenta:

* Los datos recibidos son heterogéneos, por lo tanto no todos se procesarán de la misma manera
* Dependiendo del tipo de dato, la actualización de estos será cada "x" tiempo.
* Dependiento del tipo de dato, se mostrarán en un determinado gráfico.

Para trabajar con gráficos se ha decidido utilizar GoogleChart.

Samuel nos suministrará de una BDD de prueba para poder trabajar con la recepción de datos.

##Documentación:##

En la siguiente [enlace](https://github.com/julioxus/iv-aerospace/blob/master/doc/INDICE.md) puedes encontrar el indice a toda la información del proyecto.

##Creación de un entorno de pruebas para la aplicación.:##

+ **Creación de un entorno de pruebas para la aplicación**: Las técnicas de virtualización que hemos usado han sido tanto el contenedor Docker como la jaula. Sin embargo, hemos utilizado sobretodo la jaula más que el contenedor.
Todos los procesos de creación de entornos de pruebas están automatizados mediante scripts. Aquí explicamos brevemente lo realizado en ambos casos:

    * **Contenedor Docker:** El [script](https://github.com/julioxus/iv-aerospace/blob/master/provisionamiento/install_docker.sh) se encargará de instalar Docker, ejecutarlo como un demonio e instalar la imagen que vamos a utilizar, Ubuntu en nuestro caso.
Finalmente accederá al contenedor descargando y lanzando otro [script](https://github.com/julioxus/iv-aerospace/blob/master/provisionamiento/install.sh) también automatizado para la instalación de la aplicación y la ejecutará.

    * **Jaula:** El [script jaula.sh](https://github.com/julioxus/iv-aerospace/blob/master/doc/jaula.sh) instalará debootstrap y crear el directorio destino para la jaula, instalará en función de nuestra arquitectura una jaula de 32 o 64 bits, ubuntu saucy o trusty respectivamente. A continuación se descargará el [script install.sh](https://github.com/julioxus/iv-aerospace/blob/master/provisionamiento/install.sh) que instalará y ejecutará la aplicación.

+ **Testeo de la aplicacion**: Al ser por ahora una página html simple, sólo hemos comprobado que funciona correctamente con "curl" como se muestra en esta [explicación](https://github.com/julioxus/iv-aerospace/blob/master/provisionamiento/test_disponibilidad.md). Por otro lado, nos hemos informado sobre el testeo en Django a través de diferentes fuentes y hemos añadido un [resumen explicativo](https://github.com/julioxus/iv-aerospace/blob/master/test/testing_tools_django.md) sobre el testeo con Django para cuando avancemos en los próximos días, poder realizarlo correctamente.

+ **Progreso global del proyecto**: Hoy, día 15/12/2014,hemos tenido en clase una reunión con Samuel y JJ para detallar como iba a ser el proyecto. Finalmente, nos ha quedado claro lo que tenemos que hacer. En la wiki de nuestro proyecto se explica las conclusiones obtenidas en dicha reunión y los puntos en los cuales, nos vamos a basar para desarrollar nuestra aplicación.

Nos hemos inscrito en el certamen de la OSL con nombre "UGR Aerospace Virtualization":

![inscripcion](http://i.imgur.com/fVNpRkx.png)
