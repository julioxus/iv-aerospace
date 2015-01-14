
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

from google.appengine.ext.webapp.util import run_wsgi_app
import os
import webapp2
import jinja2
import feedparser


class ErrorPage(webapp2.RequestHandler):
    
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template_values={}
        template = JINJA_ENVIRONMENT.get_template('template/error.html')
        self.response.write(template.render(template_values))
        
class MainPage(webapp2.RequestHandler):
    
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        
        rss = feedparser.parse('http://www.sti.nasa.gov/scan/rss99-01.xml')
        
        titulos = []
        links = []
        descripciones = []
        
        for i in range (len(rss.entries)):

            titulos.append(rss.entries[i].title)
            links.append(rss.entries[i].link)
            descripcion = rss.entries[i].description
            descripciones.append(descripcion)
        
        template_values={'titulos':titulos, 'links':links, 'descripciones':descripciones}
        template = JINJA_ENVIRONMENT.get_template('template/index.html')
        self.response.write(template.render(template_values))
        
class InfoPage(webapp2.RequestHandler):
    
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template_values={}
        template = JINJA_ENVIRONMENT.get_template('template/info_proyecto.html')
        self.response.write(template.render(template_values))
        
class FormularioRegistro(webapp2.RequestHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template_values={}
        template = JINJA_ENVIRONMENT.get_template('template/registro.html')
        self.response.write(template.render(template_values))

class Usuario(ndb.Model):
    usuario = ndb.StringProperty()
    password = ndb.StringProperty()
    nombre = ndb.StringProperty()
    apellido = ndb.StringProperty()
    correo = ndb.StringProperty()
    telefono = ndb.StringProperty()

class registro_usuario(webapp2.RequestHandler):
    
    def post(self):
        user = Usuario()
        usu=self.request.get('usuario')
        result = Usuario.query()
        for usuario in result:
            if usuario == usu:
                self.response.write('El usuario ya existe en la base de datos')
                self.redirect('/reg_usuario')

        user.usuario = self.request.get('usuario')
        user.password = self.request.get('password')
        user.nombre = self.request.get('nombre')
        user.apellido = self.request.get('apellido')
        user.correo = self.request.get('correo')
        user.telefono = self.request.get('telefono')
                
        user.put()
        
        self.redirect('/')


class consulta_usuario(webapp2.RequestHandler):
    def get(self):
        usuarios = []
        result = Usuario.query()
        for usuario in result:
            usuarios.append(usuario)
        self.response.headers['Content-Type'] = 'text/html'
        template_values = {'usuarios':usuarios}
        template = JINJA_ENVIRONMENT.get_template('template/consulta_usuario.html')
        self.response.write(template.render(template_values))

urls = [('/',MainPage),
        ('/error',ErrorPage),
        ('/registrarse',FormularioRegistro),
        ('/info_page',InfoPage),
        ('/reg_usuario', registro_usuario),
        ('/consulta_usuario', consulta_usuario),
       ]
application = webapp2.WSGIApplication(urls, debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
