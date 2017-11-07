class Student:
    StuCount=0

    def __init__(self,name,stu_nu,class_nu,gender):
        self.name=name
        self.stu_nu=stu_nu
        self.class_nu=class_nu
        self.gender=gender
        Student.StuCount+=1

    def study(self):
        print "Student can study"
    def getstucount(self):
        return Student.StuCount

class primaryStudent(Student):
    primaryStuCount=0

    def canRecite(self):
        print "Primary Student can recite"
    def canOral(self):
        print "Primary Student can oral"


        
class middleStudent(Student):
    middleStuCount=0
    
    def __init__(self,name,stu_nu,class_nu,gender):
        self.name=name
        self.stu_nu=stu_nu
        self.class_nu=class_nu
        self.gender=gender
        Student.StuCount+=1
        middleStudent.middleStuCount+=1

    def canChemistry(self):
        print "middle Student can chemistry"
    def canPyhics(self):
        print "middle Student can pyhics"
        
