# Señales y Sistemas

En este repositorio hay algunos scripts (Python 3) preparados para
mostrar algunos aspectos de los temas cubiertos en el curso de Señales
y Sistemas de la carrera de Ingeniería Eléctrica (Facultad de
Ingeniería, Universidad de la República)

Los scripts están disponibles en https://github.com/seys-fing/scripts
bajo el formato de Jupyter Notebooks (*.ipynb). Este formato permite
ejecutar de forma interactiva scripts de varios lenguajes a través de
un navegador web.

## Qué es un Jupyter Notebook?

Un "notebook" o "cuaderno" es un documento que contiene código
ejecutable, texto enriquecido (Markup), figuras, enlaces, ecuaciones,
etc. Debido a la combinación de elementos de código y texto, estos
documentos permiten reunir la descripción y análisis de un programa o
scripts, así como sus resultados y el análisis de datos en tiempo
real.

La aplicación Jupyter Notebook produce estos documentos.

## Cómo ejecutarlos?

Los notebooks están compuestos por celdas (cells) de dos tipos. Uno de
los tipos de celdas es de código en algún lenguaje (Python 3 en
nuestro caso). El otro tipo es texto enriquecido. Cada una de las
celdas se puede ejecutar (run), en caso de ser una celda de código,
este se interpreta y produce los resultados que en caso de ser
necesario son desplegados (texto, gráficas, etc.). 

Las celdas deben ejecutarse en el orden natural para que el código se
vaya corriendo de forma correcta. Sin embargo, también es posible
modificar una celda de código y volver a ejecutarla sin necesidad de
volver a ejecutar una celda anterior. De esta forma se puede modificar
algún parámetro y evaluar los cambios sin necesidad de ejecutar todo
el código nuevamente.

Para ejecutar un Jupyter Notebook es necesaria una aplicación
corriendo en un servidor. Esto se puede hacer con instalaciones
locales de entornos Python, por ejemplo, Anaconda o Miniconda. Una
forma de ejecutar los notebooks sin necesidad de instalar un entorno
en un servidor propio es a través de servidores que permiten cargar y
ejecutar notebooks de forma interactiva. Las siguientes dos opciones
se presentan para correr los scripts que iremos haciendo públicos.

* Se puede ejecutar de forma interactiva a través del siguiente enlace
sin necesidad de crear un usuario
https://mybinder.org/v2/gh/seys-fing/scripts/master


[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/seys-fing/scripts/master)

Luego de cargado el servidor se muestra un conjunto de archivos. Los
archivos de extensión ipynb son notebooks ejecutables, se abren
haciendo click sobre ellos.

* También pueden verse los archivos *.ipynb desde el GitHub
seleccionándolos. En este caso los notebooks nos son ejecutables
interactivamente, pero se les ofrece un link a través de una imagen
para abrir el notebook en el entorno Colaboratory de Google y
ejecutarlo interactivamente desde ahí; se precisa un usuario de
GMail. Para esto se puede seguir el enlace de "Open in Colab"
(![Colab](https://colab.research.google.com/assets/colab-badge.svg)).
