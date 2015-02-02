## Comparación de integración continua: Shippable VS Travis ##

Habiendo probado y usado las dos plataformas para realizar integración contínua en nuestro proyecto analizamos las ventajas e inconvenientes que tiene cada uno:

### Shippable

* Notificaciones por correo cuando se completa la build
* Permite configurar variables de entorno encriptadas
* Consola donde se muestra la configuración y ejecución de todas las builds registradas en el historial
* Sincronización con Docker Hub
* Limitaciones por usar versión gratuita (1 GB de almacenamiento, 60 minutos de build timeout)

### Travis

* Notificaciones en los commits de GitHub
* Permite configurar variables de entorno
* Consola donde se muestra la configuración y ejecución de la última build
* La única limitación es el "Uso justo" del sistema, sin límites de espacio ni repositorios


Como podemos observar tienen características muy parecidas, pero nos quedamos con Shippable porque permite una mejor depuración ya que tenemos un log de todas las builds realizadas y otras opciones como la sincronización con Docker y una interfaz de usuario más sencilla. Tiene el problema de la limitación de uso gratuita, pero para un proyecto pequeño no es problema.