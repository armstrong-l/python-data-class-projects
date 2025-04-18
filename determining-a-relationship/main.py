import requests
import pandas as pd


# Standardizes currency to USD values so that we can better compare results
def format_currency(dataset):
  url = "https://api.exchangerate-api.com/v4/latest/USD"

  # Requests data from API
  response = requests.get(url)
  data = response.json()

  def convert_currency(row):
    rate = data["rates"][row["Unit Code"]]
    return row["Value"] / rate

  for index, row in dataset.iterrows():
    dataset.at[index, "Unit Code"] = "USD"
    dataset.at[index, "Value"] = convert_currency(row)
  return dataset


# ADD CODE: Pandas dataframes
wage = pd.read_csv("wage.csv", delimiter=",")
# print(wage)
happiness = pd.read_csv("happiness.csv", delimiter=",")
# print(happiness)

wage_usd = format_currency(wage)
# print(wage_usd)

wage_and_happiness = wage.merge(happiness)
# print(wage_and_happiness)

wage_and_happiness_by_country = wage_and_happiness.groupby("Country")

wage_average_per_country = wage_and_happiness_by_country["Value"].mean()

happiness_average_per_country = wage_and_happiness_by_country["Happiness score"].mean()

print(f"Countries with the highest average wages: {round(wage_average_per_country.nlargest(10), 2)}")
print(f"Countries with the lowest average wages: {round(wage_average_per_country.nsmallest(10), 2)}")

print(f"Countries with the highest average happiness score: {round(happiness_average_per_country.nlargest(10), 2)}")
print(f"Countries with the lowest average happiness score: {round(happiness_average_per_country.nsmallest(10), 2)}")
