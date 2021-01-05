#author:wang fang
import socket
#买手机
phone=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#绑定电话卡
phone.bind(('127.0.0.1',8080))
#开机
phone.listen(5) #5指的是半连接池的大小
print('service start successful,address is %s : %s'%('127.0.0.1','8080'))
conn,client_addr=phone.accept()
print(conn)
print('client_addr:',client_addr)
data=conn.recv(1024) #最大接收1024的字节
print("client message:",data.decode('gbk'))
conn.send(data.upper()) #将传的消息进行大写
conn.close() #关闭连接
#phone.close() #关机