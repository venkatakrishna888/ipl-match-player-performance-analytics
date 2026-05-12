import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page config
st.set_page_config(
    page_title="IPL Analytics Dashboard",
    layout="wide"
)

# Title
st.title("🏏 IPL Match & Player Performance Analytics")

# Load datasets
matches = pd.read_csv("data/cleaned_matches.csv")
deliveries = pd.read_csv("data/cleaned_deliveries.csv")

# Sidebar
st.sidebar.header("Filters")

# Team filter
teams = sorted(matches['team1'].dropna().unique())

selected_team = st.sidebar.selectbox(
    "Select Team",
    teams
)

# Venue filter
venues = sorted(matches['venue'].dropna().unique())

selected_venue = st.sidebar.selectbox(
    "Select Venue",
    venues
)

# Player filter
players = sorted(deliveries['batter'].dropna().unique())

selected_player = st.sidebar.selectbox(
    "Select Player",
    players
)

# ===============================
# TEAM ANALYSIS
# ===============================

st.header(f"Team Analysis — {selected_team}")

team_wins = matches[matches['winner'] == selected_team]

st.metric(
    "Total Wins",
    team_wins.shape[0]
)

# ===============================
# PLAYER ANALYSIS
# ===============================

st.header(f"Player Analysis — {selected_player}")

player_runs = deliveries[
    deliveries['batter'] == selected_player
]['batsman_runs'].sum()

st.metric(
    "Total Runs",
    player_runs
)

# Boundary analysis
fours = deliveries[
    (deliveries['batter'] == selected_player) &
    (deliveries['batsman_runs'] == 4)
].shape[0]

sixes = deliveries[
    (deliveries['batter'] == selected_player) &
    (deliveries['batsman_runs'] == 6)
].shape[0]

col1, col2 = st.columns(2)

col1.metric("Fours", fours)
col2.metric("Sixes", sixes)

# ===============================
# TOP BATSMEN GRAPH
# ===============================

st.header("Top 10 IPL Run Scorers")

top_batsmen = deliveries.groupby(
    'batter'
)['batsman_runs'].sum()

top_batsmen = top_batsmen.sort_values(
    ascending=False
).head(10)

fig, ax = plt.subplots(figsize=(10,5))

top_batsmen.plot(
    kind='bar',
    ax=ax
)

plt.title("Top 10 IPL Run Scorers")

st.pyplot(fig)

# ===============================
# VENUE ANALYSIS
# ===============================

st.header(f"Venue Analysis — {selected_venue}")

venue_matches = matches[
    matches['venue'] == selected_venue
]

st.metric(
    "Matches Played",
    venue_matches.shape[0]
)

# ===============================
# TOSS IMPACT
# ===============================

st.header("Toss Impact Analysis")

toss_match_win = matches[
    matches['toss_winner'] == matches['winner']
]

total_matches = matches.shape[0]

toss_wins = toss_match_win.shape[0]

toss_percentage = (
    toss_wins / total_matches
) * 100

st.write(
    f"Teams winning toss and match: {round(toss_percentage,2)}%"
)