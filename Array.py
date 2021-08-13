'''

import array
from array import *

vals=array('i',[1,2,3,90,23])

for i in vals:
    print(i)

'''
'''
import array
from array import *

arr=array('i',[])
x=int(input("Enter the length of array"))

for i in range(x):
    x=int(input("Enter the next value"))
    arr.append(x)

print(arr)

val=int(input("Enter the value you want to search"))

print(arr.index(val))


k=0

for e in arr:
    if e==val:
        print(k)
        break
    k+=1

'''

import array

from array import *

arr=array('i',[])

x=int(input("Enter the length of array"))

for i in range(x):
    n=int(input("Enter the next array"))
    arr.append(n)

print(arr)


val=int(input("Enter the value for search"))

print(arr.index(val))

k=0

for e in arr:
    if e==val:
        print(k)
        break
    k+=1









