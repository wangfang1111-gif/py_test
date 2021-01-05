#author:wang fang
#shutil模块注意用于拷贝和解压，压缩
import  shutil
##shutil.copy('sys.py','sys_bak.py')
#压缩
#shutil._make_zipfile('C:/Users/WF/PycharmProjects/s01/day04/sys.py','C:/Users/WF/PycharmProjects/s01/day04')

#序列化
import json
# json_res=json.dumps([1,'aaa','True','False'])
# print(json_res,type(json_res))

#反序列化
#res=json.loads(json_res)
# print(res,type(res))

#文件写入json格式复杂化
'''
with(open('test.json','wt',encoding='utf-8')) as f:
    json_res = json.dumps([1, 'aaa', 'True', 'False'])
    f.write(json_res)
    f.close()
'''
#文件写入json格式简化
'''
with(open('test.json','wt',encoding='utf-8')) as f:
    json_res = json.dump([1,'aaa','True','False'],f)
'''
#文件读取json格式复杂化
'''
with(open('test.json','rt',encoding='utf-8')) as f:
    res=f.read()
    l= json.loads(res)
    print(l)
    f.close()
'''
#文件读取json格式简化
'''
with(open('test.json','rt',encoding='utf-8')) as f:
    l=json.load(f)
    print(l)
    f.close()
'''
#pickle模块 dump,load都是需要写文件的，以二进制方式
import  pickle
json_res=pickle.dumps([1,'aaa','True','False'])
print(json_res)
res=pickle.loads(json_res)
print(res)

