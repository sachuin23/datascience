import sys
import json

dic_nword={};

def printDic(dic):
    for key in dic:
       print key , "\t",dic[key]  
       
def hw(sent_file,tweet_file):
    dic= fileToDic(sent_file)
    arr= textFromTweet(tweet_file)

    arr_senti=[]
    for line in arr:
        if isinstance(line,basestring):
            words = line.split()
            senti_sum=0.0;
            arr_nword=[];
            for w in words:
                if dic.has_key(w):
                    senti_sum = senti_sum+ dic.get(w)
                else:
                    arr_nword.append(w);
                    senti_sum = senti_sum+0.0;     
        for w in arr_nword:
            if dic_nword.has_key(w):
                dic_nword[w].append(float(senti_sum))
            else:
                dic_nword[w]=[float(senti_sum)];
    
    #print dic_nword
    calculateSentiments(dic_nword)    
    printDic(dic_nword)
  

def lines(fp):
    print str(len(fp.readlines()))
    
    

    

def calculateSentiments(dicWords):
    for key in dicWords:
        wordCount= len(dicWords[key])
        dicWords[key]=sum(dicWords[key])/wordCount

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    sent_file.close()
    tweet_file.close();

def fileToDic(psent_file):
    scoreDict={};
    for line in psent_file:
        key, value = line.split("\t")
        scoreDict[key]=int(value);
        
    return scoreDict

def textFromTweet(tweet_file):
    output=[] ; dic={}
    index=0;
    for line in tweet_file:
        dic=json.loads(line)
        if 'text' in dic.keys() :
           if 'lang' in dic.keys():
              if dic.get('lang') == 'en':   # Looking for english only words
                  output.append(dic.get('text'))
        
    return output
    
if __name__ == '__main__':
    main()
