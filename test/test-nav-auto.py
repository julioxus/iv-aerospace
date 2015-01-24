from splinter import Browser

browser = Browser()
browser.visit('http://ugraerospaceprogram.appspot.com/')
browser.fill('usuario', 'osquiya')
browser.fill('password', '12345')
browser.find_by_name('init_sesion').click()
print "Iniciando sesion"
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
print "cerrando sesion"
browser.find_by_id('boton-cerrar').click()
browser.execute_script("alert('Navegacion acabada');")
browser.quit()


