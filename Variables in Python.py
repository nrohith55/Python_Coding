Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=2
>>> x
2
>>> x+3
5
>>> y=3
>>> x+y
5
>>> x=9
>>> x+y
12
>>> x
9
>>> abc
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    abc
NameError: name 'abc' is not defined
>>> x+10
19
>>> _+y
22
>>> name='youtube
SyntaxError: EOL while scanning string literal
>>> name='youtube'
>>> name
'youtube'
>>> name+'rocks
SyntaxError: EOL while scanning string literal
>>> name+'rocks'
'youtuberocks'
>>> name[0]
'y'
>>> name[6]
'e'
>>> name[8]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    name[8]
IndexError: string index out of range
>>> name[-1]
'e'
>>> name[-2]
'b'
>>> name[-7]
'y'
>>> name[0:2]
'yo'
>>> name[1:4]
'out'
>>> name[1:]
'outube'
>>> name[:4]
'yout'
>>> name[3:10]
'tube'
>>> name[0:3]='my'
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    name[0:3]='my'
TypeError: 'str' object does not support item assignment
>>> name[0]='R'
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    name[0]='R'
TypeError: 'str' object does not support item assignment
>>> 'my'+name[3:]
'mytube'
>>> 'my' +name[2:]
'myutube'
>>> myname='Rohith Neelagiriyappa'
>>> len(myname)
21
>>> 