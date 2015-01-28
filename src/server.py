#!/usr/bin/python
# -⁻- coding: UTF-8 -*-
#-------------------------------------------------------------------------------------------------------
# Aplicación Web de las asignaturas Diseño de aplicaciones para internet y Infraestructura virtual
#
# Desarrolladores:
#	Óscar Sánchez Martínez
#	Julio Martínez Martínez-Checa
#	Hans Manuel Grenner Noguerón
#	Juan Francisco Rodríguez Vilchez
#	Jose Antonio Plata Muñoz
#	Miguel Martínez Castellanos
#	Cristina Rosillo Arenas
#
# Aplicación desarrollada para el Proyecto UGR Aerospace Program
#
# En este archivo se encuentra las diferentes clases que administran la aplicación.
# Aplicación desplegada en el Paas Google App Engine : http://ugraerospaceprogram.appspot.com/
# 
# Utilización de la tecnología de Google para el desarrollo de la Aplicación.
# IVAerospace Copyright (C) 2014 - ivaerospace2014@gmail.com This program is free software: you can 
# redistribute it and/or modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even 
# the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public 
# License for more details.
#
#-------------------------------------------------------------------------------------------------------

from google.appengine.ext import ndb


from google.appengine.ext.webapp.util import run_wsgi_app
import os
import webapp2
import jinja2
import feedparser
import random
import json
import math
import datetime
import time
import urllib

# Clase que administra las urls no válidas de la aplicación.

class ErrorPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template_values={}
        template = JINJA_ENVIRONMENT.get_template('template/error.html')
        self.response.write(template.render(template_values))

# Clase que administra la página principal de la aplicación.

class MainPage(webapp2.RequestHandler):
    
    
    def get(self):
        
        if self.request.cookies.get("logged") == "true":
            username = str(self.request.cookies.get("username"))
            self.response.headers['Content-Type'] = 'text/html'
            rss = feedparser.parse('http://www.sondasespaciales.com/portada/feed/')
            titulos = []
            links = []
            descripciones = []
    
            for i in range (len(rss.entries)):

                titulos.append(rss.entries[i].title)
                links.append(rss.entries[i].link)
                descripcion = rss.entries[i].description
                descripciones.append(descripcion)
    
            template_values={'titulos':titulos, 'links':links, 'descripciones':descripciones,'sesion':username}
            template = JINJA_ENVIRONMENT.get_template('template/index_loged.html')
            self.response.write(template.render(template_values))
        else:
                
            self.response.headers['Content-Type'] = 'text/html'
            
            rss = feedparser.parse('http://www.sondasespaciales.com/portada/feed/')
            
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

#Clase que devuelve la información del proyecto.

class InfoPage(webapp2.RequestHandler):
    
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template_values={}
        template = JINJA_ENVIRONMENT.get_template('template/info_proyecto.html')
        self.response.write(template.render(template_values))

#Clase que devuelve un formulario de registro.

class FormularioRegistro(webapp2.RequestHandler):
    
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = JINJA_ENVIRONMENT.get_template('template/registro.html')
        self.response.write(template.render(message=""))

#Clase donde se define el modelo del usuario de la base de datos.

class Usuario(ndb.Model):
    usuario = ndb.StringProperty()
    password = ndb.StringProperty()
    nombre = ndb.StringProperty()
    apellido = ndb.StringProperty()
    correo = ndb.StringProperty()
    telefono = ndb.StringProperty()

#Clase que registra al usuario si pasa las restricciones.

class registro_usuario(webapp2.RequestHandler):
    
    def post(self):
        user = Usuario()
        usu=self.request.get('usuario')
        aparece=0
        result = Usuario.query()
        for us in result:
            if us.usuario == usu: #Si el usuario aparece, se muestra mensaje de error: usuario existente
                aparece=1
                self.response.headers['Content-Type'] = 'text/html'
                template = JINJA_ENVIRONMENT.get_template('template/registro.html')
                self.response.write(template.render(message="El usuario ya se encuentra registrado en la base de datos"))
 
        if aparece != 1:    #Si no aparece se cogen los datos introducidos en el formulario y se introducen en la base de datos
            
            user.usuario = self.request.get('usuario')
            user.password = self.request.get('password')
            user.nombre = self.request.get('nombre')
            user.apellido = self.request.get('apellido')
            user.correo = self.request.get('correo')
            user.telefono = self.request.get('telefono')
                        
            user.put()
                
            self.redirect('/')

#Clase que permite editar los campos de los usuarios.

