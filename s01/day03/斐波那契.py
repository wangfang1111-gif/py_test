#author:wang fang
#函数做的生成器
def fib(max):
    n,a,b=0,0,1
    while n<max:
        #生成器
        yield b
        a,b=b,a+b
        n=n+1
    return "---done"


f=fib(100)
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())
print(f.__next__())







