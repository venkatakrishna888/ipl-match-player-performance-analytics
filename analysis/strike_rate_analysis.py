import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned deliveries dataset
deliveries = pd.read_csv("data/cleaned_deliveries.csv")

# Filter players with minimum 500 balls played
balls_faced = deliveries.groupby('batter')['ball'].count()

runs_scored = deliveries.groupby('batter')['batsman_runs'].sum()

# Create DataFrame
strike_rate_df = pd.DataFrame({
    'Runs': runs_scored,
    'Balls': balls_faced
})

# Filter serious batsmen
strike_rate_df = strike_rate_df[strike_rate_df['Balls'] >= 500]

# Calculate strike rate
strike_rate_df['Strike Rate'] = (
    strike_rate_df['Runs'] / strike_rate_df['Balls']
) * 100

# Top strike rates
top_sr = strike_rate_df.sort_values(
    by='Strike Rate',
    ascending=False
).head(10)

print("Top 10 Strike Rates:")
print(top_sr[['Strike Rate']])

# Plot graph
plt.figure(figsize=(12,6))

top_sr['Strike Rate'].plot(kind='bar')

plt.title("Top IPL Strike Rates")
plt.xlabel("Players")
plt.ylabel("Strike Rate")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show(block=True)