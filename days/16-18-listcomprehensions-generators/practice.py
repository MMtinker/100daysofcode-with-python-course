from pprint import pprint
import random

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

listOfNames = [name.title() for name in NAMES]

# pprint(listOfNames)

def split_names(name):
    firstName, lastName = name.split(' ')
    return f'{lastName} {firstName}'

reversedNames = [split_names(name).title() for name in NAMES]

def gen_pairs():
    #  again a list comprehension is great here to get the first names
    # and title case them in just 1 line of code (this comment took 2)
    first_names = [name.split()[0].title() for name in NAMES]
    while True:

        #  added this when I saw Julian teaming up with Julian (always test your code!)
        first, second = None, None
        while first == second:
            first, second = random.sample(first_names, 2)

        yield f'{first} teams up with {second}'


pairs = gen_pairs()
for _ in range(10):
    x = next(pairs)
    print(x)

