#author:wang fang
#当被修饰函数传参数时传参数
import sys,time
def timer(func):
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args, **kwargs)  # test1(x,y)
        end_time = time.time()
        print(end_time - start_time)
    return deco
@timer #test1=timer(test1)
def test1(x,y):
    time.sleep(1)
    print('%s in the test1'%(x+y))
@timer
def test2():
    time.sleep(1)
    print('in the test2')
test1(4,5)
test2()

