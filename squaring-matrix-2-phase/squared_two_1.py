import MapReduce
import itertools
from itertools import combinations
import sys


"""
Squaring Matrix using MapReduce framework:Phase 1
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    mr.emit_intermediate(record[1],('A',record[0],record[2]))
	mr.emit_intermediate(record[0],('B',record[1],record[2]))
	
    
def reducer(key, list_of_values):
    a=[]
    b=[]
    dcombine={}
    for ele in list_of_values:
        if ele[0]=='A':
            a.append(ele);
        else:
            b.append(ele);        

    for x in a:
        for y in b:
            mr.emit((x[1],y[1],x[2]*y[2]))

    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)