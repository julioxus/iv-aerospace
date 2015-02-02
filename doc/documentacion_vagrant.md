##¿Qué es Vagrant?

Es una herramienta de código abierto cuyo objetivo principal es la creación y configuración de ambientes virtuales de desarrollo de manera muy ligera, reproducible y portátil. Esto con el fin de ser desplegado múltiples veces sin dificultad en diferentes ambientes que harán de su hogar, de ahí su nombre de Vagrant (vagabundo). Estos ambientes pueden estar proveídos por populares servicios como VirtualBox, VMWare y AWS pero debe funcionar correctamente con cualquier otro proveedor.

El corazón de cada instancia de maquina virtual se denomina Vagrantfile, el cual es un archivo que describe la configuración de la maquina requerida, este archivo es a menudo sometido a control de versiones para permitir a los desarrolladores levantar el ambiente con un simple comando y comenzar manipular el proyecto.

Una de las grandes ventajas del uso de Vagrant es su integración con herramientas de suministro como Chef y Puppet las cuales se basan en la creación de recetas o scripts que permiten alterar la configuración, instalar de software y mucho más durante el proceso de levantamiento del ambiente.

##¿Qué hace nuestro script?

Es bastante sencillo:

-Instala virtualbox virtualbox-dkms (entorno de virtualización)

-Instala Vagrant

-Añade la caja o "box" que es la imagen que es usada para clonar las máquinas virtuales.

-Y por último, lanza la máquina añadida anteriormente y la provisiona tal y como le expecificamos en el archivo Vagrantfile.
