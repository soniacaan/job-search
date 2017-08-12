import requests
import json
from collections import OrderedDict
import urllib.request as request






def get_glassdoor():
    #authentication
    params_gd = OrderedDict({
        "v": "1",
        "format": "json",
        "t.p": "t.p=106965",
        "t.k": "t.k=jsora0nBXXc",
        #programmatically look up IP address
        "userip": json.loads(request.urlopen("http://ip.jsontest.com/").read().decode('utf-8'))['ip'],
        "userip": "userip=2001:569:bddb:4900:79d4:a3b8:f459:b37d",
        "action": "employers",
        #"country": "canada",
        #"city": "vancouver"
        "q": "IBM"
    })
    #URL
    basepath_gd = "http://api.glassdoor.com/api/api.htm"

    #request the API
    data = requests.get(basepath_gd,
                           params=params_gd,
                           headers={
                               "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"
                           })


    #request = requests.get(url + "?" + version + "&" + format + "&" + t_p + "&" + t_k + "&" + 
    #	action + "&" + q + "&" + user_ip + "&" + useragent)
    
    #request = (url + "?" + version + "&" + format + "&" + t_p + "&" + t_k + "&" + 
    #	action + "&" + q + "&" + user_ip + "&" + useragent)
    #data =json.get(request)
   
    return data