# -*- coding: gbk -*-    # 防止出现乱码等格式错误
# ip代理网站：http://www.66ip.cn/areaindex_19/1.html

import requests
from fake_useragent import UserAgent
import pandas as pd
from lxml import etree  # xpath


# ---------------爬取该网站并获取通过xpath获取主要信息----------------
def get_list_ip(city_id):
    url = 'http://www.66ip.cn/areaindex_{}/1.html'.format(city_id)
    headers = {
        'User-Agent': UserAgent().random,
    }
    data_html = requests.get(url=url, headers=headers)
    data_html.encoding = 'gbk'
    data_html = data_html.text

    html = etree.HTML(data_html)
    etree.tostring(html)
    list_ip = html.xpath('//div[@align="center"]/table/tr/td/text()')  # 获取html含有ip信息的那一行数据
    return list_ip


# --------------将爬取的list_ip关键信息进行处理、方便后续保存----------------
def dispose_list_ip(list_ip):
    num = int((int(len(list_ip)) / 5) - 1)  # 5个一行，计算有几行，其中第一行是标题直接去掉
    content_list = []

    for i in range(num):
        a = i * 5
        ip_index = 5 + a  # 省去前面的标题，第5个就是ip，往后每加5就是相对应ip
        location_index = 6 + a
        place_index = 7 + a

        items = []
        items.append(list_ip[ip_index])
        items.append(list_ip[location_index])
        items.append((list_ip[place_index]))
        content_list.append(items)
    return content_list


# -----------将处理结果保存在csv-------------
def save_list_ip(content_list, file_path):
    columns_name = ["ip", "port", "place"]
    test = pd.DataFrame(columns=columns_name, data=content_list)  # 去掉索引值，否则会重复
    test.to_csv(file_path, mode='a', encoding='utf-8')
    print("保存成功")


# -----------读取爬取的ip并验证是否合格-----------
def verify_ip(file_path):
    file = pd.read_csv(file_path)
    df = pd.DataFrame(file)
    verify_ip = []

    for i in range(len(df)):
        ip_port = str(df["ip"][i]) + ":" + str(df["port"][i])  # 初步处理ip及端口号
        headers = {
            "User-Agent": UserAgent().random
        }
        proxies = {
            'http': 'http://' + ip_port
            # 'https': 'https://'+ip_port
        }
        '''http://icanhazip.com访问成功就会返回当前的IP地址'''
        try:
            p = requests.get('http://weather.uwyo.edu/', headers=headers, proxies=proxies, timeout=3)
            item = []  # 将可用ip写入csv中方便读取
            item.append(df["ip"][i])
            item.append(df["port"][i])
            item.append(df["place"][i])
            verify_ip.append(item)
            print(ip_port + "成功！")
        except Exception as e:
            print("失败")
    return verify_ip


if __name__ == '__main__':

    # ----------爬取与保存------------
    save_path = "test.csv"
    city_num = int(input("需要爬取几个城市ip"))  # 1~34之间，该网站只有34个城市页面
    content_list = []
    for i in range(city_num):  # 批量爬取list_ip关键信息并保存
        response = get_list_ip(i)
        list = dispose_list_ip(response)
        content_list += list  # 将每一页获取的列表连接起来

    save_list_ip(content_list, save_path)
    # -----------验证--------------
    open_path = "test.csv"
    ip = verify_ip(open_path)
    # ---------保存验证结果-----------
    save_path = "verify_ip.csv"
    save_list_ip(ip, save_path)