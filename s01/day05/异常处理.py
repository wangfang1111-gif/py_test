#author:wang fang
#1.什么是异常
#异常的特征：异常的类型，异常内容，异常的追踪信息
#异常是程序发生的信号，一旦出错，程序立即停止
#处理异常，为了增强代码的健壮性，应该要捕捉信息记录日志

#语法错误必须改正，逻辑错误：
#预料不出来的代码才需要用到
try:
    a={'111','bb'}
    a[3]
    x=1

except ConnectionRefusedError :
    print('a error')

except NameError :
    print('two error')
except  TypeError :
    print('three error')
else:
    print('sssss')
finally:
    print('ggggg') #不影响子代码
