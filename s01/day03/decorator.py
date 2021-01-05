#author:wang fang
#装饰器定义：本质是函数，（装饰其他函数）就是为其他函数添加附加功能
#原则：1.不能修改被装饰的函数的源代码
#2.不能修改被装饰函数的调用函数

#实现装饰器的知识储备：1.函数即变量
# 2.高价函数 ：把一个函数名当作实参传递给另一个函数（不能修改被装饰的函数的源代码） ，返回值包含函数名（不改变函数调用方式）
# 3.嵌套函数
import time,sys
def timer(func): #func=test1
    def deco():
        start_time = time.time()
        func()#运行test1函数
        end_time = time.time()
        print(end_time - start_time)
    return deco

@timer #哪个函数需要调用附加功能，就哪里加
def test1():
    time.sleep(1)
    print('in the test1')
    return 0


#test1=timer(test1)  相当于@timer
test1()