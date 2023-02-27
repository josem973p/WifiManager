from NcosSdk.csclient import CSClient,EventingCSClient


cp = EventingCSClient('ibr1700_gnss')

def manageWiFiStatus(inPolygon):


    if(inPolygon==False):# si no esta en la geocerca  prende el WIFI
        cp.put('/config/wlan/radio/1/bss/0/enabled', True)
        cp.log("No estoy en ninguna Geocerca prendiendo el WIFI")
        print("No estoy en ninguna Geocerca prendiendo el WIFI")

    else: # si esta en la geocerca  apaga  el WIFI
        cp.put('/config/wlan/radio/1/bss/0/enabled', False)
        cp.log("Estoy en  Geocerca apagando el WIFI")
        print("Estoy en  Geocerca apagando el WIFI")



