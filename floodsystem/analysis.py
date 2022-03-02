import numpy as np
import matplotlib
from matplotlib.dates import date2num

def polyfit(dates, levels, p):
    if dates == []:
        return None, None
    x = date2num(dates)
    p_coeff = np.polyfit(x-x[0], levels, p)
    poly = np.poly1d(p_coeff)

    return poly, x[0]
