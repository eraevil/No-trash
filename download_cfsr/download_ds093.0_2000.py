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

pswd = "Zhaml632903299"

url = 'https://rda.ucar.edu/cgi-bin/login'
values = {'email' : '632903299@qq.com', 'passwd' : pswd, 'action' : 'login'}
# Authenticate
ret = requests.post(url,data=values)
if ret.status_code != 200:
    print('Bad Authentication')
    print(ret.text)
    exit(1)
dspath = 'https://rda.ucar.edu/data/ds093.0/'
filelist = [
'2000/flxf06.gdas.20000101-20000105.tar',
'2000/pgbh06.gdas.20000101-20000105.tar',
# '2000/flxf06.gdas.20000106-20000110.tar',
# '2000/pgbh06.gdas.20000106-20000110.tar',
# '2000/flxf06.gdas.20000111-20000115.tar',
# '2000/pgbh06.gdas.20000111-20000115.tar',
# '2000/flxf06.gdas.20000116-20000120.tar',
# '2000/pgbh06.gdas.20000116-20000120.tar',
# '2000/flxf06.gdas.20000121-20000125.tar',
# '2000/pgbh06.gdas.20000121-20000125.tar',
# '2000/flxf06.gdas.20000126-20000131.tar',
# '2000/pgbh06.gdas.20000126-20000131.tar'
# '2000/flxf06.gdas.20000201-20000205.tar',
# '2000/pgbh06.gdas.20000201-20000205.tar',
# '2000/flxf06.gdas.20000206-20000210.tar',
# '2000/pgbh06.gdas.20000206-20000210.tar',
# '2000/flxf06.gdas.20000211-20000215.tar',
# '2000/pgbh06.gdas.20000211-20000215.tar',
# '2000/flxf06.gdas.20000216-20000220.tar',
# '2000/pgbh06.gdas.20000216-20000220.tar',
# '2000/flxf06.gdas.20000221-20000225.tar',
# '2000/pgbh06.gdas.20000221-20000225.tar',
# '2000/flxf06.gdas.20000226-20000229.tar',
# '2000/pgbh06.gdas.20000226-20000229.tar'
# '2000/flxf06.gdas.20000301-20000305.tar',
# '2000/pgbh06.gdas.20000301-20000305.tar',
# '2000/flxf06.gdas.20000306-20000310.tar',
# '2000/pgbh06.gdas.20000306-20000310.tar',
# '2000/flxf06.gdas.20000311-20000315.tar',
# '2000/pgbh06.gdas.20000311-20000315.tar',
# '2000/flxf06.gdas.20000316-20000320.tar',
# '2000/pgbh06.gdas.20000316-20000320.tar',
# '2000/flxf06.gdas.20000321-20000325.tar',
# '2000/pgbh06.gdas.20000321-20000325.tar',
# '2000/flxf06.gdas.20000326-20000331.tar',
# '2000/pgbh06.gdas.20000326-20000331.tar'
# '2000/flxf06.gdas.20000401-20000405.tar',
# '2000/pgbh06.gdas.20000401-20000405.tar',
# '2000/flxf06.gdas.20000406-20000410.tar',
# '2000/pgbh06.gdas.20000406-20000410.tar',
# '2000/flxf06.gdas.20000411-20000415.tar',
# '2000/pgbh06.gdas.20000411-20000415.tar',
# '2000/flxf06.gdas.20000416-20000420.tar',
# '2000/pgbh06.gdas.20000416-20000420.tar',
# '2000/flxf06.gdas.20000421-20000425.tar',
# '2000/pgbh06.gdas.20000421-20000425.tar',
# '2000/flxf06.gdas.20000426-20000430.tar',
# '2000/pgbh06.gdas.20000426-20000430.tar'
# '2000/flxf06.gdas.20000501-20000505.tar',
# '2000/pgbh06.gdas.20000501-20000505.tar',
# '2000/flxf06.gdas.20000506-20000510.tar',
# '2000/pgbh06.gdas.20000506-20000510.tar',
# '2000/flxf06.gdas.20000511-20000515.tar',
# '2000/pgbh06.gdas.20000511-20000515.tar',
# '2000/flxf06.gdas.20000516-20000520.tar',
# '2000/pgbh06.gdas.20000516-20000520.tar',
# '2000/flxf06.gdas.20000521-20000525.tar',
# '2000/pgbh06.gdas.20000521-20000525.tar',
# '2000/flxf06.gdas.20000526-20000531.tar',
# '2000/pgbh06.gdas.20000526-20000531.tar'
# '2000/flxf06.gdas.20000601-20000605.tar',
# '2000/pgbh06.gdas.20000601-20000605.tar',
# '2000/flxf06.gdas.20000606-20000610.tar',
# '2000/pgbh06.gdas.20000606-20000610.tar',
# '2000/flxf06.gdas.20000611-20000615.tar',
# '2000/pgbh06.gdas.20000611-20000615.tar',
# '2000/flxf06.gdas.20000616-20000620.tar',
# '2000/pgbh06.gdas.20000616-20000620.tar',
# '2000/flxf06.gdas.20000621-20000625.tar',
# '2000/pgbh06.gdas.20000621-20000625.tar',
# '2000/flxf06.gdas.20000626-20000630.tar',
# '2000/pgbh06.gdas.20000626-20000630.tar'
# '2000/flxf06.gdas.20000701-20000705.tar',
# '2000/pgbh06.gdas.20000701-20000705.tar',
# '2000/flxf06.gdas.20000706-20000710.tar',
# '2000/pgbh06.gdas.20000706-20000710.tar',
# '2000/flxf06.gdas.20000711-20000715.tar',
# '2000/pgbh06.gdas.20000711-20000715.tar',
# '2000/flxf06.gdas.20000716-20000720.tar',
# '2000/pgbh06.gdas.20000716-20000720.tar',
# '2000/flxf06.gdas.20000721-20000725.tar',
# '2000/pgbh06.gdas.20000721-20000725.tar',
# '2000/flxf06.gdas.20000726-20000731.tar',
# '2000/pgbh06.gdas.20000726-20000731.tar'
# '2000/flxf06.gdas.20000801-20000805.tar',
# '2000/pgbh06.gdas.20000801-20000805.tar',
# '2000/flxf06.gdas.20000806-20000810.tar',
# '2000/pgbh06.gdas.20000806-20000810.tar',
# '2000/flxf06.gdas.20000811-20000815.tar',
# '2000/pgbh06.gdas.20000811-20000815.tar',
# '2000/flxf06.gdas.20000816-20000820.tar',
# '2000/pgbh06.gdas.20000816-20000820.tar',
# '2000/flxf06.gdas.20000821-20000825.tar',
# '2000/pgbh06.gdas.20000821-20000825.tar',
# '2000/flxf06.gdas.20000826-20000831.tar',
# '2000/pgbh06.gdas.20000826-20000831.tar'
# '2000/flxf06.gdas.20000901-20000905.tar',
# '2000/pgbh06.gdas.20000901-20000905.tar',
# '2000/flxf06.gdas.20000906-20000910.tar',
# '2000/pgbh06.gdas.20000906-20000910.tar',
# '2000/flxf06.gdas.20000911-20000915.tar',
# '2000/pgbh06.gdas.20000911-20000915.tar',
# '2000/flxf06.gdas.20000916-20000920.tar',
# '2000/pgbh06.gdas.20000916-20000920.tar',
# '2000/flxf06.gdas.20000921-20000925.tar',
# '2000/pgbh06.gdas.20000921-20000925.tar',
# '2000/flxf06.gdas.20000926-20000930.tar',
# '2000/pgbh06.gdas.20000926-20000930.tar'
# '2000/flxf06.gdas.20001001-20001005.tar',
# '2000/pgbh06.gdas.20001001-20001005.tar',
# '2000/flxf06.gdas.20001006-20001010.tar',
# '2000/pgbh06.gdas.20001006-20001010.tar',
# '2000/flxf06.gdas.20001011-20001015.tar',
# '2000/pgbh06.gdas.20001011-20001015.tar',
# '2000/flxf06.gdas.20001016-20001020.tar',
# '2000/pgbh06.gdas.20001016-20001020.tar',
# '2000/flxf06.gdas.20001021-20001025.tar',
# '2000/pgbh06.gdas.20001021-20001025.tar',
# '2000/flxf06.gdas.20001026-20001031.tar',
# '2000/pgbh06.gdas.20001026-20001031.tar'
# '2000/flxf06.gdas.20001101-20001105.tar',
# '2000/pgbh06.gdas.20001101-20001105.tar',
# '2000/flxf06.gdas.20001106-20001110.tar',
# '2000/pgbh06.gdas.20001106-20001110.tar',
# '2000/flxf06.gdas.20001111-20001115.tar',
# '2000/pgbh06.gdas.20001111-20001115.tar',
# '2000/flxf06.gdas.20001116-20001120.tar',
# '2000/pgbh06.gdas.20001116-20001120.tar',
# '2000/flxf06.gdas.20001121-20001125.tar',
# '2000/pgbh06.gdas.20001121-20001125.tar',
# '2000/flxf06.gdas.20001126-20001130.tar',
# '2000/pgbh06.gdas.20001126-20001130.tar'
# '2000/flxf06.gdas.20001201-20001205.tar',
# '2000/pgbh06.gdas.20001201-20001205.tar',
# '2000/flxf06.gdas.20001206-20001210.tar',
# '2000/pgbh06.gdas.20001206-20001210.tar',
# '2000/flxf06.gdas.20001211-20001215.tar',
# '2000/pgbh06.gdas.20001211-20001215.tar',
# '2000/flxf06.gdas.20001216-20001220.tar',
# '2000/pgbh06.gdas.20001216-20001220.tar',
# '2000/flxf06.gdas.20001221-20001225.tar',
# '2000/pgbh06.gdas.20001221-20001225.tar',
# '2000/flxf06.gdas.20001226-20001231.tar',
# '2000/pgbh06.gdas.20001226-20001231.tar'
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
