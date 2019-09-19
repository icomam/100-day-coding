Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> List=[1,2,3,4]
>>> print(List)
[1, 2, 3, 4]
>>> 
>>> List.pop(3)
4
>>> print(List)
[1, 2, 3]
>>> 
>>> List.insert("A",22)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    List.insert("A",22)
TypeError: 'str' object cannot be interpreted as an integer
>>> List.insert(22,100)
>>> print(List)
[1, 2, 3, 100]
>>> 
>>> List.insert(22,33)
>>> print(List)
[1, 2, 3, 100, 33]
>>> 
>>> List.remove(1)
>>> print(List)
[2, 3, 100, 33]
>>> 
>>> List.count(3)
1
>>> print(List)
[2, 3, 100, 33]
>>> 
>>> tuple=("java","python","swift")
>>> print(tuple)
('java', 'python', 'swift')
>>> 
>>> tuple.index(1)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    tuple.index(1)
ValueError: tuple.index(x): x not in tuple
>>> 
>>> print(tuple)
('java', 'python', 'swift')
>>> 
>>> if "python" in List:
	print("Yes , 'python'in the list")

	
>>> 
>>> 
>>> if "python" in tuple:
	print("Yes'python' in the tuple")

	
Yes'python' in the tuple
>>> 
>>> 
