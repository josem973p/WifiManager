
from shapely.geometry import Polygon

geofence = {
        "array": [

            {
                "geocerca": [
                    {

                        "latitude": 19.433930,
                        "longitude": -99.114814
                    },
                    {

                        "latitude": 19.435215090089617,
                        "longitude": -99.11360118721001
                    },
                    {

                        "latitude": 19.43456756951304,
                        "longitude": -99.10999629865519
                    },
                    {

                        "latitude": 19.433019580170313,
                        "longitude": -99.11210987914716
                    },
                    {

                        "latitude": 19.43253393341419,
                        "longitude":  -99.11483500323325
                    }
                ]
            },
            {
                "geocerca": [
                    {

                        "latitude": 18.520333056247,
                        "longitude": -88.29410815063281
                    },
                    {

                        "latitude": 18.520027859972544,
                        "longitude": -88.29086804246745
                    },
                    {

                        "latitude": 18.521859029450386,
                        "longitude": -88.28904414052008
                    },
                    {

                        "latitude": 18.52320187460655,
                        "longitude": -88.29091095780738
                    },
                    {

                        "latitude": 18.522042145319837,
                        "longitude": -88.29357170888356
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
                        "latitude": 18.64335989143167,
                        "longitude": -91.81329151616812
                    },
                    {

                        "latitude": 18.643771608224544,
                        "longitude": -91.8126102351466
                    },
                    {
                        "latitude": 18.64296596393621,
                        "longitude": -91.81192358970759
                    },
                    {

                        "latitude": 18.642556786666987,
                        "longitude": -91.81220522162594
                    },
                    {
                        "latitude": 18.643146408257216,
                        "longitude": -91.81322177874073
                    }
                ]
            },
            {
                "geocerca": [
                    {

                        "latitude": 21.151268805296,
                        "longitude": -86.86633285697575
                    },
                    {

                        "latitude": 21.154250576763307,
                        "longitude": -86.85980972530511
                    },
                    {
                        "latitude": 21.148046823674253,
                        "longitude": -86.85841497675712
                    },
                    {

                        "latitude": 21.14774663548172,
                        "longitude": -86.86184820395219
                    },
                    {

                        "latitude": 21.14758653484614,
                        "longitude": -86.8661611956805
                    }
                ]
            },
            {
                "geocerca": [
                    {

                        "latitude": 19.822998786725428,
                        "longitude": -90.5323553782207
                    },
                    {

                        "latitude": 19.823685115751356,
                        "longitude": -90.53080506156543
                    },
                    {
                        "latitude": 19.822943274689365,
                        "longitude": -90.53064949345814
                    },
                    {

                        "latitude": 19.82152518792212,
                        "longitude": -90.53052074743833
                    },
                    {

                        "latitude": 19.82164125955638,
                        "longitude": -90.5315185290919
                    }
                ]
            },
            {
                "geocerca": [
                    {

                        "latitude": 18.463240398524018,
                        "longitude": -97.40510532022272
                    },
                    {

                        "latitude": 18.46314880918184,
                        "longitude": -97.4023265519617
                    },
                    {
                        "latitude": 18.460294250173426,
                        "longitude": -97.40253039981245
                    },
                    {

                        "latitude": 18.460192482487642,
                        "longitude": -97.4050677692863
                    },
                    {

                        "latitude": 18.461897083264738,
                        "longitude": -97.40526088831601
                    }
                ]
            },
            {
                "geocerca": [
                    {

                        "latitude": 18.884922816296882,
                        "longitude": -96.91946172536326
                    },
                    {

                        "latitude": 18.884983724137804,
                        "longitude": -96.91707992399668
                    },
                    {
                        "latitude": 18.883532081235913,
                        "longitude": -96.91572809078862
                    },
                    {

                        "latitude": 18.882181940532046,
                        "longitude": -96.91557788709883
                    },
                    {

                        "latitude": 18.88269966494547,
                        "longitude": -96.91788458662053
                    }
                ]
            },
            {
                "geocerca": [
                    {

                        "latitude": 18.119804914327318,
                        "longitude": -94.44845945141569
                    },
                    {

                        "latitude": 18.12077360522449,
                        "longitude": -94.44654971878843
                    },
                    {
                        "latitude": 18.119335862072347,
                        "longitude": -94.44314867809834
                    },
                    {

                        "latitude": 18.11664388570241,
                        "longitude": -94.44457561315127
                    },
                    {

                        "latitude": 18.118214210280836,
                        "longitude": -94.44819123054108
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



