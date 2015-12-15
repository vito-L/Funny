# /usr/bin/env python
#coding:utf-8

import urllib2,json

city = raw_input("Input City:")
url = "https://api.heweather.com/x3/weather?city="+city+"&key=XXXXXXXXXX"

Html_url = urllib2.urlopen(url).read()
Json_url = json.JSONDecoder().decode(Html_url)


def Sevenday():
    print "##### 未来七天天气预报 #####"
    for weather in Json_url["HeWeather data service 3.0"][0]["daily_forecast"]:
        print u'日期：'+weather['date']
        print u'温度：'+weather['tmp']['max']+"~"+weather['tmp']['min']+u'度'
        print u'风力等级：'+weather['wind']['sc']
        print u'风向：'+weather['wind']['dir']
        print u'白天：'+weather['cond']['txt_d']+" "+u'夜间：'+weather['cond']['txt_n']
        print u'降雨量(mm)：'+weather['pcpn']
        print u'能见度(km)：'+weather['vis']
        print "~~~~~~~~~~~~~~^_^~~~~~~~~~~~~~~"
    print "#####    END    #####"

# try:
#     Sevenday()
# except KeyError:
#     print "找不到您输入的城市的天气预报！"

def Aqi():
    pm25 = Json_url['HeWeather data service 3.0'][0]['aqi']['city']['pm25']
    aqi = Json_url['HeWeather data service 3.0'][0]['aqi']['city']['aqi']
    info = Json_url['HeWeather data service 3.0'][0]['aqi']['city']['qlty']
    print "##### 空气质量指数 #####"
    print "PM 2.5:"+pm25+u' ug/m³'
    print "AQI:"+aqi
    print u'空气质量类别:'+info
# try:
#     Aqi()
# except KeyError:
#     print "只支持部分城市"

def Nowtmp():
    tmp = Json_url['HeWeather data service 3.0'][0]['now']['tmp']
    fl = Json_url['HeWeather data service 3.0'][0]['now']['fl']
    spd = Json_url['HeWeather data service 3.0'][0]['now']['wind']['spd']
    txt = Json_url['HeWeather data service 3.0'][0]['now']['cond']['txt']
    pcpn = Json_url['HeWeather data service 3.0'][0]['now']['pcpn']
    vis = Json_url['HeWeather data service 3.0'][0]['now']['vis']
    print "##### 实时温度 #####"
    print u'实时温度：'+tmp+u'度'
    print u'体感：'+fl+u'度'
    print u'风速：'+spd+" Kmph"
    print u'天气状况：'+txt
    print u'降雨量：'+pcpn+" mm"
    print u'能见度：'+vis+" Km"
try:
    Nowtmp()
except:
    print "IINPUT Error"
