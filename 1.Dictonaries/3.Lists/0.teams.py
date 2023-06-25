teams = ['KKR', 'CSK', 'RR', 'RCB']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(f"{home_team} vs {away_team}")