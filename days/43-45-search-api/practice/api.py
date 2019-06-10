from typing import List
import requests
from pprint import pprint
import collections

Movie = collections.namedtuple('Movie', 'imdb_code, title, director, keywords, '
                                        'duration, genres, rating, year, imdb_score')


def find_movie_by_title(keyword: str) -> List[Movie]:
    url = f'http://movie_service.talkpython.fm/api/search/{keyword}'
    #print(url)

    resp = requests.get(url)
    resp.raise_for_status()  # Check for errors

    # print(resp.text)
    results = resp.json()

    movies = []
    for r in results.get('hits'):
        movies.append(Movie(**r))

    return movies






