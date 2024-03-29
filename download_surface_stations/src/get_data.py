﻿import random
import shutil
import threading

import pandas as pd
import os
import time
import requests
from bs4 import BeautifulSoup  # 导入 BeautifulSoup 的方法
import requests  # 导入模块
from lxml import etree
from fake_useragent import UserAgent
import multiprocessing

daylist = []
hourlist = []

# 初始化
def init():
    daylist = DAYlist('2000-01-01', '2020-12-31')
    hourlist = HOURlist()

    # TODO LIST
    areas = ['usne','usne','usne','usne','usne']
    stations = ['ACK','FOK','WWD','WAL','HUL']
    return daylist,hourlist,stations,areas

# 生成时间列表
def DAYlist(start,end):
    yearmonthday = pd.date_range(start,end,freq="D").strftime("%Y%m%d").to_list()
    return yearmonthday
def HOURlist():
    for i in range(0, 24):
        hourlist.append("{:02d}".format(i))
    return hourlist

# 创建目录
def check_dir(path):
    try:
        if not os.path.exists(path):
            os.makedirs(path)
    except:
        pass

ip_index = 0
def download(area,station,day,hour,ip_index):
    # 检查目录
    path = './data/' + area + '/' + station + '/' + day[0:4] + '/' + day
    url = 'http://weather.uwyo.edu/cgi-bin/wyowx.fcgi?TYPE=sflist&DATE=' + day + '&HOUR=' + hour + '&UNITS=M&STATION=' + station
    # print(path)
    print('请求', url)

    try:
        # res = requests.get(url, headers=headers, proxies=proxies, timeout=5)
        res = requests.get(url, timeout=5)
        check_dir(path)  # 创建目录
        # print(index, ip_port, "成功！")、
        if res.status_code == 200:
            html_doc = res.text
            soup = BeautifulSoup(html_doc, 'html.parser')  # 这里一定要指定解析器，可以使用默认的 html，也可以使用 lxml。
            file = path + '/' + station + '_' + day + '_' + hour + '.txt' # 数据文件名
            if os.path.exists(file):  # 如果数据文件已存在，删除
                os.remove(file)

            # 储存数据
            with open(file, 'a', encoding='utf-8') as f:
                try:
                    soup.pre.string
                    f.write(soup.title.string + '\n')
                    f.write(soup.h3.string + '\n')
                    f.write(soup.h5.string + '\n')
                    f.write(soup.i.string + '\n')
                    f.write(soup.pre.string)
                    f.close()
                    print("获取到数据")
                except Exception as nodataErr:
                    # print(soup.prettify())
                    print("未获取到数据")
                    try:
                        f.write(soup.title.string + '\n')
                        f.write(soup.h3.string + '\n')
                        f.write(soup.h5.string + '\n')
                        f.write('Sorry, unable to get data' + '\n')
                        f.close()
                        errormsg = time.asctime() + " |## " + station + ' ' + day + ' ' + hour + ' ##| Unable to find data file.\n'
                        with open('../logs/error_list.txt', 'a', encoding='utf-8') as f:
                            f.write(errormsg)  # 写入错误日志
                            f.close()
                    except Exception as xErr:
                        pass
                        # print(xErr)

                        if soup.title.string == 'Welcome To Zscaler Directory Authentication':
                            print("请求失败，重新获取")
                            ip_index += 1
                            # resxx = get_res(url)
                            download(area, station, day, hour, ip_index)
                            return
                        else:
                            print("未知站点")
                            f.write('Unknown station.' + '\n')
                            f.close()
                        # shutil.rmtree('./data/' + area + '/' + station, ignore_errors=False, onerror=None)  # 删除该站点目录
                    return
        else:
            with open(file, 'a', encoding='utf-8') as f:
                f.write(res.status_code)
                f.close()
    except Exception as requestErr:
        ip_index += 1
        print("请求失败，重新请求")
        # resxx = get_res(url)
        download(area, station, day, hour, ip_index)
        return


# 多线程
from threading import Thread
from queue import Queue
import time

if __name__ == "__main__":
    print("##########")

    # 单点测试
    # download('alaska', 'PABA', '20000101', '00') # 无数据
    # download('alaska', 'PABA', '20021006', '02') # 正常
    # download('alaska', 'ABAB', '20021006', '02')  # 未知站点

    # 开8个线程
    # t = ThreadPool(5000)
    # 提交10个任务
    # for i in range(10):
    #     t.apply_async(fun, args=(i,))
    # t.join()

    num = 0 # 站点计数器
    daylist,hourlist,stations,areas = init()
    
    

    print(stations)
    for station in stations:
        pool = multiprocessing.Pool(processes=16)  # 创建进程池
        area = areas[num]
        for day in daylist:
            for hour in hourlist:
                #(area,station,day,hour,0) # 下载数据
                pool.apply_async(download, args=([area, station, day, hour, 0])) # 多线程下载

            print("# ",time.asctime(), station, day, "完成请求")
            logmsg = "# " + time.asctime() + ' ' + ' ' + station + ' ' + day +" 完成请求\n"
            with open('../logs/logs.txt', 'a', encoding='utf-8') as f:
                f.write(logmsg)  # 写入工作日志
                f.close()
        num += 1
        print("### ",time.asctime(),"完成站点",station,"20年全部数据下载")
        print("### 累计完成 ", num, "个站点")
        logmsg1 = "### " + time.asctime() + " 完成站点 " + station + " 20年全部数据下载\n"
        logmsg2 = "### 累计完成 " + str(num) + " 个站点数据下载\n"
        with open('../logs/logs.txt', 'a', encoding='utf-8') as f:
            f.write(logmsg1)  # 写入工作日志
            f.write(logmsg2)
            f.close()

        with open('../logs/ok_list.txt', 'a', encoding='utf-8') as f:
            f.write(station + " ")  # 写入成功日志
            f.close()
        pool.close()
        pool.join()


