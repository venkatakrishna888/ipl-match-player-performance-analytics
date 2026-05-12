import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned matches dataset
matches = pd.read_csv("data/cleaned_matches.csv")

# Total matches won by each team
team_wins = matches['winner'].value_counts()

print("Team Wins:")
print(team_wins)

# Plot team wins
plt.figure(figsize=(12,6))
team_wins.plot(kind='bar')

plt.title("IPL Team Wins")
plt.xlabel("Teams")
plt.ylabel("Number of Wins")

plt.xticks(rotation=75)

plt.show()