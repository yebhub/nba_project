from createrosters import RosterCreator as rc


urls = ['http://www.espn.com/nba/team/roster/_/name/gs/golden-state-warriors', 'http://www.espn.com/nba/team/roster/_/name/lal/los-angeles-lakers', 'http://www.espn.com/nba/team/roster/_/name/hou/houston-rockets', 'http://www.espn.com/nba/team/roster/_/name/bos/boston-celtics', 'http://www.espn.com/nba/team/roster/_/name/phi/philadelphia-76ers']

team_names = ['goldenstate', 'lakers', 'rockets', 'celtics', '76ers']

zipped_names_urls = zip(team_names, urls)

for team_name, url in zipped_names_urls:
    generated_textfile = team_name + "_roster.txt"
    team = rc(url, "../" + team_name +'/' + generated_textfile)

    names = team.scrape_playernames()
    team.create_roster(names)







