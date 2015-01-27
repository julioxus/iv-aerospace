## Integración continua con: Shippable ##

Shippable es una plataforma en la nube que nos ofrece integración continua y testeo con repositorios de Github. La integración continua con shippable se construye usando Docker.

Este servicio soporta numerosos lenguajes de programación como: Ruby, Python, Java, Scala, Node.js, PHP, MySQL, Redis, PostgreSQL, Elasticsearch, Memcached, SQLite3 y MongoDB en Ubuntu. Debido a esto, hemos decidido usar Shippable, ya que se adaptaba perfectamente a nuestra aplicación y era facilmente sincronizable con Github.

Para utilizar este tipo de integración continua ha sido necesario un archivo llamado **shippable.yml** que se encuentra en la raíz de nuestro repositorio y se va a encargar de instalar el sdk de GAE y ejecutar los test en su [web](https://www.shippable.com/). El otro archivo necesario es el llamado **requirements.txt** en el que introducimos todas las herramientas necesarias para hacer los test:

nose
coverage
NoseGAE
WebTest

En nuestro caso han sido necesarias las cuatro herramientas anteriores, que explicaré posteriormente.

Cada vez que hagamos un commit, se va a crear una nueva build de Shippable y posteriormente, si pasa los test pertinentes, se va a proceder a desplegar automáticamente la aplicación en Google App Engine.

## Testeo de la Aplicación ##

Para ejecutar los test con Shippable, previamente tendremos que añadir en **shippable.yml**:

```sh
    nosetests src/test.py
    --with-gae --gae-lib-root=$GAE_DIR/google_appengine --gae-application=src
    --with-xunit --xunit-file=shippable/testresults/test.xml
    --with-coverage --cover-xml --cover-xml-file=shippable/codecoverage/coverage.xml
```

Con la herramienta **nosetest** vamos a ejecutar los test que se encuentran en el fichero src del proyecto, le indicamos donde se encuentra el directorio de GAE para ejecutar los test en él y algunos parámetros necesarios para que se puedan realizar los test obtenidos de la documentación de Shippable en Github.

Para la realización de los test, hemos utilizado la herramienta [unittest de Google](https://cloud.google.com/appengine/docs/python/tools/localunittesting) que nos permite realizar una amplia variedad de tests en nuestra aplicación web.

Los test los hemos realizado dentro de nuestro controlador [server.py](https://github.com/julioxus/iv-aerospace/blob/master/src/server.py) en una nueva clase llamada Tests. Desde el fichero [test.py](https://github.com/julioxus/iv-aerospace/blob/master/src/test.py) llamamos a la clase anterior y ejecutamos dicho test haciendo uso de la herramienta **testbed**. Posteriormente, vamos llamando a cada una de las funciones de la clase Tests y con el método: self.assertEqual(response, True) podemos indicar la respuesta que esperamos a dicho test, para que usando shippable nos indique si el test se ha pasado correctamente o no.


**Enlaces de interés:**

https://docs.python.org/2/library/unittest.html
https://cloud.google.com/appengine/docs/python/tools/localunittesting
https://www.shippable.com/
https://github.com/Shippable
