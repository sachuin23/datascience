import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

uniqueWord =set()
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:    
          mr.emit_intermediate(w, key)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    l=set()
    for v in list_of_values:
        l.add(v)

    mr.emit((key, list(l)))

def isAlreadyUsed(word):
    return uniqueWord.__contains__(word);

def addToSet(word):
    uniqueWord.add(word)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
