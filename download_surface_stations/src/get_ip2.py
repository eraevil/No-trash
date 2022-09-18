# -*- coding: gbk -*-    # ��ֹ��������ȸ�ʽ����
# ip������վ��http://www.66ip.cn/areaindex_19/1.html

import requests
from fake_useragent import UserAgent
import pandas as pd
from lxml import etree  # xpath


# ---------------��ȡ����վ����ȡͨ��xpath��ȡ��Ҫ��Ϣ----------------
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
    list_ip = html.xpath('//div[@align="center"]/table/tr/td/text()')  # ��ȡhtml����ip��Ϣ����һ������
    return list_ip


# --------------����ȡ��list_ip�ؼ���Ϣ���д��������������----------------
def dispose_list_ip(list_ip):
    num = int((int(len(list_ip)) / 5) - 1)  # 5��һ�У������м��У����е�һ���Ǳ���ֱ��ȥ��
    content_list = []

    for i in range(num):
        a = i * 5
        ip_index = 5 + a  # ʡȥǰ��ı��⣬��5������ip������ÿ��5�������Ӧip
        location_index = 6 + a
        place_index = 7 + a

        items = []
        items.append(list_ip[ip_index])
        items.append(list_ip[location_index])
        items.append((list_ip[place_index]))
        content_list.append(items)
    return content_list


# -----------��������������csv-------------
def save_list_ip(content_list, file_path):
    columns_name = ["ip", "port", "place"]
    test = pd.DataFrame(columns=columns_name, data=content_list)  # ȥ������ֵ��������ظ�
    test.to_csv(file_path, mode='a', encoding='utf-8')
    print("����ɹ�")


# -----------��ȡ��ȡ��ip����֤�Ƿ�ϸ�-----------
def verify_ip(file_path):
    file = pd.read_csv(file_path)
    df = pd.DataFrame(file)
    verify_ip = []

    for i in range(len(df)):
        ip_port = str(df["ip"][i]) + ":" + str(df["port"][i])  # ��������ip���˿ں�
        headers = {
            "User-Agent": UserAgent().random
        }
        proxies = {
            'http': 'http://' + ip_port
            # 'https': 'https://'+ip_port
        }
        '''http://icanhazip.com���ʳɹ��ͻ᷵�ص�ǰ��IP��ַ'''
        try:
            p = requests.get('http://weather.uwyo.edu/', headers=headers, proxies=proxies, timeout=3)
            item = []  # ������ipд��csv�з����ȡ
            item.append(df["ip"][i])
            item.append(df["port"][i])
            item.append(df["place"][i])
            verify_ip.append(item)
            print(ip_port + "�ɹ���")
        except Exception as e:
            print("ʧ��")
    return verify_ip


if __name__ == '__main__':

    # ----------��ȡ�뱣��------------
    save_path = "test.csv"
    city_num = int(input("��Ҫ��ȡ��������ip"))  # 1~34֮�䣬����վֻ��34������ҳ��
    content_list = []
    for i in range(city_num):  # ������ȡlist_ip�ؼ���Ϣ������
        response = get_list_ip(i)
        list = dispose_list_ip(response)
        content_list += list  # ��ÿһҳ��ȡ���б���������

    save_list_ip(content_list, save_path)
    # -----------��֤--------------
    open_path = "test.csv"
    ip = verify_ip(open_path)
    # ---------������֤���-----------
    save_path = "verify_ip.csv"
    save_list_ip(ip, save_path)