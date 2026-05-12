import pandas as pd

matches = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

print(matches.head())
print(deliveries.head())

print(matches.shape)
print(deliveries.shape)