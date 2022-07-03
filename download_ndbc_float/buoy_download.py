
from urllib3 import *
import threading

http = PoolManager()
disable_warnings()  # 禁用警告
#print(1)
f = open('b.txt', 'r')

urllist = []
while True:
    url = f.readline()

    #print(url)
    if url == '':
        break
    urllist.append(url.strip())
f.close()

#多线程类
class DownloadThread(threading.Thread):
    def __init__(self, func, args):
        super().__init__(target=func, args=args)

def download(filename, url):
    response = http.request('GET', url)
    f = open(filename,'wb')  # wb的b表示我们要写的文件是一个二进制的文件
    f.write(response.data)
    f.close()
    print('<',url,'>','下载完成。')

for i in range(len(urllist)):
    # print(i)
    name0=''.join(urllist[i])
    name1=name0[-17:]
    #print(type(name1))
    #print(name1)
    #print(3)
    thread = DownloadThread(download, (name1, urllist[i]))
    thread.start()
