# Single Inheritance
#Multilevel Inheritance
#Multiple Inheritance

class A:
    def func1(self):
        return "Function 1 is working"

    def func2(self):
        return "Function 2 is working"


class B(A):
    def func3(self):
        return "Function 3 is working"

    def func4(self):
        return "Function 4 is working"


class C(A,B):
    def func5(self):
        return "Function 5 is working"



print(C().func2())
print(C().func5())