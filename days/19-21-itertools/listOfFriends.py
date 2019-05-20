import itertools

listOfFriends = 'Mike Sam Tom David'.split()
# team_size = 2
# order_does_matter = False

def friends_teams(listOfFriends, team_size = 2, order_does_matter = False):
    if order_does_matter:
        my_iter_list = itertools.permutations(listOfFriends, team_size)


    else:
        my_iter_list = itertools.combinations(listOfFriends, team_size)

    print(list(my_iter_list))

    # pass

if __name__ == '__main__':
    friends_teams(listOfFriends)