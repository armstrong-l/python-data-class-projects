import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

with open("tips.csv", "r") as csvfile:
    tips = pd.read_csv(csvfile, delimiter=",")

tips_pivoted = tips.pivot_table(values="tip", index=["size"], columns=["time"])

fig = sns.heatmap(tips_pivoted, annot=True, cmap="viridis")

fig.set_ylim(6,0)

plt.xlabel = "Time of Day"
plt.ylabel = "Dining Group Size"
plt.title = "Tip Amount ($) for Group Size and Time of Day"

plt.savefig("tips_time_group_size.png")