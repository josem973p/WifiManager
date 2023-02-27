from shapely.geometry import Point, Polygon

def isInPolygon(localization):

    # Crear objeto Polygon con las coordenadas de la geocerca
    geocerca = Polygon([(19.431848, -99.114692), (19.431606, -99.110829), (19.429096, -99.111237), (19.429582, -99.114424)])

    # Verificar si una coordenada dada está dentro del polígono
    #19.42969324131995, -99.11748132827125
    #coordenada = Point(19.42969324131995, -99.11748132827125)
    esta_dentro = geocerca.contains(localization)

    print(esta_dentro)

    return  esta_dentro