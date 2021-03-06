import MapReduce
import sys
import re

"""
Program to calculate term frequency and document frequency using MapReduce
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    
    for w in words:
      if(re.match('^[\w_]+$', w) is not None):
        mr.emit_intermediate(w.lower(), key)
      
      
def reducer(key, list_of_values):
    # key: word
    # value: list of document identifiers
    d={}
    output_list =[]
    for v in list_of_values:
      d.setdefault(v,0)
      d[v]+=1;
    
    for k,v in d.iteritems():
      temp = [k,v]
      output_list.append(temp)

    final_list=[key,len(d),output_list]
    mr.emit(final_list)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
