##Creación de un entorno de pruebas para la aplicación:##

+ **Creación de un entorno de pruebas para la aplicación**: Las técnicas de virtualización que hemos usado han sido tanto el contenedor Docker como la jaula. Sin embargo, hemos utilizado sobretodo la jaula más que el contenedor.
Todos los procesos de creación de entornos de pruebas están automatizados mediante scripts. Aquí explicamos brevemente lo realizado en ambos casos:

    * **Contenedor Docker:** 
    
    El [Dockerfile](https://github.com/julioxus/iv-aerospace/blob/master/Dockerfile) contiene toda la información subida a la página de Docker como imagen **iv-aerospace** y despliega en local la aplicación automaticamente.
    Por otro lado tenemos el [script](https://github.com/julioxus/iv-aerospace/blob/master/provisionamiento/install_dock.sh) que se encargará de instalar Docker, ejecutarlo como un demonio e instalar nuestra imagen **iv-aerospace**.
    Finalmente, la imagen de Docker llamará a [run.sh](https://github.com/julioxus/iv-aerospace/blob/master/run.sh) que lanzará finalmente la aplicación.

    * **Jaula:**
    
    El [script jaula.sh](https://github.com/julioxus/iv-aerospace/blob/master/provisionamiento/jaula.sh) instalará debootstrap y crear el directorio destino para la jaula, instalará en función de nuestra arquitectura una jaula de 32 o 64 bits, ubuntu saucy o trusty respectivamente. A continuación se llama a [run.sh](https://github.com/julioxus/iv-aerospace/blob/master/run.sh) que lanzará finalemnte la aplicación 

El script [run.sh](https://github.com/julioxus/iv-aerospace/blob/master/run.sh)muestra un mensaje de éxito al arrancar servidor de la aplicación.

En concreto este es el fragmento:

```
if [ $(curl localhost:8080 | wc -l) > 0 ]; then
        echo  '\n LA WEB FUNCIONA!!! \n'
else
        echo "\n LA WEB NO FUNCIONA :S \n"
fi
```

Previamente hemos tenido que lanzar el servidor en background.
Con wc -l contamos las líneas que nos saca curl. Si son > 0 quiere decir que nuestra web nos devuelve contenido html y está operativa.

