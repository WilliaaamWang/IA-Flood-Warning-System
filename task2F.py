import datetime
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
update_water_levels(stations)
res = []
for station in stations:
    if (station.relative_water_level() != None):
        res.append(tuple((station, station.relative_water_level())))
        res.sort(key = lambda x:x[1], reverse=True)
stations_high = res[1:6]
greatest_level_stations = []
for tuples in stations_high:
    greatest_level_stations.append(tuples[0])
dates = []
levels = []
for item in greatest_level_stations:
    date, level = fetch_measure_levels(
        item.measure_id, dt=datetime.timedelta(days=2))
    dates.append(date)
    levels.append(level)

plot_water_level_with_fit(greatest_level_stations, dates, levels, 4)