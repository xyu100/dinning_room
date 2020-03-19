import csv
from collections import Counter
import numpy as np
tiztong={}
list1=[]
with open('南一食堂一楼变.csv','r',newline='') as cun:
    data=csv.reader(cun) #把csv里的文件内容读出来
    content=list(data)  #把读出的内容转成一个大的列表
    b=(content[1:])   #定义一个不含标题的新的大列表
    for i in b:
        list1.append(i[0])  #把标题即题号放进list1里
        del i[0]   #再删除b里每个列表里的题号
        def all_np(arr):
            arr = np.array(arr)
            key = np.unique(arr)
            result = {}
            for k in key:
                mask = (arr == k)
                arr_new = arr[mask]
                v = arr_new.size
                result[k] = v
            return result
        a = all_np(i[:])
        print(a)
print(all_np(b))







