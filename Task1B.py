from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    """Requirements for Task 1B"""

    # Build list of stations and specify p
    stations = build_station_list()
    p = (52.2053, 0.1218)
    list_by_distance = stations_by_distance(stations, p)
    demo_list = []
    for i in range(len(list_by_distance)):
        demo_list.append((list_by_distance[i][0].name, list_by_distance[i][0].town, list_by_distance[i][1]))
    print(demo_list[:10])
    print(demo_list[-10:])

if __name__ == '__main__':
    print("*** Task 1B: CUED Part IA Flood Warning System ***")
    run()