from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood as flood

def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)
    test = flood.stations_level_over_threshold(stations, 1)
    assert(type(test)) == list

def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    test = flood.stations_highest_rel_level(stations, 12)
    assert(type(test)) == list