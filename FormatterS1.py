#String Formatting Operators
#1.Formatting Operators
#2{}
#3.Template String

'''
%s-Formatting String Value
%d-Integer
%f-Float
%o-OCtal
%x(Hex value for lower case)
%X(Hex value for Upper Case Letters)
%c-Character
'''
name="CSE-A"
print("Hello %s !How are you?" %(name))
#'C' Language ...printf("Hello %s !How are you",name)
age=19
print("Age is %d" %(age))
#Combining the %s and %d formatters
#Hello CSE-A!Your age is 19!
print("Hello %s !Your Age is %d"%(name,age))
percentage=8.9

print("Hello %s !Your Age is %d and grade value is %f"
            %(name,age,percentage))

print("Hello %s ! grade value is %.2f"%(name,percentage))
#Formatting of X Hex
a=15
print ("No is %X"%(a))











'''

# This prints out "Hello, Priya!"
name = "Priya"
print("Hello, %s!" % (name))
age=12 
print("Hello, %d!" % (age))
#Name &age

print("Hello, %s! and age is %d " % (name,age))
'''
