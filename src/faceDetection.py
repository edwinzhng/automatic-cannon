import requests
import json

img_height = 720
img_width = 720

# make the post request to skybiometry for face detection and return resulting json
def detectFace():
    api_key = "n3vg0dfc4j42o0ap4b54mm0msg"
    api_secret = "l20v0d9j4a7bnb7lqcqps7rddm"

    img_url = "http://52.14.199.236/data.jpg"
    url = "http://api.skybiometry.com/fc/faces/detect?api_key=" + api_key + "&api_secret=" + api_secret + "&urls=" + img_url

    r = requests.get(url)

    data = json.loads(r.content)
    return (data[u'photos'][0][u'tags'][0])

# returns {width, height, center: {x,y}} of face in pixels
def getFaceDimensions():
    details = detectFace()

    width = (details[u'width']/100.0)*img_width
    height = (details[u'height']/100.0)*img_height

    center_x = (details[u'center'][u'x']/100.0)*img_width
    center_y = (details[u'center'][u'y']/100.0)*img_height

    return {"width": width, "height": height, "center": {"x": center_x, "y": center_y}}

