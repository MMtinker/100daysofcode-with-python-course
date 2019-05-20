import itertools
import os
import urllib.request

# PREWORK
DICTIONARY = os.path.join('/tmp', 'dictionary.txt')
urllib.request.urlretrieve('http://bit.ly/2iQ3dlZ', DICTIONARY)

with open(DICTIONARY) as f:
    dictionary = set([word.strip().lower() for word in f.read().split()])

print(dictionary)

def get_possible_dict_words(draw):
    """Get all possible words from a draw (list of letters) which are
       valid dictionary words. Use _get_permutations_draw and provided
       dictionary"""
    # pass
    permutations = _get_permutations_draw(draw)
    print(permutations)
    wordList = []
    for word in permutations:
        if word.lower() in dictionary:
            wordList.append(word)

    return wordList


def _get_permutations_draw(draw):
    """Helper to get all permutations of a draw (list of letters), hint:
       use itertools.permutations (order of letters matters)"""
    myList = []
    for idx in range(2, len(draw)+1):
        myWord = itertools.permutations(draw, idx)
        myList += ["".join(a) for a in myWord]
    return myList

# ----------

draw = 'G A R Y T E V'.lower().split()

# permutations = _get_permutations_draw(draw)
# print(permutations)

allWords = get_possible_dict_words(draw)

print(allWords)