#Task 2B
def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples of stations at which the latest water level
    is greater than the input tolerance"""
    res = []
    for station in stations:
        if (station.relative_water_level() != None) and (station.relative_water_level() > tol):
            res.append(tuple((station.name, station.relative_water_level())))
    return res