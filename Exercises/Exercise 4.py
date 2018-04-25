# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 14:56:08 2018

@author: Udvardy
"""

"""Exercise 4"""

print("This is exercise 4, please follow the instructions\n")
num=int(input("Gimme a umber that I will give you the divisors: "))
mylist=range(1,num+1);
mylist2=[];
remainder=0;
for i in mylist:
    remainder=num%i;
    if remainder ==0:
        mylist2.append(i);
print ("The divisors are: " + str(mylist2))
        