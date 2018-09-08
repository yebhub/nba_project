#will scrape the espn website and populate an empty text file with the names of each player in the golden state warriors.

#later on, we can grab player names as well as their positions within csv files. 

 







goldenstate_names = scrape_playernames('http://www.espn.com/nba/team/roster/_/name/gs/golden-state-warriors')

create_roster(goldenstate_names, 'goldenstate_roster.txt')

