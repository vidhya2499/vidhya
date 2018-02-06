Python 3.6.3 (default, Oct  3 2017, 21:45:48) 
[GCC 7.2.0] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a=100
>>> type(a)
<class 'int'>
>>> a="hello"
>>> type(a)
<class 'str'>
>>> a="python"
>>> a[0]
'p'
>>> a[0:6]
'python'
>>> a[4]
'o'
>>> a[4][5]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    a[4][5]
IndexError: string index out of range
>>> l=[0,2,16,13]
>>> l[3]
13
>>> l[3][0]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    l[3][0]
TypeError: 'int' object is not subscriptable
>>> l=[0,2,3,"python",4,5,6]
>>> l[3][2]
't'
>>> l=[23,34,56,"vidhya","chiru","pooja"]
>>> l[3][4]
'y'
>>> l=[23,34,56,"vidhya","chiru","pooja"]
>>> l[4][0]
'c'
>>> l=[23,34,56,"vidhya","chiru","pooja"]
>>> l[3][0]
'v'
>>> l=["vidhya","chiru"]
>>> l=[0][3]
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    l=[0][3]
IndexError: list index out of range
>>> l=["vidhya","chiru"]
>>> l[1][2]
'i'
>>> l=[243,"vidhya","chiru"]
>>> l[1][3]
'h'
>>> complex(10,20)
(10+20j)
>>> complex(24,3)
(24+3j)
>>> complex(3,243)
(3+243j)
>>> l=[243,"vidhya","chiru"]
>>> l[1]="chiru"
>>> l[2]=vidhya
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    l[2]=vidhya
NameError: name 'vidhya' is not defined
>>> l=[243,"vidhya","chiru"]
>>> l[0]=12
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 


>>> 


>>> 

>>> 

>>> 


>>> 
>>> 


>>> 

>>> 


>>> 
>>> 


>>> l=[243,"vidhya","chiru"]
>>> l[1]="anju"
>>> T=(1,2,3,4,5,6)
>>> T[1]
2
>>> T=("ANJU","VIDHYA","CHIRU")
>>> T[2]
'CHIRU'
>>> T[1]
'VIDHYA'
>>> T[0]
'ANJU'
>>> T[2][1]
'H'
>>> T[1][2]
'D'
>>> T[1][3]
'H'
>>> T[2][1]
'H'
>>> T[2]
'CHIRU'
>>> T[1]
'VIDHYA'
>>> T[0]
'ANJU'
>>> T[0:3]
('ANJU', 'VIDHYA', 'CHIRU')
>>> T[0;3]
SyntaxError: invalid syntax
>>> T[0:3]
('ANJU', 'VIDHYA', 'CHIRU')
>>> T[2]="ANJU"
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    T[2]="ANJU"
TypeError: 'tuple' object does not support item assignment
>>> D={"VIDHYA":"CHIRU","ANJU":"VIJAY":10:20}
SyntaxError: invalid syntax
>>> D={"VIDHYA":"CHIRU","ANJU":"VIJAY":10,20}
SyntaxError: invalid syntax
>>>  D={"VIDHYA":"CHIRU","ANJU":"VIJAY",10:20}
 
SyntaxError: unexpected indent
>>> D={"VIDHYA":"CHIRU","ANJU":"VIJAY",10:20}
>>> D["VIDHYA"]
'CHIRU'
>>> D.KEYS()
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    D.KEYS()
AttributeError: 'dict' object has no attribute 'KEYS'
>>> D.keys()
dict_keys(['VIDHYA', 'ANJU', 10])
>>> D.values()
dict_values(['CHIRU', 'VIJAY', 20])
>>> S={1,2,3,4,"VIDHYA","CHIRU"}
>>> S1={5,6,7,3,2,"ANJU"}
>>> S+S1
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    S+S1
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> S&S1
{2, 3}
>>> S/S1
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    S/S1
TypeError: unsupported operand type(s) for /: 'set' and 'set'
>>> S|S1
{1, 2, 3, 4, 5, 6, 7, 'ANJU', 'VIDHYA', 'CHIRU'}
>>> S^S1
{1, 4, 5, 6, 7, 'ANJU', 'CHIRU', 'VIDHYA'}
>>> S-S1
{1, 4, 'VIDHYA', 'CHIRU'}
>>> S*S1
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    S*S1
TypeError: unsupported operand type(s) for *: 'set' and 'set'
>>> S+S1
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    S+S1
TypeError: unsupported operand type(s) for +: 'set' and 'set'
>>> 2<<2
8
>>> 1<<4
16
>>> 65>>59
0
>>> 65>>65
0
>>> 66>>43
0
>>> 12>>4
0
>>> 2>>2
0
>>> 1>>2
0
>>> 0>>0
0
>>> ^TRUE
SyntaxError: invalid syntax
>>> TRUE
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    TRUE
NameError: name 'TRUE' is not defined
>>> true
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    true
NameError: name 'true' is not defined
>>> 2==2
True
>>> 2!=2 or 2==2
True
>>> 2!=2 and 2==2
False
>>> 2!=2
False
>>> 
=============== RESTART: /home/cs2017b105/vidhya/program23.py ===============
1
2
3
4
>>> 
=============== RESTART: /home/cs2017b105/vidhya/program23.py ===============
vidhya
chiru
pooja
aishu
rangu
>>> 2=2
