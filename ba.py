# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
class account(object):
    def __init__(self,name,email,num,addr):
        '''
        function to assign the account name,email,num,addr
        '''
        self.name=name
        self.email=email
        self.num=num
        self.addr=addr
    def get_name(self):
        return self.name
    def get_email(self):
        return self.email
    def get_num(self):
        return self.num
    def get_addr(self):
        return self.addr
def add_account():
    name=str(input("Enter the name of the student:")) 
    email=str(input("Enter the E-Mail ID of the student: "))
    addre=str(input("Enter the address of the student: "))
    while True:    
        number=str(input("Enter Phone Number of student: "))
        if(len(number)==10):
            break
        else:
            print("Please enter a valid Phone Number.") 
    s=account(name,email,number,addre)
    return s
def writeaccount(s):
    fw=open('studlist.txt','a')
    writelist=str(s.get_name()+'$$'+s.get_email()+'$$'+s.get_num()+'$$'+s.get_addr()+'\n')
    fw.write(writelist)
    fw.close()
def readaccount():
     fr=open('studlist.txt','r')
     a=[]
     for line in fr:
         x=line.split('$$')
         a.append(account(x[0],x[1],x[2],x[3]))
     fr.close()
     return a
def searchaccount(name):
    '''
    Function to search for student in the file and return the details of the student.
    Arguments: reg_no of type string.
    Return: s of type Student.
    '''
    studlist=readaccount()
    for i in studlist:
        if(i.get_name()==name):
            return i
def modifyaccount(name):
    '''
    Function to Modify list of students, given the registration number.
    Arguments: reg_no of type string.
    Return: None
    '''
    studlist=readaccount()
    fw=open('studlist1.txt','a')
    for i in studlist:
        if(i.get_name()==name):
            s=add_account()
            writelist=str(s.getname()+'$$'+s.get_email()+'$$'+s.get_num()+'$$'+s.get_addr()+'\n')
            fw.write(writelist)
        else:
            writelist=str(i.getname()+'$$'+i.get_email()+'$$'+i.get_num()+'$$'+i.get_addr())
            fw.write(writelist)           
    fw.close()
    os.remove('studlist.txt')
    os.rename('studlist1.txt','studlist.txt')
def deleteStudent(name):
    '''
    Function to delete a student, given the registration number.
    Arguments: reg_no of type string.
    Return: None
    '''
    studlist=readaccount()
    fw=open('studlist1.txt','a')
    for i in studlist:
        if(i.get_name()==name):
            continue
        else:
            writelist=str(i.getname()+'$$'+'$$'+i.get_email()+'$$'+i.get_num()+'$$'+i.get_addr())
            fw.write(writelist)           
    fw.close()
    os.remove('studlist.txt')
    os.rename('studlist1.txt','studlist.txt')
def menu():
    while True:
        os.system('clear')
        print("Main Menu".center(40))
        print("1.addaccount")
        print("2.viewaccount detail")
        print("3.modifyaccountdetailed")
        print("4.delete account")
        print("5.exit")
        ch=int(input("Enter your choice: " ))
        if(ch in range(1,6)):
            break
        else:
            print("Please Enter a valid choice!")
            input("Press <Enter> to return back to the menu.")
    if(ch==1):
        os.system('clear')
        print("Add a Student Member".center(40))
        s=add_account()
        writeaccount(s)
        print("Student Member Successfully added!")
        input("Press <Enter> to return back to the menu.")
        menu()
menu()
