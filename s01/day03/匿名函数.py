#author:wang fang
#变量名= lambda 参数:表达式(block)
#  lambda 参数列表：return [表达式] 变量
#  由于lambda返回的是函数对象（构建的是一个函数对象），所以需要定义一个变量去接收
T=lambda x,y:x+y
print(T(4,5))

import functools
#对参数序列中元素进行累加
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
v1=[33,44,55]
#映射, 循环让每个元素执行函数，将每个函数执行的结果保存到新的列表中
result=map(lambda x:x+100,v1)
print(list(result))
#按条件删除
result2=filter(lambda x:x>40,v1)
print(list(result2))
salaries={
    'egon':3000,
    'alex':100000000,
    'wupeiqi':10000,
    'yuanhao':2000
}
print(min(salaries,key=lambda x:salaries[x]))
