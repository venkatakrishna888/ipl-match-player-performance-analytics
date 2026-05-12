import pandas as pd
import matplotlib.pyplot as plt

# Load datasets
matches = pd.read_csv("data/cleaned_matches.csv")
deliveries = pd.read_csv("data/cleaned_deliveries.csv")

# Calculate total runs in each match
match_runs = deliveries.groupby('match_id')['total_runs'].sum()

# Merge with matches dataset
venue_data = matches[['id', 'venue']]

venue_data = venue_data.merge(
    match_runs,
    left_on='id',
    right_on='match_id'
)

# Average score by venue
venue_avg = venue_data.groupby('venue')['total_runs'].mean()

# Sort highest average score
venue_avg = venue_avg.sort_values(ascending=False).head(10)

print("Top High Scoring Venues:")
print(venue_avg)

# Plot graph
plt.figure(figsize=(12,6))

venue_avg.plot(kind='bar')

plt.title("Highest Scoring IPL Venues")
plt.xlabel("Venue")
plt.ylabel("Average Match Runs")

plt.xticks(rotation=75)

plt.tight_layout()

plt.show(block=True)