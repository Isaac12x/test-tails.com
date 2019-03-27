import os
import json

from operator import itemgetter
from main.app.api_utils import PostcodeFinder
from main.app.area_calculations import haversine, test_fall_within_area


def get_order(postcode, radius):
    """
        Gets the lat and long for a postcode, checks what falls within
        the radius and returns a list

        Params
        ----
        postcode - a uk postcode
        radius - radius in km

        Return
        ----
        Ordered list of stores within radius ordered from north to south
    """
    stores = load_data("main/app/stores.json")
    close_stores = []
    lat, long = PostcodeFinder.get_postcode_coords(postcode, validate=True)


    for store in stores:
        if store["lat"] is not None:
            unit = haversine(lat, long, store["lat"], store["long"])
            if test_fall_within_area(radius, unit):
                close_stores.append(store)

    # certainly would grab the ones wihtout latitude and either retry to get the latitude
    # or prune them from our basic db :)
    return order_list(close_stores, sort_by_lat=True)


def load_data(filepath):
    if os.path.exists(filepath):
        with open(filepath, "r") as file:
            stores = json.load(file)
            file.close()
        return stores
    return "No such file"


def write_to_file(data, filepath):
    with open(filepath, "w+") as file:
        stores = order_list(data)
        json.dump(stores, file)
        file.close()
    return f"Wrote data to {filepath}"


def get_and_insert(store):
    """
        Gets the postcode and returns a complete store object with lat and long
        Notes: The function that calls this one will be better off by
               using gevent to make parallel request into greenlets.
    """
    lat, long = PostcodeFinder.get_postcode_coords(store["postcode"], validate=False)
    store["lat"] = lat
    store["long"] = long
    return store


def order_list(list_to_order, *args, **kwargs):
    """ Sorts the list in order by name or postcode """
    if kwargs.get("sort_by_postcode", False):
        return sorted(list_to_order, key=itemgetter("postcode"))

    if kwargs.get("sort_by_lat", False):
        return sorted(list_to_order, key=itemgetter("lat"), reverse=True)

    return sorted(list_to_order, key=itemgetter("name"))
