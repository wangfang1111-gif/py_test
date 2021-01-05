#author:wang fang
import hashlib
m=hashlib.md5()
m.update('hello'.encode('utf-8'))
m.update('world'.encode('utf-8'))
res=m.hexdigest()
print(res)

m=hashlib.md5()
m.update('hello'.encode('utf-8'))
m.update('wor'.encode('utf-8'))
m.update('ld'.encode('utf-8'))
res2=m.hexdigest()
print(res2)

#如果是大文件的读取校验，seek到某个点再固定读
with open('a.txt',mode='rb') as f :
    m = hashlib.md5()
    f.seek(20)
    m1=f.read(200)
    m.update( m1)
    res3=m.hexdigest()
    print(res3)


