Test de disponibilidad de la aplicación
=======================================

He realizado una prueba en el script [run.sh](https://github.com/julioxus/iv-aerospace/blob/master/workspace/guestbook/run.sh) para que muestre un mensaje de éxito al arrancar servidor de la aplicación.

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
