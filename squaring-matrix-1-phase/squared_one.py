import MapReduce
import itertools
from itertools import combinations


"""
Squaring Matrix using MapReduce framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	for k in range(5):
		mr.emit_intermediate((record[0],k),('A',record[0],record[1],record[2]))
		mr.emit_intermediate((k,record[1]),('B',record[0],record[1],record[2]))
	
    
def reducer(key, list_of_values):
    d={}
    for ele in list_of_values:
    	if ele[0] == 'A':
    		d.setdefault(ele[2],[])
    		d[ele[2]].append(ele[3])

    	if ele[0] == 'B':
    		d.setdefault(ele[1],[])
    		d[ele[1]].append(ele[3])

    total=0
    for k, v in d.iteritems():
    		total += v[0]*v[1]		
    
    mr.emit(key+(total,))
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
