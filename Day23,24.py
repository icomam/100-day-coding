Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Day 23
>>> thisdict={"brand":"ford",
	  "model":"Mustang",
	  "yesr":1964
	  }
>>> if"model"in thisdict:
	print("Yes,'model is one of the key in thisdict'")

	
Yes,'model is one of the key in thisdict'
>>> 
>>> print(len(thisdict))
3
>>> 
>>> thisdict["color"]="red"
>>> print(thisdict)
{'brand': 'ford', 'model': 'Mustang', 'yesr': 1964, 'color': 'red'}
>>> 
>>> thisdict.pop("color")
'red'
>>> print(thisdict)
{'brand': 'ford', 'model': 'Mustang', 'yesr': 1964}
>>> 
>>> thisdict.popitem()
('yesr', 1964)
>>> print(thisdict)
{'brand': 'ford', 'model': 'Mustang'}
>>> 
>>> del thisdict["model"]
>>> print(thisdict)
{'brand': 'ford'}
>>> 
>>> del thisdict
>>> print (thisdict)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print (thisdict)
NameError: name 'thisdict' is not defined
>>> 
>>> 
>>> #DAY24
>>> 
>>> thisdict={"brand":"ford",
	  "model":"Mustang",
	  "year":1964
	  }
>>> mydict=thisdict.copy()
>>> print(mydict)
{'brand': 'ford', 'model': 'Mustang', 'year': 1964}
>>> 
>>> mydict2=dict (thisdict)
>>> print(mydict2)
{'brand': 'ford', 'model': 'Mustang', 'year': 1964}
>>> 
>>> myfamily={
	"child1":{
		"name":"Emil",
		"yeay":"2004"},
	"child2":{
		"name":"Tobias",
		"year":2007
		},
	"child3":{
		"name":"Linus",
		"year":2011
		}
	}
>>> print(myfamily)
{'child1': {'name': 'Emil', 'yeay': '2004'}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}
>>> 
>>> 
>>> thisdict2=dict(brand="ford",model="mustang",year=1964)
>>> print(thisdict2)
{'brand': 'ford', 'model': 'mustang', 'year': 1964}
>>> 
