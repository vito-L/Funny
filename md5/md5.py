# /usr/bin/env python
#coding:utf-8

import urllib2,json

s_url = "http://apis.baidu.com/chazhao/md5decod/md5decod?md5="
input_md5 = raw_input("Enter Md5:")
url = s_url+input_md5
req = urllib2.Request(url)
req.add_header("apikey","XXXXXXXXXXXXX")
Html_url = urllib2.urlopen(req).read()
Json_url = json.JSONDecoder().decode(Html_url)
