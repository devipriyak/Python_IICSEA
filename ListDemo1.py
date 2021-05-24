#Create a list of branches offered by college
branch_names=["CSE","IT","ECE","MECH","AGRI"]
#Print
print(branch_names)#All Items are printed
#Access list of elements through the index
print(branch_names[1])#IT
print(branch_names[4])#AGRI
#<type 'list'>
print("Data Type of Branch is",type(branch_names))
#List with Different Datatypes
colleges=[1,"AEC","JTNUK","IIT",2,3,"KKD",8.8,"SURAMPALEM","KAR"]
print(colleges)
#Data type of Colleges-<type 'list'>
print("Data Type of College is",type(colleges))
#Modifing List-YES
branch_names[3]="PT"
print(branch_names)#['CSE', 'IT', 'ECE', 'PT', 'AGRI']
#Access List- Element by Element using for Loop
for i in branch_names:# i-->CSE,i-->IT,i-->ECE,i-->PT,i-->AGRI
      print(i)
'''
CSE
IT
ECE
PT
AGRI
'''








