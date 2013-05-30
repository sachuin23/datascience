import sys
import json

dic_nwords={}
def calFrequency(tweet_file):
    arr_tweetText= textFromTweet(tweet_file)
    for line in arr_tweetText:
        words = line.split();
        for w in words:
            if dic_nwords.has_key(w):
                dic_nwords[w]= dic_nwords.get(w)+1;
            else:
                dic_nwords[w]=1
    
    numWords=sum(dic_nwords.values())
    for keys in dic_nwords:
        dic_nwords[keys]= float(dic_nwords[keys])/numWords
  

    printDic(dic_nwords)
    
def printDic(dic_file):
    for key in dic_file:
        print  key.encode('utf-8'),  dic_file[key]
        
def main():
    tweet_file = open(sys.argv[1])
    calFrequency(tweet_file)
    tweet_file.close()

def textFromTweet(tweet_file):
    output=[]
    dic={}
    index=0;
    
    for line in tweet_file:
        dic=json.loads(line)
        if 'text' in dic.keys() :
            if 'lang' in dic.keys():
              if dic.get('lang') == 'en':   # Looking for english only words
                  if not '@' in dic.get('text'): 
                      if not '#' in dic.get('text'):
                          output.append(dic.get('text'))
        
    return output
  
if __name__ == '__main__':
    main()