import matplotlib.pyplot as plt
import matplotlib 
import numpy as np
from floodsystem.analysis import polyfit

def plot_water_levels(stations, dates, levels):
    #Task 2E
    
    for i in range(len(stations)):
        plt.subplot(2, 3, i+1)
        plt.plot(dates[i], levels[i])

        plt.xlabel('dates')
        plt.ylabel('water level (m)')
        plt.xticks(rotation=45)
        plt.title("Station A")

        plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()


def plot_water_level_with_fit(stations, dates, levels, p):

    for i in range(len(stations)):
        plt.subplot(2, 3, i+1)
        poly, d = polyfit(dates[i], levels[i], p)
        x = matplotlib.dates.date2num(dates[i])
        plt.plot(x, levels[i], '.')
        x1 = np.linspace(x[0], x[-1], 30)
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