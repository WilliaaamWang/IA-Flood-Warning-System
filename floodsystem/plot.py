import matplotlib.pyplot as plt
import matplotlib 
import numpy as np
from floodsystem.analysis import polyfit

def plot_water_levels(stations, dates, levels):
    #Task 2E
    
    for i in range(len(stations)):
        plt.subplot(2, 3, i+1)
        x = matplotlib.dates.date2num(dates[i])
        low_range = stations[i].typical_range[0]
        high_range = stations[i].typical_range[1]
        high_ranges = [high_range for i in range(len(x))]
        low_ranges = [low_range for i in range(len(x))]
        xs = np.linspace(x[0], x[-1], len(x))
        plt.plot(x, levels[i])
        plt.plot(xs, high_ranges, label ='relative_high')
        plt.plot(xs, low_ranges, label ='relative_low')
        plt.xlabel('dates')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45)
        plt.title(stations[i].name)

        plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


def plot_water_level_with_fit(stations, dates, levels, p):

    for i in range(len(stations)):
        plt.subplot(2, 3, i+1)
        poly, d = polyfit(dates[i], levels[i], p)
        x = matplotlib.dates.date2num(dates[i])
        plt.plot(x, levels[i], '.')
        x1 = np.linspace(x[0], x[-1], 30)
        low_range = stations[i].typical_range[0]
        high_range = stations[i].typical_range[1]
        high_ranges = [high_range for i in range(len(x))]
        low_ranges = [low_range for i in range(len(x))]
        xs = np.linspace(x[0], x[-1], len(x))
        plt.plot(xs, high_ranges, label ='relative_high')
        plt.plot(xs, low_ranges, label ='relative_low')
        plt.plot(x1, poly(x1-d))
        plt.title(stations[i].name)

        plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

def plot_water_level_with_fit_single(stations, dates, levels, p):

    poly, d = polyfit(dates, levels, p)
    x = matplotlib.dates.date2num(dates)
    plt.plot(x, levels, '.')
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1-d))
    plt.title(stations.name)

    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()