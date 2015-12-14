# /usr/bin/env python
#coding:utf-8

import urllib2,json

s_url = "http://apis.baidu.com/3023/shorturl/shorten?url_long="
url_long = raw_input("Enter url:")
url = s_url+url_long
request = urllib2.Request(url)
request.add_header("apikey","XXXXXXXXXXXXX")
Html_url = urllib2.urlopen(request).read()
Json_url = json.JSONDecoder().decode(Html_url)
Short_url = Json_url['urls'][0]['url_short']
Long_url = Json_url['urls'][0]['url_long']
print u"短网址:"+Short_url
