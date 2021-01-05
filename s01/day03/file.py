#author:wang fang
#打开文件，读取文件内容，修改文件，关闭文件
f=open("day03",'r',encoding='utf-8')
f1=open('day03_bak','w',encoding='utf-8')
#读取文件内容，
#print(f.readline())
#print(f.read())
#修改文件1 replace

update_str=input('please input update str:')
new_str='wanto to update'
for line in f:
    if update_str in line:
        line=line.replace(update_str,new_str)
    f1.write(line)
f1.close()
with(open('day03_bak','r',encoding='utf-8')) as f2:
    print(f2.read())

# 关闭文件
f.close()
