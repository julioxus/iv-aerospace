## Integración continua con: Travis ##

![imagen](https://travis-ci.com/img/travis-mascot-200px.png)

En desarrolllo software, Travis CI es un servicio distribuido de integración continua usado para crear y testear proyectos de GitHub.

Se configura añadiendo un fichero llamado .travis.yml, que se trata de un fichero tipo YAML, al directorio root del repositorio de GitHub.

Travis CI automáticamente detecta ( al igual que Shippable ) cuando se ha realizado un commit y push al repositorio de GitHub, y cada vez que esto ocurre, se intentará montar el proyecto y ejecutar tests sobre él.

Ofrece soporte para múltiples lenguajes de programación.

Una de las ventajas más claras de usar Travis CI es que el entorno de integración continua esta compuesto de multiples runtimes (Node.js, o versiones de PHP, por ejemplo) o data stores. De este modo, podemos probar nuestras librerías o aplicaciones contra distintas configuraciones sin tener que tenerlas instaladas localmente. Tienen varias maquinas virtuales preparadas para cada combinación, allí puedes instalar MySQL o lo que necesites.

Lo podemos enganchar sencillamente con nuestro repositorio público de Github en un par de pasos para darle acceso de lectura a nuestro código y definir los test necesarios. Realmente la documentación está bastante bien explicada y detallada cada proceso, así como las herramientas de terceros y recursos, así como la guía de desarrolladores con la propia API de Travis CI.

Este [enlace](https://travis-ci.org/julioxus/iv-aerospace/builds) muestra el historial de builds del proyecto realizadas con Travis.