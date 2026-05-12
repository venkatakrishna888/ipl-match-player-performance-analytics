import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
matches = pd.read_csv("data/cleaned_matches.csv")

# Select useful columns
data = matches[[
    'team1',
    'team2',
    'toss_winner',
    'toss_decision',
    'venue',
    'winner'
]]

# Remove unknown winners
data = data[data['winner'] != 'Unknown']

# Drop missing values
data.dropna(inplace=True)

# Encode categorical columns
label_encoders = {}

for column in data.columns:

    encoder = LabelEncoder()

    data[column] = encoder.fit_transform(data[column])

    label_encoders[column] = encoder

# Features and target
X = data.drop('winner', axis=1)

y = data['winner']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Improved Model Accuracy:", round(accuracy * 100, 2), "%")