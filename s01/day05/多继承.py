#author:wang fang
#学校  注册学生，雇佣老师，名字
#学校的人 名字 性别，age
#学生 交学费
#老师 教课程
class School:
    def __init__(self,name,addr):
        self.name=name
        self.addr=addr
        self.student=[]
        self.staff = []
        print('%s School set %s'%(self.name,self.addr))
    def registered(self,stu_obj):
        print('%s registered in %s success'%(stu_obj.name,self.name))
        self.student.append(stu_obj)
    def hire(self,staff_obj):
        print('%s is hired this school'%(staff_obj.name))
        self.staff.append(staff_obj)

class SchoolMemeber:
    def __init__(self,name,sex,age):
        self.name=name
        self.sex=sex
        self.age=age

class Teacher(SchoolMemeber):
    def __init__(self,name,sex,age,course,salary):
        super(Teacher,self).__init__(name,sex,age)
        self.course=course
        self.salary=salary
        print('''-----info of %s------
        Name:%s
        Sex:%s
        Sge:%s
        Course:%s
        Salary:%s
        '''%(self.name,self.name,self.sex,self.age,self.course,self.salary))
    def teach(self):
        print('---%s is teaching %s course----'%(self.name,self.course))

class Student(SchoolMemeber):
    def __init__(self, name, sex, age, grade, tuition):
        super(Student, self).__init__(name, sex, age)
        self.grade = grade
        self.tuition = tuition
        print('''-----info of %s------
          Name:%s
          Sex:%s
          Sge:%s
          Grade:%s
          Tuition:%s
          ''' % (self.name, self.name, self.sex, self.age, self.grade, self.tuition))

    def  pay_tuition(self):
        print('%s pay tuition is %s'%(self.name,self.tuition))

School=School('linzikouzhonogxue','xiangyinxian')
T1=Teacher('wangfang','girl','26','chinese','5000')
T2=Teacher('liuyang','boy','26','Engshil','6000')
T1.teach()
T2.teach()
s1=Student('chenrong','boy','22','60','5000')
s2=Student('liming','boy','24','70','5000')
s1.pay_tuition()
s2.pay_tuition()
School.registered(s1)
School.hire(T1)