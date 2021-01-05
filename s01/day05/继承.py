#author:wang fang
#paython 2 是深度优先，paython3是广度优先
#A,B,C,D

class A(object):
    def __init__(self):
        print('---A---')


class B(A):
    def __init__(self):
        print('---B---')

class C(A):
    def __init__(self):
        print('---C---')

class D(B,A):
    pass
    # def __init__(self):
    #     print('---D---')

obj=D()