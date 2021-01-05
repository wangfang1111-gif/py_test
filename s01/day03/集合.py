#author:wang fang
#定义，交集，并集，差集，子集，对称差集
list_1=[1,3,4,5,5,6,7,9,3,1]
list_2=set(list_1)
list_3=set([1,9,6,2,7,8,8])
print(list_2,type(list_2))
print(list_3,type(list_3))

#交集
print('jiaoji',list_2.intersection(list_3))
print('jiaoji',list_2 &(list_3))

#并集
print('bingji',list_2.union(list_3))
print('bingji',list_2 |(list_3))
#差集
print('chaji',list_2.difference(list_3))
print('chaji',list_2 -(list_3))


#对称差集
print('duichengchaji',list_2.symmetric_difference(list_3))
print('duichengchaji',list_2 ^(list_3))


#增，删
#增元素
list_3.add(10)
print('list_3_add',list_3)
list_3.update(list_2)
print('list_3_update',list_3)


#删元素discard删除不存在的元素返回none
list_2.discard(3)
list_2.discard(10)
print(list_2)
list_2.remove(6)
print(list_2)
#交集，并集，差集，对称差集的符号

