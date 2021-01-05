#author:wang fang
f=open("day03",'r+',encoding='utf-8')
#打印当前位置
print(f.tell())
print(f.readline())
print(f.tell())
#回到某一位置
print(f.seek(10))
print(f.tell())
#flush刷新下，将缓存写入文件
import sys,time

for i in range(10):
    sys.stdout.write('#')
    sys.stdout.flush()
    time.sleep(0.1)