class editar_perfil(webapp2.RequestHandler):
    def get(self):
        if self.request.cookies.get("logged") == "true":  #Si la cookie está activada
            username = str(self.request.cookies.get("username"))
            usuarios = []
            result=Usuario.query(Usuario.usuario==username)	#Se consulta dicho usuario en la base de datos y se añade a un array de ususarios
            if result>0:
                for usuario in result:
                    usuarios.append(usuario)
                self.response.headers['Content-Type'] = 'text/html'
                template_values = {'usuarios':usuarios,'sesion':username}
                template = JINJA_ENVIRONMENT.get_template('template/editar_perfil.html')
                self.response.write(template.render(template_values,message=""))
        else:
            self.redirect('/')
            
        
    def post(self):
        if self.request.cookies.get("logged") == "true":
            username = str(self.request.cookies.get("username"))
            result = Usuario.query()
            for us in result:
                if us.usuario == username:			# Se hace un put de los datos nuevos a la base de datos
                    us.password = self.request.get('password')
                    us.nombre = self.request.get('nombre')
                    us.apellido = self.request.get('apellido')
                    us.correo = self.request.get('correo')
                    us.telefono = self.request.get('telefono')
                            
                    us.put()
                    
                    self.redirect('/loged')

#Clase que devuelve la gráfica de temperatura.

class highchart_temperatura(webapp2.RequestHandler):
    def get(self):
        if self.request.cookies.get("logged") == "true":
            username = str(self.request.cookies.get("username"))
            template_values={'sesion':username}
            self.response.headers['Content-Type'] = 'text/html'
            template = JINJA_ENVIRONMENT.get_template('template/highchart_temperatura.html')
            self.response.write(template.render(template_values))
        else:
            self.redirect('/')

#Clase que devuelve la gráfica de velocidad del viento.

class highchart_velocidadviento(webapp2.RequestHandler):
    def get(self):
        if self.request.cookies.get("logged") == "true":
            username = str(self.request.cookies.get("username"))
            template_values={'sesion':username}
            self.response.headers['Content-Type'] = 'text/html'
            template = JINJA_ENVIRONMENT.get_template('template/highchart_velocidadviento.html')
            self.response.write(template.render(template_values))
        else:
            self.redirect('/')

#Clase que devuelve la gráfica de humedad

class highchart_humedad(webapp2.RequestHandler):
    def get(self):
        if self.request.cookies.get("logged") == "true":
            username = str(self.request.cookies.get("username"))
            template_values={'sesion':username}
            self.response.headers['Content-Type'] = 'text/html'
            template = JINJA_ENVIRONMENT.get_template('template/highchart_humedad.html')
            self.response.write(template.render(template_values))
        else:
            self.redirect('/')

#Clase que devuelve la gráfica de precipitación.

class highchart_precipitacion(webapp2.RequestHandler):
    def get(self):
        if self.request.cookies.get("logged") == "true":
            username = str(self.request.cookies.get("username"))
            template_values={'sesion':username}
            self.response.headers['Content-Type'] = 'text/html'
            template = JINJA_ENVIRONMENT.get_template('template/highchart_precipitacion.html')
            self.response.write(template.render(template_values))
        else:
            self.redirect('/')


# Variables globales.
        
temperaturas = []
humedades = []
precipitaciones = []
velocidades = []
media_velocidades=0
media_temperaturas=0
direccion_viento=""
direccion_racha=0
media_rachas=""
media_precipitaciones=0
media_presiones=0
media_tendencias=0
media_humedades=0
ARRAY_LIMIT = 50

#Clase que genera los datos de la gráfica de temperatura en la monitorización.
        
class datos_temperatura(webapp2.RequestHandler):
    def get(self):
        
        global temperaturas
        global media_velocidades
        global direccion_viento
        global direccion_racha
        global media_rachas
        global media_precipitaciones
        global media_presiones
        global media_tendencias
        global media_humedades
        global media_temperaturas
        global ARRAY_LIMIT

        
        num = float(random.random()*50)
        temperaturas.append(num)
        if len(temperaturas) == ARRAY_LIMIT:
            
            sum = 0
            for i in temperaturas:
                sum+=i
            media_temperaturas = round(sum/len(temperaturas),3)

            temperaturas = []
               
        self.response.write(json.dumps(num))

#Clase que genera los datos de la gráfica de velocidad del viento en la monitorización.
        
