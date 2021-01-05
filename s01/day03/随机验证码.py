#author:wang fang
#随机验证码
#6个随机验证码
import  random
def make_code(size=6):
    res = ''
    for i in range(size):
        s1=chr(random.randint(65,90))
        s2=str(random.randint(0,9))
        res+=random.choice([s1,s2])
    return res

print(make_code(4))
