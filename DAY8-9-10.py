Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #DAY8
>>> a="Hello , World!"
>>> print(a.strip())
Hello , World!
>>> a="Hello , World!"
>>> print(len(a))
14
>>> a="Hello , World!"
>>> print(a.lower())
hello , world!
>>> a="Hello , World!"
>>> print(a.upper())
HELLO , WORLD!
>>> a="Hello , World!"
>>> print(a.replace("H","J"))
Jello , World!
>>> a="Hello , World!"
>>> print(a.split(","))
['Hello ', ' World!']
>>> 
>>> #DAY9
>>> age=36
>>> txt="My name is john, I am "+age
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    txt="My name is john, I am "+age
TypeError: can only concatenate str (not "int") to str
>>> txt="My name is john, I am "+ age
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    txt="My name is john, I am "+ age
TypeError: can only concatenate str (not "int") to str
>>> txt="My name is john, I am " + age
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    txt="My name is john, I am " + age
TypeError: can only concatenate str (not "int") to str
>>> 
>>> 
>>> 
>>> 
>>> txt="My name is john, I am {}"
>>> print(txt.format(age))
My name is john, I am 36
>>> 
>>> quntity=3
>>> itemno=567
>>> price="I want {} pieces of item {} for {} dollars."
>>> print(myorder.format(quantity,itemno,price))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(myorder.format(quantity,itemno,price))
NameError: name 'myorder' is not defined
>>> price=49.95
>>> myorder="I want {} pieces of item {} for {} dollars."
>>> print(myorder.format(quantity,itemno,price))
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    print(myorder.format(quantity,itemno,price))
NameError: name 'quantity' is not defined
>>> 
>>> quantity=3
>>> itemno=567
>>> price=49.95
>>> myorder="I want {} pieces of item {} for {} dollars."
>>> print(myorder.format(quantity,itemno,price))
I want 3 pieces of item 567 for 49.95 dollars.
>>> 
KeyboardInterrupt
>>> myorder="I want to pay {2} dollars for {0} pices of item{1}."
>>> print(myorder.format(quantity,itemno,price))
I want to pay 49.95 dollars for 3 pices of item567.
>>> 
>>> 
>>> DAY10
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    DAY10
NameError: name 'DAY10' is not defined
>>> #DAY10
>>> 
>>> #DAY10
>>> 
>>> x=5
>>> y=3
>>> print(x*y)
15
>>> x=5
>>> x/=3
>>> print(x)
1.6666666666666667
>>> y=3
>>> y/=1
>>> print(y)
3.0
>>> x=20
>>> x/=2
>>> print(x)
10.0
>>> 
>>> 
>>> x=5
>>> y=3
>>> print(x<y)
False
>>> 
>>> x=5
>>> y=3
>>> print(x>y)
True
>>> print(x!=y)
True
>>> print(x=y)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    print(x=y)
TypeError: 'x' is an invalid keyword argument for print()
>>> print(x==y)
False
>>> 
