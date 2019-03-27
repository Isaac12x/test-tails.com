#!/usr/bin/env python
# -*- coding: utf-8 -*

import pytest
import unittest
from main.app.area_calculations import haversine, test_fall_within_area
from main.app.utils import get_order
from main.app.api_utils import PostcodeFinder
#
# class TestPostcodeFinder(unittest.TestCase):
#     @pytest.fixture
#     def postcode_app():
#         try:
#             return PostcodeFinder()
#         except ModuleNotFoundError:
#             return "Module not found"
#
#     def test_invalid_postcode(postcode_app):
#         resp = PostcodeFinder.get_postcode("12x4232")
#         assert resp.status_code == 404
#
#     def test_postcode_lookup(postcode_app):
#         resp = PostcodeFinder.get_postcode("w11 4uy")
#         assert type(resp) == dict
#
#     def test_invalid_postcode(postcode_app):
#         resp = PostcodeFinder.validate_postcode("123xc231")
#         assert resp.status_code == 404
#
#     def test_valid_postcode(postcode_app):
#         resp = PostcodeFinder.validate_postcode("ub3 1ha")
#         assert resp.status_code == 200


class TestPostcodesInRadius(unittest.TestCase):
    def test_close_neighbors(self):
        radius = 10
        close_neighbors = [
            {
                "name": "Basildon",
                "postcode": "SS13 3BY",
                "lat": 51.564192,
                "long": 0.505725,
            },  # this is used as referent
            {
                "name": "Basildon_Pipps_Hill",
                "postcode": "SS14 3AF",
                "lat": 51.581143,
                "long": 0.443534,
            },
        ]
        res = haversine(
            close_neighbors[0]["lat"],
            close_neighbors[0]["long"],
            close_neighbors[1]["lat"],
            close_neighbors[1]["long"],
        )
        assert test_fall_within_area(radius, res) is True

    def test_far_away_neighbors(self):
        radius = 10
        far_away = [
            {
                "name": "Basildon",
                "postcode": "SS13 3BY",
                "lat": 51.564192,
                "long": 0.505725,
            },  # this is used as referent
            {
                "name": "Dover",
                "postcode": "CT16 3PS",
                "lat": 51.153865,
                "long": 1.29854,
            },
        ]
        res = haversine(
            far_away[0]["lat"],
            far_away[0]["long"],
            far_away[1]["lat"],
            far_away[1]["long"],
        )
        assert test_fall_within_area(radius, res) is False

    def test_res_with_ordering(self):
        ordered_list = get_order("ub3 1ha", 200)
        assert ordered_list[0]["lat"] > ordered_list[1]["lat"]

    # can be only ordered by luck so lets add another one
    def test_res_with_ordering_ending(self):
        ordered_list = get_order("w11 4uy", 200)
        assert ordered_list[-1]["lat"] < ordered_list[-2]["lat"]

    # still can be ordered by luck but getting to a point I'm fairly confident
    # it's not.

if __name__ == "__main__":
    unittest.main()
