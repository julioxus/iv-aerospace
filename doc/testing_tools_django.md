## Herramientas de testeo para Django ##

Django nos ofrece una serie de herramientas para escribir test: podemos realizar peticiones GET y POST a nuestra aplicación y observar como responde, chequear la url y el estado de nuestra aplicación paso a paso, e incluso testear si el template esta siendo servido con los datos correctos.

Por ejemplo, de esta forma podemos ver como responde el login de nuestra página web, obteniendo datos sobre el contenido o el estado:

```sh

>>> from django.test import Client
>>> c = Client()
>>> response = c.post('/login/', {'username': 'john', 'password': 'smith'})
>>> response.status_code
200
>>> response = c.get('/customer/details/')
>>> response.content
'<!DOCTYPE html...'

```

### Realizando peticiones ###

Si queremos realizar una petición GET a nuestra aplicación:

```sh 
>>> c = Client()
>>> c.get('/customers/details/', {'name': 'fred', 'age': 7})
```

De esta forma evaluará la petición GET que sería equivalente a:

```sh
/customers/details/?name=fred&age=7
```
Además, podemos especificar las cabeceras que serán enviadas en la petición como por ejemplo:

```sh
>>> c = Client()
>>> c.get('/customers/details/', {'name': 'fred', 'age': 7},
...       HTTP_X_REQUESTED_WITH='XMLHttpRequest')
```
Si queremos realizar la petición GET directamente, podemos hacerlo de la siguiente forma:

```sh

>>> c = Client()
>>> c.get('/customers/details/?name=fred&age=7')
```
Si tenemos una URL como por ejemplo '/redirect_me/ que redirecciona a '/next/' que redirecciona a '/final/', podemos realizar la petición como se muestra:

```sh
>>> response = c.get('/redirect_me/', follow=True)
>>> response.redirect_chain
[('http://testserver/next/', 302), ('http://testserver/final/', 302)]
```
Si añadimos 'secure = True' el cliente estará emulando una petición HTTPS.

Sin embargo, si queremos realizar una petición POST deberemos hacerlo de la siguiente forma:

**post(path, data=None, content_type=MULTIPART_CONTENT, follow=False, secure=False)**

```sh
>>> c = Client()
>>> c.post('/login/', {'name': 'fred', 'passwd': 'secret'})
```
Si queremos indicarle diferentes valores de llaves, podemos generar una lista o tupla de llaves requeridas. Por ejemplo, de esta forma se podría elegir entre 3 valores diferentes de llaves:

```sh
{'choices': ('a', 'b', 'd')}
```

Para realizar un POST de un archivo, solamente tenemos que indicar el nombre y el archivo que deseamos subir. Por ejemplo:

```sh
>>> c = Client()
>>> with open('wishlist.doc') as fp:
...     c.post('/customers/wishes/', {'name': 'fred', 'attachment': fp})
```

Si queremos comprobar que el 'login' de nuestra aplicación funciona correctamente, podemos hacerlo de la siguiente forma:

```sh
>>> c = Client()
>>> c.login(username='fred', password='secret')
```

Login devuelve True si los credenciales son correctos y el login se ha realizado correctamente. De igual forma, podemos comprobar el 'logout' simulando el logout de un usuario en nuestro sitio web.

Podemos modificar las variables de sesión y posteriormente guardarlas:

```sh
def test_something(self):
    session = self.client.session
    session['somekey'] = 'test'
    session.save()
```
Por ejemplo, de esta forma se puede probar mediante test unitarios el funcionamiento correcto:

```sh
import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_details(self):
        # Issue a GET request.
        response = self.client.get('/customer/details/')

        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, 200)

        # Check that the rendered context contains 5 customers.
        self.assertEqual(len(response.context['customers']), 5)
```

Otra gran forma de realizar tests con Django son los 'LiveServerTestCase'. Estos tests nos permiten ejecutar (mediante el cliente de Selenium)  diferentes test funcionales dentro del navegador para simular acciones reales de los futuros usuarios.

