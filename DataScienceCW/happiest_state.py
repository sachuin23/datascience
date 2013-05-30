import sys
import json
import operator


arr_happy=[]
dic_happyState={} # dictionary of tweet state to its sentiment value
dic_affine={}
dic_sa={}

def fileToDic(psent_file):
    for line in psent_file:
        key, value = line.split("\t")
        dic_affine[key]=int(value);
       

def calculateSentiment(dic_tweet):
    senti_value=0.0
    for key in dic_tweet.keys():
        if 'text' in dic_tweet.keys():
            text = dic_tweet.get('text');
            words = text.split();
            for w in words:
                if dic_affine.has_key(w.strip()):
                   senti_value= senti_value+dic_affine.get(w)
                
    return senti_value           

def parseStateInfo(dic_tweet):
    state=''
    for keys in dic_tweet.keys():
        if 'place' in dic_tweet.keys():
            if dic_tweet.get('place') is not None:
                if dic_tweet.get('place').get('country_code') == 'US':
                   if dic_tweet.get('place').get('full_name') is not None:
                        city,state= dic_tweet.get('place').get('full_name').split(",")
    return state

def findHappiest(dic_happy):
    happiest=''
    highestSoFar=-9999.9999
    for key in dic_happy:
        if dic_happy[key] > highestSoFar:
            highestSoFar=dic_happy[key]
            happiest =key    
    return happiest
            
      
def calcHappiest(affine_file,tweet_file):
    fileToDic(affine_file)    
    for line in tweet_file:
        dic = json.loads(line)
        senti = calculateSentiment(dic)
        state = parseStateInfo(dic)
        state = state.strip()
        if (state =='' or len(state) > 2 or state == 'US' or state is None):
           continue           
    
        if dic_happyState.has_key(state):
           dic_happyState[state].append(float(senti))
        else:
           dic_happyState[state]=[senti]
           
    #dic_sa= dic_happyState.copy()
    for key in dic_happyState:
        dic_sa[key]=dic_happyState[key]
        # non zero tweets = 
        obj=[]
        for x in dic_happyState[key]: 
            if x!=0.0:
               obj.append(x)
   
        if(obj ==[]):
            obj.append(0.0)
             
        dic_happyState[key]= sum(obj)/len(obj)  
 
    return findHappiest(dic_happyState)
        

def main():
    affine_file= open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    print calcHappiest(affine_file,tweet_file)
    tweet_file.close()
    affine_file.close()
#        
#    sorted_touple_list = sorted(dic_happyState.iteritems(),key=operator.itemgetter(1), reverse=True)
#    for key in sorted_touple_list:
#        print key[0], key[1]
#
#    print "*******************************"
#    for key in dic_sa.keys():
#        print key , dic_sa[key]
#        
#    print "********************************"


if __name__ == '__main__':
    main()