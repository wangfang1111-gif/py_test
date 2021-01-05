#author:wang fang
#静态方法：@staticmethod只是名义上归类管，实际静态方法里访问不了类的属性，调用的是函数

#类方法 @classmethod 只能访问类变量，不能访问实例变量,调用的是类，传入的是类
#提供新的造对象方式，不是赋值，从哪里获取，如读取配置文件的ip port

#属性方法 @property把方法变成一个静态属性  航空公司状态

#类的特殊成员方法
'''
1.__doc__ 输出类的描述信息
2.__module__ 输出模块
3.__class__ 输出的类本身
4.__init__ 构造方法，类创建对象
5.__del__ 析构方法，释放对象
6.__call__ 
7.__dict__ 查看类中所以成员
8.__str__ 返回方法的返回值
9.__getitem__
10.__setitem__
11.__delitem__
12.__new__
13.__metaclass__
'''
class Aniaml:
    def __init__(self,name):
        self.name=name

    @staticmethod
    def aniaml_talk(obj):
        obj.talk()

    def talk(self):
        pass


class cat(Aniaml):
    '''talking is do nothing'''
    def talk(self):
        print ('MoMo')

class dog(Aniaml):
    def talk(self):
        print ('wangwang')
c1=cat('cat')
Aniaml.aniaml_talk(c1)
print(c1.__doc__)
print(Aniaml.__module__)
print(c1.__class__)
print(c1.__dict__)