class datos_velocidadviento(webapp2.RequestHandler):
    def get(self):
        global velocidades
        global media_velocidades
        global direccion_viento
        global direccion_racha
        global media_rachas
        global media_precipitaciones
        global media_presiones
        global media_tendencias
        global media_humedades
        global media_temperaturas
        global ARRAY_LIMIT

        num = float(random.random()*100)
        velocidades.append(num)
        if len(velocidades) == ARRAY_LIMIT:
            sum = 0
            for i in velocidades:
                sum+=i
            media_velocidades = round(sum/len(velocidades),3)       
            velocidades = []
            
        self.response.write(json.dumps(num))

#Clase que genera los datos de la gráfica de humedad en la monitorización.
       
class datos_humedad(webapp2.RequestHandler):
    def get(self):
        global humedades
        global media_velocidades
        global direccion_viento
        global direccion_racha
        global media_rachas
        global media_precipitaciones
        global media_presiones
        global media_tendencias
        global media_humedades
        global media_temperaturas
        global ARRAY_LIMIT

        num = float(random.random()*100)
        humedades.append(num)
        if len(humedades) == ARRAY_LIMIT:
            sum = 0
            for i in humedades:
                sum+=i
            media_humedades = round(sum/len(humedades),3)       
            humedades =[]
        self.response.write(json.dumps(num))

#Clase que genera los datos de la gráfica de precipitacion en la monitorización y genera media de los datos.

class datos_precipitacion(webapp2.RequestHandler):
    def get(self):
        global precipitaciones
        global media_velocidades
        global direccion_viento
        global direccion_racha
        global media_rachas
        global media_precipitaciones
        global media_presiones
        global media_tendencias
        global media_humedades
        global media_temperaturas
        global ARRAY_LIMIT

        
        num = int(random.random()*3)
         
        if num == 0: 
            direccion_viento = 'norte'
        elif num == 1:
            direccion_viento = 'sur'
        elif num == 2:
            direccion_viento = 'este'
        elif num == 3:
            direccion_viento = 'oeste'
        
        num = int(random.random()*3)
         
        if num == 0: 
            direccion_racha = 'norte'
        elif num == 1:
            direccion_racha = 'sur'
        elif num == 2:
            direccion_racha = 'este'
        elif num == 3:
            direccion_racha = 'oeste'
            
        media_rachas = round(float(random.random()*30),3)
        media_presiones = round(float(random.random()*100) + 900,3)
        media_tendencias = round(float(random.random()*4) - 2,3)
        
        num = float(random.random()*20)
        precipitaciones.append(num)
        
        print len(precipitaciones)
        if len(precipitaciones) == ARRAY_LIMIT:
            sum = 0
            for i in precipitaciones:
                sum+=i
            media_precipitaciones = round(sum/len(precipitaciones),3)
            datos = TablaDatos()
            datos.fecha = datetime.datetime.strptime(time.strftime("%d/%m/%Y"), '%d/%m/%Y')
            datos.hora = datetime.datetime.now().strftime('%H:%M:%S')
            datos.temperatura = float(media_temperaturas)
            
            datos.velocidadViento = float(media_velocidades)
            datos.direccionViento = direccion_viento
            datos.racha = float(media_rachas)
            datos.direccionRacha = direccion_racha
            datos.precipitacion = float(media_precipitaciones)
            datos.presion = float(media_presiones)
            datos.tendencia = float(media_tendencias)
            datos.humedad = float(media_humedades)
             
            datos.put()     
            precipitaciones = []        

        self.response.write(json.dumps(num))

# Clase que genera datos aleatorios para las gráficas de temperatura.

class datos_temperatura2(webapp2.RequestHandler):
    def get(self):
        num = int(random.random()*50)
        self.response.write(json.dumps(num))    

# Clase que genera datos aleatorios para las gráficas de velocidad de viento.

class datos_velocidadviento2(webapp2.RequestHandler):
    def get(self):
        num = int(random.random()*100)
        self.response.write(json.dumps(num))

# Clase que genera datos aleatorios para las gráficas de humedad.
     
class datos_humedad2(webapp2.RequestHandler):
    def get(self):
        num = int(random.random()*100)
        self.response.write(json.dumps(num))

# Clase que genera datos aleatorios para las gráficas de precipitación.

class datos_precipitacion2(webapp2.RequestHandler):
    def get(self):
        num = int(random.random()*20)
        self.response.write(json.dumps(num))    

# Clase que define el modelo de la tabla de datos para la base de datos.

