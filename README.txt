# solar - HET

software para la simulación de celdas solares compuestas 
por una heterounión de la familia de películas delgadas.


Se requieren de varias librerias para ejecutar el programa, fue escrito
en Python3, las principales librerias son wx, numpy, matplotlib y scipy.
Para correr las simulaciones se necesita:

    + 3 archivos .txt con datos de Reflectancia, Transmitancia y el espectro AMS1.5
      compuestos por dos columnas, la longitud de onda en la primera columna y los
      datos referentes a cada archivo en la segunda columna. Se omitira la primera 
      línea.
      
    + Conocer los parametros físicos de las capas tipo P y tipo N.
      Permitividad relativa, Número de acceptores/Donores, Energía de la banda prohibida,...

El software grafica los resultados obtenidos o permite descargar 
los datos para su posterior manipulación si así lo desea el usuario.

El ejecutable para windows que puede ser usado con Wine 
en sistemas operativos de Linux estará disponible pronto.
