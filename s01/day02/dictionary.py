#author:wang fang
#定义，增删，改，查
student={'st01':'wangfang',
'st02':'wangjia1',
'st03':'xiaoyang'}
student2={'st07':'limei',
          'st08':'zhangyang'}
#增
student['st04']='liyiyi'
print(student)
#查
print(student['st02'])
print(student.get('st02'))
#返回一个新的字典
print(student.fromkeys('st01'))
print(student.items())
print(student.keys())
print(student.values())
#返回key的对应值，没有则位null
print(student.setdefault('st06'))
#    dict2 -- 添加到指定字典dict里的字典。

print(student.update(student2))



#改
student['st02']='wangpeng'
print(student)
#删除
#student.pop('st02')
