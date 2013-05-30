import json
import urllib


url = "http://search.twitter.com/search.json?q=apple"

response = urllib.urlopen(url);
dic= json.load(response)

print dic["results"][0]
print dic["results"][0]['created_at']
print dic["results"][0]['from_user_name']
