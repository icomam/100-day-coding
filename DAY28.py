Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #DAY 28
>>> 
>>> i=1
>>> while i<6
SyntaxError: invalid syntax
>>> while i<6:
	print(i)
	i+=1

	
1
2
3
4
5
>>> 
>>> i=1
>>> while i<6:
	print(i)
	if i==3:
		break
	i+=1

	
1
2
3
>>> 
>>> i=3
>>> while i<6:
	print(i)
	if i==3:
		break
	i+=1

	
3
>>> 
>>> i=0
>>> whilr i<6:
	
SyntaxError: invalid syntax
>>> 
>>> i=0
>>> while i<6:
	i+=1
	if i==3:
		continue
	print(i)

	
1
2
4
5
6
>>> 
>>> i=1
>>> while i<6:
	print(i)
	i+=1
	else:
		
SyntaxError: invalid syntax
>>> p
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    p
NameError: name 'p' is not defined

>>> 
>>> i=1
>>> while i<6:
	prin(i)
	i +=1
else:
	print("i is no longer less than 6")

	
Traceback (most recent call last):
  File "<pyshell#49>", line 2, in <module>
    prin(i)
NameError: name 'prin' is not defined
>>> 
>>> 
>>> i=1
>>> while i<6:
	print(i)
	i+=1
else:
	print("i is no longer less than 6")

	
1
2
3
4
5
i is no longer less than 6
>>> 
>>> 
>>> 
>>> 
>>> i=10
>>> while i<6:
	print(i)
	i+=1
else:
	print("i is no longer less than 6")

	
i is no longer less than 6
>>> 
