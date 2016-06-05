from urllib2 import urlopen
from json import load

api_url = "https://data.sfgov.org/resource/wwmu-gmzc.json"
response = urlopen(api_url)
movies_year = []

def year_movie(json, year):
    json_obj = load(response)
    for item in json_obj:
        if item["release_year"] == year:
            if item["title"] in movies_year:
                pass
            else:
                movies_year.append(item["title"])
    if len(movies_year) == 0:
        print "There are no movies in that year"

    return movies_year

def print_list():
    for title in movies_year:
        print "*", title

def main():
    year = raw_input("What year do you want to search:? ")
    movie_list = year_movie(api_url, year)
    print_list()

if __name__ == '__main__':
    main()
