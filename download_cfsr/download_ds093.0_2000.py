#!/usr/bin/env python
#################################################################
# Python Script to retrieve 16 online Data files of 'ds093.0',
# total 49.33G. This script uses 'requests' to download data.
#
# Highlight this script by Select All, Copy and Paste it into a file;
# make the file executable and run it on command line.
#
# You need pass in your password as a parameter to execute
# this script; or you can set an environment variable RDAPSWD
# if your Operating System supports it.
#
# Contact dattore@ucar.edu (Bob Dattore) for further assistance.
#################################################################


import sys, os
import requests

def check_file_status(filepath, filesize):
    sys.stdout.write('\r')
    sys.stdout.flush()
    size = int(os.stat(filepath).st_size)
    percent_complete = (size/filesize)*100
    sys.stdout.write('%.3f %s' % (percent_complete, '% Completed'))
    sys.stdout.flush()

# Try to get password

pswd = "lisheng123"

url = 'https://rda.ucar.edu/cgi-bin/login'
values = {'email' : 'lisheng_rc@163.com', 'passwd' : pswd, 'action' : 'login'}
# Authenticate
ret = requests.post(url,data=values)
if ret.status_code != 200:
    print('Bad Authentication')
    print(ret.text)
    exit(1)
dspath = 'https://rda.ucar.edu/data/ds093.0/'
filelist = [
'2007/flxf06.gdas.20070101-20070105.tar',
'2007/pgbh06.gdas.20070101-20070105.tar',
'2007/flxf06.gdas.20070106-20070110.tar',
'2007/pgbh06.gdas.20070106-20070110.tar',
'2007/flxf06.gdas.20070111-20070115.tar',
'2007/pgbh06.gdas.20070111-20070115.tar',
'2007/flxf06.gdas.20070116-20070120.tar',
'2007/pgbh06.gdas.20070116-20070120.tar',
'2007/flxf06.gdas.20070121-20070125.tar',
'2007/pgbh06.gdas.20070121-20070125.tar',
'2007/flxf06.gdas.20070126-20070131.tar',
'2007/pgbh06.gdas.20070126-20070131.tar',
'2007/flxf06.gdas.20070201-20070205.tar',
'2007/pgbh06.gdas.20070201-20070205.tar',
'2007/flxf06.gdas.20070206-20070210.tar',
'2007/pgbh06.gdas.20070206-20070210.tar',
'2007/flxf06.gdas.20070211-20070215.tar',
'2007/pgbh06.gdas.20070211-20070215.tar',
'2007/flxf06.gdas.20070216-20070220.tar',
'2007/pgbh06.gdas.20070216-20070220.tar',
'2007/flxf06.gdas.20070221-20070225.tar',
'2007/pgbh06.gdas.20070221-20070225.tar',
'2007/flxf06.gdas.20070226-20070229.tar',
'2007/pgbh06.gdas.20070226-20070229.tar',
'2007/flxf06.gdas.20070301-20070305.tar',
'2007/pgbh06.gdas.20070301-20070305.tar',
'2007/flxf06.gdas.20070306-20070310.tar',
'2007/pgbh06.gdas.20070306-20070310.tar',
'2007/flxf06.gdas.20070311-20070315.tar',
'2007/pgbh06.gdas.20070311-20070315.tar',
'2007/flxf06.gdas.20070316-20070320.tar',
'2007/pgbh06.gdas.20070316-20070320.tar',
'2007/flxf06.gdas.20070321-20070325.tar',
'2007/pgbh06.gdas.20070321-20070325.tar',
'2007/flxf06.gdas.20070326-20070331.tar',
'2007/pgbh06.gdas.20070326-20070331.tar',
'2007/flxf06.gdas.20070401-20070405.tar',
'2007/pgbh06.gdas.20070401-20070405.tar',
'2007/flxf06.gdas.20070406-20070410.tar',
'2007/pgbh06.gdas.20070406-20070410.tar',
'2007/flxf06.gdas.20070411-20070415.tar',
'2007/pgbh06.gdas.20070411-20070415.tar',
'2007/flxf06.gdas.20070416-20070420.tar',
'2007/pgbh06.gdas.20070416-20070420.tar',
'2007/flxf06.gdas.20070421-20070425.tar',
'2007/pgbh06.gdas.20070421-20070425.tar',
'2007/flxf06.gdas.20070426-20070430.tar',
'2007/pgbh06.gdas.20070426-20070430.tar',
'2007/flxf06.gdas.20070501-20070505.tar',
'2007/pgbh06.gdas.20070501-20070505.tar',
'2007/flxf06.gdas.20070506-20070510.tar',
'2007/pgbh06.gdas.20070506-20070510.tar',
'2007/flxf06.gdas.20070511-20070515.tar',
'2007/pgbh06.gdas.20070511-20070515.tar',
'2007/flxf06.gdas.20070516-20070520.tar',
'2007/pgbh06.gdas.20070516-20070520.tar',
'2007/flxf06.gdas.20070521-20070525.tar',
'2007/pgbh06.gdas.20070521-20070525.tar',
'2007/flxf06.gdas.20070526-20070531.tar',
'2007/pgbh06.gdas.20070526-20070531.tar',
'2007/flxf06.gdas.20070601-20070605.tar',
'2007/pgbh06.gdas.20070601-20070605.tar',
'2007/flxf06.gdas.20070606-20070610.tar',
'2007/pgbh06.gdas.20070606-20070610.tar',
'2007/flxf06.gdas.20070611-20070615.tar',
'2007/pgbh06.gdas.20070611-20070615.tar',
'2007/flxf06.gdas.20070616-20070620.tar',
'2007/pgbh06.gdas.20070616-20070620.tar',
'2007/flxf06.gdas.20070621-20070625.tar',
'2007/pgbh06.gdas.20070621-20070625.tar',
'2007/flxf06.gdas.20070626-20070630.tar',
'2007/pgbh06.gdas.20070626-20070630.tar',
'2007/flxf06.gdas.20070701-20070705.tar',
'2007/pgbh06.gdas.20070701-20070705.tar',
'2007/flxf06.gdas.20070706-20070710.tar',
'2007/pgbh06.gdas.20070706-20070710.tar',
'2007/flxf06.gdas.20070711-20070715.tar',
'2007/pgbh06.gdas.20070711-20070715.tar',
'2007/flxf06.gdas.20070716-20070720.tar',
'2007/pgbh06.gdas.20070716-20070720.tar',
'2007/flxf06.gdas.20070721-20070725.tar',
'2007/pgbh06.gdas.20070721-20070725.tar',
'2007/flxf06.gdas.20070726-20070731.tar',
'2007/pgbh06.gdas.20070726-20070731.tar',
'2007/flxf06.gdas.20070801-20070805.tar',
'2007/pgbh06.gdas.20070801-20070805.tar',
'2007/flxf06.gdas.20070806-20070810.tar',
'2007/pgbh06.gdas.20070806-20070810.tar',
'2007/flxf06.gdas.20070811-20070815.tar',
'2007/pgbh06.gdas.20070811-20070815.tar',
'2007/flxf06.gdas.20070816-20070820.tar',
'2007/pgbh06.gdas.20070816-20070820.tar',
'2007/flxf06.gdas.20070821-20070825.tar',
'2007/pgbh06.gdas.20070821-20070825.tar',
'2007/flxf06.gdas.20070826-20070831.tar',
'2007/pgbh06.gdas.20070826-20070831.tar',
'2007/flxf06.gdas.20070901-20070905.tar',
'2007/pgbh06.gdas.20070901-20070905.tar',
'2007/flxf06.gdas.20070906-20070910.tar',
'2007/pgbh06.gdas.20070906-20070910.tar',
'2007/flxf06.gdas.20070911-20070915.tar',
'2007/pgbh06.gdas.20070911-20070915.tar',
'2007/flxf06.gdas.20070916-20070920.tar',
'2007/pgbh06.gdas.20070916-20070920.tar',
'2007/flxf06.gdas.20070921-20070925.tar',
'2007/pgbh06.gdas.20070921-20070925.tar',
'2007/flxf06.gdas.20070926-20070930.tar',
'2007/pgbh06.gdas.20070926-20070930.tar',
'2007/flxf06.gdas.20071001-20071005.tar',
'2007/pgbh06.gdas.20071001-20071005.tar',
'2007/flxf06.gdas.20071006-20071010.tar',
'2007/pgbh06.gdas.20071006-20071010.tar',
'2007/flxf06.gdas.20071011-20071015.tar',
'2007/pgbh06.gdas.20071011-20071015.tar',
'2007/flxf06.gdas.20071016-20071020.tar',
'2007/pgbh06.gdas.20071016-20071020.tar',
'2007/flxf06.gdas.20071021-20071025.tar',
'2007/pgbh06.gdas.20071021-20071025.tar',
'2007/flxf06.gdas.20071026-20071031.tar',
'2007/pgbh06.gdas.20071026-20071031.tar',
'2007/flxf06.gdas.20071101-20071105.tar',
'2007/pgbh06.gdas.20071101-20071105.tar',
'2007/flxf06.gdas.20071106-20071110.tar',
'2007/pgbh06.gdas.20071106-20071110.tar',
'2007/flxf06.gdas.20071111-20071115.tar',
'2007/pgbh06.gdas.20071111-20071115.tar',
'2007/flxf06.gdas.20071116-20071120.tar',
'2007/pgbh06.gdas.20071116-20071120.tar',
'2007/flxf06.gdas.20071121-20071125.tar',
'2007/pgbh06.gdas.20071121-20071125.tar',
'2007/flxf06.gdas.20071126-20071130.tar',
'2007/pgbh06.gdas.20071126-20071130.tar',
'2007/flxf06.gdas.20071201-20071205.tar',
'2007/pgbh06.gdas.20071201-20071205.tar',
'2007/flxf06.gdas.20071206-20071210.tar',
'2007/pgbh06.gdas.20071206-20071210.tar',
'2007/flxf06.gdas.20071211-20071215.tar',
'2007/pgbh06.gdas.20071211-20071215.tar',
'2007/flxf06.gdas.20071216-20071220.tar',
'2007/pgbh06.gdas.20071216-20071220.tar',
'2007/flxf06.gdas.20071221-20071225.tar',
'2007/pgbh06.gdas.20071221-20071225.tar',
'2007/flxf06.gdas.20071226-20071231.tar',
'2007/pgbh06.gdas.20071226-20071231.tar',
]
for file in filelist:
    filename=dspath+file
    file_base = os.path.basename(file)
    print('Downloading',file_base)
    req = requests.get(filename, cookies = ret.cookies, allow_redirects=True, stream=True)
    filesize = int(req.headers['content-length'])
    with open(file_base, 'wb') as outfile:
        chunk_size=1048576
        for chunk in req.iter_content(chunk_size=chunk_size):
            outfile.write(chunk)
            if chunk_size < filesize:
                check_file_status(file_base, filesize)
    check_file_status(file_base, filesize)
    print()
