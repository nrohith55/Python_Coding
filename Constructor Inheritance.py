class A:

    def __init__(self):
        print("in A is working")

    def feature1(self):
        return "Feature1 is working"

    def feature1(self):
        return "Feature1 is working"


class B:

    def __init__(self):
        print("in B is working")

    def feature3(self):
        return "Feature3 is working"

    def feature4(self):
        return "Feature4 is working"


class C(A,B):

    def __init__(self):
        super().__init__()
        print("in C is working")


var=C()

print(var)


