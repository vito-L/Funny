#!/usr/bin/env python3
# coding:utf-8
# Created by Vito at 2020/4/4
# FILE_NAME: apiclient.py

import unittest
import ddt
import requests
from BeautifulReport import BeautifulReport as bf
from urllib import parse

@ddt.ddt #声明这个类要用ddt
class Switch(unittest.TestCase):
    base_url = 'http://127.0.0.1:5000'
    # ddt自动读取文件，并获取内容传给下面的函数，循环调用，运行如果出现字符编码问题，打开file_data源文件，搜索open，加上encoding=utf-8
    @ddt.file_data('config.yaml')
    def test_request(self,**kwargs):
        detail = kwargs.get('detail','nothing')
        self._testMethodDoc=detail
        url = kwargs.get('url')
        url = parse.urljoin(self.base_url,url)
        method = kwargs.get('method','get')
        data = kwargs.get('data',{})
        header = kwargs.get('header',{})
        cookie = kwargs.get('cookie',{})
        check = kwargs.get('check')
        method=method.lower()
        try:
            if method == 'get':
                res = requests.get(url,params=data,cookies=cookie,headers=header).text
            else:
                res = requests.post(url,data,cookies=cookie,headers=header).text
        except Exception as e:
            print('api error')
            res = e
        for c in check:
            self.assertIn(c,res,msg='不符合预期,预期:%s,实际:%s' % (c,res))

suite = unittest.TestSuite()
# suite.addTest(Switch('test_request'))
suite.addTest(unittest.makeSuite(Switch))
run = bf(suite)
run.report('switch_test','开关测试')
print(run.success_count)
print(run.failure_count)





