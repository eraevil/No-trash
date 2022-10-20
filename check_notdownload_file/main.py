import os
import pandas as pd


# https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/6/MOD021KM/2007/365/MOD021KM.A2007365.2355.006.2014231160035.hdf


if __name__ == "__main__":
    path = r"F:\MOD_02\200801" # 数据所在文件夹
    downlistpath = "F:\MOD_02\\200801\\4204065123-download.txt" # 需要下载的文件列表
    f = os.listdir(path)

    # print(f)

    downloadlist = pd.read_csv(downlistpath,header=None) # 读取需要下载的所有
    print(downloadlist)

    downloadlist['isdownloaded'] = ["yes" if (item[75:] in f) else "no" for item in downloadlist[0]] # 查看是否下载
    index = downloadlist[downloadlist.isdownloaded == "yes"].index.tolist()
    downloadlist = downloadlist.drop(index=index) # 删掉已下载目录
    downloadlist.drop(['isdownloaded'], axis=1, inplace=True)
    # print(index)

    print(downloadlist)
    downloadlist.to_csv(path + '\\buchong.txt', mode='w', index=False,header=None) # 覆盖需要下载的文件列表
    print("已生成所需补充下载的文件列表，请在 " + path + '\\buchong.txt' +" 查看...")