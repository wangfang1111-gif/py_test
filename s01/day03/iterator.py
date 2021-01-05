#author:wang fang

#迭代器：可以被next函数调用并不断返回下一个值的对象，iterator
from collections import Iterator

print(isinstance((i for i in range(2)),Iterator))

print(isinstance((),Iterator))


#迭代对象：集合行数据list,tuple，set,dict,str,和带生成器的函数，以及生成器，iterable
#isinstance判断是否是迭代对象
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance('sss',Iterable))

