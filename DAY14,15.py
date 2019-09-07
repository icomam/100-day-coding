Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> thislist=["A","B","C","D","E"]
>>> print(thislist[1:3])
['B', 'C']
>>> if "A" in thislist:
	print("Yes,A is in the list")

	
Yes,A is in the list
>>> 
>>> thislist=["بايثون"]*4
>>> print(thislist)
['بايثون', 'بايثون', 'بايثون', 'بايثون']
>>> 
>>> list1=["Ahmed","Khalid","Omar"]
>>> list2=["Sara","Hind","Batool"]
>>> list3=list1+list2
>>> print(list3)
['Ahmed', 'Khalid', 'Omar', 'Sara', 'Hind', 'Batool']
>>> 
>>> thislist=["A","B","C","D","E"]
>>> 
>>> #DAY15
>>> 
>>> list=["apple","banana","cherry"]
>>> print(len(list))
3
>>> 
>>> list.append("Orange")
>>> print(list)
['apple', 'banana', 'cherry', 'Orange']
>>> 
>>> list.insert(1,"Orange")
>>> print(list)
['apple', 'Orange', 'banana', 'cherry', 'Orange']
>>> 
>>> list.remove("Orange")
>>> print(list)
['apple', 'banana', 'cherry', 'Orange']
>>> 
>>> list.pop()
'Orange'
>>> 
>>> list.pop()
'cherry'
>>> print(list)
['apple', 'banana']
>>> 
>>> print(list)
['apple', 'banana']
>>> 
>>> list.clear()
>>> print(list)
[]
>>> print(thislist1)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    print(thislist1)
NameError: name 'thislist1' is not defined
>>> print(list1)
['Ahmed', 'Khalid', 'Omar']
>>> list1.clear()
>>> print(list1)
[]
>>> list1=["apple","banana","cherry"]
>>> mylist=list1.copy()
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> list1.pop(0)
'apple'
>>> print(mylist)
['apple', 'banana', 'cherry']
>>> print(list1)
['banana', 'cherry']
>>> mylist=list1
>>> list1.pop(0)
'banana'
>>> print(mylist)
['cherry']
>>> print(list1)
['cherry']
>>> 
>>> list1.insert(1,"orange")
>>> print(list1)
['cherry', 'orange']
>>> mylist=list(list1)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    mylist=list(list1)
TypeError: 'list' object is not callable
>>> print(list1)
['cherry', 'orange']
>>> print(mylist)
['cherry', 'orange']
>>> mylist=list(list1)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    mylist=list(list1)
TypeError: 'list' object is not callable
>>> 
>>> list1=list(("apple","banana","orange"))
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    list1=list(("apple","banana","orange"))
TypeError: 'list' object is not callable
>>> print(list)
[]
>>> list.delete()
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    list.delete()
AttributeError: 'list' object has no attribute 'delete'
>>> 
