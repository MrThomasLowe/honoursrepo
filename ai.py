import pandas as pd

dataFileName = input("Please enter the name of the data file.")
print(dataFileName)
data = pd.read_csv("Stocks/prices.csv")

head(data)