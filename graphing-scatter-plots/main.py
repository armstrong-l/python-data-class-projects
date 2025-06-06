import csv
import numpy as np
import matplotlib.pyplot as plt

with open("tips.csv", "r") as file:
  data = csv.reader(file,delimiter=",")
  headers = next(data)
  data_list = list(data)
  data_numpy = np.array(data_list)

size = np.array(data_numpy[:,6], dtype=int)
tips = np.array(data_numpy[:,1], dtype=float)
bills = np.array(data_numpy[:,0], dtype=float)
tip_percentages = tips/bills*100

print(f"The average bill amount is ${round(np.mean(bills), 2)}")
print(f"The median bill amount is ${round(np.median(bills), 2)}")
print(f"The smallest bill is ${round(np.min(bills), 2) }")
print(f"The largest bill is ${round(np.max(bills), 2)}")

plt.scatter(size, tip_percentages, color="purple")
plt.xlabel("Dinner Group Size")
plt.ylabel("Tip Percentage (%)")
plt.title("Comparing Tip Percentage to Group Size")
plt.savefig("tips_to_group_size.png")