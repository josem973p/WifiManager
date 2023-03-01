from shapely.geometry import Point, Polygon


def positionConverter(nmeaObject):
    latitude = nmeaObject['latitude']
    longitude = nmeaObject['longitude']

    decimal_latitude = latitude['degree'] + (
        latitude['minute'] if latitude['degree'] >= 0 else -latitude['minute']) / 60 + (
                           latitude['second'] if latitude['degree'] >= 0 else -latitude['second']) / 3600
    decimal_longitude = longitude['degree'] + (
        longitude['minute'] if longitude['degree'] >= 0 else -longitude['minute']) / 60 + (
                            longitude['second'] if longitude['degree'] >= 0 else -longitude['second']) / 3600


    routerLocalization = Point(decimal_latitude, decimal_longitude)
    #routerLocalization = Point(17.44444, -99.9999999)

    return routerLocalization


