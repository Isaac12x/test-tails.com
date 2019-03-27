from math import radians, cos, sin, asin, sqrt


def haversine(lon1, lat1, lon2, lat2):
    """
        Calculate the great circle distance between two points
        on the earth (specified in decimal degrees)

        This code has been borrowed from:
        https://stackoverflow.com/questions/42686300/how-to-check-if-coordinate-inside-certain-area-python

        If the goal was to be even more accurate we would be using
        Vincenty's formula
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r


def test_fall_within_area(radius, haversine_distance):
    """
        Checks if a harvesine distance is within radius returns False otherwise
    """
    if haversine_distance <= radius:
        return True
    return False
