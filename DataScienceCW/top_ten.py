import sys
import json

import heapq



dic_hasTag={}

arr_heapDS=[];

MAX_SIZE=10;


def getTop10():

    for key in dic_hasTag.keys():
        if len(arr_heapDS) <MAX_SIZE+1:
            heapq.heappush(arr_heapDS,(dic_hasTag.get(key),key ))
        else:
#            print arr_heapDS
            item = heapq.heappop(arr_heapDS)
            if int(item[0]) < int(dic_hasTag.get(key)):
                heapq.heapreplace(arr_heapDS,(dic_hasTag.get(key), key))
            
def fileToDic(psent_file):
    scoreDict={};
    for line in psent_file:
        key, value = line.split("\t")
        scoreDict[key]=int(value);
        
    return scoreDict

def printDic(dic):
    for line in dic.keys():
        print line, dic[line]
        
def addToHashTagDic(key):
    if dic_hasTag.has_key(key):
        dic_hasTag[key]= int(dic_hasTag[key])+1.0
    else:
        dic_hasTag[key]=1.0;
    

def hashTagsFromTweet(tweet_file):
    output={} ; dic={};
    for line in tweet_file:
        dic= json.loads(line)
        arr_htag=[]        
        if 'entities' in dic.keys() :
                if dic.get('entities').has_key('hashtags'):
                    arr_htag = dic['entities']['hashtags']
                    for d in arr_htag:
                        if  'text' in d.keys():
                            addToHashTagDic(d.get('text'))
            
    
    
def main():
    tweet_file = open(sys.argv[1])
    hashTagsFromTweet(tweet_file)
    tweet_file.close();
    getTop10()
    for item in arr_heapDS:
        print item[1], item[0]
    
if __name__ == '__main__':
    main()

