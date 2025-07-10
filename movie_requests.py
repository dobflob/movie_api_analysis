from keys import api_key
from sample_data import data
from datetime import datetime
import requests
import csv
import re

movies = []

def parse_awards(award_str):

    match = re.search(r'(Won (?P<oscars>\d+) Oscars?. )?((?P<wins>\d+) wins & )?((?P<noms>\d+) nominations)?', award_str)

    oscars = int(match.group('oscars')) if match.group('oscars') else 0
    wins = int(match.group('wins')) if match.group('wins') else 0
    noms = int(match.group('noms')) if match.group('noms') else 0

    return oscars, wins, noms
    
def format_date(date_str):
    format_str = '%d %b %Y'
    dt = datetime.strptime(date_str, format_str)
    return dt.date()

def parse_runtime(runtime_str):
    words = runtime_str.split()
    return int(words[0])

def parse_boxoffice(box_str):
    if box_str == 'N/A':
        box_office = 0
    else:
        box_office = box_str.replace('$', '').replace(',', '')
    return int(box_office)

def add_movie(movie_info):
    movie = {}

    movie['Title'] = movie_info['Title']
    movie['Year'] = int(movie_info['Year'])
    movie['Rated'] = movie_info['Rated']
    movie['Released'] = format_date(movie_info['Released'])
    movie['Runtime'] = parse_runtime(movie_info['Runtime'])
    movie['Genre'] = movie_info['Genre']
    movie['Actors'] = movie_info['Actors']
    movie['Oscars'], movie['Award_Wins'], movie['Award_Nominations'] = parse_awards(movie_info['Awards'])
    movie['Box_Office'] = parse_boxoffice(movie_info['BoxOffice'])

    movies.append(movie) 

# Create a function to request data from the OMDb API for each movie in the CSV file using their IMDB Ids
def get_movie_data(id):
    res = requests.get(f'http://www.omdbapi.com/?apikey={api_key}&i={id}')
    data = res.json()
    return data

def main():
    with open('more_oscar_winners.csv', 'r') as csvfile:
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            movie_info = get_movie_data(row['IMDB'])
            add_movie(movie_info)
            
    with open('oscar_winners.csv', 'r') as csvfile:
        data = csv.DictReader(csvfile, delimiter=',')
        for row in data:
            movie_info = get_movie_data(row['IMDB'])
            add_movie(movie_info)
    
    fieldnames = ['Title','Year','Rated','Released','Runtime','Genre','Actors','Oscars','Award_Wins','Award_Nominations','Box_Office']

    with open('movies.csv', 'w') as savefile:
        writer = csv.DictWriter(savefile, fieldnames=fieldnames)
        writer.writeheader()
        
        for movie in movies:
            writer.writerow(movie)

if __name__ == '__main__':
    main()