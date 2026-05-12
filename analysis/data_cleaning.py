import pandas as pd

# Load datasets
matches = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

# Display basic info
print("Matches Dataset")
print(matches.info())

print("\nDeliveries Dataset")
print(deliveries.info())

# Check missing values
print("\nMissing Values in Matches")
print(matches.isnull().sum())

print("\nMissing Values in Deliveries")
print(deliveries.isnull().sum())

# Remove duplicate rows
matches.drop_duplicates(inplace=True)
deliveries.drop_duplicates(inplace=True)

# Fill missing values
matches.fillna("Unknown", inplace=True)
deliveries.fillna(0, inplace=True)

# Standardize team names
matches.replace("Delhi Daredevils", "Delhi Capitals", inplace=True)
deliveries.replace("Delhi Daredevils", "Delhi Capitals", inplace=True)

# Convert date column to datetime
if 'date' in matches.columns:
    matches['date'] = pd.to_datetime(matches['date'])

# Save cleaned datasets
matches.to_csv("data/cleaned_matches.csv", index=False)
deliveries.to_csv("data/cleaned_deliveries.csv", index=False)

print("\nData Cleaning Completed Successfully")