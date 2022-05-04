import csv 
import pandas as pd
import numpy as np
import math

df = pd.read_csv("bobadata.csv", usecols = ["address"])
address_df = pd.read_csv("cleaned_address_data.csv", usecols = ["address"])
distance_df = pd.read_csv("cleaned_distance_data.csv", usecols = ["distance"])
review_count_df = pd.read_csv("minmax_cleaned_review_count.csv", usecols = ["cleaned_id"])
chain_df = pd.read_csv("NOT_cleaned_chain_col", usecols = ["chain_id"])
rating_df = pd.read_csv("bobadata.csv", usecols = ["rating"])


stored_streets = []

index = 0
while index < 603:
    if not pd.isnull(df.loc[index].at["address"]):
        stored_streets.append(df.loc[index].at["address"].split()[1:])
        index = index + 1
    else: 
        stored_streets.append(["NA"])
        index = index + 1

#print(stored_streets)
count = 0
stored_street_instances_dict = {}
for street in stored_streets:
    if ' '.join([str(elem) for elem in street]) in stored_street_instances_dict.keys():
        stored_street_instances_dict[' '.join([str(elem) for elem in street])] += 1
        count = count + 1
    else: 
        stored_street_instances_dict[' '.join([str(elem) for elem in street])] = 1
        count = count + 1

#print(stored_street_instances_dict)
#print(len(stored_street_instances_dict))

multiple_loc_dict = {}
for street_key in stored_street_instances_dict:
    if stored_street_instances_dict[street_key] > 1:
        multiple_loc_dict[street_key] = stored_street_instances_dict[street_key]

#print(multiple_loc_dict)
#print(len(multiple_loc_dict))
sorted_multiple_loc_dict = {k: v for k, v in sorted(multiple_loc_dict.items(), key=lambda item: item[1])} #Taken from https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
print(sorted_multiple_loc_dict)


data = []
for key in sorted_multiple_loc_dict:
    data.append(sorted_multiple_loc_dict[key])

# Statistical methods taken from online
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
print(f"Average # of locations per street: {avg_data}")
print(f"Variance: {var_data}")
print(f"Standard Deviation: {stdev_data}")

def street_conversion(num):
    if num < 3:
        return 1
    elif num < 6:
        return 2
    elif num < 8:
        return 4
    elif num < 11:
        return 5
    elif num < 13:
        return 6
    elif num < 16:
        return 7
    else:
        return 8

index = 0
while index < 603:
    if not pd.isnull(df.loc[index].at["address"]):
        df.loc[index].at["address"] = street_conversion(stored_street_instances_dict[' '.join([str(elem) for elem in df.loc[index].at["address"].split()[1:]])])
        index = index + 1
    else:
        df.loc[index].at["address"] = "0"
        index = index + 1


#print(df)
df.to_csv('cleaned_address_data.csv', index = False)

#Next step is to link back the popular roads to the boba shops in the csv file. Lets start with the most popular street name. 
#if "address[1:] == key name, return the whole address."

# index = 0
# street_name = str(input("Enter the name of the general street: "))
# if street_name == "":
#     street_name = "El Camino Real"
# Boba_places_at_El_Camino_Real = []
# while index < 603:
#     if not pd.isnull(df.loc[index].at["address"]):
#         if ' '.join([str(elem) for elem in df.loc[index].at["address"].split()[1:]]) == street_name:
#             Boba_places_at_El_Camino_Real.append(df.loc[index].at["address"])
#     index = index + 1

#print(Boba_places_at_El_Camino_Real)