import csv 
import pandas as pd
import numpy as np
import math

address_df = pd.read_csv("cleaned_address_data.csv", usecols = ["address"])
distance_df = pd.read_csv("cleaned_distance_data.csv", usecols = ["distance"])
review_count_df = pd.read_csv("minmax_cleaned_review_count.csv", usecols = ["cleaned_id"])
chain_df = pd.read_csv("NOT_cleaned_chain_col.csv", usecols = ["chain_id"])
rating_df = pd.read_csv("bobadata.csv", usecols = ["rating"])
latitude_df = pd.read_csv("bobadata.csv", usecols = ["lat"])
longitude_df = pd.read_csv("bobadata.csv", usecols = ["long"])
city_df = pd.read_csv("cleaned_city_data_2.csv", usecols = ["city"])
frames = [address_df, distance_df]
result = address_df
result["distance"] = distance_df["distance"]
result["review_count"] = review_count_df["cleaned_id"]
result["ratings"] = rating_df["rating"]
result["chain"] = chain_df["chain_id"]
result["city"] = city_df["city"]
result["lat"] = latitude_df["lat"]
result["long"] = longitude_df["long"]
result.to_csv('merged_data.csv', index = False)