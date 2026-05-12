import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned deliveries dataset
deliveries = pd.read_csv("data/cleaned_deliveries.csv")

# Powerplay overs (1-6)
powerplay = deliveries[deliveries['over'] <= 6]

# Death overs (16-20)
death_overs = deliveries[deliveries['over'] >= 16]

# Total runs
powerplay_runs = powerplay['total_runs'].sum()
death_runs = death_overs['total_runs'].sum()

print("Powerplay Runs:", powerplay_runs)
print("Death Overs Runs:", death_runs)

# Data for graph
phases = ['Powerplay', 'Death Overs']
runs = [powerplay_runs, death_runs]

# Plot graph
plt.figure(figsize=(8,6))

plt.bar(phases, runs)

plt.title("IPL Powerplay vs Death Overs Runs")
plt.xlabel("Match Phases")
plt.ylabel("Total Runs")

plt.tight_layout()

plt.show(block=True)