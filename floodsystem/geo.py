# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa
def rivers_by_station_number(stations, N):
    output = []
    river_nums = {}
    for s in stations:
        if s.river in river_nums.keys():
            river_nums[s.river] += 1
        else:
            river_nums.update({s.river:1})
    unique_nums = sorted(set(river_nums.values()),reverse=True)[0:N]
    for item in river_nums:
        if river_nums[item] in unique_nums:
            output.append([item, river_nums[item]])
    output = sorted(output, key = lambda x: x[1], reverse=True)
    return output
    