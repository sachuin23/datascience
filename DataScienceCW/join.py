import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1] 
    value = record
    #print key, value
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
#    total = 0
#    for v in list_of_values:
#      total += v
#    mr.emit((key, total))
# 
    union_list=[]
    order_list=[]
    line_list =[]
    for el in list_of_values:
        if(el[0]=='order'):
            order_list.append(el)
        else:
            line_list.append(el)
            
    for el in order_list:
        temp_list=el[:]
        for el2 in line_list:
            union_list=temp_list[:]
            for item in el2:
                union_list.append(item)         
            mr.emit(union_list)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
