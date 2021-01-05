#author:wang fang
class Role:
    cn='china'#类变量，节省内存
    def __init__(self, name, role, weapon, life_value=10000, money=15000):
        # 构造函数 实例化类的初始方法
        self.name = name #实例变量，静态属性，作用域实例本身
        self.role = role
        self.weapon = weapon
        self.__life_value = life_value#私有属性，只能在类里调用
        self.money = money

    def buy_gun(self):
        print('%s brought a %s' % (self.name, self.weapon))

    def shot(self):
        print("shotting")
    def show(self):
        print('%s is %s,life_value is %s'%(self.name,self.role,self.__life_value))
    #私有方法
    def __bullt_prove(self):
        print('add a bullt')

    #析构函数
    def __del__(self):
        print('%s has been die'%self.name)



r1= Role('wangfang','police','AK13')
r1.buy_gun()
r1.shot()
r1.show()
#del r1
r2= Role('liuyang','police','B16')
r1.name='wangjia'
r1.cn='America'
print(r1.name,r1.role,r1.weapon,r1.money,r1.cn)
#del r1.weapon
print(r2.name,r2.role,r2.weapon,r2.money,r2.cn)


