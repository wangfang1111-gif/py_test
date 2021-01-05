#author:wang fang
#登录接口，输入用户名密码，成功显示欢迎信息
#输入3次锁定
user_dict=[{'username':'wangfang','pwd':'123'},
           {'username':'lili','pwd':'123'}]
username=input('please input username:')
pwd=input('please input password:')
count=0
for item in user_dict:
    if username==item['username'] and pwd==item['pwd']:
        print('welcome to page')
    else:
        count+=1
        print('username or pwd is not correct')


