Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup=(21,36,23,45)
>>> tup
(21, 36, 23, 45)
>>> tup[1]
36
>>> tup[1]=22
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tup[1]=22
TypeError: 'tuple' object does not support item assignment
>>> s={22,3,43,44,32,4}
>>> s
{32, 3, 4, 22, 43, 44}
>>> s1={2,1,2,3,3,4,5,6,3,5}
>>> s1
{1, 2, 3, 4, 5, 6}
>>> s1[2]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    s1[2]
TypeError: 'set' object is not subscriptable
>>> 