class TablaDatos(ndb.Model):
    fecha = ndb.DateProperty();
    hora = ndb.StringProperty();
    temperatura = ndb.FloatProperty()
    velocidadViento = ndb.FloatProperty()
    direccionViento = ndb.StringProperty()
    racha = ndb.FloatProperty()
    direccionRacha = ndb.StringProperty()
    precipitacion = ndb.FloatProperty()
    presion = ndb.FloatProperty()
    tendencia = ndb.FloatProperty()
    humedad = ndb.FloatProperty()

# Clase que genera la monitorización del dron.

class monitor(webapp2.RequestHandler):
    def get(self):
        if self.request.cookies.get("logged") == "true":
            username = str(self.request.cookies.get("username"))
            template_values={'sesion':username}
            self.response.headers['Content-Type'] = 'text/html'
            template = JINJA_ENVIRONMENT.get_template('template/monitor.html')
            self.response.write(template.render(template_values))
        else:
            self.redirect('/')

# Clase que devuelve información para mandar tweets

class twitter(webapp2.RequestHandler):
    def get(self):
        if self.request.cookies.get("logged") == "true":
            username = str(self.request.cookies.get("username"))
            template_values={'sesion':username}
            self.response.headers['Content-Type'] = 'text/html'
            template = JINJA_ENVIRONMENT.get_template('template/contacto.html')
            self.response.write(template.render(template_values))
        else:
            self.redirect('/')
        
lat = 37.19699469878369
lng =  -3.6241040674591507
grados = 0

# Clase que genera las coordenadas del dron.

class coordenadas(webapp2.RequestHandler):
    def get(self):
        global lat
        global lng
        global grados
        grados+=5
        lat += 0.00001 * math.cos((grados/180)*math.pi)
        lng += 0.00001 * math.sin((grados/180)*math.pi)
        latLng = [lat, lng]
        self.response.write(json.dumps(latLng))

# Clase que implementa el login de usuarios guardando la sesión en una cookie.

class loguearse(webapp2.RequestHandler):
    
    def post(self):
        usu=self.request.get('usuario')
        result=Usuario.query(Usuario.usuario==usu)
        usur=result.get()
        if usur is not None:
            usur=result.get()
            pas=self.request.get('password')
            if usur.password==pas:
                self.response.headers.add_header('Set-Cookie',"logged=true")
                self.response.headers.add_header('Set-Cookie',"username="+str(usur.usuario))

                
                self.response.headers['Content-Type'] = 'text/html'
                rss = feedparser.parse('http://www.sondasespaciales.com/portada/feed/')
                titulos = []
                links = []
                descripciones = []
        
                for i in range (len(rss.entries)):

                    titulos.append(rss.entries[i].title)
                    links.append(rss.entries[i].link)
                    descripcion = rss.entries[i].description
                    descripciones.append(descripcion)
        
                template_values={'titulos':titulos, 'links':links, 'descripciones':descripciones,'sesion':usur.usuario}
                template = JINJA_ENVIRONMENT.get_template('template/index_loged.html')
                self.response.write(template.render(template_values))
            else:
                self.response.headers['Content-Type'] = 'text/html'
                rss = feedparser.parse('http://www.sondasespaciales.com/portada/feed/')
        
                titulos = []
                links = []
                descripciones = []
        
                for i in range (len(rss.entries)):

                    titulos.append(rss.entries[i].title)
                    links.append(rss.entries[i].link)
                    descripcion = rss.entries[i].description
                    descripciones.append(descripcion)
        
                template_values={'titulos':titulos, 'links':links, 'descripciones':descripciones,'mensaje':'Password incorrecto.'}
                template = JINJA_ENVIRONMENT.get_template('template/index.html')
                self.response.write(template.render(template_values))
        else:
            self.response.headers['Content-Type'] = 'text/html'
            rss = feedparser.parse('http://www.sondasespaciales.com/portada/feed/')
        
            titulos = []
            links = []
            descripciones = []
        
            for i in range (len(rss.entries)):

                titulos.append(rss.entries[i].title)
                links.append(rss.entries[i].link)
                descripcion = rss.entries[i].description
                descripciones.append(descripcion)
        
            template_values={'titulos':titulos, 'links':links, 'descripciones':descripciones,'mensaje':'Usuario incorrecto.'}
            template = JINJA_ENVIRONMENT.get_template('template/index.html')
            self.response.write(template.render(template_values))

# Clase que cierra la sesión del usuario.

class cerrar_sesion(webapp2.RequestHandler):
    def get(self):
        self.response.headers.add_header("Set-Cookie", "logged=; Expires=Thu, 01-Jan-1970 00:00:00 GMT")
        self.response.headers.add_header("Set-Cookie", "username=; Expires=Thu, 01-Jan-1970 00:00:00 GMT")
        self.redirect('/')

