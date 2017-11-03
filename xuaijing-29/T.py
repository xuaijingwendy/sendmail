class Student:
   '所有学生的基类'
   empCount = 0
 
   def __init__(self,name,male,stu_nu,stu_class):
      self.name = name
      self.male= male
      self.stu_nu=stu_nu
      self.stu_class=stu_class
      Student.empCount += 1
   
   def displayCount(self):
    print "Total Employee %d" % Student.empCount
 
   def displayEmployee(self):
      print "Name : ", self.name,  ",Stu_num: ", self.stu_num
      
   def displayStu(self):
      print ",Name:",self.name
      
   def  displaydance(self):
      print "Male:",self.male, ",Name : ", self.name
