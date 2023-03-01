
from shapely.geometry import Polygon

geofence = {
        "array": [

            {
                "geocerca": [
                    {
                        "latitude": 14.5555,
                        "longitude": 12.2223333
                    },
                    {
                        "latitude": 14.5555,
                        "longitude": 12.2223333
                    },
                    {
                        "latitude": 14.5555,
                        "longitude": 12.2223333
                    },
                    {
                        "latitude": 14.5555,
                        "longitude": 12.2223333
                    },
                    {
                        "latitude": 14.5555,
                        "longitude": 12.2223333
                    }
                ]
            },
            {
                "geocerca": [
                    {
                        "latitude": 14.5555,
                        "longitude": 12.2223333
                    },
                    {
                        "latitude": 14.5555,
                        "longitude": 12.2223333
                    },
                    {
                        "latitude": 14.5555,
                        "longitude": 12.2223333
                    },
                    {
                        "latitude": 14.5555,
                        "longitude": 12.2223333
                    },
                    {
                        "latitude": 14.5555,
                        "longitude": 12.2223333
                    }
                ]
            },
{
                "geocerca": [
                    {
                        "latitude": 19.433479796664603,
                        "longitude": -99.11106966828282
                    },
                    {
                        "latitude": 19.433561,
                        "longitude": -99.109675
                    },
                    {

                        "latitude": 19.430363546885538,
                        "longitude": -99.11067270138295
                    },

                    {

                        "latitude": 19.431122379444293,
                        "longitude": -99.11294721439968
                    },
                    {

                        "latitude": 19.433044739392315,
                        "longitude": -99.11292575672971
                    }
                ]
            },
            {
                "geocerca": [
                    {
                        "latitude": 14.5555,
                        "longitude": 12.2223333
                    },
                    {
                        "latitude": 14.5555,
                        "longitude": 12.2223333
                    },
                    {
                        "latitude": 14.5555,
                        "longitude": 12.2223333
                    },
                    {
                        "latitude": 14.5555,
                        "longitude": 12.2223333
                    },
                    {
                        "latitude": 14.5555,
                        "longitude": 12.2223333
                    }
                ]
            }

        ]

    }



def makePolygons(geofence):
    # Definir lista para almacenar los polígonos
    polys = []

    # Recorrer la lista de geocercas y crear un polígono a partir de cada una
    for geocerca in geofence["array"]:
        coordenadas = [( punto["latitude"],punto["longitude"]) for punto in geocerca["geocerca"]]
        poligono = Polygon(coordenadas)
        print(poligono)
        polys.append(poligono)

    return  polys



