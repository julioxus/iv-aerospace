##¿Cómo funciona el test?##

El test se encargar de realizar un ping un número de veces predeterminado a la dirección de nuestra aplicación web.

Para poder realizarlo es necesario importar la librería os:

[Os](https://docs.python.org/2/library/os.html): que nos proporciona funciones para interactuar con el sistema operativo.
	
El módulo .system nos permite ejecutar órdenes desde el shell.

**Ahora explicaremos paso a paso cómo funciona el test**

Lo primero que nos encontramos es el import al paquete o módulo que necesitamos (os). 
Definimos dos variables, num especifica el número de peticiones que vamos a enviar y ping que almacena el comando (en éste caso ping -c1 direcciónWeb > /dev/null) que queremos que se ejecute. AL final del comando incluimos /dev/null para que no devuelva la información por pantalla.

A partir de ahí tenemos un bucle for que ejecutará el comando tantas veces como se haya indicado en la variable num. A continuación mostramos la salida dada por la ejecución de el comando, si el valor es 0 el test de dará por finalizado correctamente pero si el valor es distinto de 0 el resultado del test será negativo.
	
