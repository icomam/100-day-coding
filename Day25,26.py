Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Day25,Day26
>>> 
>>> thisset1={1,3,5,7,8}
>>> print(thisset1)
{1, 3, 5, 7, 8}
>>> thisset1.update(4,8,12)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    thisset1.update(4,8,12)
TypeError: 'int' object is not iterable
>>> thisset1.update([4,8,12])
>>> print(thisset1)
{1, 3, 4, 5, 7, 8, 12}
>>> 
>>> thisset1.remove(8)
>>> print(thisset1)
{1, 3, 4, 5, 7, 12}
>>> 
>>> thisset1.clear()
>>> print(thisset1)
set()
>>> 
>>> #ثانيا
>>> 
>>> thisdict=dict(name="pigeon",type="bird",skin cover="feathers")
SyntaxError: invalid syntax
>>> thisdict=dict(name="pigeon",type="bird",skincover="feathers")
>>> print(thisdict)
{'name': 'pigeon', 'type': 'bird', 'skincover': 'feathers'}
>>> 
>>> x=thisdic["type"]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    x=thisdic["type"]
NameError: name 'thisdic' is not defined
>>> 
>>> 
>>> x=thisdict[type]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    x=thisdict[type]
KeyError: <class 'type'>
>>> 
>>> x=thisdict["type"]
>>> print(x)
bird
>>> 
>>> thisdict["skincover"]="fur"
>>> 
>>> print(thisdict)
{'name': 'pigeon', 'type': 'bird', 'skincover': 'fur'}
>>> 
>>> 
