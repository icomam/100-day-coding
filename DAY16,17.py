Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #DAY 16
>>> 
>>> thistuple=("apple","banana","cherry")
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> 
>>> thistuple=()
>>> print(thistuple)
()
>>> thistuple=(3,)
>>> print(thistuple)
(3,)
>>> thistuple=(3, 1.3, 4.1, 7)
>>> print(thistuple)
(3, 1.3, 4.1, 7)
>>> 
>>> thistuple=("Ahmed", 1.1 , 4 , "بايثون")
>>> print(thistuple)
('Ahmed', 1.1, 4, 'بايثون')
>>> 
>>> print(thistuple[1])
1.1
>>> 
>>> thistuple=("apple","banana","cherry")
>>> for x in thistuple:
	print(x)

	
apple
banana
cherry
>>> 
>>> for x in thistuple:
	print(x[1])

	
p
a
h
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> thistuple[3]="orange"
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    thistuple[3]="orange"
TypeError: 'tuple' object does not support item assignment
>>> thistuple=("apple","banana","cherry")
>>> thistuple[3]="orange"
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    thistuple[3]="orange"
TypeError: 'tuple' object does not support item assignment
>>> 
>>> del thistuple
>>> print(thistuple)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    print(thistuple)
NameError: name 'thistuple' is not defined
>>> 
>>> 
>>> thistuple=("apple","banana","cherry","orange")
>>> print(thistuple[0:3])
('apple', 'banana', 'cherry')
>>> 
>>> 
>>> 
>>> #DAY 17
>>> 
>>> if "apple"in thistuple:
	print("Yes, 'apple' is in the fruite tuple")

	
Yes, 'apple' is in the fruite tuple
>>> 
>>> 
>>> thistuple("بايثون",)*3
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    thistuple("بايثون",)*3
TypeError: 'tuple' object is not callable
>>> thistuple=("بايثون",)*3
>>> print(thistuple)
('بايثون', 'بايثون', 'بايثون')
>>> 
>>> 
>>> tuple2=(1 ,2 ,3 ,4)
>>> tuple1=(5 , 6)
>>> thistuple3=tuple1+tuple2
>>> print(thistuple3)
(5, 6, 1, 2, 3, 4)
>>> 
>>> x=(3,4,5,6)
>>> x=x+(1,2,3)
>>> print(x)
(3, 4, 5, 6, 1, 2, 3)
>>> 
>>> print(len(tuple2))
4
>>> print(len(tuple2))
4
>>> print(len(thistuple3))
6
>>> thistuple=tuple(("apple","banana","cherry"))
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> 
>>> thielist=[3, 4, 5 , 6 ,"A" ,"B"]
>>> thistuple=tuple(thislist)
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    thistuple=tuple(thislist)
NameError: name 'thislist' is not defined
>>> print(thistuple)
('apple', 'banana', 'cherry')
>>> thislist=[3, 4, 5 , 6 ,"A" ,"B"]
>>> thistuple=tuple(thislist)
>>> print(thistuple)
(3, 4, 5, 6, 'A', 'B')
>>> 
>>> print(count(thistuple))
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    print(count(thistuple))
NameError: name 'count' is not defined
>>> print(count(thistuple))
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    print(count(thistuple))
NameError: name 'count' is not defined
>>> print(index(thistuple))
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    print(index(thistuple))
NameError: name 'index' is not defined
>>> print(index()thistuple)
SyntaxError: invalid syntax
>>> 
>>> print(thistuple.index())
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    print(thistuple.index())
TypeError: index() takes at least 1 argument (0 given)
>>> print(index().thistuple)
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    print(index().thistuple)
NameError: name 'index' is not defined
>>> 
>>> thislist= index((3, 4, 5 , 6 ,"A" ,"B"))
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    thislist= index((3, 4, 5 , 6 ,"A" ,"B"))
NameError: name 'index' is not defined
>>> 
