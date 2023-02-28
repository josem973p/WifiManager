
from Polygon import PolygonManager,NmeaConverter
from NcosSdk.Auth import Auth
from NcosSdk.csclient import CSClient,EventingCSClient
from NcosSdk import ManageWiFi
from shapely.geometry import Point, Polygon
import pynmea2
import threading
import time
import Geofence



# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    listaPoly =Geofence.makePolygons(Geofence.geofence)

    cp = EventingCSClient('ibr1700_gnss')
    system_id = cp.get('config/system/system_id')
    cp.put('/config/wlan/radio/1/bss/0/enabled', True)
    cp.put('/config/wlan/radio/0/bss/0/enabled', True)
    wifi = cp.get('config/wlan/radio/1/bss/0/')



    resp = cp.get('status/gps/fix')


    def validatePositionStatus():
        wasInGeofence= False
        aux=False
        while True:
            try:
                resp = cp.get('status/gps/fix')
                routerLocalization = NmeaConverter.positionConverter(resp)

                inPolygon = PolygonManager.isInPolygon(routerLocalization,listaPoly,wasInGeofence,aux)

                aux=inPolygon


            except Exception as e:
                print(f"Error: {e}")
                # Esperar unos segundos antes de reiniciar el bucle
                time.sleep(5)


    # Crear un hilo y ejecutar la función
    thread = threading.Thread(target=validatePositionStatus)
    thread.start()
    #19.432640916666667 - 98.88908681666666
    #19.43266, -99.11098
