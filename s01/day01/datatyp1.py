# -*- coding:utf-8 -*-
#author:wang fang

'''
多行注释
'''
import getpass
#getpass.getpass("password:") 加密
name=input("please input name:")
pwd=input("please input password:")
age=int(input("please input your age:"))
print(name,pwd,age)
print(type(name))
print(type(age))

#三元运算
a=1
b=2
c=3
result=a if a>b else c
print(result)

