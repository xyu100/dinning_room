import csv
my_openfile = input('请输入需要处理的文件名（.csv)：')
with open(my_openfile,newline='',encoding='utf-8') as f: #打开文件
    my_readers=csv.reader(f)        #将文件写入变量my_readers
    my_oldlists = []            #创建空列表，用于原文件以列表形式呈现
    for my_oldlist in my_readers:   #创建原文件列表
        my_oldlists.append(my_oldlist)

my_newlists = []    #创建空列表
my_newlists = list(map(list, zip(*my_oldlists))) #将原文件列表my_oldlist行列转换成新列表my_newlist

my_count = []  #创建空列表，用于存放统计值
for my_newlist in my_newlists: #对转换后列表逐行统计
    print(my_newlist)
    A = B = C = D = E = Z = 0  #定义变量，并下一行开始时清零
    A = my_newlist.count('A')  #统计A在当前行（列表）的个数
    B = my_newlist.count('B')
    C = my_newlist.count('C')
    D = my_newlist.count('D')
    E = my_newlist.count('E')
    Z = len(my_newlist) -1  #统计当前行（列表）长度
    my_count.append([my_newlist[0],Z,A,B,C,D,E,A/Z,B/Z,C/Z,D/Z,E/Z])  #计算统计值，并赋值结字典my_count

for mycount_value in my_count:    #遍历列表
    print( mycount_value)   #打印统计结果


#统计结果写入文件
my_savefile = input('请输入保存文件名(.csv)：')
with open(my_savefile, 'a', newline='') as csvfile:
    # 调用open()函数打开csv文件，传入参数：文件名“assets.csv”、追加模式“a”、newline=''。
    writer = csv.writer(csvfile, dialect='excel')
    # 用csv.writer()函数创建一个writer对象。
    header = ['题号', '问卷总数', 'A选项小计', 'B选项小计', 'C选项小计', 'D选项小计', 'E选项小计',
              'A占比','B占比','C占比','D占比','E占比']
    writer.writerow(header)
    for my_value in my_count:    #遍历列表
        writer.writerow(my_value)