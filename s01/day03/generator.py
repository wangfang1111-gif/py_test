#author:wang fang
#列表生成式
a=[i*2 for i in range(10)]
print(a)

#生成器定义，只能调用时生成数据，节省空间
b=(i*2 for i in range(10))
print(b)





