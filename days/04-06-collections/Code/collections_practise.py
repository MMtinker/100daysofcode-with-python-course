# using collections library

import collections
from pprint import pprint

# dic = {
#     'two': 2,
#     'five': 5,
#     'one': 1,
#     'three': 3,
#     'four': 4
# }

dic = collections.defaultdict(int)
pprint(dic)

# Order dictionary

# dic_ordered = collections.OrderedDict(dic)
#
# pprint(dic_ordered)