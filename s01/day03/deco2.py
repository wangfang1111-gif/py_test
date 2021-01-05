#author:wang fang
#当被修饰函数需要传参数，同时返回值s
#装饰器需要加参数 还未写
#登录3个主页面,需要验证
#\033[32;1m  \033[0m  表示字体颜色
import time
user,pwd='abc','123'
def auth(func):
    def wrapper(*args,**kwargs):
        username=input("Please input username:")
        password=input("Please input password:")
        if username==user and password==pwd:
            print("\033[32;1m User has passed authentication \033[0m")
            res=func(*args,**kwargs)
            print('----after authentication')
            return res
        else:
            exit("\033[31;1mUser has passed authentication\033[0m")
    return wrapper

@auth  #auth=auth(index)
def index():
    print("welcome to index page ")
@auth
def home():
    print("welcome to home page ")
    return "from home"
@auth
def bbs():
    print("welcome to home page ")
index()
print(home())
bbs()