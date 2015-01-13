import os
import urllib
from google.appengine.api import users
from google.appengine.ext import ndb
import jinja2
import webapp2
from datetime import datetime

class Usuario(ndb.Model):
  usuario = ndb.StringProperty()
  password = ndb.StringProperty()
  nombre = ndb.StringProperty()
  apellido = ndb.StringProperty()
  correo = ndb.StringProperty()
  telefono = ndb.StringProperty()

class registro_usuario(webapp2.RequestHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template_values={}
        template = JINJA_ENVIRONMENT.get_template('template/registro.html')
        self.response.write(template.render(template_values))
    def post(self):
        user = Usuario()
        user.usuario = self.request.get('usuario')
        user.password = self.request.get('password')
        user.nombre = self.request.get('nombre')
        user.apellido = self.request.get('apellido')
        user.correo = self.request.get('correo')
        user.telefono = self.request.get('telefono')

        user.put()

        self.response.write('El usuario se ha registrado correstamente')

class consulta_usuario(webapp2.RequestHandler):
    def get(self):
        usuarios = []
        result = Usuario.query()
        for usuario in result:
            usuarios.append(usuario)
            print usuario
        self.response.headers['Content-Type'] = 'text/html'
        template_values = {'usuarios':usuarios}
        template = JINJA_ENVIRONMENT.get_template('template/consulta_usuario.html')
        self.response.write(template.render(template_values))

application = webapp2.WSGIApplication([
    ('/reg_usuario', registro_usuario),
    ('/consulta_usuario', consulta_usuario)
], debug=True)

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader('./'),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
