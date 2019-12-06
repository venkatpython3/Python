#!/usr/bin/env python
# coding: utf-8

# Task 1:
# #Question 1:
# Install Jupyter notebook and run the first program and share the screenshot of the output.
# 

# In[1]:


print("Hello world. welcome to Python")


# #Question 2:
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple
# of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a
# comma-separated sequence on a single line.
# 

# In[2]:


s=[]
for i in range(2000,3201):
    if i%7==0:
        if i%5!=0:
            s.append(i)
print(s)


# #Question 3:
# Write a Python program to accept the user's first and last name and then getting them printed in
# the the reverse order with a space between first name and last name.
# 

# In[3]:


firstname=input("please enter your first name")
lastname=input("Please enter your lastname")
print(firstname[::-1]+' '+lastname[::-1])


# #Question 4
# Write a Python program to find the volume of a sphere with diameter 12 cm.
# Formula: V=4/3 * π * r
# 3

# In[4]:


r=12
v=(4/3)*(22/7)*r**3
print(v)


# TASK 2:
# 
# 1.Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list.
# 

# In[6]:


numbers=input("Please enter comma seperated numbers to generate list")
s=[]
for i in numbers:
    if i==',':
        continue
    else:
        s.append(i)
print(s)


# 2.Create the below pattern using nested for loop in Python.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# In[7]:


symbol=int(input("please enter the number to print symbol"))
i=0
while i<=symbol:
    print(i*'*')
    i+=1
for i in range(symbol-1,0,-1):
    print(i*'*')


# 3.Write a Python program to reverse a word after accepting the input from the user

# In[9]:


reverse=input("Please enter the word to reverse")
reverse[::-1]


# 4.
# Write a Python Program to print the given string in the format specified in the sample output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a
# SOVEREIGN, SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all
# its citizens

# In[13]:


print("WE, THE PEOPLE OF INDIA\n\thaving solemnly resolved to constitute India into a SOVEREIGN,"+"!"+"\n\t\tSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC\n\t\tand to secure to all its citizens")


# In[ ]:




