#author:wang fang
import subprocess
#运行系统命令，正确的输出到stdout管道，错误的输出到stderr
obj=subprocess.Popen('ipconfig',shell=True,
                 stdout=subprocess.PIPE,
                 stderr=subprocess.PIPE)

print(obj)
res=obj.stdout.read()
print(res.decode('gbk'))
res1=obj.stderr.read()
print(res1.decode('gbk'))
