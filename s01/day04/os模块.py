#author:wang fang
import os
print(os.getcwd())#取当前脚本工作文件路径
#os.chdir("dirname")#改变当前脚本工作目录
# os.curdir 返回当前目录
# os.pardir #取上级目录
os.mkdir("dirname")#生成单级目录
os.rmdir('dirname')#删除单级目录
os.makedirs('dirname1/diranme2')#生成递归目录
os.removedirs('dirname1/diranme2')#删除空文件夹
#path/filename
os.stat('C:/Users/WF/PycharmProjects/s01/day04/os2.py')#获取文件目录信息
os.sep #输出操作系统特定路径分隔符，win下"\\" linux'/'
os.linesep#输出当前平台的行终止符，win下"\r\n" linux'\n'
os.pathsep #输出用于分割文件路径的字符串win下位；linux下为：
os.name #输出字符串只是当前使用平台
##掌握
dir=os.listdir('C:/Users/WF/PycharmProjects/s01')#列出目录下所有文件和子目录
print(dir)
#os.remove()#删除一个文件
#os.rename('oldname','newname')#重命名文件
##掌握
#os.system('ls') #运行shell 命令直接显示
#key和word都是字符串
s1=os.environ #获取系统环境变量
print(s1)

