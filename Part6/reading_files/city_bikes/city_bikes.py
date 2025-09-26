import math
def get_station_data(filename: str):
    station_dictionary = {}
    with open(filename) as file:
        for line in file:
            line = line.split(";")
            if line[3] == "name":
                continue

            if line[3] not in station_dictionary:
                station_dictionary[line[3]] = ()

            station_dictionary[line[3]] += (float(line[0]), float(line[1]))
    return station_dictionary


def distance(stations: dict, station1: str, station2: str):
    longitude1 = stations[station1][0]
    longitude2 = stations[station2][0]
    latitude1 = stations[station1][1]
    latitude2 = stations[station2][1]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km ** 2 + y_km ** 2)
    return distance_km

def greatest_distance(stations: dict):
    longest = 0
    station1 = ""
    station2 = ""
    for station_name1 in stations:
        for station_name2 in stations:
            if longest < distance(stations, station_name1, station_name2):
                longest = distance(stations, station_name1, station_name2)
                station1 = station_name1
                station2 = station_name2


    return station1, station2, longest

if __name__ == '__main__':
    stations = get_station_data('stations1.csv')
    greatest_distance(stations)
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)