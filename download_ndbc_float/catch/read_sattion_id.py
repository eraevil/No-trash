
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
print('idlist',len(idlist))

idset = set(idlist)
print('idset',len(idset))

