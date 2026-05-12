CREATE DATABASE IPL_ANALYSIS;

USE IPL_ANALYSIS;

CREATE TABLE matches (
    id INT PRIMARY KEY,
    city VARCHAR(100),
    match_date DATE,
    player_of_match VARCHAR(100),
    venue VARCHAR(255),
    team1 VARCHAR(100),
    team2 VARCHAR(100),
    toss_winner VARCHAR(100),
    toss_decision VARCHAR(50),
    winner VARCHAR(100),
    result_type VARCHAR(50),
    result_margin FLOAT
);

CREATE TABLE deliveries (
    match_id INT,
    inning INT,
    batting_team VARCHAR(100),
    bowling_team VARCHAR(100),
    over_number INT,
    ball INT,
    batter VARCHAR(100),
    bowler VARCHAR(100),
    batsman_runs INT,
    extra_runs INT,
    total_runs INT,
    is_wicket INT
);

SHOW TABLES;

SELECT * FROM MATCHES;
SELECT * FROM DELIVERIES;

SELECT COUNT(*) FROM MATCHES;
SELECT COUNT(*) FROM DELIVERIES;

# most winning teams
SELECT winner, COUNT(*) AS total_wins
FROM matches
GROUP BY winner
ORDER BY total_wins DESC;

# Top run scorer
SELECT batter, SUM(batsman_runs) AS total_runs
FROM deliveries
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 10;

# Most wickets
SELECT bowler, COUNT(*) AS wickets
FROM deliveries
WHERE is_wicket = 1
GROUP BY bowler
ORDER BY wickets DESC
LIMIT 10;

# Toss win impact
SELECT 
    COUNT(*) AS toss_and_match_win
FROM matches
WHERE toss_winner = winner;

# Highest score venus
SELECT 
    m.venue,
    AVG(d.total_runs) AS avg_runs
FROM matches m
JOIN deliveries d
ON m.id = d.match_id
GROUP BY m.venue
ORDER BY avg_runs DESC
LIMIT 10;

# Best strike rate
SELECT 
    batter,
    SUM(batsman_runs) AS runs,
    COUNT(ball) AS balls,
    (SUM(batsman_runs) / COUNT(ball)) * 100 AS strike_rate
FROM deliveries
GROUP BY batter
HAVING balls >= 500
ORDER BY strike_rate DESC
LIMIT 10;