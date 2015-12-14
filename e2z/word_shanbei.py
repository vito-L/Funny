# /usr/bin/env python
#coding:utf-8
#author = 'zuona'

import urllib2
import json

word = raw_input("Enter word:")
url = "https://api.shanbay.com/bdc/search/?word="+word

wordhtml = urllib2.urlopen(url).read()
wordjson = json.JSONDecoder().decode(wordhtml)
wordinfo = wordjson[u'data']

print  wordinfo[u'cn_definition'][u'defn']
