# /usr/bin/env python
#coding:utf-8
#author = 'zuona'

import urllib2,json

url = "http://apis.baidu.com/apistore/aqiservice/aqi?city=上海"
req = urllib2.Request(url)
req.add_header("apikey","XXXXXXXXXXXX")
resp = urllib2.urlopen(req).read()
content = json.JSONDecoder().decode(resp)
Cityinfo = content['retData']['city']
AQI = content['retData']['aqi']
Level = content['retData']['level']
Time = content['retData']['time']
print "City:"+Cityinfo
print "AQI:"+str(AQI)
print "Level:"+Level
print "Time:"+Time
