# 将下载的MAC数据按天分类，存放到相应的文件夹下
# MAC06S0.A2008001.0000.002.2017074151447.hdf  -->  ./20080101/
# MAC06S0.A2008001.0005.002.2017074151457.hdf  -->  ./20080101/
# ...
# MAC06S0.A2008366.0000.002.2017122183611.hdf  -->  ./20081231/

import os
import shutil
import pandas as pd

# 获取文件下所有文件名
def get_files(root_path):  # 注意root_path前加上r
    '''
    获得目录root_path下（包括各级子目录）所有文件的路径
    '''
    file_list = os.listdir(root_path)
    return file_list

# 按天查找文件名
def word_in_files(root_path, word):
    '''
    获得目录root_path下（包括各级子目录）所有包含字符串word的文件的路径
    '''
    file_list = get_files(root_path)
    result = []
    for path in file_list:
        if path[13:16] == word:
            result.append(path)
    return result

# 生成日期列表
def DAYlist(start,end):
    yearmonthday = pd.date_range(start,end,freq="D").strftime("%Y%m%d").to_list()
    return yearmonthday



if __name__ == '__main__':
    # print(word_in_files('./','(1)'))
    days = DAYlist('2008-01-01','2008-12-31') # 生成日期列表
    daynums = [] # 日期儒略日
    for i in range(1,367):
        daynums.append(str(i).zfill(3))

    for daynum in daynums:
        print(daynum)
        files = word_in_files('./', daynum)
        path = days[int(daynum)-1]
        if not os.path.exists(path): # 创建日期文件夹
            os.mkdir(path)

        for file in files:
            filepath = path + '/' + file # 拼接移动目标路径
            # print(filepath)
            shutil.move(file,filepath) # 移动源文件到目标文件夹
        # break
    pass