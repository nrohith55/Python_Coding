
'''
a=4

b=0

try:

    print(a/b)

except Exception as e:
    print("Hey you cannot divide the number by zero", e)

'''

a = 5
b = 2

try:
    print("resource Open")
    print(a/b)
    k = int(input("Enter a number"))
    print(k)

except ZeroDivisionError as e:
    print("Hey, You cannot divide a Number by Zero" , e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went Wrong...")

finally:
    print("resource Closed")