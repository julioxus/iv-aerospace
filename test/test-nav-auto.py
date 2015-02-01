from splinter import Browser
from time import time
def registro():
	browser = Browser()
	browser.visit('http://ugraerospaceprogram.appspot.com/')
	print "Iniciando registro"
	browser.find_by_id('registro').click()
	browser.fill('usuario', 'test')
	browser.fill('password', '12345')
	browser.fill('nombre', 'Paco')
	browser.fill('apellido', 'del rozal')
	browser.fill('correo', 'pacorozal@gmail.com')
	browser.fill('telefono', '958956789')
	browser.find_by_id('checkit').click()
	browser.find_by_id('envia').click()
	browser.quit()

def navegacion(num):
	try:
		browser = Browser()
		browser.visit('http://ugraerospaceprogram.appspot.com/')
		print "Iniciando prueba "
		browser.fill('usuario', 'test')
		browser.fill('password', '12345')
		browser.find_by_name('init_sesion').click()
		
		browser.find_by_name('btn_editar').click()
		browser.find_by_name('btn_inicio').click()
		browser.find_by_name('btn_monitorizacion').click()

		browser.find_by_id('tipoGrafica-temp').find_by_id('element_line_temp').click()
		browser.find_by_id('botonGrafica-temp').click()

		browser.find_by_id('tipoGrafica-velocidadviento').find_by_id('element_line_v').click()
		browser.find_by_id('botonGrafica-velocidadviento').click()

		browser.find_by_id('tipoGrafica-humedad').find_by_id('element_line_h').click()
		browser.find_by_id('botonGrafica-humedad').click()

		browser.find_by_id('tipoGrafica-precipitacion').find_by_id('element_line_p').click()
		browser.find_by_id('botonGrafica-precipitacion').click()

		browser.find_by_name('btn_estadisticas').click()

		browser.find_by_name('btn_twitter').click()
		
		browser.find_by_id('boton-cerrar').click()
		browser.execute_script("alert('Navegacion acabada');")
		browser.quit()
		return True
	except:
		return False
print "iniciando registro de prueba"
registro()
print "iniciando test"
tim=0.0
rango=5
for i in range(rango):
	start_time = time()
	var=navegacion(i)
	elapsed_time = time() - start_time
	if var == True:
		tim=tim + elapsed_time
tim=tim/float(rango)
print("Tiempo medio: %.10f segundos." % tim)

