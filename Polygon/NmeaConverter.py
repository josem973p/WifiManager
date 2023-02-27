from shapely.geometry import Point, Polygon


def positionConverter(nmeaObject):
    latitude = nmeaObject['latitude']
    longitude = nmeaObject['longitude']

    decimal_latitude = latitude['degree'] + (latitude['minute'] / 60) + (latitude['second'] / 3600)
    decimal_longitude = longitude['degree'] + (longitude['minute'] / 60) + (longitude['second'] / 3600)
    routerLocalization = Point(decimal_latitude, decimal_longitude)

    return routerLocalization


