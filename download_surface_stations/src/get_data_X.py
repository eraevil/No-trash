import random
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
import get_ip2 # 更新ip

daylist = []
hourlist = []
stations = []
areas = []

def init():
    daylist = DAYlist('2000-01-01', '2020-12-31')
    hourlist = HOURlist()
    with open('../result/station_list.txt', 'r') as f:
        stations = f.readline()
        stations = stations.split(' ')[:-1]
        f.close()
    with open('../result/station_area.txt', 'r') as f:
        areas = f.readline()
        areas = areas.split(' ')[:-1]
        f.close()
    # print(area)
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

# 简单的反爬，设置一个请求头来伪装成浏览器
def request_header():
    headers = {
        # 'User-Agent': UserAgent().random #常见浏览器的请求头伪装（如：火狐,谷歌）
        'User-Agent': UserAgent().Chrome  # 谷歌浏览器
    }
    return headers


# exit()
ip_index = 0
def download(area,station,day,hour,ip_index):

    # 检查目录
    path = './data/' + area + '/' + station + '/' + day[0:4] + '/' + day
    url = 'http://weather.uwyo.edu/cgi-bin/wyowx.fcgi?TYPE=sflist&DATE=' + day + '&HOUR=' + hour + '&UNITS=M&STATION=' + station
    # print(path)

    # 取一个ip
    file = pd.read_csv('verify_ip.csv')
    df = pd.DataFrame(file)
    if ip_index > len(df) - 1:
        ip_index = 0
        return "需要重新获取ip"
    # index = random.randrange(0, len(df))
    # index = 0
    ip_port = str(df["ip"][ip_index]) + ":" + str(df["port"][ip_index])  # 初步处理ip及端口号

    headers = {
        "User-Agent": UserAgent().random
    }
    proxies = {
        'http': 'http://' + ip_port
    }

    print(ip_index, ip_port, '请求', url)

    try:
        res = requests.get(url, headers=headers, proxies=proxies, timeout=5)
        check_dir(path)  # 创建目录
        # print(index, ip_port, "成功！")

        # print(res)

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
                        with open('../result/error_list.txt', 'a', encoding='utf-8') as f:
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
class ThreadPool:
    # 初始化
    def __init__(self, n):
        self.queue = Queue()
        for i in range(n):
            # 创建线程
            Thread(target=self.worker, daemon=True).start()  # daemon是开启守护线程

    # 执行任务
    def worker(self):
        while True:
            func, args, kwargs = self.queue.get()
            func(*args, *kwargs)
            self.queue.task_done()

    # 获取任务，将任务添加到队列中
    def apply_async(self, target, args=(), kwargs={}):
        self.queue.put((target, args, kwargs))

    # 阻塞
    def join(self):
        self.queue.join()

if __name__ == "__main__":
    pass

    # 单点测试
    # download('alaska', 'PABA', '20000101', '00') # 无数据
    # download('alaska', 'PABA', '20021006', '02') # 正常
    # download('alaska', 'ABAB', '20021006', '02')  # 未知站点

    # 开8个线程
    t = ThreadPool(8)
    # 提交10个任务
    # for i in range(10):
    #     t.apply_async(fun, args=(i,))
    # t.join()

    num = 0 # 站点计数器
    daylist,hourlist,stations,areas = init()
    for station in stations:
        area = areas[num]
        for day in daylist:
            for hour in hourlist:
                # try:
                #     t = threading.Thread(
                #         target=download,
                #         args=([area,station,day,hour])
                #     )
                #     t.start() # 多线程下载数据
                #     exit(0)
                # except:
                #     print("线程错误！")
                #     exit(0)

                # t = threading.Thread(
                #     target=download,
                #     args=([area, station, day, hour,0])
                # )
                # t.start()  # 多线程下载数据

                # exit(0)

                t.apply_async(download, args=([area, station, day, hour,0]))

                # download(area,station,day,hour) # 下载数据

            print("# ",time.asctime(), station, day, "完成请求")
            logmsg = "# " + time.asctime() + ' ' + ' ' + station + ' ' + day +" 完成请求\n"
            with open('../result/logs.txt', 'a', encoding='utf-8') as f:
                f.write(logmsg)  # 写入工作日志
                f.close()
        num += 1
        print("### ",time.asctime(),"完成站点",station,"20年全部数据下载")
        print("### 累计完成 ", num, "个站点")
        logmsg1 = "### " + time.asctime() + " 完成站点 " + station + " 20年全部数据下载\n"
        logmsg2 = "### 累计完成 " + str(num) + " 个站点数据下载\n"
        with open('../result/logs.txt', 'a', encoding='utf-8') as f:
            f.write(logmsg1)  # 写入工作日志
            f.write(logmsg2)
            f.close()
        with open('../result/ok_list.txt', 'a', encoding='utf-8') as f:
            f.write(station + " ")  # 写入成功日志
            f.close()
        t.join()


