# 将下载的CALIPSO数据按天分类，存放到相应的文件夹下
# CAL_LID_L2_01kmCLay-Standard-V4-20.2007-12-31T23-51-28ZN.hdf  -->  ./20071231/
# CAL_LID_L2_01kmCLay-Standard-V4-20.2008-01-01T00-37-48ZD.hdf  -->  ./20080101/
# ...
# CAL_LID_L2_01kmCLay-Standard-V4-20.2008-12-31T23-15-13ZD.hdf  -->  ./20081231/

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
        if path[35:45] == word:
            result.append(path)
    return result

# 生成日期列表
def DAYlist(start,end):
    yearmonthday = pd.date_range(start,end,freq="D").strftime("%Y-%m-%d").to_list()
    return yearmonthday



if __name__ == '__main__':
    # print(word_in_files('./','(1)'))
    days = DAYlist('2008-01-01','2008-12-31') # 生成日期列表
    for daynum in days:
        files = word_in_files('F:/CALIPSO/2008', daynum)
        path = 'F:/CALIPSO/2008/' + daynum[0: 4]+daynum[5:7] + daynum[8:10]
        # print(path)
        if not os.path.exists(path): # 创建日期文件夹
            os.mkdir(path)

        for file in files:
            filepath = path + '/' + file # 拼接移动目标路径
            file = 'F:/CALIPSO/2008/' + file
            # print(filepath)
            shutil.move(file,filepath) # 移动源文件到目标文件夹
        # break
    pass