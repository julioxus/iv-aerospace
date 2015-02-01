##Test de navegación automática con splinter##

Splinter es una herramienta open source para testear aplicaciones web con python.Nos permite hacer interacción automática con navegadores, hacer referencia a elementos y visitar urls.

**Cómo funciona el test**

- Primero hacemos un registro en la base de datos para hacer la prueba de un usuario.

- Después,ejecutamos 5 veces una navegación automática que visita cada apartado de la aplicación y saca el tiempo de cada navegación.

-Por último , saca la media de las mediciones anteriores y las muestra por consola


Para ejecutar el test basta con irte al directorio "iv-aerospace/test" y ejecutar el test-nav-auto.sh con el comando:

./test-nav-auto.sh
