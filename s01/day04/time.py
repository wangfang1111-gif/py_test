#author:wang fang
#时间戳，格式化字符串，元组类9个元素
import time,datetime

print(time.time())
x=time.localtime()
print(x.tm_year)
print(time.gmtime())
print(time.strftime("%Y-%m-%d %H:%M:%S",x))
print(time.strptime('2020-10-15 22:57:21','%Y-%m-%d %H:%M:%S'))
time.clock()
time.asctime()
time.ctime()
print(datetime.datetime.now())
print(datetime.datetime.now()+datetime.timedelta(3))
