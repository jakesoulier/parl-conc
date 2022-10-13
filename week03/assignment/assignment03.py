"""
Course: CSE 251 
Lesson Week: 03
File: assignment.py 
Author: Brother Comeau

Purpose: Retrieve Star Wars details from a server

Instructions:

- Each API call must only retrieve one piece of information
- You are not allowed to use any other modules/packages except for the ones used
  in this assignment.
- Run the server.py program from a terminal/console program.  Simply type
  "python server.py"
- The only "fixed" or hard coded URL that you can use is TOP_API_URL.  Use this
  URL to retrieve other URLs that you can use to retrieve information from the
  server.
- You need to match the output outlined in the decription of the assignment.
  Note that the names are sorted.
- You are requied to use a threaded class (inherited from threading.Thread) for
  this assignment.  This object will make the API calls to the server. You can
  define your class within this Python file (ie., no need to have a seperate
  file for the class)
- Do not add any global variables except for the ones included in this program.

The call to TOP_API_URL will return the following Dictionary(JSON).  Do NOT have
this dictionary hard coded - use the API call to get this.  Then you can use
this dictionary to make other API calls for data.

{
   "people": "http://127.0.0.1:8790/people/", 
   "planets": "http://127.0.0.1:8790/planets/", 
   "films": "http://127.0.0.1:8790/films/",
   "species": "http://127.0.0.1:8790/species/", 
   "vehicles": "http://127.0.0.1:8790/vehicles/", 
   "starships": "http://127.0.0.1:8790/starships/"
}
"""

from datetime import datetime, timedelta
import requests
import json
import threading

# Include cse 251 common Python files
from cse251 import *

# Const Values
TOP_API_URL = 'http://127.0.0.1:8790'

# Global Variables
call_count = 0


# TODO Add your threaded class definition here
class myThread(threading.Thread):
    def __init__(self, url):
        threading.Thread.__init__(self)
        self.url = url
        self.response = {}

    def run(self):
        global call_count
        call_count += 1
        print(f'URL: {self.url}')
        response = requests.get(self.url)
        self.response = response.json()
        # self.film_six()
        # print(self.response)
        # return self.response

    # def film_six(self):
    #     film = self.response['films'] + '6'
    #     print(film)


# TODO Add any functions you need here
def film_six(homepage):
    film6 = myThread(rf'{homepage["films"]}6')
    film6.start()
    film6.join()
    return(film6.response)

# def get_characters(person):
#     return person.response['name']
def main():
    log = Log(show_terminal=True)
    log.start_timer('Starting to retrieve data from the server')

    # TODO Retrieve Top API urls
    url = myThread(rf'{TOP_API_URL}')
    url.start()
    url.join()

    # TODO Retireve Details on film 6
    sixthFilm = film_six(url.response)

    # TODO Display results
    print(f'Title: ', sixthFilm['title'])
    print(f'Director: ', sixthFilm['director'])
    print(f'Producer: ', sixthFilm['producer'])
    print(f'Released: ', sixthFilm['release_date'])
    print(f'Characters: ', len(sixthFilm['characters']))
    # print(sixthFilm['characters'])
    peoples = []
    people = []
    for i in range(len(sixthFilm['characters'])):
        person = myThread(sixthFilm['characters'][i])
        person.start()
        people.append(person)
    for x in people:
        x.join()
        peoples.append(x.response['name'])
    people_org = sorted(peoples)
    print(', '.join(people_org))
    # for person in people_org:
    #   print(person, end=", ")
    # Planets
    # print()
    print(f'Planets: ', len(sixthFilm['planets']))
    planets = []
    all_planets = []
    for i in range(len(sixthFilm['planets'])):
      planet = myThread(sixthFilm['planets'][i])
      planet.start()
      planets.append(planet)
    for planet in planets:
      planet.join()
      all_planets.append(planet.response['name'])
    planets_org = sorted(all_planets)
    print(', '.join(planets_org))
    # for planet in planets_org:
    #   print(planet, end= ", ")
    # Starships
    # print()
    print(f'Starships: ', len(sixthFilm['starships']))
    stars = []
    star_ships = []
    for i in range(len(sixthFilm['starships'])):
      star = myThread(sixthFilm['starships'][i])
      star.start()
      stars.append(star)
    for star in stars:
      star.join()
      star_ships.append(star.response['name'])
    star_org = sorted(star_ships)
    print(', '.join(star_org))
    # for star in star_org:
    #   print(star, end=", ")
    # Vehicles
    # print()
    print(f'Vehicles: ', len(sixthFilm['vehicles']))
    stars = []
    star_ships = []
    for i in range(len(sixthFilm['vehicles'])):
      star = myThread(sixthFilm['vehicles'][i])
      star.start()
      stars.append(star)
    for star in stars:
      star.join()
      star_ships.append(star.response['name'])
    vehicle_org = sorted(star_ships)
    print(', '.join(vehicle_org))
    # for vehicle in vehicle_org:
    #   print(vehicle, end=", ")
    # Species 
    # print()
    print(f'Species: ', len(sixthFilm['species']))
    stars = []
    star_ships = []
    for i in range(len(sixthFilm['species'])):
      star = myThread(sixthFilm['species'][i])
      star.start()
      stars.append(star)
    for star in stars:
      star.join()
      star_ships.append(star.response['name'])
    species_org = sorted(star_ships)
    print(', '.join(species_org))
    # for species in species_org:
    #   print(species, end=", ")

    log.stop_timer('Total Time To complete')
    log.write(f'There were {call_count} calls to the server')


if __name__ == "__main__":
    main()
 