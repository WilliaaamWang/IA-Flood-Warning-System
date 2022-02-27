from distutils.command.build import build
from attr import asdict
from floodsystem.stationdata import build_station_list, update_water_levels
import floodsystem.flood as flood

def run():
    stations = build_station_list()
    update_water_levels(stations)
    ans = flood.stations_highest_rel_level(stations, 10)
    for i in ans:
        print("{} {}".format(i[0], i[1]))

if __name__ == '__main__':
    print("*** Task 2C: CUED Part IA Flood Warning System *** ")
    run()