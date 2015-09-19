import MapReduce
import itertools
from itertools import combinations
import sys


"""
Phase2: Squaring Matrix using MapReduce framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    key = (record[0],record[1])
    mr.emit_intermediate(key,record[2])
	
    
def reducer(key, list_of_values): 
    sum=0
    for ele in list_of_values:
    	sum+=ele
    mr.emit(key+(sum,))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)