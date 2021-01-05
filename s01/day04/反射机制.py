#author:wang fang
#反射:程序在运行种可以动态（不见棺材不掉泪）的获取对象
class People(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say(self):
        print('%s age is %s'%(self.name,self.age))

obj=People('wangfang','18')
#实现反射机制
#dir，得知对象的属性，通过字符串反射到属性上，得到属性值
#hasattr
print(dir(obj))
print(hasattr(obj,'name'))
#getattr
print(getattr(obj,'name'))
#setattr
setattr(obj,'name','wangjia')
print(getattr(obj,'name'))

#delattr
delattr(obj,'name')


