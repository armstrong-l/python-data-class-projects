import csv
import numpy as np

with open("tips.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  data_numpy = np.array(data_list)


size = data_numpy[:,6]

tips = np.array(data_numpy[:,1], dtype=float)

bills = np.array(data_numpy[:,0], dtype=float)

# print(size)
# print(tips)
# print(bills)

tip_percentages=(tips/bills*100)

print(tip_percentages)