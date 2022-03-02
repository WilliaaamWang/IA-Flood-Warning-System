import datetime
import matplotlib
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.analysis import polyfit
from floodsystem.stationdata import build_station_list, update_water_levels

def test_polyfit():
    stations = build_station_list()
    update_water_levels(stations)
    station = stations[1]
    date, level = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=1))
    poly, d = polyfit(date, level, 3)

test_polyfit()
print('done')
