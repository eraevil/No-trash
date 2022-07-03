import re

import requests as rb           # 导入requests库
from bs4 import BeautifulSoup   #   调用beautifulsoup库
# =====================读取需要的站点id==========================
from urllib3 import *
disable_warnings()  # 禁用警告
f = open('../b1.txt', 'r')
urllist = []
while True:
    url = f.readline()
    if url == '':
        break
    urllist.append(url.strip())
f.close()

idlist = []
for i in urllist:
    idlist.append(i[49:55])
# print('idlist',len(idlist))

idset = set(idlist)
# print('idset',len(idset))
# ===============================================================

# url = input("Enter Link:")      # 获取输入
print("读取 https://www.ndbc.noaa.gov/historical_data.shtml#stdmet 包含的链接")
url = 'https://www.ndbc.noaa.gov/historical_data.shtml#stdmet'
if ("https" or "http") in url:
    data = rb.get(url)          #获取HTML网页，对应HTTP的GET
else:
    data = rb.get("https://" + url)         #获取HTML网页，对应HTTP的GET
soup = BeautifulSoup(data.text,"html.parser")       #使用BeautifulSoup解析获取到的数据
links = []          #定义空列表links
for link in soup.find_all("a",string=re.compile('2021')):
    name = link.get("href")[28:45]
    id = name[0:6]
    if id in idset:
        links.append('https://www.ndbc.noaa.gov/data/historical/stdmet/' + name)
for link in soup.find_all("a", string=re.compile('2020')):
    name = link.get("href")[28:45]
    id = name[0:6]
    if id in idset:
        links.append('https://www.ndbc.noaa.gov/data/historical/stdmet/' + name)


# 将输出写入文件（Links.txt）
# 可以将“a”更改为“w”，以便每次都覆盖该文件
# with open("Links.txt",'a') as saved:
#     print(links[:100],file=saved)

with open(r"Links.txt", 'w') as f:
    for i in links:
        f.write(i + '\n')

print("ok!")