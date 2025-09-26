# City bikes

In this exercise we will write some functions for working on a file containing location data from the stations for 
city <br> 
bikes in Helsinki.

Each file will follow this format:

> Longitude;Latitude;FID;name;total_slot;operative;id <br>
24.950292890004903;60.155444793742276;1;Kaivopuisto;30;Yes;001 <br>
24.956347471358754;60.160959093887129;2;Laivasillankatu;12;Yes;002 <br>
24.944927399779715;60.158189199971673;3;Kapteeninpuistikko;16;Yes;003 <br>

Each station has a single line in the file. The line contains the coordinates, name,
and other identifying information for the station.

## Part 1: Distance between stations

First, write a function named get_station_data(filename: str). This function should read the names and locations of all<br> 
the stations in the file, and return them in a dictionary with the following format:

>{ <br>
  "Kaivopuisto": (24.950292890004903, 60.155444793742276), <br>
  "Laivasillankatu": (24.956347471358754, 60.160959093887129), <br>
  "Kapteeninpuistikko": (24.944927399779715, 60.158189199971673) <br>
}

Dictionary keys are the names of the stations, and the value attached is a tuple containing the location coordinates of<br> 
the station. The first element in the tuple is the Longitude field, and the second is the Latitude field.

Next, write a function named distance(stations: dict, station1: str, station2: str), which returns the distance between<br> 
the two stations given as arguments.

The distance is calculated using the Pythagorean theorem. The multiplication factors below are approximate values for<br> 
converting latitudes and longitudes to distances in kilometres in the Helsinki region.

```
# we will need the function sqrt from the math module 
import math

x_km = (longitude1 - longitude2) * 55.26 <br>
y_km = (latitude1 - latitude2) * 111.2 <br>
distance_km = math.sqrt(x_km**2 + y_km**2)<br>
```

Some examples of the function in action:
```
stations = get_station_data('stations1.csv') <br>
d = distance(stations, "Designmuseo", "Hietalahdentori") <br>
print(d) <br>
d = distance(stations, "Viiskulma", "Kaivopuisto") <br>
print(d) <br>
```

### Sample output
>0.9032737292463177 <br>
>0.7753594392019532 <br>

## Part 2: The greatest distance

Please write a function named greatest_distance(stations: dict), which works out the two stations on the list with the<br> 
greatest distance from each other. The function should return a tuple, where the first two elements are the names of the<br> 
two stations, and the third element is the distance between the two.

``` 
stations = get_station_data('stations1.csv')
station1, station2, greatest = greatest_distance(stations)
print(station1, station2, greatest)
```

### Sample output
> Laivasillankatu Hietalahdentori 1.478708873076181