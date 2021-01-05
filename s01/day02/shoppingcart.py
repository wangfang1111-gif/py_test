#author:wang fang
'''
1.启动程序，让用户输入工资，打印商品列表
2.允许用户根据商品编号购买商品
3.用户选择商品后，检测余额是否足够，够则直接扣款，不够提醒
4.可以随时退出，退出时，打印已购商品和余额
'''
goods=[('dianshan','100'),('cup','30'),('milk','50'),('latiao','30')]
salary=int(input("please input your salary:"))
for i in range(len(goods)):
    print(i,goods[i])
Flag=True
cart = []
while Flag:
    cart_user = input('plsease choose goods:')
    if cart_user.isdigit():
        if int(cart_user) <= len(goods) - 1:
            if salary >= int(goods[int(cart_user)][1]):
                salary = salary - int(goods[int(cart_user)][1])
                cart.append(int(cart_user))

            else:
                print('salary is not enough')
        else:
            print('good is not exist')
    else:
        Flag = False
        print('you buy good is :')
        for i in range(len(cart)):
            print(goods[int(cart[i])])
        print('Remaining money is:',salary)






