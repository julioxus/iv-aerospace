#Webapp2
Webapp2 es un framework para aplicaciones web basado en python, que por defecto viene instalado en el entorno de
desarrollo de GAE, por tanto no necesitamos enlazarlo. Nos permite crear las URL y la gestión de los GET /POST
de nuestra aplicación Web. Es considerado un framework ligero.

Para utilizar Webapp2 simplemente tenemos que hacer un import de webapp2:
`import webapp2`

Ejemplo de código sencillo:

```
import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.write('Hello, World!')

application = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True) 
```

Lo que hacemos básicamente es definir un Request Handler (MainPage) asociado a la raíz. Cuando webbapp2 recibe una solicitud GET HTPP a la dirección /, se crea una instancia de la clase MainPage y llama al método get de la instancia. Dentro de éste, la información sobre la solicitud la tenemos disponible en "self.request"


# Jinja2

Jinja2 es un motor de plantillas para Python (inspirado en el sistema de plantilas de Django). Lo hemos utilizado para renderizar el código dinámicos de las 
páginas HTML. Consideramos que es una muy buena opción para generar contenido basado en plantillas e independizarlas del código. Aparte nos permite trabajar con cualquier framework que queramos.

Para instalar Jinja2:

pip install jinja2

Jinja2 es compatible con Python 3.




