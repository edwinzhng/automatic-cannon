import requests
import json

def detectFace():
    api_key = "n3vg0dfc4j42o0ap4b54mm0msg"
    api_secret = "l20v0d9j4a7bnb7lqcqps7rddm"
    img_url = "http://www.ibrahimirfan.com/d6.jpg"

#    url = "http://api.skybiometry.com/fc/faces/detect?api_key=" + api_key + "&api_secret=" + api_secret + "&urls=" + img_url + "&namespaces=se101"
 #   url = "http://api.skybiometry.com/fc/tags/save?api_key=" + api_key + "&api_secret=" + api_secret + "&urls=" + img_url + "&tids=TEMP_F@0b7f8a323da412635ec90b1401fb016b_dec3106e90d1f_50.70_48.34_0_1,TEMP_F@010799f55da2de8817a8ede801bc01a6_d353379e29a66_44.40_56.19_0_1,TEMP_F@0c3bd5753451c0564486c0c101fb01a4_a28e724f90e35_50.70_55.93_0_1,TEMP_F@0cac4f004c98068205b1e27a02a601f9_cb1ab31b0eb53_67.80_67.24_0_1" + "&uid=derrek@se101"
    #url = "http://api.skybiometry.com/fc/faces/train?api_key=" + api_key + "&api_secret=" + api_secret + "&uids=derrek@se101"
    url = "http://api.skybiometry.com/fc/faces/recognize?api_key=" + api_key + "&api_secret=" + api_secret + "&urls=" + img_url + "&uids="

    r = requests.get(url)
    data = json.loads(r.content)
    print data

detectFace()


