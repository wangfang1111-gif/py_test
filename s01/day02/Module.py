#author:wang fang
#lib下有很多第3方库
import  sys
import os
#print(sys.path)
#打印环境变量
'''
print(sys.argv)
#打印行对路径和参数
cmd_res=os.system("dir")
#结果直接输出到屏幕后清空,执行命令不保存结果
print("--->",cmd_res)


cmd_res1=os.popen("dir").read()
print("--->",cmd_res1)
'''
os.mkdir("new_dir")
#创建目录
#模块在同一目录可以引用
os.removedirs("new_dir")
#删除目录

