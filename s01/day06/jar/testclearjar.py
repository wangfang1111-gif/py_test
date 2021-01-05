#author:wang fang
import os,sys,re

#删除低版本的jar 1.将jar的文件名读出到文件上 2.比较文件名字，-前面一样，-后面是数字1.几的代表是两个版本的jar 3.低版本删除

# file_path=os.getcwd() #获取当前脚本的路径
# print(file_path)
sys.path.append(os.path.dirname(__file__))
filePath = r'%s' % os.path.dirname(__file__)
print(filePath)
dir=os.listdir(filePath)
print(dir)
#print(dir[1],type(dir[1]))

#列出当前路径jar文件名
jar_list=[]
for i,v in enumerate(dir):
     if re.findall('\.jar$',v):
         jar_list.append(v)
print(jar_list)

# 先把字符串拆成字典，造一个的数组jar_list=[{'unit1': 'ant-launcher', 'number': '1.9.12.jar'}, {'unit1': 'asm', 'number': '5.2.jar'}]
#如果数组i['unit1'] ==j['unit1'], 再组成一个数组

jar_full_list = []
jar_compare_list=[]
res_list=[]
for item in jar_list:
    str_list= item.split('-')
    print(item)
    temp_value = ''
    temp_lsit = {'unitl': None, 'number': None}
    for i, v in enumerate(str_list):
        if not v[0].isdigit():
            temp_value += str_list[i] + '-'
        else:
            temp_lsit['number'] = v

    temp_lsit['unitl']=temp_value
    jar_compare_list.append(temp_value)
    print('temp_lsit is', temp_lsit)
    jar_full_list.append(temp_lsit)
    print('jar_full_list is',jar_full_list)
    print('jar_compare_list is',jar_compare_list)



Repeat_jar=[]

for i in jar_compare_list:
    tag = 0
    test_jar = []
    for j in jar_full_list:
        if j['unitl']==i and (j['number'] is not None):
            l = j['unitl'] + j['number']
            tag = tag + 1
            test_jar.append(l)
            print('test_jar is', test_jar)
    if tag>1:
        Repeat_jar.append(test_jar)
        print('Repeat_jar is',Repeat_jar)
res_list=[]
for item in Repeat_jar:
    if not item in res_list:
        res_list.append(item)
print(res_list)
with open('wf_test.log','w+',encoding='utf-8') as f:
    for item in res_list:
        print('============start=============')
        f.write('============start=============\n')
        item.sort()
        for i in item:
            print(i)
            f.write('%s' % i + '\n')
        print('============end=============\n')
        f.write('============end=============\n\r')























