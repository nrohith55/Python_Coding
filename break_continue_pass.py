'''
av=5

x=int(input("How many candies you want?"))

i=1

while i<=x:

    if x>5:
        print("Out of stock")
        break

    print("candy")
    i+=1

print('Bye')

'''

'''
for i in range(100):

    if i %3==0 or i%5==0:
        continue

    print(i)


'''
'''
for i in range(100):

    if i%2!=0:
        pass
    else:
        print(i)

'''

#Break
'''
for i in range(5):

    if i==3:
        break
    print("Hello",i)

'''

for  i in range(5):
    if i==3:
        continue
    print("Hello",i)



