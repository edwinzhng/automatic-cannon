import requests
import json

outFile = open("coordinates.json", "w")

api_key = "n3vg0dfc4j42o0ap4b54mm0msg"
api_secret = "l20v0d9j4a7bnb7lqcqps7rddm"

img_url = "http://ibrahimirfan.com/d3.jpg"
url = "http://api.skybiometry.com/fc/faces/detect?api_key=" + api_key + "&api_secret=" + api_secret + "&urls=" + img_url

r = requests.get(url)

data = json.loads(r.content)
outFile.write(json.dumps(data[u'photos'][0][u'tags'][0]))
print("Saved to coordinates.json")
outFile.close()





