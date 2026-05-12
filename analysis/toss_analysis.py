import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned matches dataset
matches = pd.read_csv("data/cleaned_matches.csv")

# Find matches where toss winner also won match
toss_match_win = matches[matches['toss_winner'] == matches['winner']]

# Count total matches
total_matches = matches.shape[0]

# Count toss winner victories
toss_win_matches = toss_match_win.shape[0]

# Calculate percentage
percentage = (toss_win_matches / total_matches) * 100

print("Total Matches:", total_matches)
print("Matches Won After Winning Toss:", toss_win_matches)
print("Toss Impact Percentage:", round(percentage, 2), "%")

# Data for pie chart
labels = ['Won Match After Toss Win', 'Lost Match After Toss Win']

sizes = [
    toss_win_matches,
    total_matches - toss_win_matches
]

# Plot pie chart
plt.figure(figsize=(8,8))

plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%'
)

plt.title("Toss Impact Analysis in IPL")

plt.show(block=True)