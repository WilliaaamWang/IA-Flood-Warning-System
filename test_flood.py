from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood as flood

def test_stations_level_over_threshold():
    stations = build_station_list()
    update_water_levels(stations)
    test = flood.stations_level_over_threshold(stations, 1)
    assert(type(test)) == list
    for i in test:
        assert i[1] > 1

def test_stations_highest_rel_level():
    stations = build_station_list()
    update_water_levels(stations)
    test = flood.stations_highest_rel_level(stations, 12)
    assert(type(test)) == list
    assert len(test) == 12