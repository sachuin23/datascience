import oauth2 as oauth
import urllib2 as urllib

import time as time

# See Assignment 1 instructions or README for how to get these credentials
access_token_key = ""
access_token_secret = ""

consumer_key = ""
consumer_secret = ""

_debug = 0

oauth_token    = oauth.Token(key=access_token_key, secret=access_token_secret)
oauth_consumer = oauth.Consumer(key=consumer_key, secret=consumer_secret)

signature_method_hmac_sha1 = oauth.SignatureMethod_HMAC_SHA1()
               

http_method = "GET"

myFile="/home/pankaj/DataScience/DataScienceCW/twitterFeed3.txt"


http_handler  = urllib.HTTPHandler(debuglevel=_debug)
https_handler = urllib.HTTPSHandler(debuglevel=_debug)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''
def twitterreq(url, method, parameters):
  req = oauth.Request.from_consumer_and_token(oauth_consumer,
                                             token=oauth_token,
                                             http_method=http_method,
                                             http_url=url, 
                                             parameters=parameters)

  req.sign_request(signature_method_hmac_sha1, oauth_consumer, oauth_token)

  headers = req.to_header()

  if http_method == "POST":
    encoded_post_data = req.to_postdata()
  else:
    encoded_post_data = None
    url = req.to_url();

  opener = urllib.OpenerDirector()
  opener.add_handler(http_handler)
  opener.add_handler(https_handler)

  response = opener.open(url,encoded_post_data)
  return response

def fetchsamples():
  url = "https://stream.twitter.com/1/statuses/sample.json"
  #url= "http://search.twitter.com/search.json?q=immigration"
  parameters = {
    'oauth_version': "1.0",
    'oauth_nonce': oauth.generate_nonce(),
    'oauth_timestamp': int(time.time()),
    'user': 'pankaj'
   }

  response = twitterreq(url, "GET", parameters)
  myFileHandle= open(myFile,'w')
  start = time.time()
  for line in response:
    if (time.time()-start) < 300:
        myFileHandle.write(line.strip() + '\n')
    else:
        print "finished 10 minutes :"+ str(time.time()-start)
        break
    
  myFileHandle.close()
  
if __name__ == '__main__':
  fetchsamples()
