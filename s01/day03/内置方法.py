#author:wang fang
#元素里都是非0数字，则返回真
print(all([0,1,2]))
print(all([-1,1,2]))
print(abs(-1))
#元素里只要有一个元素非0，则返回真
print(any([0,1,2]))
print(bin(111))
print(oct(111))
print(hex(111))

print(ascii("开发"))
print(bool())
#是否可调用
print(callable('ss'))
#返回ASCII码
print(chr(98))
print(ord('a'))
#字典,dir返回内置方法
a=dict()
print(dir(a))
print(divmod(10,2))
#可以把字符串里的字符转换为可执行代码，但只支持一行字符。可以返回执行后得到的值
res=eval('1+2')
#可以把字符串里的字符转换为可执行代码，可以支持多行字符。但是拿不到返回结果
#exec()
#不可编辑
a=frozenset([1,2,2,4])

#hash(不可变类型)
#类型判断
print(isinstance([],list))
#x=__import__('time')  导入字符串

#打印key和值
for i,v in enumerate(['a','b','c','d']):
    print(i,v)
