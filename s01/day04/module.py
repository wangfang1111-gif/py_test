#author:wang fang
#定义 模块本质就是实现一个功能的py文件
#导入方法
#from module import * 不建议用
#from module import logger as logger1
import sys,time
#import本质,就是把paython文件解释一遍

#包的定义:组织模块逻辑，本质就是目录，必须有_init_.py文件
#导入包的本质就是执行_init_.py文件
#搜索当前路经
#sys.path()
#os.path.abspath()
#os.path.dirname()

#导入优化
#from module import logger
#导入优化
#a标准库 b开源模块 c自定义模块