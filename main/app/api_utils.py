import requests
import time


class PostcodeFinder:
    """ This class handles everything related to finding postcodes """

    base_url = "http://api.postcodes.io/postcodes/"

    @classmethod
    def validate_postcode(cls, postcode, *args, **kwargs):
        """ Validates a given postcode against postcode.io database

            Returns
            ---
            True if postcode is valid
            False otherwise (this also accounts for network problems)
        """

        res = requests.get(f"{cls.base_url}{postcode}/validate")
        if res.json()["result"] == True:
            return True
        return False

    @classmethod
    def get_postcode_coords(cls, postcode, *args, **kwargs):
        """ This method gets the lat and longitude and returns it """

        if kwargs["validate"]:
            valid = cls.validate_postcode(postcode)
            if not valid:
                return f"An error ocurred with status code {valid}"

        try:
            res = requests.get(f"{cls.base_url}{postcode}")
        except requests.ConnectionError:
            time.sleep(1)
            requests.get(f"{cls.base_url}{postcode}")
        finally:
            if res.status_code == 200:
                return cls.parse_response(res.json())
            return 0, 0  # postcode not found :(

    @staticmethod
    def parse_response(obj, *args, **kwargs):
        """
            Parses the response from postcode.io and gets lat and long
            ----
            **kwargs (or *args for the matter) can be used to pass other
            properties we want from the response.

            We would need to return a list of those properties if we were
            going down that root.
        """
        obj = obj["result"]
        lat = obj["latitude"]
        long = obj["longitude"]
        return lat, long
