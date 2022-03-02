import datetime
import numpy as np
import matplotlib
from floodsystem.analysis import polyfit
from floodsystem.plot import plot_water_level_with_fit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
update_water_levels(stations)
dt = 5
compare_list = []
res = []
for station in stations:
    if (station.relative_water_level() != None):
        res.append(station)
        res.sort(key = lambda x:x.relative_water_level(), reverse=True)
stations_high = res[1:10]
for station in stations_high:
    date, level = fetch_measure_levels(
        station.measure_id, dt=datetime.timedelta(days=dt))
    poly, d = polyfit(date, level, 4)
    if poly != None:
        x = matplotlib.dates.date2num(date)
        noise_distribution = np.array(level) - poly(x - d)
        variance = np.var(noise_distribution)
        prediction = poly(x[-1] + 1 - d)
        result = prediction + 0.5 * variance
        compare_list.append(tuple((station, result)))

compare_list.sort(key = lambda x:x[1], reverse=True)

print(compare_list[0][0].name)

