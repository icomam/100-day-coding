Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> x=1
>>> y=2.8
>>> z=1j
>>> print(x)
1
>>> print(y)
2.8
>>> print(z)
1j
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'complex'>
>>> 
>>> 
>>> x=35e3
>>> print(type(x))
<class 'float'>
>>> 
>>> x=5
>>> y=2.1
>>> z=h2
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    z=h2
NameError: name 'h2' is not defined
>>> 
>>> x=2
>>> y=1
>>> z=2h
SyntaxError: invalid syntax
>>> z=1j
>>> z=2t
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> 
>>> x=2
>>> y=1
>>> z=1j
>>> 
>>> a=float(x)
>>> b=int(z)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    b=int(z)
TypeError: can't convert complex to int
>>> b=init(y)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    b=init(y)
NameError: name 'init' is not defined
>>> 
>>> 
>>> 
>>> a=float(x)
>>> b=int(y)
>>> c=complex(x)
>>> print(x)
2
>>> print(a)
2.0
>>> print(b)
1
>>> print(c)
(2+0j)
>>> 
>>> print(type(a))
<class 'float'>
>>> 
>>> import random
>>> print(random.randrange(1,10))
1
>>> 
>>> 
KeyboardInterrupt
>>> print(random.randrange(1,10))
8
>>> print(random.randrange(1,10))
3
>>> print(random.randrange(1,10))
8
>>> print(random.randrange(1,10))
7
>>> print(random.randrange(1,10))
8
>>> print(random.randrange(1,10))
7
>>> 
