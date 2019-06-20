import uplink
from pprint import pprint


@uplink.response_handler
def raise_for_status(response):
    response.raise_for_status()
    return response


@uplink.json
@raise_for_status
class MovieSearchClient(uplink.Consumer):

    def __init__(self):
        super().__init__(base_url='http://movie_service.talkpython.fm')

    @uplink.get('/api/search/{keyword}')
    def movie_name(self, keyword):
        """ Search Movies """

    @uplink.get('/api/director/{director_name}')
    def director_name(self, director_name):
        """ Search Movies by Director """

    @uplink.get('/api/movie/{imdb_number}')
    def imdb_number(self, imdb_number):
        """ Search Movie by IMDB code """


def search_movie_name():
    get_name = input('Enter movie name to search for ')
    response = get_movies.movie_name(get_name)
    results = response.json()
    for idx in results['hits']:
        print(f'{idx["title"]} - {idx["director"]} - {idx["imdb_code"]}')


def search_director_name():
    get_name = input('Enter Director name to search for ')
    response = get_movies.director_name(get_name)
    results = response.json()
    for idx in results['hits']:
        print(f'{idx["title"]} - {idx["director"]} - {idx["imdb_code"]}')


def search_imdb_number():
    get_name = input('Enter IMDB Number to search for ')
    response = get_movies.imdb_number(get_name)
    results = response.json()
    # pprint(results)
    print(f'{results["title"]} - {results["director"]} - {results["imdb_code"]}')


get_movies = MovieSearchClient()

print('Select how would you like to search by')
selection_list = ['Movie Title', 'Director Name', 'IMDB Code']

for idx, idx_title in enumerate(selection_list, start=1):
    print(f'{idx} {idx_title}')

while True:
    user_selection = input()
    if user_selection and user_selection.isdigit():
        if int(user_selection) <= len(selection_list):
            if user_selection == '1':
                search_movie_name()
                break
            elif user_selection == '2':
                search_director_name()
                break
            elif user_selection == '3':
                search_imdb_number()
                break

    print('Incorrect selection. Try again')



#
# response = get_movies.movie_name('spider')
# results = response.json()
#
# # get_all_movies = MovieSearchClient.all_entries('spider')
# pprint(results)
#
# for idx in results['hits']:
#     print(idx['title'])

