import requests
import json

def detectFace():
    api_key = "n3vg0dfc4j42o0ap4b54mm0msg"
    api_secret = "l20v0d9j4a7bnb7lqcqps7rddm"
    img_url = "http://www.ibrahimirfan.com/rollen5.jpg"

#    url = "http://api.skybiometry.com/fc/faces/detect?api_key=" + api_key + "&api_secret=" + api_secret + "&urls=" + img_url + "&namespaces=se101"
 #   url = "http://api.skybiometry.com/fc/tags/save?api_key=" + api_key + "&api_secret=" + api_secret + "&urls=" + img_url + "&tids=TEMP_F@0769c1ef3e529c643b07c4a6011100d7_d9e85c0129c4a_68.25_35.83_0_1,TEMP_F@04a457bc7a3dec2621822ccd00ae011c_d252e8069c129_79.09_86.06_0_1" + "&uid=derek@se101"
    #url = "http://api.skybiometry.com/fc/faces/status?api_key=" + api_key + "&api_secret=" + api_secret + "&uids=rollen@se101"
    url = "http://api.skybiometry.com/fc/faces/recognize?api_key=" + api_key + "&api_secret=" + api_secret + "&urls=" + img_url + "&uids=rollen@se101"

    r = requests.get(url)
    data = json.loads(r.content)
    print data

detectFace()


