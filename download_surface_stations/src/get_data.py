import shutil
import pandas as pd
import os
import time
import requests
from bs4 import BeautifulSoup  # 导入 BeautifulSoup 的方法


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
    if not os.path.exists(path):
        # 多层创建目录path
        os.makedirs(path)

def download(area,station,day,hour):
    # 检查目录
    path = './data/' + area + '/' + station + '/' + day[0:4] + '/' + day
    url = 'http://weather.uwyo.edu/cgi-bin/wyowx.fcgi?TYPE=sflist&DATE=' + day + '&HOUR=' + hour + '&UNITS=M&STATION=' + station
    print(url)
    # print(path)
    check_dir(path)

    # 发起请求
    res = requests.get(url)
    # print(res.text)
    html_doc = res.text
    # 可以传入一段字符串，或者传入一个文件句柄。一般都会先用 requests 库获取网页内容，然后使用 soup 解析。
    soup = BeautifulSoup(html_doc,'html.parser')  # 这里一定要指定解析器，可以使用默认的 html，也可以使用 lxml。
    # print(soup.prettify())  # 按照标准的缩进格式输出获取的 soup 内容。
    # print(soup.title.string)
    # print(soup.h3.string)
    # print(soup.h5.string)
    # print(soup.i.string)
    # print(soup.pre.string)  # 获取 title 的内容

    file = path + '/' + station + '_' + day + '_' + hour + '.txt'
    if os.path.exists(file): # 如果数据文件已存在，删除
        os.remove(file)
    # print(file)

    # 储存数据
    with open(file, 'a', encoding='utf-8') as f:
        try:
            f.write(soup.title.string + '\n')
            f.write(soup.h3.string + '\n')
            f.write(soup.h5.string + '\n')
            f.write(soup.i.string + '\n')
            f.write(soup.pre.string)
            f.close()
        except AttributeError:
            try:
                f.close()
                soup.h3.string
                print(station,day,hour,'Sorry, unable to find data file.')
                os.remove(file) # 删除该数据文件
                if not os.listdir(path): # 如果文件夹为空，删除文件夹
                    shutil.rmtree(path, ignore_errors=False, onerror=None)
                errormsg = time.asctime() + " |## " + station + ' ' + day + ' ' + hour + ' ##| Unable to find data file.\n'
                with open('../result/error_list.txt', 'a', encoding='utf-8') as f:
                    f.write(errormsg) # 写入错误日志
                    f.close()
            except AttributeError:
                f.close()
                print(station,'is Unknown station.')
                shutil.rmtree('./data/' + area + '/' + station, ignore_errors = False, onerror = None) # 删除该站点目录
                errormsg =time.asctime() + " |## " + station + ' ' + day + ' ' + hour + ' ##| Unknown station.\n'
                with open('../result/error_list.txt', 'a', encoding='utf-8') as f:
                    f.write(errormsg) # 写入错误日志
                    f.close()
    # time.sleep(0.1)



# download('alaska','PAAQ','20210927','00')


# check_dir('./data/alaska/PAAQ/2000')

if __name__ == "__main__":
    num = 0 # 站点计数器
    daylist,hourlist,stations,areas = init()
    for station in stations:
        area = areas[num]
        for day in daylist:
            for hour in hourlist:
                download(area,station,day,hour) # 下载数据
            print("# ",time.asctime(), station, day, "完成下载")
            logmsg = "# " + time.asctime() + ' ' + ' ' + station + ' ' + day +" 完成下载\n"
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


