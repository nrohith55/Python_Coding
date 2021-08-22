

def topten():

    n=1

    while n<=10:
        sq=n*n
        yield sq
        n+=1

var=topten()

for i in var:
    print(i)