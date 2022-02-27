#Task 2B
def stations_level_over_threshold(stations, tol):
    """Returns a list of tuples of stations at which the latest water level
    is greater than the input tolerance"""
    res = []
    for station in stations:
        if (station.relative_water_level() != None) and (station.relative_water_level() > tol):
            res.append(tuple((station.name, station.relative_water_level())))
            res.sort(key = lambda x:x[1], reverse=True)
    return res

#Task 2C
def stations_highest_rel_level(stations, N):
    """Returns a list of N stations with highest water level relative to typical range"""
    res  = []
    count = 0
    for station in stations:
        if station.relative_water_level() != None:
            res.append(tuple((station.name, station.relative_water_level())))
        res.sort(key = lambda x:x[1], reverse=True)
    return res[:N]