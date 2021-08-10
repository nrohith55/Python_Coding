Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> NUM=5
>>> num=5
>>> num
5
>>> id(num)
345061419440
>>> name='rohith'
>>> id(name)
345107637552
>>> a=10
>>> b=a
>>> a
10
>>> b
10
>>> id(a)
345061419600
>>> id(b)
345061419600
>>> id(10)
345061419600
>>> k=10
>>> id(k)
345061419600
>>> type(k)
<class 'int'>
>>> pi=3.142
>>> pi
3.142
>>> type(pi)
<class 'float'>
>>> 