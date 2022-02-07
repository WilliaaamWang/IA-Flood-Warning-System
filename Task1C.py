from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_within_radius

def run():
    """Requirements for Task 1C"""
    
    stations = build_station_list()
    centre = (52.2053, 0.1218)
    r = 10.0
    list_within_radius = stations_within_radius(stations, centre, r)
    #demoC_list = []
    #for station in list_within_radius:
        #demoC_
    print(list_within_radius)

if __name__ == '__main__':
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()