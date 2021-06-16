class School:
    def __init__(self):
        self.cl1=None
        self.fie=None
        self.pl=None
        self.tr=None
        self.sd=None

class Class1:
    def __init__(self,few):
        self.few=few
        self.object=None
class Object:
    def __init__(self,chs):
        self.chs=chs
        self.hm=None
class Howmany:
    def __init__(self,h1):
        self.h1=h1

class Field:
    def __init__(self,saveral):
        self.saveral=saveral

class Parkinglot:
    def __init__(self,many):
        self.many=many

class Tree:
    def __init__(self,afew):
        self.afew=afew

class Salesdepartment:
    def __init__(self,stalls):
        self.stalls=stalls

Kaohsuing=School()
Kaohsuing.cl1=Class1(50)
Kaohsuing.cl1.object=Class1(150)
Kaohsuing.cl1.object.chs=Object(60)
Kaohsuing.cl1.object.chs.hm=Howmany(20)
print(Kaohsuing.cl1.object.chs.hm.h1)

Kaohsuing.fie=Field(2)
Kaohsuing.pl=Parkinglot(3)
Kaohsuing.tr=Tree(100)
Kaohsuing.sd=Salesdepartment(5)
