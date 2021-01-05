#author:wang fang
#format()   格式化拼接
Name=input("please you name:")
Job=input("please you job:")
Age=input("please you age:")
Salary=input("please you Salary:")
#字符串拼接，格式化输出 %d %s %f
info='''------------info of %s-------------------
Name：%s
Job:%s
Age:%s
Salary:%s
'''%(Name,Name,Job,Age,Salary)
print(info)

#format()   格式化拼接
#这种方式使用花括号{}做占位符，在format方法中再转入实际的拼接值。容易看出，它实际上是对%号拼接方式的改进
info2='''------------info of {name1}-------------------
Name：{name1}
Job:{job1}
Age:{age1}
Salary:{salary1}
'''.format(name1=Name,job1=Job,age1=Age,salary1=Salary)
print(info2)


info3='''------------info of {0}-------------------
Name：{0}
Job:{1}
Age:{2}
Salary:{3}
'''.format(Name,Job,Age,Salary)
print(info3)
