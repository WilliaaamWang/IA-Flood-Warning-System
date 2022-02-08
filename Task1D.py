from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station
from floodsystem.geo import stations_by_river

def run():
    """Requirements for Task 1D"""
    
    stations = build_station_list()
    river_set = rivers_with_station(stations)
    river_dict = stations_by_river(stations)
    #Part 1 - Sets of River
    print("Part 1 - Sets of River")
    print("{:d} stations. First 10 - {}".format(len(river_set), river_set[:10]))
    #Part 2 - Stations by Rivers
    print("Part 2 - Stations by Rivers")
    print("River Aire: {}".format(river_dict["River Aire"]))
    print("River Cam: {}".format(river_dict["River Cam"]))
    print("River Thames: {}".format(river_dict["River Thames"]))

if __name__ == '__main__':
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()