import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]
empty = '- - - - - - -'.split()
loc = itertools.chain(locations, empty)
conf = itertools.chain(confirmed, empty)


def get_attendees():
    # for participant in zip(names, locations, confirmed):
    #     print(participant)
    for participants in names:
        tupleOut = (participants, next(loc), next(conf))
        print(tupleOut)

if __name__ == '__main__':
    get_attendees()