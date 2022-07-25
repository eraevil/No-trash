import requests
from bs4 import BeautifulSoup  # 导入 BeautifulSoup 的方法
import pprint
import re
import numpy as np

# res = requests.get('http://weather.uwyo.edu/cgi-bin/wyowx.fcgi?TYPE=sflist&DATE=current&HOUR=current&UNITS=A&STATION=W63')
# # print(res.text)
# html_doc = res.text
# # 可以传入一段字符串，或者传入一个文件句柄。一般都会先用 requests 库获取网页内容，然后使用 soup 解析。
# soup = BeautifulSoup(html_doc,'html.parser')  # 这里一定要指定解析器，可以使用默认的 html，也可以使用 lxml。
# print(soup.prettify())  # 按照标准的缩进格式输出获取的 soup 内容。
# print(soup.pre.string)  # 获取 title 的内容


# exit()
# 获取站点列表
url = 'http://weather.uwyo.edu/surface/meteorogram/index.shtml'
res = requests.get(url).text
content = BeautifulSoup(res, "html.parser")
links = content.find_all('ul')[1].findAll('a')


def area_link(url):
    stations = []
    # url = 'http://weather.uwyo.edu/surface/meteorogram/alaska.shtml'
    res = requests.get(url).text
    content = BeautifulSoup(res, "html.parser")
    data = content.find_all('area', attrs={'shape': 'circle'})

    for item in data:
        # pprint.pprint(item)
        text1 = str(re.findall('(?<=title=").*$', str(item))[0])[0:4].strip() # 获取站点名
        stations.append(text1)
    print(stations)
    return stations

station_list = []
for link in links:
    print(link['href'])
    aurl = 'http://weather.uwyo.edu/surface/meteorogram/' + link['href']
    # print(aurl)
    result = area_link(aurl)
    station_list = np.concatenate((station_list, result), axis=0)

print(len(station_list))

# exit(0)


# /html/body/map

# area_link('http://weather.uwyo.edu/surface/meteorogram/alaska.shtml')