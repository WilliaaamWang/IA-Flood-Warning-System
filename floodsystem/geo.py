# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key  # noqa
from haversine import haversine
import floodsystem.utils

def stations_by_distance(stations, p):
    """Given a list of stations and a coordinate p, return a list of tuples of the station name and its distance from p"""
    unsorted_list_tuple = []
    for station in stations:
        coord = station.coord
        distance = haversine(p, coord)
        unsorted_list_tuple.append((station, distance))
    list_tuple = sorted_by_key(unsorted_list_tuple, 1)
    return list_tuple

def stations_within_radius(stations, centre, r):
    """Given a list of stations, a coordinate and a specified radius around the coordinate,
     return a list of stations within the radius in alphabetical order"""
    radius_list = []
    for station in stations:
        coord =  station.coord
        distance = haversine(centre, coord)
        if distance <= r:
            radius_list.append(station.name)
    radius_list.sort()
    return radius_list
