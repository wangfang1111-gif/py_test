
#author:wang ang
import socket,time
#买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#拨电话
phone.connect(('127.0.0.1',8080)) #5指的是半连接池的大小
#通信
time.sleep(3)
phone.send('hello world hahah'.encode('gbk'))
data=phone.recv(1024)
print(data.decode('gbk'))
phone.close() #关闭连接，回收资源的操作