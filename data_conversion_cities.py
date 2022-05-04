import csv 
import pandas as pd
import numpy as np
import math

df = pd.read_csv("bobadata.csv", usecols = ["city"])

stored_cities = []

index = 0
while index < 603:
    if not pd.isnull(df.loc[index].at["city"]):
        stored_cities.append(df.loc[index].at["city"])
        index = index + 1
    else: 
        stored_cities.append(["NA"])
        index = index + 1

count = 0
stored_cities_instances_dict = {}
for city in stored_cities:
    if city in stored_cities_instances_dict.keys():
        stored_cities_instances_dict[city] += 1
        count = count + 1
    else: 
        stored_cities_instances_dict[city] = 1
        count = count + 1

print(stored_cities_instances_dict)

multiple_loc_dict = {}
for street_key in stored_cities_instances_dict:
    if stored_cities_instances_dict[street_key] > 1:
        multiple_loc_dict[street_key] = stored_cities_instances_dict[street_key]

print(multiple_loc_dict)
print(len(multiple_loc_dict))
stored_cities_instances_dict = {k: v for k, v in sorted(stored_cities_instances_dict.items(), key=lambda item: item[1])} #Taken from https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
print(stored_cities_instances_dict)

data = []
for key in stored_cities_instances_dict:
    data.append(stored_cities_instances_dict[key])

def variance(data, ddof=0):
     n = len(data)
     mean = sum(data) / n
     return sum((x - mean) ** 2 for x in data) / (n - ddof)

def stdev(data):
     var = variance(data)
     std_dev = math.sqrt(var)
     return std_dev

def average(data):
    avg = sum(data)/len(data)
    return avg

stdev_data = stdev(data)
var_data = variance(data)
avg_data = average(data)
print(f"Average # of locations per city: {avg_data}")
print(f"Variance: {var_data}")
print(f"Standard Deviation: {stdev_data}")

def city_conversion(num):
    if num < 4:
        return 1
    elif num < 11:
        return 2
    elif num < 21:
        return 3
    else:
        return 4

index = 0
while index < 603:
    if not pd.isnull(df.loc[index].at["city"]):
        df.loc[index].at["city"] = city_conversion(stored_cities_instances_dict[df.loc[index].at["city"]])
        index = index + 1
    else:
        df.loc[index].at["city"] = "NA"
        index = index + 1

df.to_csv('cleaned_city_data_2.csv', index = False)