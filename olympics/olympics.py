'''
'''
import sys
import psycopg2
import config
import argparse

def connect_to_database():
    try:
        return psycopg2.connect(database=config.database,
                                user=config.user,
                                password=config.password)
    except Exception as e:
        print(e, file=sys.stderr)
        exit()

def parsed_arguments():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--athletes", help="A 3-letter NOC to list the athletes for that country")
    parser.add_argument("-m", "--medals", action = 'store_true', help="Lists the number of gold medals won by each NOC in descending order")
    parser.add_argument("-g", "--indigold", action = 'store_true', help="Lists all athletes who have recieved a gold medal")
    
    parsed_arguments = parser.parse_args()
    return parsed_arguments


def athletes_query(noc, cursor):
    try:
        query_string = noc 
        query = '''SELECT DISTINCT athletes.name
            FROM athletes, event_results, noc_regions
            WHERE athletes.id = event_results.athlete_id
            AND noc_regions.id = event_results.noc_id
            AND noc_regions.noc = %s'''
        cursor.execute(query, (query_string,))
        return cursor
    except Exception as e:
        print(e)
        exit()

def print_athletes_query(noc, cursor):
    print('===== All Athletes from ' + noc + ' =====')
    for row in cursor:
        print(row[0])
    print()


def gold_medals(cursor):
    try:
        query = '''SELECT noc_regions.noc, COUNT(event_results.medal)
          FROM noc_regions, event_results
          WHERE event_results.medal = 'Gold'
          AND noc_regions.id = event_results.noc_id
          GROUP BY noc_regions.noc
          ORDER BY COUNT(event_results.medal) DESC'''        
          
        cursor.execute(query)
        return cursor
    except Exception as e:
        print(e)
        exit()

def print_gold_medals(cursor):
    print('===== NOCS and their total gold medals =====')
    for row in cursor:
        print(row[0], row[1])
    print()    

def athlete_medals(cursor):
    try:
        query = '''SELECT DISTINCT athletes.name, COUNT(event_results.medal)
          FROM athletes, event_results
          WHERE event_results.medal = 'Gold'
          AND athletes.id = event_results.athlete_id
          GROUP BY athletes.name
          ORDER BY COUNT(event_results.medal) DESC'''        
          
        cursor.execute(query)
        return cursor
    except Exception as e:
        print(e)
        exit()

def print_athlete_medals(cursor):
    print('===== Athletes and their total gold medals =====')
    for row in cursor:
        print(row[0])
    print()  


def main():
    arguments = parsed_arguments()
    connection = connect_to_database()
    cursor = connection.cursor()

    if arguments.athletes: 
        noc_athletes = athletes_query(arguments.athletes, cursor)
        print_athletes_query(arguments.athletes, noc_athletes)

    if arguments.medals:
        noc_gold_medals = gold_medals(cursor)
        print_gold_medals(noc_gold_medals)

    if arguments.indigold: 
        athlete_gold_medals = athlete_medals(cursor)
        print_athlete_medals(athlete_gold_medals)

    connection.close()

if __name__ == '__main__':
    main()