Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num=2.5
>>> num
2.5
>>> type(num)
<class 'float'>
>>> num=5
>>> type(num)
<class 'int'>
>>> num=5+i7
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    num=5+i7
NameError: name 'i7' is not defined
>>> num=6+9j
>>> num
(6+9j)
>>> type(num)
<class 'complex'>
>>> a=5.6
>>> b=int(a)
>>> b
5
>>> k=float(b)
>>> k
5.0
>>> k=6
>>> c=complex(b,k)
>>> c
(5+6j)
>>> b<k
True
>>> bool=b
>>> bool=b<k
>>> bool
True
>>> type(bool)
<class 'bool'>
>>> b>k
False
>>> int(True)
1
>>> int(False)
0
>>> lst=[25,36,12]
>>> type(lst)
<class 'list'>
>>> s={1,2,1,2,3,4}
>>> s
{1, 2, 3, 4}
>>> type(s)
<class 'set'>
>>> t=(1,2,3,2,1,2,3)
>>> t
(1, 2, 3, 2, 1, 2, 3)
>>> type(t)
<class 'tuple'>
>>> str="Rohith"
>>> str
'Rohith'
>>> type(str)
<class 'str'>
>>> st='s'
>>> type(st)
<class 'str'>
>>> range(0,10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> list(range(2,11,2))
[2, 4, 6, 8, 10]
>>> typ(range(10))
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    typ(range(10))
NameError: name 'typ' is not defined
>>> type(range(10))
<class 'range'>
>>> d={'rohith':'samsung','rahul':'iphone}
   
SyntaxError: EOL while scanning string literal
>>> d={'rohith':'samsung','rahul':'iphone'}
>>> d
{'rohith': 'samsung', 'rahul': 'iphone'}
>>> d.keys
<built-in method keys of dict object at 0x000000B7FA778240>
>>> d.keys()
dict_keys(['rohith', 'rahul'])
>>> d.values()
dict_values(['samsung', 'iphone'])
>>> d['rahul']
'iphone'
>>> d.get('rohith')
'samsung'
>>> 