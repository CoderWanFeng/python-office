import requests
import re

#天气爬虫
def weather_spider(url,headers):
    response = requests.get(url,headers)
    content = response.content.decode('utf-8')
    pat_weather = re.compile('<input type="hidden" id="hidden_title" value="(.*?)" />')
    pat_up_time = re.compile('<input type="hidden" id="fc_24h_internal_update_time" value="(.*?)"/>')
    weather = pat_weather.findall(content)
    up_time = pat_up_time.findall(content)
    print(weather[0])
    print('更新时间：',up_time[0])
    ask_ok = input('是否深入查看（Y/N）：')
    if ask_ok == 'Y' or ask_ok == 'y':
        pat_more_weather = re.compile('<li class="li. hot".*?\n<i></i>.<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>.*?\n</li>',re.S)
        more_weather = pat_more_weather.findall(content)
        for item in more_weather:
            if item[1] != '减肥指数':
                print(item[1],':',item[0],',',item[2])
            else:
                print(item[1],':',item[2])


