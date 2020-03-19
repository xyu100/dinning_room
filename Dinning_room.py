'''
基本解决蓉蓉的需求，但有以下问题
1.把结果数据放在源文件里，这样源数据会丢失；
2.首行没有列标签，看起来不直观；
3.首列和末列数据有问题，首列为1 [59，末列为0.06779661016949153, 0.0]
    前后两个列表的中括号影响美观和数据使用
4.首列的题号和统计数（59）没有分列
'''
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
f = open('南一食堂一楼2.csv', 'a')    #打开文件
for my_key,my_value in my_count.items():    #遍历字典
    print(my_key, my_value,file=f)      #逐行写入
f.close()       #关闭文件
