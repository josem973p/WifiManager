from csclient import EventingCSClient


cp = EventingCSClient('ibr1700_gnss')

def manageWiFiStatus(inPolygon,aux):

    if not inPolygon and aux:  # Si no está en la geocerca y la bandera auxiliar es verdadera, enciende WLAN
        for i in range(2):
            cp.put(f'/config/wlan/radio/{i}/bss/0/enabled', True)
        cp.log("No estoy en ninguna geocerca, encendiendo WLAN")
        return False
    elif inPolygon:  # Si está en la geocerca, apaga WLAN
        for i in range(2):
            cp.put(f'/config/wlan/radio/{i}/bss/0/enabled', False)
        cp.log("Estoy en una geocerca, apagando WLAN")
        return True
    else:
        return False




    #if(inPolygon==False and aux==True):# si no esta en la geocerca  prende el WIFI
    #    cp.put('/config/wlan/radio/1/bss/0/enabled', True)
    #    cp.put('/config/wlan/radio/0/bss/0/enabled', True)
    #    cp.log("No estoy en ninguna Geocerca prendiendo el WIFI")
    #    wifi = cp.get('config/wlan/radio/1/bss/0/')
    #    wifi2 = cp.get('config/wlan/radio/0/bss/0/')
    #    print("No estoy en ninguna Geocerca prendiendo el WIFI")
    #    return  False;

    #elif(inPolygon==True): # si esta en la geocerca  apaga  el WIFI

    #    cp.put('/config/wlan/radio/1/bss/0/enabled', False)
    #    cp.put('/config/wlan/radio/0/bss/0/enabled', False)
    #    wifi = cp.get('config/wlan/radio/1/bss/0/')
    #    wifi2 = cp.get('config/wlan/radio/0/bss/0/')
    #    cp.log("Estoy en  Geocerca apagando el WIFI")
    #    print("Estoy en  Geocerca apagando el WIFI")


    #    return True;

    #return False
