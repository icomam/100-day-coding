Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Day 21
>>> 
>>> set1={"apple","banana","orange"}
>>> print(set1)
{'apple', 'banana', 'orange'}
>>> 
>>> print(len(set1))
3
>>> 
>>> set1.remove("banana")
>>> print(set1)
{'apple', 'orange'}
>>> 
>>> set1.discard("banana")
>>> 
>>> print("set1")
set1
>>> 
>>> print(set1)
{'apple', 'orange'}
>>> 
>>> set1.discard("apple")
>>> 
>>> print(set1)
{'orange'}
>>> 
>>> x=set1.pop()
>>> print(x)
orange
>>> 
>>> print(set1)
set()
>>> 
>>> print(set1)
set()
>>> x=set1.pop()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x=set1.pop()
KeyError: 'pop from an empty set'
>>> del set1
>>> 
>>> print(set1)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(set1)
NameError: name 'set1' is not defined
>>> 
>>> 
>>> set2=set(("apple","banana","cherry"))
>>> print(set2)
{'apple', 'banana', 'cherry'}
>>> 
>>> 
>>> #DAY22
>>> 
>>> Dic1={"brand":"ford","model":"mustang","year":1964}
>>> print(Dic1)
{'brand': 'ford', 'model': 'mustang', 'year': 1964}
>>> 
>>> x=Dic1["model"]
>>> print(x)
mustang
>>> x=Dic1["brand"]
>>> print(x)
ford
>>> 
>>> x=Dic1.get("model")
>>> print(x)
mustang
>>> 
>>> Dic1["year"]=2018
>>> print(Dic1)
{'brand': 'ford', 'model': 'mustang', 'year': 2018}
>>> for x in Dic1:
	print(x)

	
brand
model
year
>>> 
>>> for x in Dic1:
	print(Dic[x])

	
Traceback (most recent call last):
  File "<pyshell#57>", line 2, in <module>
    print(Dic[x])
NameError: name 'Dic' is not defined
>>> for x in Dic1:
	print(Dic1[x])

	
ford
mustang
2018
>>> 
>>> for x in Dic1.values():
	print(x)

	
ford
mustang
2018
>>> 
>>> print(Dic1.values())
dict_values(['ford', 'mustang', 2018])
>>> 
>>> 
>>> for x in Dic1.items():
	print(x,y)

	
Traceback (most recent call last):
  File "<pyshell#71>", line 2, in <module>
    print(x,y)
NameError: name 'y' is not defined
>>> 
>>> 
>>> for x,y in Dic1.items():
	print(x,y)

	
brand ford
model mustang
year 2018
>>> 
>>> 
>>> for x,y in Dic1.items():
	print (x,y)

	
brand ford
model mustang
year 2018
>>> 
