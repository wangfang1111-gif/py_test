#author:wang fang
import random

print(random.random())#取大于0，小于1
print(random.uniform(1,3))#取大于1，小于3

print(random.randint(1,3))#取大于1且小于等于3的整数
print(random.randrange(1,3))#取大于等于1且小于3的整数
print(random.choice(['1','aa',[44,55]]))#取大于等于1且小于3的整数
print(random.sample(['1','aa',[44,55]],2))#取任意两个元素
#任意排序
item=[1,2,3,5,9]
random.shuffle(item)
print(item)

