
num=int(input("Enter the number"))

for i in range(2,num):

    if i % 2 == 0:
        print("Number is not Prime")
        break
else:
    print("Number is Prime")