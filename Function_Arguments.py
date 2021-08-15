'''
def update(x):
    x=10
    print(x)
    print(id(x))
'''
'''
result=update(15)
print(result)

a=20
update(a)
print(a)
print(id(a))



def person(name,age=31): # Defaul Argument
    print(name)
    print(age)
person(name="Rohith",age=31) # Keyword Argument'''


def sum(*b):
    c=0

    for i in b:
        c=c+i
    print(c)

sum(1,2,3,4)

