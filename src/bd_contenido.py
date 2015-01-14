import cgi
import webapp2

from google.appengine.ext import ndb
from google.appengine.ext.webapp.util import run_wsgi_app

class TablaDatos(ndb.Model):
   temperatura = ndb.FloatProperty()
   velocidadViento = ndb.IntegerProperty()
   direccionViento = ndb.StringProperty()
   racha = ndb.IntegerProperty()
   direccionRacha = ndb.StringProperty()
   precipitacion = ndb.IntegerProperty()
   presion = ndb.FloatProperty()
   tendencia = ndb.FloatProperty()
   humedad = ndb.IntegerProperty()
   
class Principal(webapp2.RequestHandler):
     def get(self):
         self.response.out.write("""
         <html>
         <head></head>
         <body>
             <h3> Menú Principal</h3>
             <a href="formulario">Insertar nuevos datos</a><br>
             <a href="listar">Mostrar datos</a>
             </form>
         </body>
         </html>    
         """)

class FormularioInsercion(webapp2.RequestHandler):
     def get(self):
         self.response.out.write("""
         <html>
         <head></head>
         <body>
             <h3> Inserción datos </h3>
             <form action="guardarDatos" method="post">
                 <div>Temperatura (ºC): <input type="text" name="temperatura"></div>
                 <div>Velocidad del viento (km/h): <input type="text" name="velocidadViento"></div>
                 <div>Dirección del viento: <input type="text" name="direccionViento"></div>
                 <div>Racha (km/h): <input type="text" name="racha"></div>
                 <div>Dirección de racha: <input type="text" name="direccionRacha"></div>
                 <div>Precipitación (mm): <input type="text" name="precipitacion"></div>
                 <div>Presión (hPa): <input type="text" name="presion"></div>
                 <div>Tendencia (hPa): <input type="text" name="tendencia"></div>
                 <div>Humedad (%): <input type="text" name="humedad"></div>
                 
                 <div><input type="submit" value="Guardar"></div>
             </form>
         </body>
         </html>        
         """)
 
class InsertarDatos(webapp2.RequestHandler):
     def post(self):
         self.response.out.write("<html><head></head><body>")
       
         temperatura = cgi.escape(self.request.get('temperatura'))
         velocidadViento = cgi.escape(self.request.get('velocidadViento'))
         direccionViento = cgi.escape(self.request.get('direccionViento'))
         racha = cgi.escape(self.request.get('racha'))
         direccionRacha = cgi.escape(self.request.get('direccionRacha'))
         precipitacion = cgi.escape(self.request.get('precipitacion'))
         presion = cgi.escape(self.request.get('presion'))
         tendencia = cgi.escape(self.request.get('tendencia'))
         humedad = cgi.escape(self.request.get('humedad'))
         
         datos = TablaDatos()
         datos.temperatura = float(temperatura)
         datos.velocidadViento = int(velocidadViento)
         datos.direccionViento = direccionViento
         datos.racha = int(racha)
         datos.direccionRacha = direccionRacha
         datos.precipitacion = int(precipitacion)
         datos.presion = float(presion)
         datos.tendencia = float(tendencia)
         datos.humedad = int(humedad)
         
         datos.put()
         
         self.response.out.write("<h3>Datos guardados</h3>")
         self.response.out.write("""<a href="/formulario">Insertar otro</a>""")
         self.response.out.write("""<a href="/">Volver al menú principal</a>""")
         self.response.out.write("</body></html>")

         
class ListarDatos(webapp2.RequestHandler):
     def get(self):
         self.response.out.write("""
         <html>
             <head></head>
         <body>
             <table>
                 <tr>
                     <td><strong>Temperatura (ºC)</strong></td>
                     <td><strong>Velocidad del viento (km/h)</strong></td>
                     <td><strong>Dirección del viento</strong></td>
                     <td><strong>Racha (km/h)</strong></td>
                     <td><strong>Dirección de racha</strong></td>
                     <td><strong>Precipitación (mm)</strong></td>
                     <td><strong>Presión (hPa)</strong></td>
                     <td><strong>Tendencia (hPa)</strong></td>
                     <td><strong>Humedad (%)</strong></td>
                 </tr>
                 """)
         lista = ndb.Query()
         
         
         for datos in lista:
             self.response.out.write("<tr>")
             self.response.out.write("<td>" + str(datos.temperatura) + "</td>")
             self.response.out.write("<td>" + str(datos.velocidadViento) + "</td>")
             self.response.out.write("<td>" + datos.direccionViento + "</td>")
             self.response.out.write("<td>" + str(datos.racha) + "</td>")
             self.response.out.write("<td>" + datos.direccionRacha + "</td>")
             self.response.out.write("<td>" + str(datos.precipitacion) + "</td>")
             self.response.out.write("<td>" + str(datos.presion) + "</td>")
             self.response.out.write("<td> " + str(datos.tendencia) + "</td>")
             self.response.out.write("<td>" + str(datos.humedad) + "</td>")
             self.response.out.write("</tr></table>")
         
         self.response.out.write("""<a href="/">Principal</a>""")
         self.response.out.write("</body></html>")


app = webapp2.WSGIApplication([
  ('/', Principal),
  ('/formulario', FormularioInsercion),
  ('/guardarDatos', InsertarDatos),
  ('/listar', ListarDatos)], debug=True)

def main():
    run_wsgi_app(app)

if __name__ == "__main__":
    main()
