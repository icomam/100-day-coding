Python 3.7.4 (tags/v3.7.4:e09359112e, Jul  8 2019, 19:29:22) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> x="apple",y="Orange",z="limon"
SyntaxError: can't assign to literal
>>> x= "apple"
>>> y="orange"
>>> z="limon"
>>> basket=x+y+z
>>> 
>>> print(basket)
appleorangelimon
>>> x= " apple  " , y="orange" , z= " limon"
SyntaxError: can't assign to literal
>>> x="apple" , y="orange" , z= " limon"
SyntaxError: can't assign to literal
>>> x="apple  "
>>> y="orange  "
>>> z="limon"
>>> basket=x+y+z
>>> print(basket)
apple  orange  limon
>>> 
