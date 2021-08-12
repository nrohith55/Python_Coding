Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import math
>>> x=math.sqrt(25)
>>> x
5.0
>>> x=math.sqrt(15)
>>> x
3.872983346207417
>>> print(math.floor(2.9))
2
>>> print(math.ceil(2.2))
3
>>> 3**@
SyntaxError: invalid syntax
>>> 3**2
9
>>> print(math.pow(3,2))
9.0
>>> print(math.pi)
3.141592653589793
>>> print(math.e)
2.718281828459045
>>> import math as m
>>> m.sqrt(25)
5.0
>>> m.factorial(5)
120
>>> from math import sqrt,pow
>>> sqrt(25)
5.0
>>> pow(5)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    pow(5)
TypeError: pow expected 2 arguments, got 1
>>> pow(3,4)
81.0
>>> 