# /usr/bin/env python
#coding:utf-8
#author = 'zuona'

import urllib2,json

url = "http://open.iciba.com/dsapi/"
Html_url = urllib2.urlopen(url).read()
Json_url = json.JSONDecoder().decode(Html_url)
Content_url = Json_url[u'content']
Note_url = Json_url[u'note']

print Content_url + "\n" + Note_url