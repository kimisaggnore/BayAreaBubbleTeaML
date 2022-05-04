from wsgiref.headers import Headers
import requests
import json
import csv
import pickle
import pandas as pd
import math
# client_id = "SwVekfDaylYP1LLiWR3AvA"
# API_key = "Aq5hRVHJYyzQHC9DI722Dv_PlVVLlZVTlCBeM4j0R_XIXBe4_NXhEQWiKFCx6mUvjsnMFj7owdCZU0fjZ7uqu4PJrkSXLJ4edF1T8TTDmGOSrsKJ5_nUgNFQpg3zYXYx"
# endpoint = f"https://api.yelp.com/v3/businesses/{id}"

# df = pd.read_csv("bobadata.csv", usecols = ["id"])

# list_of_dicts = []
# index = 0
# headers = {'Authorization': 'bearer %s' % API_key}
# while index < 603:
#     id = df.loc[index].at["id"]
#     endpoint = f"https://api.yelp.com/v3/businesses/{id}"
#     response = requests.get(url = endpoint, headers = headers)
#     print(f"{index} : {response}")
#     data = response.json()
#     list_of_dicts.append(data)
#     index = index + 1


# print(endpoint)
# response = requests.get(url = endpoint, headers = headers)
# data = response.json()
# print(data)

# pickle_out = open("boba_dicts_info.pickle", "wb")
# pickle.dump(list_of_dicts, pickle_out)
# pickle_out.close()
# print(list_of_dicts)

pickle_in = open("boba_dicts_info.pickle", "rb")
opened_dict = pickle.load(pickle_in)
print(opened_dict[602])

# df = pd.read_csv("bobadata.csv", usecols = ["id"])
# review_count_arr = []
# index = 0
# while index < 603:
#     if len(opened_dict[index]) != 1:
#         df.loc[index].at["id"] = opened_dict[index]["review_count"]
#         review_count_arr.append(opened_dict[index]["review_count"])
#         index = index + 1
#     else:
#         df.loc[index].at["id"] = "NA"
#         index = index + 1

# df.to_csv('NOT_cleaned_review_count_data.csv', index = False)

# data = review_count_arr
# # Statistical methods taken from online
# def variance(data, ddof=0):
#      n = len(data)
#      mean = sum(data) / n
#      return sum((x - mean) ** 2 for x in data) / (n - ddof)

# def stdev(data):
#      var = variance(data)
#      std_dev = math.sqrt(var)
#      return std_dev

# def average(data):
#     avg = sum(data)/len(data)
#     return avg

# stdev_data = stdev(data)
# var_data = variance(data)
# avg_data = average(data)
# print(f"Average # of reviews: {avg_data}")
# print(f"Variance: {var_data}")
# print(f"Standard Deviation: {stdev_data}")