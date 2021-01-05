#author:wang fang
#author:wang fang
#迭代器和生成器并行
import time

def consumer(name):
    print("start eat")
    while True:
        baozi=yield
        print('baozi[%s] coming ,[%s]eat'%(baozi,name))


#c=consumer('wangfang')
#c.__next__()
#b='jiucaixian'
#send是传值同时调用yield
#c.send(b)
def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print('start do baozi')
    for i in range(5):
        time.sleep(1)
        print('do  2 baozi')
        c.send(i)
        c2.send(i)

producer("wang")
