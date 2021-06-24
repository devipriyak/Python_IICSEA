#function with default values
def test(name="AEC",Rollno="501"):
      print "Hello "+name,Rollno
#Read name from the user
input_name=raw_input("Enter branch Name")
#call function
test(input_name,"502")
#call function
test("CSE-A")#No RollNumber
#call function
test()#call function without any parameter
#The above function is executed because the name argument
#takes the default value as AEC

'''
Enter branch NameIT
Hello IT 502
Hello CSE-A 501
Hello AEC 501
'''




'''TypeError: test() takes exactly 1 argument (0 given)'''
'''
if the user does not provide required values to function
arguments then 
Is there any possibility to consider defalut values?
'''
