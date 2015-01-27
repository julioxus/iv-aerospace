##Python NDB  API##

**¿Qué es NDB?**

Es un almacén de datos para Google App Engine Python. Fué desarrollado como un
proyecto de código abierto por Guido van Rossum. 
NDB es actualmente un componente estándar de la App Engine SDK Python.

**¿Para qué sirve?**

La API NDB nos brinda un almacenamiento persistente en un almacén de datos. Podemos
decir que NDB es muy adecuado para el almacenamiento  de registros de datos estructurados.

**¿Cómo se estructura?**

NDB guarda objetos de datos, llamados entidades. Una entidad puede tener una o más propiedades
que pueden ser una cadena, un entero o una referencia a otra entidad.
Cada entidad se identifica por una clave. un identificador único dentro del almacén de datos.

**Funcionamiento**

Una aplicación utiliza NDB para definir modelos. Un modelo es una clase Python que actúa como un
esquema de base de datos. En ella describimos eltipo de datos y sus propiedades.
Para que funcione, a la hora de crear nuestra aplicación y antes de definir el modelo debemos
referenciar el paquete de google de ésta forma: 
	
	> from NDB import google.appengine.ext

**Ejemplo de funcionamiento**


```sh
import cgi
import urllib

import webapp2

from google.appengine.ext import ndb


class Greeting(ndb.Model):
  """Models an individual Guestbook entry with content and date."""
  content = ndb.StringProperty()
  date = ndb.DateTimeProperty(auto_now_add=True)
  ...
``` 

Para más información puede visitar la [documentación de Google](https://cloud.google.com/appengine/docs/python/ndb/).
