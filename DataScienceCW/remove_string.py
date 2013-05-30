import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""


mr = MapReduce.MapReduce()
list_unique=set()

dic_noDup={}
# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key,value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    output=''
    for seq in list_of_values:
        output= seq[0:-10]
        if(list_unique.__contains__(output) is not True):
            list_unique.add(output)
            mr.emit(output)
    
    

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
