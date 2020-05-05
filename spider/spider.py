#!/usr/bin/env python3
# coding:utf-8
# Created by Vito at 2020/5/5
# FILE_NAME: spider.py

# 教程中抓取的是熊猫TV，因该平台倒闭无法访问，故用其他链接代替并保留适合该链接的方法

from urllib import request
import re


class Spider():
    url = "https://books.studygolang.com/gobyexample/"
    # 匹配标签内所有内容，非贪婪模式
    root_pattern = '<ul>([\s\S]*?)</ul>'
    name_pattern = '/">([\s\S]*?)</a>'
    link_pattern = 'href="([\s\S]*?)/">'

    # 私有方法
    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        # bytes
        htmls = r.read()
        # 转str再次赋值给htmls，编码utf-8
        htmls = str(htmls, encoding='utf-8')
        return htmls

    # 分析方法
    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        anchors = {}
        links = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)  # list
            link = re.findall(Spider.link_pattern, html)  # list
            # 拼接完整url
            for link_url in link:
                links.append(Spider.url + link_url)
            # 将name和link这两个list组合成一个dict
            anchors = dict(zip(links, name))
        return anchors

    def __show(self, anchors):
        for link in anchors:
            print("标题：{}\n链接：{}".format(anchors[link], link))

    # 入口方法/总控方法
    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        self.__show(anchors)


spider = Spider()
spider.go()
