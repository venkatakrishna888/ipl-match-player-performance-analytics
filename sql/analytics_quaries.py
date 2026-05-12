-- Total Matches Played
SELECT COUNT(*) AS total_matches
FROM matches;

-- Team Wise Wins
SELECT winner, COUNT(*) AS wins
FROM matches
GROUP BY winner
ORDER BY wins DESC;

-- Top 10 Run Scorers
SELECT batter, SUM(batsman_runs) AS total_runs
FROM deliveries
GROUP BY batter
ORDER BY total_runs DESC
LIMIT 10;

-- Top Wicket Takers
SELECT bowler, COUNT(*) AS wickets
FROM deliveries
WHERE is_wicket = 1
GROUP BY bowler
ORDER BY wickets DESC
LIMIT 10;

-- Toss Impact Analysis
SELECT toss_winner, COUNT(*) AS toss_wins
FROM matches
GROUP BY toss_winner
ORDER BY toss_wins DESC;

-- Best Venues for Chasing
SELECT venue, COUNT(*) AS chasing_wins
FROM matches
WHERE winner = team2
GROUP BY venue
ORDER BY chasing_wins DESC;

-- Powerplay Runs
SELECT batting_team,
       SUM(total_runs) AS powerplay_runs
FROM deliveries
WHERE over <= 6
GROUP BY batting_team
ORDER BY powerplay_runs DESC;

-- Death Overs Runs
SELECT batting_team,
       SUM(total_runs) AS death_over_runs
FROM deliveries
WHERE over >= 16
GROUP BY batting_team
ORDER BY death_over_runs DESC;
