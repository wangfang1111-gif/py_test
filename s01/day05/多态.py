#author:wang fang
class Aniaml:
    def __init__(self,name):
        self.name=name

    @staticmethod
    def aniaml_talk(obj):
        obj.talk()

    def talk(self):
        pass


class cat(Aniaml):
    def talk(self):
        print ('MoMo')

class dog(Aniaml):
    def talk(self):
        print ('wangwang')


d1=dog('dog')
# d1.talk()
c1=cat('cat')
# c1.talk()
# aniaml_talk(d1)
# aniaml_talk(c1)
Aniaml.aniaml_talk(d1)
Aniaml.aniaml_talk(c1)