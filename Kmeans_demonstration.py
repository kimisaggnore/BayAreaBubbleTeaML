from os import name
from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
import csv
import seaborn as sns
import matplotlib.pyplot as plt
# df = pd.read_csv("iris.data", names = None)
# print(df)

file_name = str(input("enter the data file name in your working directory (as a string): "))
num_col = input("enter the number of columns in dataset: ")
if num_col != "":
    num_col = int(num_col)

# col_names = input("enter the column names (if applicable) as a list (Ex: [name, age, school, ...] in order (or None if you don't want labels): ")
# print(col_names)
# if (type(col_names) == list) & (type(num_col) == int): 
#     while col_names.len != num_col:
#         print(f"You need to input {num_col} columns")
#         col_names = input("enter the column names (if applicable) as a list (Ex: [name, age, school, ...] in order (or None if you don't want labels): ")
# if col_names == "None":
#     col_names = None

col_names = None
if type(num_col) == int:
    col_names = []
    for i in range(0, num_col):
        name = str(input(f"enter the name of the {i+1} column: "))
        col_names.append(name)
col_names = ["sepal length","sepal width", "petal length", "petal width", "type"]
df = pd.read_csv(file_name, names = col_names)
num_rows = df.count() + 1
print(df)
fields = []
rows = []
with open(file_name, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    fields = next(csvreader)
    for row in csvreader:
        row = row[:-1]
        rows.append(row)

print(rows)
rows = rows[:149]

#print(num_rows)
# arr_of_arrays = []
# arr_of_arrays.append(df.iloc[0])
# print(arr_of_arrays)
# i = 0
# while i < num_rows:
#     arr_of_arrays.append(df.loc[f"{i}"])
#     i += 1

data_array = np.array(rows)
kmeans = KMeans(n_clusters= 2, init = "k-means++", n_init =10, max_iter =300, random_state = None,  ).fit(data_array)
cluster_centers = kmeans.cluster_centers_
print(cluster_centers) #coordinates of cluster centers
print(kmeans.labels_) #Labels for each data point
print(kmeans.inertia_) #Sum of squared distances of samples to their closest cluster center

#df.describe()
#sns.pairplot(df['sepal length',"sepal width", "petal length", "petal width", "type"])
# sns.pairplot(df[['a',"s", "d", "f", "g"]])
# plt.show()
df = df.drop(df.index[-1])
df['Clusters'] = kmeans.labels_
df['Clusters'].value_counts()
# sns.scatterplot(x = "sepal length", y= "sepal width", hue = "Clusters", data = df)
# plt.show()
# sns.scatterplot(x = "sepal length", y= "petal length", hue = "Clusters", data = df)
# plt.show()
# j = 0

plt.figure()
j = 0
col_names = ["sepal length","sepal width", "petal length", "petal width"]
for label in col_names:
    i = j
    while i < len(col_names)-1:
        i = i + 1
        #plt.subplot(2,2,j+1)
        sns.scatterplot(x = f"{label}", y= f"{col_names[i]}", hue = "Clusters", data = df)
        plt.show()
    j = j + 1
#plt.show() 

