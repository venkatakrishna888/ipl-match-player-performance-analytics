import pandas as pd
import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Your_SQL_Password",
    database="ipl_analysis"
)

cursor = conn.cursor()

# Load CSV files
matches = pd.read_csv("data/cleaned_matches.csv")
deliveries = pd.read_csv("data/cleaned_deliveries.csv")

# Insert matches data
for _, row in matches.iterrows():
    sql = """
    INSERT INTO matches (
        id, city, match_date, player_of_match,
        venue, team1, team2, toss_winner,
        toss_decision, winner, result_type,
        result_margin
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        int(row['id']),
        str(row['city']),
        str(row['date']),
        str(row['player_of_match']),
        str(row['venue']),
        str(row['team1']),
        str(row['team2']),
        str(row['toss_winner']),
        str(row['toss_decision']),
        str(row['winner']),
        str(row['result']),
        float(row['result_margin']) if row['result_margin'] != 'Unknown' else 0
    )

    cursor.execute(sql, values)

conn.commit()

print("Matches Data Imported Successfully")

# Insert deliveries data
for _, row in deliveries.iterrows():

    sql = """
    INSERT INTO deliveries (
        match_id, inning, batting_team,
        bowling_team, over_number, ball,
        batter, bowler, batsman_runs,
        extra_runs, total_runs, is_wicket
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (
        int(row['match_id']),
        int(row['inning']),
        str(row['batting_team']),
        str(row['bowling_team']),
        int(row['over']),
        int(row['ball']),
        str(row['batter']),
        str(row['bowler']),
        int(row['batsman_runs']),
        int(row['extra_runs']),
        int(row['total_runs']),
        int(row['is_wicket'])
    )

    cursor.execute(sql, values)

conn.commit()

print("Deliveries Data Imported Successfully")

# Close connection
cursor.close()
conn.close()
