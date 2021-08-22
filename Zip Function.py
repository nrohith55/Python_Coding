names=('Ravi','Ram','Laxman')
company=('HP','MS','BMW')

zipped=list(zip(names,company))

print(zipped)

p=zip(names,company)

for (a,b) in p:
    print(a,b)

zipped1=dict(zip(names,company))

print(zipped1)