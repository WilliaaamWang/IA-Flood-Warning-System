from typing import Set
from floodsystem.stationdata import build_station_list
import floodsystem.geo as geo

"""Since data are in real-time, only the type of output
or the possiblity for calling the function can be tested"""

def test_stations_by_distance():
    stations = build_station_list()
    p = tuple((52.2053, 0.1218))
    test = geo.stations_by_distance(stations, p)
    assert type(test) == list

def test_stations_within_radius():
    stations = build_station_list()
    centre = tuple((52.2053, 0.1218))
    r = 10.0
    test = geo.stations_within_radius(stations, centre, r)
    assert type(test) == list
    
def test_rivers_with_station(): 
    stations = build_station_list()
    test = geo.rivers_with_station(stations)
    assert type(test) == list
    #Sets cannot be indexed/subscripted so list output is needed

def test_stations_by_river(): 
    stations = build_station_list()
    test = geo.stations_by_river(stations)
    assert type(test) == dict

def test_rivers_by_station_number(): 
    stations = build_station_list()
    test = geo.rivers_by_station_number(stations, 1)
    assert type(test) == list
