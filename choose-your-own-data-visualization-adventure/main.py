import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("books.csv", delimiter=",")

reviewsCount = data["text_reviews_count"]
averageRating = data["average_rating"]

plt.scatter(averageRating, reviewsCount, color="green")

plt.xlabel("Average Rating")
plt.ylabel("Number of Reviews")
plt.title("Average Rating Compared to Number of Reviews")

plt.savefig("rating_review_graph.png")

