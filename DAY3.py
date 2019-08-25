Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x=5
>>> y="john"
>>> print(x)
5
>>> print(y)
john
>>> print(x) print(y)
SyntaxError: invalid syntax
>>> print(x , y)
5 john
>>> 
>>> x=4
>>> x="Sally"
>>> print(x)
Sally
>>> 
>>> x,y,z="Orange","Banana","Cherry"
>>> print(x)
Orange
>>> print(y)
Banana
>>> print(z)
Cherry
>>> 
>>> x=y=z="Apple"
>>> print(x)
Apple
>>> print(y)
Apple
>>> print(z)
Apple
>>> 
>>> x="great"
>>> print("python is "+ x)
python is great
>>> 
>>> x="python is"
>>> y="great"
>>> print(x+y)
python isgreat
>>> 
>>> 
>>> x=5
>>> y=10
>>> print(x+y)
15
>>> x=5
>>> y="john"
>>> print(x+y)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    print(x+y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> 
