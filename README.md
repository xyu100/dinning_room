## Dinning_room项目说明

| 群友的一个实际工作中的统计项目                               |
| ------------------------------------------------------------ |
| 她平时每月需要处理像“南一食堂一楼.csv”这样的文件数十份，每一份都是问卷调查的结果，每个问卷20道题，需要把每道题里的ABCDE各项的百分比算出来，还要把每一个sheet里的各个百分比都算出来，传统的工作模式是用excle里的counif函数完成，即使作了宏，也很耗费时间，毕竟有数十份文件要处理，她的诉求是想作个python的程序完成这项工作。 |

**好吧，说的有点啰嗦，直接上图：**

![](https://github.com/xyu100/dinning_room/blob/master/csv.png)

根据小伙伴的要求，我作了一段代码如下：（文件是another_dinning.py）

```python
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
```

能勉强统计出sheet里的数据情况，但是结果距离小伙伴的要求差的好远，汗。

群友 `活在当下`也作了一段代码如下：（文件名dinning_room.py）

```py
import csv
with open('南一食堂一楼1.csv',newline='',encoding='utf-8') as f: #打开文件
    my_readers=csv.reader(f)        #将文件写入变量my_readers
    my_oldlists = []            #创建空列表，用于原文件以列表形式呈现
    for my_oldlist in my_readers:   #创建原文件列表
        my_oldlists.append(my_oldlist)

my_newlists = []    #创建空列表
my_newlists = list(map(list, zip(*my_oldlists))) #将原文件列表my_oldlist行列转换成新列表my_newlist

my_count = dict()  #创建空字典，用于存放统计值
for my_newlist in my_newlists: #对转换后列表逐行统计
    A = B = C = D = E = Z = 0  #定义变量，并下一行开始时清零
    A = my_newlist.count('A')  #统计A在当前行（列表）的个数
    B = my_newlist.count('B')
    C = my_newlist.count('C')
    D = my_newlist.count('D')
    E = my_newlist.count('E')
    Z = len(my_newlist)   #统计当前行（列表）长度
    my_count[my_newlist[0]]=[Z,A,B,C,D,E,A/Z,B/Z,C/Z,D/Z,E/Z]   #计算统计值，并赋值结字典my_count

for mycount_key,mycount_value in my_count.items():    #遍历字典
    print(mycount_key, mycount_value)   #打印统计结果
    print(my_count)

#统计结果写入文件
f = open('南一食堂一楼1.csv', 'a')    #打开文件
for my_key,my_value in my_count.items():    #遍历字典
    print(my_key, my_value,file=f)      #逐行写入
f.close()       #关闭文件
```

比较完美的解决了小伙伴的问题，但是有些瑕疵，我给提了点建议如下：

```py
'''
基本解决蓉蓉的需求，但有以下问题
1.把结果数据放在源文件里，这样源数据会丢失；
2.首行没有列标签，看起来不直观；
3.首列和末列数据有问题，首列为1 [59，末列为0.06779661016949153, 0.0]
    前后两个列表的中括号影响美观和数据使用
4.首列的题号和统计数（59）没有分列
'''
```

邀请大家一起动脑研究，争取作出完美的项目。

帮助伙伴，提升自己。

