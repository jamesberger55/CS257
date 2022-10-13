'''
convert.py

Doug Pham
October 10, 2022

This program creates separate csv files for the different fields in the athlete_events.csv file
into organize tables to be used in SQL

NOTE - The following fields are ignored in the athlete_events.csv file:

    Year (column 9) field is ignored since it is exactly repeated in the Games field
    Season (column 10) field is ignored since it is exactly repeated in the Games field
    Sport (column 12) field is ignored since it is exactly repeated in the Event field
'''

import csv

athletes = {}
with open('athlete_events.csv') as original_data_file,\
        open('athletes.csv', 'w') as athletes_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(athletes_file, lineterminator='\n')
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        athlete_id = row[0]
        athlete_name = row[1]
        if athlete_id not in athletes:
            athletes[athlete_id] = athlete_name
            writer.writerow([athlete_id, athlete_name])


events = {}
with open('athlete_events.csv') as original_data_file,\
        open('events.csv', 'w') as events_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(events_file, lineterminator= '\n')
    heading_row = next(reader) # eat up and ignore the heading row of the data file
    for row in reader:
        event_name = row[13]
        if event_name not in events:
            event_id = len(events) + 1
            events[event_name] = event_id
            writer.writerow([event_id, event_name])

countries = {}
with open('athlete_events.csv') as original_data_file,\
        open('countries.csv', 'w') as countries_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(countries_file, lineterminator= '\n')
    heading_row = next(reader)
    for row in reader:
        country_noc = row[7]
        if country_noc not in countries:
            country_id = len(countries) + 1
            country_team = row[6]
            countries[country_noc] = country_id
            writer.writerow([country_id, country_team, country_noc])

settings = {}
with open('athlete_events.csv') as original_data_file,\
        open('settings.csv', 'w') as settings_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(settings_file, lineterminator= '\n')
    heading_row = next(reader)
    for row in reader:
        games = row[8]
        if games not in settings:
            games_id = len(settings) + 1
            games_city = row[11]
            settings[games] = games_id
            writer.writerow([games_id, games, games_city])

results = {}
with open ('athlete_events.csv') as original_data_file,\
        open('results.csv', 'w') as results_file:
    reader = csv.reader(original_data_file)
    writer = csv.writer(results_file, lineterminator= '\n')
    heading_row = next(reader)
    for row in reader:
        medal = row[14]
        if medal not in results:
            medal_id = len(results) + 1
            results[medal] = medal_id
            writer.writerow([medal_id, medal])
