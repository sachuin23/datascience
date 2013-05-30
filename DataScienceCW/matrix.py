import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()
MAX_ROW=5
MAX_COL=5

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    arr     = record[0]
    i       = record[1]
    j       = record[2]
    value   = record[3]
    

    if(arr=='a'):
        for k in range(0,MAX_ROW):
            key =(i,k)
            valueT={}
            valueT[('a',i,j)]=value
            mr.emit_intermediate(key,valueT)
    if( arr =='b'):
        for k in range(0,MAX_COL):
            key=(k,j)
            valueT={}
            valueT[('b',i,j)]=value
            mr.emit_intermediate(key,valueT)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    row =key[0];
    col =key[1];
    print key , list_of_values
    sum=0
    foundA=0;

    for k in range(0,MAX_COL):
        aKey=('a',row,k)
        bKey=('b',k,col);
        aKeyValue=0
        bKeyValue=0
        for item in list_of_values:
            if aKey in item:
                aKeyValue= item.get(aKey)
                print  'found a', aKeyValue;
                bKey=('b',k,col)
                break;
        
        for item in list_of_values:
            if bKey in item :
                bKeyValue= item.get(bKey)
                print 'found b',bKeyValue
                break; 
        print 'looking for ', aKey, bKey
        lprod=aKeyValue*bKeyValue;
        sum =sum+ lprod;
        print 'Keys:', aKey, bKey, 'product:',aKeyValue, bKeyValue,'lprod :',lprod 

    
    mr.emit((row,col,sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
