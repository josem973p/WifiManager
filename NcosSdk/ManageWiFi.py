from NcosSdk.csclient import CSClient,EventingCSClient


cp = EventingCSClient('ibr1700_gnss')

def manageWiFiStatus(inPolygon,wasInGeofence,aux):




    if(inPolygon==False and aux==True):# si no esta en la geocerca  prende el WIFI
        cp.put('/config/wlan/radio/1/bss/0/enabled', True)
        cp.put('/config/wlan/radio/0/bss/0/enabled', True)
        cp.log("No estoy en ninguna Geocerca prendiendo el WIFI")
        wifi = cp.get('config/wlan/radio/1/bss/0/')
        wifi2 = cp.get('config/wlan/radio/0/bss/0/')
        print("No estoy en ninguna Geocerca prendiendo el WIFI")
        return  False;

    elif(inPolygon==True): # si esta en la geocerca  apaga  el WIFI
        wasInGeofence=True;
        cp.put('/config/wlan/radio/1/bss/0/enabled', False)
        cp.put('/config/wlan/radio/0/bss/0/enabled', False)
        wifi = cp.get('config/wlan/radio/1/bss/0/')
        wifi2 = cp.get('config/wlan/radio/0/bss/0/')
        cp.log("Estoy en  Geocerca apagando el WIFI")
        print("Estoy en  Geocerca apagando el WIFI")


        return True;

    return False
