#author:wang fang
#elif 用法
#猜多次
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

