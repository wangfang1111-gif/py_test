#author:wang fang
import os

print(os.path.abspath(__file__)) #显示系统的绝对路径
print(os.path.isabs('../..s01/day01'))#是不是绝对路径
print(os.path.split('C:/Users/WF/PycharmProjects/s01/day04/os2.py')) #切割路径

#掌握
#取当前文件的目录
print(os.path.dirname('C:/Users/WF/PycharmProjects/s01/day04/os2.py'))
print(os.path.basename('C:/Users/WF/PycharmProjects/s01/day04/os2.py'))
print(os.path.isfile('/s01/day01'))
print(os.path.isdir('C:/Users/WF/PycharmProjects/s01/day04'))
print(os.path.join('C:/Users/WF/PycharmProjects/s01/day03'))
print(os.path.getsize('C:/Users/WF/PycharmProjects/s01/day04/os2.py'))