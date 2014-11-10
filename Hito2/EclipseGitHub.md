#Sincronizar Eclipe con GitHub


Para sincronizar eclipe con GitHub, debemos de seguir los siguientes pasos:

*Primero paso: Crear la Llave*

Lo primero que tenemos que hacer, es generar una llave SSH para nuestro eclipse. Simplemente debemos de ir a:

`Menú Windows-> Preferencias -> Network Connection -> SSH2`

!(http://imgur.com/VI3AC6M)

Ahí deberemos de generar una clave RSA (Generate RSA Key) y automáticamente generará nuestra clave. No olvidemos guardarla (Save Private Key) para poder utilizarla desde otros equipos. Ahora ya tenemos nuestra llave creada.

*Segundo paso: Conectar con GitHub*

Ahora nos vamos a:

`Menú Window-> Show View -> Other -> Git`

Y seleccionamos Git Repositories. Ahora nos apareceran proyectos, hacemos click derecho en Remotes (una carpeta dentro de nuestro proyecto) y le damos a "Create Remote" y escribimos el nombre que queramos


!(http://imgur.com/VI3AC6M)



