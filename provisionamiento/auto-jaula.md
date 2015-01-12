Montando nuestra aplicación en una jaula de manera automática
==============================================================

 
Para crear una jaula que automáticamente nos lance la aplicación he desarrollado los scripts:

* [install.sh](https://github.com/julioxus/iv-aerospace/blob/master/provisionamiento/install.sh): que instala todas las dependencias necesarias y ejecuta la aplicación llamando al otro script (run.sh).

* [run.sh](https://github.com/julioxus/iv-aerospace/blob/master/workspace/guestbook/run.sh): que se encarga de ejecutar la aplicación haciendo uso de las dependencias previas instaladas.


Para instalar la jaula con todo incluido y hacerla funcionar con un solo script:

[jaula.sh](https://github.com/julioxus/iv-aerospace/blob/master/provisionamiento/jaula.sh)
