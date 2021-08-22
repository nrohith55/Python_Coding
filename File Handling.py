

f1=open('abc','w') # write the file
f2=open('abc','r') # read the file
f=open('abc','a') # append the file
f.write("Something")
f.write("My name is Rohith")

for i in f:
    print(i)