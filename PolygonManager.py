import ManageWiFi


def isInPolygon(localizacion, poligonos, estabaDentro, auxiliar, numeroPol):
    conta=0
    for indice, poligono in enumerate(poligonos):
        if estabaDentro:
            break
        if auxiliar is True:
            if (indice+1)!=numeroPol:
                conta=conta+1
                continue

        estaDentro = poligono.contains(localizacion)
        estabaDentro = ManageWiFi.manageWiFiStatus(estaDentro, auxiliar)
        if not estabaDentro:
            auxiliar = False
        conta=conta+1
    return estabaDentro,conta

def isInPolygon2(localization,polygons,wasInGeofence,aux):

    for polygon_coords in polygons:


        if (wasInGeofence == True):
            break;
        #puntos = polygon_coords
        #geocerca = Polygon((19.433479796664603,-99.11106966828282),(19.433561,-99.109675),(19.430363546885538,-99.11067270138295),(19.431122379444293,-99.11294721439968),(19.433044739392315,-99.11292575672971))

        #geocerca = Polygon(puntos)
        esta_dentro = polygon_coords.contains(localization)

        status= ManageWiFi.manageWiFiStatus(esta_dentro, wasInGeofence, aux)
        wasInGeofence=status
        if(wasInGeofence==False):
            aux=False


    # Crear objeto Polygon con las coordenadas de la geocerca
    #geocerca = Polygon([(19.431848, -99.114692), (19.431606, -99.110829), (19.429096, -99.111237), (19.429582, -99.114424)])
    #geocerca = localization
    # Verificar si una coordenada dada está dentro del polígono
    #19.42969324131995, -99.11748132827125
    #coordenada = Point(19.42969324131995, -99.11748132827125)
    #esta_dentro = geocerca.contains(localization)

    #print(esta_dentro)

    return  wasInGeofence