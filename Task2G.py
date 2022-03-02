import datetime
import numpy as np
import matplotlib
from floodsystem.analysis import polyfit
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list, update_water_levels

stations = build_station_list()
update_water_levels(stations)
dt = 5
compare_list = []
town_appearance = []
town_list = {}
town_score = []
for station in stations:
    if station.town not in town_appearance:
        town_appearance.append(station.town)
        town_list[station.town] = [station]
    else:
        town_list[station.town].append(station)
for town in town_list:
    score = 0
    station_list = town_list[town]
    res = []
    for station in station_list:
        if (station.relative_water_level() != None):
            res.append(station)
    for station in res:
        date, level = fetch_measure_levels(
            station.measure_id, dt=datetime.timedelta(days=dt))
        if date != None and type(level) != float:
            try: 
                poly, d = polyfit(date, level, 4)
                if poly != None:
                    x = matplotlib.dates.date2num(date)
                    noise_distribution = np.array(level) - poly(x - d)
                    variance = np.var(noise_distribution)
                    prediction = poly(x[-1] + 1 - d)
                    result = prediction + 0.5 * variance
                    score += result
            except(TypeError):
                score += 0
        else:
            score += 0
    if len(res) == 0:
        pass
    else:
        town_score.append([town, score/len(res)])       

town_score.sort(key = lambda x: x[1], reverse=True) 

print(town_score[0][0])

