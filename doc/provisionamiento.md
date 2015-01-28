##Provisionamiento en Koding usando Ansible##

###Conexión ssh a Koding mediante par de claves pública/privada###

Para comenzar necesitamos generar una nueva clave ssh para poner conectarnos desde nuestro equipo local mediante ssh a Koding. Para ello, ejecutamos el siguiente comando:

```sh
ssh-keygen -t rsa -C "ivaerospace2014@gmail.com" -f koding.key
```
Posteriormente, nos preguntará que introduzcamos una contraseña. Una vez introducida nos dará el 'key fingerprint'. Añadimos nuestra nueva key al ssh-agent:

```sh
eval "$(ssh-agent -s)"
ssh-add koding.key
```
Subimos el archivo "koding.key.pub" a **nuestra máquina virtual de Koding** y copiamos el contenido en un fichero llamado 'authorized_keys', dentro de la carpeta ~/.ssh que tendremos que crear también. Para ello ejecutamos:

```sh
mkdir -p ~/.ssh
echo koding.key.pub >> ~/.ssh/authorized_keys
```

###Despliegue automático en Koding con Ansible###

Ahora que tenemos acceso a ssh tendremos que crear nuestro playbook para ejecutar el despligue de la aplicación con ansible.

Lo primero será descargar las dependencias necesarias:

```sh
sudo pip install paramiko PyYAML jinja2 httplib2 ansible
```

Ahora debemos crear un archivo en cualquier carpeta del sistema que contenga algo como esto:

```
[koding]
ivaerospace.koding.io
```

y acto seguido asignárselo a la variable de entorno ANSIBLE_HOSTS

Para hacerlo de manera automática:

```sh
   printf "[koding]\nivaerospace.koding.io" > ~/ansible_hosts
   export ANSIBLE_HOSTS=~/ansible_hosts
```

Creamos el archivo [despliegue.yml](https://github.com/julioxus/iv-aerospace/blob/master/despliegue.yml). En él vamos a meter instrucciones para borrar la aplicación previa, volver a descargarla y reinstalarla para que quede actualizada.

Nos apoyamos en scripts como [install.sh](https://github.com/julioxus/iv-aerospace/blob/master/install.sh) que se encargará de instalar el programa en el sistema y ejecutarlo, y [uninstall.sh](https://github.com/julioxus/iv-aerospace/blob/master/uninstall.sh) que eliminará las carpetas y archivos necesarios para desinstalar la aplicación.

Para ejecutar el despliegue basta con hacer:

```
$ ansible-playbook despliegue.yml
```

###Integración contínua con Koding###

Para hacer que este procedimiento se repita cada vez que actualicemos el repositorio habrá que configurar la máquina de Shippable mediante su script de configuración. Necesitamos la clave privada para acceder a ssh en cada instancia de Shippable, así que por ese motivo la hemos metido en el proyecto.

Los cambios necesarios han sido:

En la sección before_script:

```
   - mkdir -p shippable/codecoverage
   - eval "$(ssh-agent -s)"
   - chmod 400 secrets/koding.key
   - ssh-add secrets/koding.key
   - printf "[koding]\nivaerospace.koding.io" > ~/ansible_hosts
   - export ANSIBLE_HOSTS=~/ansible_hosts
```

En la sección after_success:

```
- ansible-playbook despliegue.yml
```

Enlaces de interés:

* https://help.github.com/articles/generating-ssh-keys/
* http://learn.koding.com/guides/ssh-into-your-vm/
* http://jj.github.io/IV/documentos/temas/Gestion_de_configuraciones (Apartado de Ansible)
* https://koding.com/
