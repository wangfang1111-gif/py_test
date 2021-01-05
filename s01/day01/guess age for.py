#author:wang fang

for i in range(0,5):
    Age = int(input("please input you guess age:"))
    if Age > 46:
        print("please guess smaller")
    elif Age < 46:
        print("please guess bigger")
    else:
        print("you are right,guess it")
        break

