#author:wang fang
#继承 父类，子类
#super 用法
#人，男人，女人，关系
class People:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def talk(self):
        print('%s is talking'%self.name)
class relationship(object):
    def make_friends(self,obj):
        print('%s is makeing friends with %s' % (self.name, obj.name))

class Men(People,relationship):
    def __init__(self,name,age,sex):
        #People.__init__(self,name,age)
        super(Men,self).__init__(name,age)#新式类写法
        self.sex=sex

    def sleep(self):
        print('...sleeping...')


class Women(People):
    def __init__(self,name,age,sex):
        People.__init__(self,name,age)
        self.sex=sex
    def make(self):
        print('...is making...')
w1=Men('liuyang',22,'boy')
m1=Women('zhangying',24,'girl')
w1.make_friends(m1)
w1.talk()
w1.sleep()
m1.talk()
m1.make()
