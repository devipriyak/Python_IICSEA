#Defintion of function
def test():
      print("test()")
      print "I am Function"
      print "Hello"
#Call to test()
test()#function call

#Function with single parameter
def show(x):
      print "show()"
      print x
      print(type(x))

#call the show()    
show("Python")#show funtion with string value
show(10)#show function with interger value
show(10.990909)#show() with float value
set1={123,457,5678}
#show() with set ds
show(set1)
list1=["Python","FLAT","CO","DAA","IOT"]
#show() with list ds
show(list1)
dict1={05:"cse",12:"IT",03:"ECE"}
#show() with dictionary ds
show(dict1)
#tuple
tuple1=(10.4,10.5,340.45)
show(tuple1)
'''
test()
I am Function
Hello
show()
Python
<type 'str'>
show()
10
<type 'int'>
show()
10.990909
<type 'float'>
show()
set([457, 123, 5678])
<type 'set'>
show()
['Python', 'FLAT', 'CO', 'DAA', 'IOT']
<type 'list'>
show()
{3: 'ECE', 12: 'IT', 5: 'cse'}
<type 'dict'>

'''
