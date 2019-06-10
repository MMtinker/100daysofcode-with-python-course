import api


def main():
    keyword = input("Keyword of title search: ")
    results = api.find_movie_by_title(keyword)

    print(f"\nThere are {len(results)} movies found: \n")
    for r in results:
        # print(f" Title: {r.get('title')}")
        print(f'{r.title} with code {r.imdb_code} has score {r.imdb_score}')



if __name__ == '__main__':
    main()
