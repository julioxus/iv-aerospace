##Provisionamiento en Koding usando Ansible##

###Conexión ssh a Koding###

Para comenzar necesitamos generar una nueva clave ssh para poner conectarnos desde nuestro equipo local mediante ssh a Koding. Para ello, ejecutamos el siguiente comando:

```sh
ssh-keygen -t rsa -C "ivaerospace2014@gmail.com"
```
Posteriormente, nos preguntará que introduzcamos una contraseña. Una vez introducida nos dará el 'key fingerprint'. Añadimos nuestra nueva key al ssh-agent:

```sh
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa
```
Abrimos el "~/.ssh/id_rsa.pub" y copiamos el contenido en un fichero llamado 'authorized_keys' en nuestra máquina virtual de Koding. Para ello ejecutamos:

```sh
mkdir -p ~/.ssh
touch ~/.ssh/authorized_keys
```
Ahora abrimos el fichero de 'authorized_keys' que acabamos de crear y copiamos nuestra clave pública. 

Enlaces de interés:

* https://help.github.com/articles/generating-ssh-keys/
* http://learn.koding.com/guides/ssh-into-your-vm/
* http://jj.github.io/IV/documentos/temas/Gestion_de_configuraciones (Apartado de Ansible)
* https://koding.com/
