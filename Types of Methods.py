
# There are basically three methods Instance,Class and Static Methods

class students:

    school = 'Cambridge'

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    @classmethod

    def get_school(cls):

        return cls.school

    @staticmethod

    def info():

        return "These students belongs to section A of 10th Class"

var1=students(11,21,12)

print(var1.avg())

print(var1.get_school())

print(var1.info())


