Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> #DAY12
>>> myorder="Please, I want {} sandwishes and {} donutes"
>>> a=5
>>> b=7
>>> print(myorder.replace("I","we"))
Please, we want {} sandwishes and {} donutes
>>> 
>>> print(myorder.format(a,b))
Please, I want 5 sandwishes and 7 donutes
>>> print(myorder.upper("a"))
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(myorder.upper("a"))
TypeError: upper() takes no arguments (1 given)
>>> print(myorder.replace("a","A"))
PleAse, I wAnt {} sAndwishes And {} donutes
>>> print(myorder.replace("I","we").format(a,b).replace("a","A"))
PleAse, we wAnt 5 sAndwishes And 7 donutes
>>> 
