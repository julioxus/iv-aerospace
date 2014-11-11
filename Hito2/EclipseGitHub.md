#Sincronizar Eclipe con GitHub


Para sincronizar eclipe con GitHub, debemos de seguir los siguientes pasos:

*Primero paso: Crear la Llave*

Lo primero que tenemos que hacer, es generar una llave SSH para nuestro eclipse. Simplemente debemos de ir a:

`Menú Windows-> Preferencias -> Network Connection -> SSH2`

![Captura](http://i.imgur.com/VI3AC6M.png)

Ahí deberemos de generar una clave RSA (Generate RSA Key) y automáticamente generará nuestra clave. No olvidemos guardarla (Save Private Key) para poder utilizarla desde otros equipos. Ahora ya tenemos nuestra llave creada.

*Segundo paso: Conectar con GitHub*

Ahora nos vamos a:

`Menú Window-> Show View -> Other -> Git`

Y seleccionamos Git Repositories. Ahora nos apareceran proyectos, hacemos click derecho en Remotes (una carpeta dentro de nuestro proyecto) y le damos a "Create Remote" y escribimos el nombre que queramos

Ahora deberemos irnos a Github e iniciar sesión. Creamos un repositorio, o nos vamos al que tengamos creados y queramos sincronizar y nos iremos a Settings (parte superior derecha), una vez allí seleccionamos SSH keys. Ahora cogemos la llave que creamos anteriormente (el archivo se llama normalmente id_rsa.pub) y la copiamos donde pone "key". Le ponemos un título y clickamos en "Add key"


![Captura](http://i.imgur.com/f4nI27H.png)

*Tercer paso: Configurar Push*

Por último, solo nos queda coger la url de nuestro repositorio, irnos de nuevo a Eclipse hacer click derecho en el los repositorios que aparecen y clickar en "Configure Push". 

Una vez ahí dentro, debemos entrar en "Change" y rellenar todos los apartados.En URI la dirección del repositorio, Protocolo utilizado SSH y el usuario y la contraseña del usuario en gitHub.

![Captura](http://i.imgur.com/6PDKKb5.png)


Una vez hecho esto, ya tenemos lista la sincronización. Solo nos quedará hacer click derecho en nuestro proyecto, hacer push y ... ya está! . Eclipse "subirá" automáticamente nuestro proyecto a Github.
