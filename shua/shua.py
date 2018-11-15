#!/usr/bin/env python2
#coding:utf-8

from selenium import webdriver
import time,random

def Views():
    url = "******"
    for i in range(3):
        browser = webdriver.PhantomJS()
        browser.get(url)
        time.sleep(random.randint(1,25))
        browser.close()
        print "成功访问{}次".format(i+1)
        i += 1

Views()

