#author:wang fang
#局部和全局变量
#局部变量只能在定义的相关函数应用
x=1
def test1():
    print('test1--X:',x)
    y=1
    print('test1--Y:',y)
    def test2():
        y = 2
        print('test1--Y:', y)
    test2()
    return 0
test1()
#递归函数:直接或间接调用函数本身，则该函数称为递归函数.自己调用自己
#优点是逻辑简单清晰, 缺点是过深的调用会导致栈溢出(即比较占用内存空间).用递归函数来实现对树形结构的遍历是一种很好的方法
def func(n):
    if n==1:
        return 1
    return n*func(n-1)
print(func(5))

#高阶函数：一个函数可以作为参数传给另外一个函数，或者一个函数的返回值为另外一个函数（若返回值为该函数本身，则为递归），满足其一则为高阶函数。
#参数为函数
def fll():
    print('in the fll')
    foo()
def foo():
    print('in the foo')

fll()

#返回值为函数
def foo1():
    print('in the foo1')
def fll1(func):
    print('in the fll1')
    return foo1


fll1=fll1(foo1)
fll1()

