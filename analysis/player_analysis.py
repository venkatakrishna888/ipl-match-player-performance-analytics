import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned deliveries dataset
deliveries = pd.read_csv("data/cleaned_deliveries.csv")

# Total runs scored by each batsman
top_batsmen = deliveries.groupby('batter')['batsman_runs'].sum()

# Sort highest to lowest
top_batsmen = top_batsmen.sort_values(ascending=False).head(10)

print("Top 10 Run Scorers:")
print(top_batsmen)

# Plot graph
plt.figure(figsize=(12,6))

top_batsmen.plot(kind='bar')

plt.title("Top 10 IPL Run Scorers")
plt.xlabel("Players")
plt.ylabel("Runs")

plt.xticks(rotation=45)

plt.show()