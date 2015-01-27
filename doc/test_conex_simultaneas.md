##¿Cómo funciona el test?##

El test se encargar de realizar un ping un número de veces predeterminado a la dirección de nuestra aplicación web.

Para poder realizarlo es necesario importar las librerías sys y subprocess.

[Sys](https://docs.python.org/2/library/sys.html): éste módulo nos provee de acceso a funciones y variables relacionadas directamente con el intérprete (sys.exit()...)
	
[Subprocess](https://docs.python.org/2/library/subprocess.html): nos permite trabajar de forma directa con órdenes del sistema. 

Éste módulo también nos provee del submódulo Popen, el cuál nos permite ejecutar órdenes y mantener un mejor control sobre las salidas. Algunas entradas y salidas que pueden ser capturadas por Popen son stdout, stdin, stderr...

**Ahora explicaremos paso a paso cómo funciona el test**

Lo primero que nos encontramos son los imports a los paquetes o módulos que necesitamos (los vistos anteriormente). 
Definimos dos variables, num especifica el número de peticiones que vamos a enviar y host almacena el comando (en éste caso ping -c1 direcciónWeb) que queremos que se ejecute.

A partir de ahí tenemos un bucle for que ejecutará el comando tantas veces como se haya indicado en la variable num. A continuación mostramos las salidas que se van recibendo a consecuencia de la ejecución de los ping.
	
