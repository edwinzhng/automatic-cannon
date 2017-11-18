import requests
import os
import json

img_height = 1080
img_width = 1920

# make the post request to skybiometry for face detection and return resulting json
def detectFace():
    api_key = "n3vg0dfc4j42o0ap4b54mm0msg"
    api_secret = "l20v0d9j4a7bnb7lqcqps7rddm"

    img_url = "http://52.14.199.236/data.jpg"
    url = "http://api.skybiometry.com/fc/faces/recognize?namespaces=se101&api_key=" + api_key + "&api_secret=" + api_secret + "&urls=" + img_url + "&uids=derrek@se101,ayush@se101,rollen@se101,derek@se101"
    r = requests.get(url)
    data = json.loads(r.content)
    print(data)
    try:
        user = data[u'photos'][0][u'tags'][0][u'uids'][0][u'uid']
        confidence =  data[u'photos'][0][u'tags'][0][u'uids'][0][u'confidence']
        if user == u'rollen@se101':
            name = "Rollen D'Souza"
        elif user == u'derek@se101':
            name = "Derek Rayside"
        elif user == u'ayush@se101':
            name = "Ayush Kapur"
        elif user == u'derrek@se101':
            name = "Derrek Chow"
        os.system("say Target Identified, with " + str(confidence) + " percent accuracy. Hello, "  + name)
    except:
        print("No user found")
    return (data[u'photos'][0][u'tags'][0])

# returns {width, height, center: {x,y}} of face in pixels
def getFaceDimensions():
    details = detectFace()

    width = (details[u'width']/100.0)*img_width
    height = (details[u'height']/100.0)*img_height

    center_x = (details[u'center'][u'x']/100.0)*img_width
    center_y = (details[u'center'][u'y']/100.0)*img_height

    return {"width": width, "height": height, "center": {"x": center_x, "y": center_y}}