# Clase que muestra las medias de los datos monitorizados.

class Estadisticas(webapp2.RequestHandler):
    def get(self):
        if self.request.cookies.get("logged") == "true":
            username = str(self.request.cookies.get("username"))
            self.response.headers['Content-Type'] = 'text/html'
            template = JINJA_ENVIRONMENT.get_template('template/estadisticas.html')
            
            lista = TablaDatos.query()
            
            datos_hoy = []
            datos_semana = []
            datos_mes = []
                    
            for dato in lista:
                if dato.fecha.strftime("%d/%m/%Y") == time.strftime("%d/%m/%Y"):
                    datos_hoy.append(dato)
                    
                if dato.fecha.strftime("%m/%Y") == time.strftime("%m/%Y"):
                    datos_mes.append(dato)
                
                dia_dato = int(dato.fecha.strftime("%d"))
                mes_dato = int(dato.fecha.strftime("%m"))
                anio_dato = int(dato.fecha.strftime("%Y"))
                
                dia_actual = int(time.strftime("%d"))
                mes_actual = int(time.strftime("%m"))
                anio_actual = int(time.strftime("%Y"))
                
                if datetime.date(anio_actual, mes_actual, dia_actual).isocalendar()[1] == datetime.date(anio_dato, mes_dato, dia_dato).isocalendar()[1]:
                    datos_semana.append(dato)
                    
            template_values={'datos_hoy':datos_hoy, 'datos_mes':datos_mes, 'datos_semana':datos_semana,'sesion':username}
            
            self.response.write(template.render(template_values))
        else:
            self.redirect('/')

# Clase que devuelve los términos y condiciones de la aplicación.

class terms(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        template = JINJA_ENVIRONMENT.get_template('template/terms.html')
        self.response.write(template.render())
        
        
        import httplib

# Clase que comprueba que las urls son válidas y devuelven páginas html. En caso negativo no se pasa el test. 
   
class Tests(webapp2.RequestHandler):
    
    def get(self):
        self.response.write('TEST')

#Test inicial para probar si los test funcionan, usando el cuadrado de un número

    def testInicial(self, numero=0):
        return numero*numero

#Test que testea cada una de las url, si alguna no funciona bien se devuelve false

    def testURL(self):  
        
        urls_test = [ '/', '/error', '/twitter', '/registrarse', '/info_page', '/editar_perfil', '/highchart_temperatura',
              '/highchart_precipitacion', '/highchart_humedad', '/highchart_velocidadviento', '/monitor', '/estadisticas', '/cerrar_sesion']
        
        for url in urls_test:
            response=urllib.urlopen('http://ugraerospaceprogram.appspot.com' + url)
            if response.getcode() >= 400:
                return False
                
        return True


#Comprueba si la página web está activa

    def testPaginaActiva(self):

	response=rullib.urlopen('http://ugraerospaceprogram.appspot.com')
	if response:
	        return True
	return False

# urls de la aplicación.

urls = [('/',MainPage),
        ('/error',ErrorPage),
        ('/twitter',twitter),
        ('/registrarse',FormularioRegistro),
        ('/info_page',InfoPage),
        ('/reg_usuario', registro_usuario),
        ('/editar_perfil',editar_perfil),
        ('/highchart_temperatura', highchart_temperatura),
        ('/highchart_velocidadviento', highchart_velocidadviento),
        ('/highchart_humedad', highchart_humedad),
        ('/highchart_precipitacion', highchart_precipitacion),
        ('/datos_temperatura', datos_temperatura),
        ('/datos_velocidadviento', datos_velocidadviento),
        ('/datos_humedad', datos_humedad),
        ('/datos_precipitacion', datos_precipitacion),
        ('/datos_temperatura2', datos_temperatura2),
        ('/datos_velocidadviento2', datos_velocidadviento2),
        ('/datos_humedad2', datos_humedad2),
        ('/datos_precipitacion2', datos_precipitacion2),
        ('/cerrar_sesion', cerrar_sesion),
        ('/loguearse',loguearse),
        ('/monitor', monitor),
        ('/coordenadas', coordenadas),
        ('/estadisticas',Estadisticas),
        ('/Tests', Tests),
        ('/.*', ErrorPage)
       ]



application = webapp2.WSGIApplication(urls, debug=True)

# Declaración del entorno de jinja2 y el sistema de templates.

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

# Despliega la aplicación al ejecutar el archivo como script. 

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
