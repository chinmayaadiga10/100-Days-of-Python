

with open("weather_data.csv")as weather_data:
    data=weather_data.readlines()
    print(data)


#using csv module to work with csv files
import csv

#opening the csv file as weather_data
with open("weather_data.csv")as weather_data:
    data=csv.reader(weather_data)
    temperatures=[]
    for row in data:
        print(row)
        temperatures.append(int(row[1]))
    temperatures=temperatures[1:]
    print(temperatures)