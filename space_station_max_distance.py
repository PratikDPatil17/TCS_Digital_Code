def flatlandSpaceStations(n, c):
    station = []
    c.sort()
    for i in range(n):
        station.append(i)
    if c==station:
        return 0
    stdiff = []
    for j in station:
        diff = []
        for i in range(len(c)):
            diff.append(abs(j-c[i]))
        stdiff.append(min(diff))
    
    return max(stdiff)
