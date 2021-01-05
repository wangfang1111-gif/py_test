#author:wang fang
#猜年纪，超过3次想继续完需要确认
count = 0
while count < 5:
    Age = int(input("please input you guess age:"))
    if Age > 46:
        print("please guess smaller")
        count =count+1
    elif Age < 46:
        print("please guess bigger")
        count = count + 1
    else:
        print("you are right,guess it")
        break
    if count==3:
        confime_info=input("DO you want to countine guess? Y is yes,N is No:")
        if confime_info=='Y':
            count = 0
        else:
            break

