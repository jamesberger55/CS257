'''
James Berger
CS257
olympics convert.py file
'''

import csv

olympian = {}
kaggle_data = open('athlete_events.csv')
reader = csv.reader(kaggle_data)
olympian_file = open('olympian.csv', 'w')
writer = csv.writer(olympian_file)
heading_row = next(reader) 
for row in reader:
    olympian_id = row[0]
    olympian_name = row[1]
    if olympian_id not in olympians:
        olympian[olympian_id] = olympian_name
        writer.writerow([olympian_id, olympian_name])
kaggle_data.close()
olympian_file.close()


event = {}
kaggle_data = open('athlete_events.csv')
reader = csv.reader(kaggle_data)
event_file = open('event.csv', 'w')
writer = csv.writer(event_file)
heading_row = next(reader) 
for row in reader:
    event_name = row[13]
    if event_name not in events:
        event_id = len(events) + 1
        event[event_name] = event_id
        writer.writerow([event_id, event_name])
event_file.close()

country = {}
kaggle_data = open('athlete_events.csv')
reader = csv.reader(kaggle_data)
country_file = open('country.csv', 'w')
writer = csv.writer(country_file)
heading_row = next(reader)
for row in reader:
    country_name = row[6]
    if country_name not in country:
        country_id = len(country) + 1
        country[country_name] = country_id
        writer.writerow([country_id, country_name])
country_file.close()

games = {}
kaggle_data = open('athlete_events.csv')
reader = csv.reader(kaggle_data)
games_file = open('games.csv', 'w')
writer = csv.writer(games_file)
heading_row = next(reader) 
for row in reader:
    game_name = row[8]
    if game_name not in games:
        game_id = len(games) + 1
        games[game_name] = game_id
        writer.writerow([game_id, game_name])
games_file.close()


olympics_info = {}
kaggle_data = open('athlete_events.csv')
reader = csv.reader(kaggle_data)
olympics_info_file = open('olympics_year.csv', 'w')
writer = csv.writer(olympics_info_file)
heading_row = next(reader)
for row in reader:
    olympic_info_year = row[9]
    olympic_info_season = row[10]
    olympic_info_city = row[11]
    if olympic_info_year not in olympics_info:
        olympic_info_id = len(olympics_info) + 1
        olympics_info[olympic_year] = olympic_info_id
        writer.writerow([olympic_id, olympic_year, olympic_season, olympic_city])
olympics_file.close()
original_data_file.close()

noc_regions = {}
noc_kaggle_file = open('noc_regions.csv', 'rU')
reader = csv.reader(noc_kaggle_file)
noc_file = open('noc_data.csv', 'w')
writer = csv.writer(noc_file)
heading_row = next(reader)
for row in reader:
    noc = row[0]
    region = row[1]
    notes = row[2]
    if noc not in noc_regions:
        noc_id = len(noc_regions) + 1
        noc_regions[noc] = noc_id
        writer.writerow([noc_id, noc, region, notes])

original_data_file = open('athlete_events.csv')
reader = csv.reader(kaggle_data)
heading_row = next(reader) 
for row in reader:
    noc = row[7]
    region = row[6]
    notes = ''
    if noc not in noc_regions:
        noc_id = len(noc_regions) + 1
        noc_regions[noc] = noc_id
        writer.writerow([noc_id, noc, region, notes])
noc_file.close()


kaggle_data = open('athlete_events.csv')
reader = csv.reader(kaggle_data)
event_results_file = open('event_results.csv', 'w')
writer = csv.writer(event_results_file)
heading_row = next(reader) 
for row in reader:
    athlete_id = row[0]
    event_name = row[13]
    event_id = events[event_name] 
    team_name = row[6]
    team_id = teams[team_name] 
    game_name = row[8]
    game_id = games[game_name] 
    olympic_year = row[9]
    olympic_id = olympics[olympic_year] 
    noc = row[7]
    noc_id = noc_regions[noc] 
    medal = row[14]
    writer.writerow([athlete_id, event_id, team_id, game_id, olympic_id, noc_id, medal])
event_results_file.close()
