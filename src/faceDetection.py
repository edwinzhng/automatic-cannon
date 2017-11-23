# This file makes a post request with the image from the RPi Camera
# and returns formatted data of the positioning of the face.

import requests
import os
import json
import constants as c

# make the post request to skybiometry for face detection and return resulting json
def detectFace():
    # prepare the payload
    url = "http://api.skybiometry.com/fc/faces/recognize?namespaces=se101"
    url += "&api_key=" + c.api_key 
    url += "&api_secret=" + c.api_secret
    url += "&urls=" + c.img_url
    url += "&uids=" + "derrek@se101,ayush@se101,rollen@se101,derek@se101"

    # make the request
    r = requests.get(url)
    data = json.loads(r.content)
    print(data)

    # try to identify a user from the trained facial recognition model
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
        os.system("espeak \"Target Identified, with " + str(confidence) + " percent accuracy. Hello, "  + name + "\"")
    except:
        print("No user found")
    
    # error check (no face detected)
    if (len(data[u'photos'][0][u'tags']) == 0):
        print("Error: No face detected")
        return -1
    return (data[u'photos'][0][u'tags'][0])

# returns {width, height, center: {x,y}} of face in pixels
def getFaceDimensions():
    details = detectFace()

    if details != -1:
        # no error - return face coordinates in pixels
        width = (details[u'width']/100.0)*c.img_width
        height = (details[u'height']/100.0)*c.img_height

        center_x = (details[u'center'][u'x']/100.0)*c.img_width
        center_y = (details[u'center'][u'y']/100.0)*c.img_height
    else:
        # error (no face detected) - return center of screen
        width = c.img_width
        height = c.img_height

        center_x = c.img_width/2
        center_y = c.img_height/2

    return {"width": width, "height": height, "center": {"x": center_x, "y": center_y}}

