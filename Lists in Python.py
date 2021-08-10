Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> nums=[25,12,36,95,14]
>>> nums
[25, 12, 36, 95, 14]
>>> nums[0]
25
>>> nums[4]
14
>>> nums[6]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    nums[6]
IndexError: list index out of range
>>> nums[1:2]
[12]
>>> nums[2:]
[36, 95, 14]
>>> nums[-1]
14
>>> nums[-1:]
[14]
>>> nums[-5]
25
>>> names=['Navin','Rohith','John']
>>> name
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    name
NameError: name 'name' is not defined
>>> names
['Navin', 'Rohith', 'John']
>>> values=[9.5,'Rohith',34]
>>> values
[9.5, 'Rohith', 34]
>>> mil=[nums,names]
>>> mil
[[25, 12, 36, 95, 14], ['Navin', 'Rohith', 'John']]
>>> nums.append(45)
>>> nums.append(45)
>>> nums
[25, 12, 36, 95, 14, 45, 45]
>>> nums.insert(2,77)
>>> nums
[25, 12, 77, 36, 95, 14, 45, 45]
>>> nums.remove(14)
>>> nums
[25, 12, 77, 36, 95, 45, 45]
>>> nums.pop(1)
12
>>> nums
[25, 77, 36, 95, 45, 45]
>>> nums.pop()
45
>>> nums
[25, 77, 36, 95, 45]
>>> del nums[2:]
>>> nums
[25, 77]
>>> nums.extend(23,34,56)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    nums.extend(23,34,56)
TypeError: list.extend() takes exactly one argument (3 given)
>>> nums.extend([23,34,56])
>>> nums
[25, 77, 23, 34, 56]
>>> min(nums)
23
>>> max(nums)
77
>>> sum(nums)
215
>>> nums.sort()
>>> nums
[23, 25, 34, 56, 77]
>>> 