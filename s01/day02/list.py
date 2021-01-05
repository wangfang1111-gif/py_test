#author:wang fang
#定义列表
names=["wangfang","xiangpeng","zhangzhizhi","liyang"]
names2=["zhangwu","xiatian","sisi","qingxie","Xiejia"]

'''
#增加
names.append("xiaoming")
names.insert(1,"Wangjia")
print(names)
#扩展，两个列表叠加
names.extend(names2)
print(names)
'''
#改
names[1]="Xaingpeng"
print(names)
#查下标
print(names.index('liyang'))
'''
#切片,只含头不含尾
print(names[1:3])
print(names[1:])
print(names[0:-1])

#删
names2.remove("xiatian")
#默认删除最后一个
names2.pop()
print(names2)
'''
#列表的其他方法

#清除
#print(names.clear())
print(names2.count('sisi'))
#元素反向排序，ASCII
#names2.reverse()
names2.sort()
print(names2)
'''
name3=names.copy()
print(name3)
'''
