'''
class zenrays:

    def add(self):
        print("Add two numbers a and b")

var=zenrays()

print(var.add())
'''

'''
class training:

    def print_name(self):
        return "Basics of oops concept"

var=training()

print(var.print_name())

'''

class details:

    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age

    def full_name(self):
        return self.fname+ " " + self.lname

var1=details("Sachin","Tendulkar",45)
var2=details("Virendra","Sehwag",40)

print(var1.full_name())