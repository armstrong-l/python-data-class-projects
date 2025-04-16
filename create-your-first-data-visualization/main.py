# Import matplotlib library here
import matplotlib.pyplot as plt 

# Let's rank some of our favorite snacks
snack_scores = [9, 7, 5]
slice_labels = ["Hot chips", "Donuts", "Nut bars"]

# Let's make a pie chart!
plt.pie(snack_scores, labels=slice_labels)

# Give your pie chart a title in the quotes
plt.title("My Favourite Snacks")

# Put the name of your file in the quotes and give it a .png extension
plt.savefig("snack-ratings.png")