import sys
import json

def hw(sent_file,tweet_file):
    dic= fileToDic(sent_file)
    arr= textFromTweet(tweet_file)

    arr_senti=[]
    counter=0;
    for line in arr:
        if isinstance(line,basestring):
            words = line.split()
            senti_sum=0.0;
            for w in words:
                if dic.has_key(w.strip()):
                    senti_sum = senti_sum+ dic.get(w)
                else:
                    senti_sum = senti_sum+0.0;     
                           
            print senti_sum

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file,tweet_file)
    sent_file.close();
    tweet_file.close();
    
    
def fileToDic(psent_file):
    scoreDict={};
    for line in psent_file:
        key, value = line.split("\t")
        scoreDict[key]=int(value);
        
    return scoreDict

def textFromTweet(tweet_file):
    output=[]
    dic={}
    index=0;
    
    for line in tweet_file:
        dic=json.loads(line)
        if 'text' in dic.keys() :
            output.append(dic.get('text'))
        
    return output

if __name__ == '__main__':
    main()