Por defecto la dirección es 'localhost:8081'. Sin embargo podemos cambiar la dirección por defecto:

```sh
./manage.py test --liveserver=localhost:8082
```
O cambiando la dirección del servidor por defecto mediante 'DJANGO_LIVE_TEST_SERVER_ADDRESS' que sería una variable del entorno que introduciriamos en nuestro script:

```sh
import os
os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = 'localhost:8082'
```
Para el caso en el que el test este siendo ejecutado por muchos procesos en paralelo, nos dará el error de que la dirección está siendo usado. Para evitar este problema, podemos utilizar una lista de puerto que definiremos a nuestro gusto:

```sh
./manage.py test --liveserver=localhost:8082,8090-8100,9000-9200,7041
```
Para demostrar como usar 'LiveServerTestCase', vamos a probar un ejemplo de test con Selenium. Para ello, antes de nada tenemos que instalarlo:

```sh
pip install selenium
```
Luego, hay que añadir el test a nuestro modulo de tests de la app:

```sh
from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver

class MySeleniumTests(LiveServerTestCase):
    fixtures = ['user-data.json']

    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_login(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/login/'))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys('myuser')
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys('secret')
        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()
```
Finalmente para ejecutar el test:

```sh
./manage.py test myapp.tests.MySeleniumTests.test_login
```

Este ejemplo automaticamente, abre Firefox y se va a la página de login, introduce los credenciales y presiona 'loguearse'. Selenium ofrece otros drivers en caso de no tener Firefox instalado. 

### Aserciones ###

Django también posee una gran cantidad de funciones dedicadas a las aserciones. Aquí indico algunas de las más interesantes:

* SimpleTestCase.assertRaisesMessage(expected_exception, expected_message, callable_obj=None, *args, **kwargs): Comprueba que cada ejecución tiene su mensaje correspondiente.

* SimpleTestCase.assertFieldOutput(fieldclass, valid, invalid, field_args=None, field_kwargs=None, empty_value=''): Comprueba que los campos del formulario se comportan correctamente.

* SimpleTestCase.assertFormError(response, form, field, errors, msg_prefix=''): Comprueba que los campos de un formulario no tiene errores al ser ejecutado.

* SimpleTestCase.assertContains(response, text, count=None, status_code=200, msg_prefix='', html=False): Comprueba que una respuesta aparece en el contenido indicado.

* SimpleTestCase.assertTemplateUsed(response, template_name, msg_prefix='', count=None): Comprueba que el template está siendo usado correctamente.

```sh
with self.assertTemplateUsed('index.html'):
    render_to_string('index.html')
with self.assertTemplateUsed(template_name='index.html'):
    render_to_string('index.html')
```
* SimpleTestCase.assertTemplateNotUsed(response, template_name, msg_prefix=''): Comprueba que el template no está siendo usado correctamente.

* SimpleTestCase.assertHTMLEqual(html1, html2, msg=None): Comprueba que dos string son iguales.

```sh
self.assertHTMLEqual('<p>Hello <b>world!</p>',
    '''<p>
        Hello   <b>world! <b/>
    </p>''')
self.assertHTMLEqual(
    '<input type="checkbox" checked="checked" id="id_accept_terms" />',
    '<input id="id_accept_terms" type='checkbox' checked>')
```

Aparte de todo esto, Django posee muchos tipos de asserts para HTML, JSON, JQUERY, XML y muchos más:

* SimpleTestCase.assertHTMLNotEqual(html1, html2, msg=None)

* SimpleTestCase.assertXMLNotEqual(xml1, xml2, msg=None)
...


### Enlaces de interés ###

* https://docs.djangoproject.com/en/dev/topics/testing/tools/#django.test.SimpleTestCase.assertInHTML
* https://docs.djangoproject.com/en/dev/topics/