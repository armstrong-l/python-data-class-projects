import matplotlib.pyplot as plt

snack_scores = [80,45,34]

slice_labels = ["Chocolate", "Cheese", "Pickles"]

colors = ["#8A2BE2", "#0000FF", "#00FFFF"]

plt.pie(snack_scores, labels=slice_labels, colors=colors)

plt.title("Snack Scores", fontsize=24)

plt.savefig("snack_scores.png")