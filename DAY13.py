Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> S=[]
>>> print(S)
[]
>>> numbers=[1,2,3,4,5]
>>> print(numbers)
[1, 2, 3, 4, 5]
>>> thislist=["apple","banana","cherry"]
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> thislist=["apple","banana","cherry",1,2,3]
>>> print(thislist)
['apple', 'banana', 'cherry', 1, 2, 3]
>>> 
>>> thislist=[1,2 , 3,0 , 4,3 , 2,1]
>>> print(thislist)
[1, 2, 3, 0, 4, 3, 2, 1]
>>> [1, 2, 3, 0, 4, 3, 2, 1]
[1, 2, 3, 0, 4, 3, 2, 1]
>>> 
>>> thislist=[1.2 , 3.5 ,1.5, 2.4]
>>> print
<built-in function print>
(
>>> print(thislist)
[1.2, 3.5, 1.5, 2.4]
>>> thislist=[1.2 , 3.5 ,1.5, 2.4]
>>> print(thislist)
[1.2, 3.5, 1.5, 2.4]
>>> 
>>> 
>>> thislist=["apple","banana","cherry"]
>>> print(thislist[1])
banana
>>> print(thislist[0])
apple
>>> print(thislist[-1])
cherry
>>> print(thislist[-2])
banana
>>> 
>>> 
>>> thislist=["apple","banana","cherry"]
>>> for x in thiislist:
	print(x)

	
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    for x in thiislist:
NameError: name 'thiislist' is not defined
>>> for x in thislist:
	print(x)

	
apple
banana
cherry
>>> 
>>> numbers=[1.5,22,4,5,3.7,9]
>>> for n in numbers
SyntaxError: invalid syntax
>>> for n in number:
	print(n)

	
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    for n in number:
NameError: name 'number' is not defined
>>> 
>>> numbers=[1.5,22,4,5,3.7,9]
>>> for n in numbers:
	print(n)

	
1.5
22
4
5
3.7
9
>>> 
>>> print(thislist)
['apple', 'banana', 'cherry']
>>> 
>>> thislist[1]="blackcurrant"
>>> print(thislist)
['apple', 'blackcurrant', 'cherry']
>>> 
>>> thislist[-1]="Orange"
>>> print(thislist)
['apple', 'blackcurrant', 'Orange']
>>> 
>>> print(thislist)
['apple', 'blackcurrant', 'Orange']
>>> del thislist[0]
>>> print(thislist)
['blackcurrant', 'Orange']
>>> 
>>> del thislist
>>> print(thislist)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    print(thislist)
NameError: name 'thislist' is not defined
>>> 
>>> 
>>> 
