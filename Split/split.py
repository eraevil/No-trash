#!/usr/bin/python
# @Author: lisheng
# @Time: 20210730
# @Function: 完成txt数据分割，生成excel表
import re
import xlwt

# 打开数据文件
print("正在打开文件。。。")
fo = open("Original_data.txt",'r+') 
def remove(string): # 处理非法字符串函数
    string = string.replace("\n", "");
    string = string.replace("\"", "");
    string = string.replace(" ", "");
    #print(string)
    return string;

# 生成合法数组
text = fo.read()
print("已读取数据！")
# 读入分割的数据长度
length = input("请输入要分割的数据长度：")
print("正在处理。。。")
text = remove(text)
data = re.findall(r'.{' + length + '}', text) 
fo.close() # 关闭文件


# 写入excel
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('My Worksheet') # 创建一个worksheet
print("正在写入Excel文件。。。")
for index, item in enumerate(data):
    worksheet.write(index,0, label = item)# 参数对应 行, 列, 值
    workbook.save('Final_data.xls')# 保存

print("完成写入！")



