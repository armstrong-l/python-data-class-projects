import csv
import numpy as np

# ADD CODE: Convert titanic1.csv
with open("titanic1.csv", "r") as file:
    data = csv.reader(file,delimiter=",")
    headers = next(data)
    data_list = list(data)
    titanic_data_1 = np.array(data_list)


# ADD CODE: Convert titanic2.csv 
with open("titanic2.csv", "r") as file:
    data = csv.reader(file,delimiter=",")
    headers = next(data)
    data_list = list(data)
    titanic_data_2 = np.array(data_list) 
    

# ADD CODE: Merge two datasets

combined_data = np.concatenate((titanic_data_1, titanic_data_2), axis=0)


# ADD CODE: Print out shape and number of dimensions of merged dataset

print(combined_data.ndim)
print(combined_data.shape)