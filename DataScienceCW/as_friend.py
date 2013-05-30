import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()
dic_list={}

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    dic_list[(key,value)]=value;
    mr.emit_intermediate(key, value);
    mr.emit_intermediate(value,key);
    


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    print key, list_of_values
    for name in list_of_values:
        nKey=(key,name)
        if(dic_list.has_key(nKey) is not True):
            mr.emit((key,name))
            mr.emit((name,key))




# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
