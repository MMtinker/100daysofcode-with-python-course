import api
import requests.exceptions

def main():
    # keyword = 'Python' # input('Keyword of title search: ')
    keyword = input('Keyword of title search: ')

    try:
        results = api.find_movie_by_title(keyword)

        print(f'There are {len(results)} movies found.')
        for r in results:
            print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")

    except requests.exceptions.ConnectionError:
        print('ERROR: check you connection!')

    except TypeError:
        print('ERROR: Got Type Error!')

    except StopIteration:
        print('ERROR: We got stop itteration error')

    except ValueError:
        print('ERROR: You must enter the name')

    except Exception as x:
        print(type(x))
        print(f'---- This did not work. error: {x} ----')

if __name__ == '__main__':
    main()
