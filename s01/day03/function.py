#author:wang fang
#函数定义,有返回值,加return
#过程定义
def test2():
    print('test2--X:')
print(test2())

#return支持返回0，1，元组,list
def test3():
    print('test3--X:')
    return 1
print(test3())
def test4():
    print('test4--X:')
    return (1,'222','www')
print(test4(),type(test4()))

#传参,位置参数，实参

def test1(x,y):
    print('test1--X:',x)
    print('test1--y:',y)
    return 0
test1(y=4,x=5)
test1(7,8)

#传参组
def test7(*args,**kwargs):
    print('test7--X:',args)
    print('test7--Y:',kwargs)
    return 0
test7(1,2,3,4,4,name='wangfang')







