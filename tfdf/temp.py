import itertools
from itertools import combinations
stuff = [1, 2, 3]

for subset in itertools.combinations(stuff, 2):
    print(subset)
