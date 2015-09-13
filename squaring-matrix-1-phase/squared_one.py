import MapReduce
import itertools
from itertools import combinations
import sys


"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    for subset in itertools.combinations(record, 2):
      mr.emit_intermediate(subset,1)

    
def reducer(key, list_of_values):
    
    total = 0
    for v in list_of_values:
      total += v
    
    if total>=100:
      mr.emit((list(key)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
