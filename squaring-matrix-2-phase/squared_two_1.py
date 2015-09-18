import MapReduce
import itertools
from itertools import combinations
import sys


"""
Squaring Matrix using MapReduce framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	mr.emit_intermediate(record[1],('A',record[0],record[2]))
	mr.emit_intermediate(record[0],('B',record[1],record[2]))
	
    
def reducer(key, list_of_values):
    d1={}
    d2={}
    for ele in list_of_values:
        if ele[0]=='A':
            d1.setdefault(ele[0],[])
            d1[ele[0]].append((ele[1],ele[2]));

        else:
            d2.setdefault(ele[0],[])
            d2[ele[0]].append((ele[1],ele[2]));
    
    
    # a={}
    # for e in d1:
    #     a.setdefault(e[0],"")
    #     a[e[0]]=e[0]
    
    a=d1['A']
    b=d2['B']

    d3={}
    for e in range(len(a)):
        d3[a[e]]=(a[0],b[0])    

    print list_of_values
    print ("d1",d1)
    print ("d2",d2)
       
    # 	if ele[0] == 'A':
    # 		d.setdefault(ele[2],[])
    # 		d[ele[2]].append(ele[3])

    # 	if ele[0] == 'B':
    # 		d.setdefault(ele[1],[])
    # 		d[ele[1]].append(ele[3])

    # total=0

    # for k, v in d.iteritems():
    # 	if len(v)<2:
    # 		total+=0
    # 	else:
    # 		total+=v[0]*v[1]
    	
    # mr.emit(key+(total,))
    sys.exit()

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)