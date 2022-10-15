'''
James Berger
CS257
olympics convert.py file
'''

import csv

athletes = {}
original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
athletes_file = open('athletes.csv', 'w')
writer = csv.writer(athletes_file)
heading_row = next(reader) 
for row in reader:
    athlete_id = row[0]
    athlete_name = row[1]
    athlete_sex = row[2]
    athlete_age = row[3]
    athlete_height = row[4]
    athlete_weight = row[5]
    if athlete_id not in athletes:
        athletes[athlete_id] = athlete_name
        writer.writerow([athlete_id, athlete_name, athlete_sex, athlete_age, athlete_height, athlete_weight])
original_data_file.close()
athletes_file.close()

events = {}
original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
events_file = open('events.csv', 'w')
writer = csv.writer(events_file)
heading_row = next(reader) 
for row in reader:
    event_name = row[13]
    sport_name = row[12]
    if event_name not in events:
        event_id = len(events) + 1
        events[event_name] = event_id
        writer.writerow([event_id, event_name, sport_name])
events_file.close()

countries = {}
original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
countries_file = open('countries.csv', 'w')
writer = csv.writer(countries_file)
heading_row = next(reader)
for row in reader:
    country_name = row[6]
    if country_name not in countries:
        country_id = len(countries) + 1
        countries[country_name] = country_id
        writer.writerow([country_id, country_name])
countries_file.close()

games = {}
original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
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
original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
olympics_info_file = open('olympics_info.csv', 'w')
writer = csv.writer(olympics_info_file)
heading_row = next(reader)
for row in reader:
    olympic_year = row[9]
    olympic_season = row[10]
    olympic_city = row[11]
    if olympic_year not in olympics_info:
        olympic_info_id = len(olympics_info) + 1
        olympics_info[olympic_year] = olympic_info_id
        writer.writerow([olympic_info_id, olympic_year, olympic_season, olympic_city])
olympics_info_file.close()
original_data_file.close()

noc_regions = {}
noc_original_file = open('noc_regions.csv')
reader = csv.reader(noc_original_file)
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
noc_file.close()


original_data_file = open('athlete_events.csv')
reader = csv.reader(original_data_file)
event_results_file = open('event_results.csv', 'w')
writer = csv.writer(event_results_file)
heading_row = next(reader)
for row in reader:
    athlete_id = row[0]
    event_name = row[13]
    event_id = events[event_name] 
    country_name = row[6]
    country_id = countries[country_name] 
    game_name = row[8]
    game_id = games[game_name] 
    olympic_year = row[9]
    olympic_id = olympics_info[olympic_year] 
    noc_id = noc_regions[noc] 
    medal = row[14]
    writer.writerow([athlete_id, event_id, country_id, game_id, olympic_id, noc_id, medal])
event_results_file.close()