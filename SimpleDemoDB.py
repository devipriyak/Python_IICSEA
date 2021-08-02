#step1
import sqlite3#import 
#step2
con = sqlite3.connect('D:\\cseAA.db')#connect() returns the connection on
     
print "connection object is created successfully"

#step3-create cursor Object-cursor() method is available with Connection object
cursorObj = con.cursor()
print "Cursor Object created successfully"
#Execute queries-execute()---on cursor
cursorObj.execute("CREATE table movies(mname text, rating integer)")

print "Movie Table Created succssfully"

'''
connection object is created successfully
Cursor Object created successfully
Movie Table Created succssfully
'''


