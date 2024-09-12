def calculatestationneeded(stations, states_needed):
    final_stations = set()
    while states_needed:
        best_station = None
        states_covered = set()
        for station, states_for_station in stations.items():
            print(station, states_for_station)
            covered = states_needed & states_for_station
            if len(covered) > len(states_covered):
                print(covered, True)
                best_station = station
                states_covered = covered
        states_needed -= states_covered
        print('states_needed', states_needed)
        final_stations.add(best_station)
    return final_stations
            
            
        



states_neededexample = set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az'])
stationsexample = {}
stationsexample["kone"] = set(["id", "nv", "ut"])
stationsexample["ktwo"] = set(["wa", "id", "mt"])
stationsexample["kthree"] = set(["or", "nv", "ca"])
stationsexample["kfour"] = set(["nv", "ut"])
stationsexample["kfive"] = set(["ca", "az"])

x =calculatestationneeded(stationsexample, states_neededexample)
print(x)
