# Señales y Sistemas: visualización de ejemplos

El objetivo de los scripts o programas que presentamos es ver una
posible implementación de algunos métodos que vemos en el curso,
verificar resultados o ver ejemplos del tipo de procesamiento de
señales que se presentan.

Estos scripts se presentan en un repositorio de GitHub como scripts en
Python 3. Los scripts están disponibles en
https://github.com/seys-fing/scripts bajo el formato de Jupyter
Notebooks (*.ipynb). Este formato permite ejecutar de forma
interactiva scripts de varios lenguajes a través de un navegador web.

## Qué es un Jupyter Notebook?

Un "notebook" o "cuaderno" es un documento que contiene código
ejecutable, texto enriquecido (Markup), figuras, enlaces, ecuaciones,
etc. Debido a la combinación de elementos de código y texto, estos
documentos permiten reunir la descripción y análisis de un programa o
scripts, así como sus resultados y el análisis de datos en tiempo
real.

La aplicación Jupyter Notebook produce estos documentos.

## Cómo ejecutarlos?

Los notebooks están compuestos por celdas (cells) de dos tipos. Uno de los tipos de celdas es de código en algún lenguaje (Python 3 en nuestro caso). El otro tipo es texto enriquecido. Cada una de las celdas se puede ejecutar (run), en caso de ser una celda de código, este se interpreta y produce los resultados que en caso de ser necesario son desplegados (texto, gráficas, etc.). 

Las celdas deben ejecutarse en el orden natural para que el código se vaya corriendo de forma correcta. Sin embargo, también es posible modificar una celda de código y volver a ejecutarla sin necesidad de volver a ejecutar una celda anterior. De esta forma se puede modificar algún parámetro y evaluar los cambios sin necesidad de ejecutar todo el código nuevamente.

Para ejecutar un Jupyter Notebook es necesaria una aplicación corriendo en un servidor. Una forma de ejecutar los notebooks sin necesidad de instalar un entorno en un servidor propio es a través de servidores que permiten cargar y ejecutar notebooks de forma interactiva. Las siguientes opciones permiten correr los scripts que iremos haciendo públicos.

### Opción 1
Se puede acceder a los .ipynb de seys en GitHub y ejecutarlos de forma interactiva a través del siguiente enlace, sin necesidad de crear un usuario: https://mybinder.org/v2/gh/seys-fing/scripts/master.

A través de ese enalce se accede a los .ipynb del repositorio GitHub de seys (GitHub y MyBinder están conectados). Desde allí pueden ejecutarse directamente. Una vez que cargue el servidor, se muestra el conjunto de archivos .ipynb de seys. Los archivos de extensión .ipynb son notebooks ejecutables, se abren haciendo click sobre ellos. Cuando el .ipynb que se eligió esté abierto en mybinder, se pueden elegir una celda y correr el escript en ella desde la barra de herramientas.

### Opción 2
Desde el entorno de desarrollo [Colaboratory](https://colab.research.google.com/) puede seleccionarse GitHub, y abrir el GitHub de seys con el enlace https://github.com/seys-fing/scripts, donde aparecen los .ipynb de seys. Allí se ejecuta cada script presionando la flecha en el ángulo superior izquierdo de la celda.

El entorno Colaboratory pertenece a Google y para ejecutar un .ipynb interactivamente desde allí se precisa un usuario de GMail.

### Opción 3
También pueden usarse instalaciones locales de entornos Python, por ejemplo, [Anaconda](https://www.anaconda.com/) o [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

