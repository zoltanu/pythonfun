# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 17:00:46 2018

@author: Udvardy
"""

"""Exercise 5"""
import random
print("This is exercise 5, please follow the instructions.\n")

"""a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13];"""
a=[random.randint(1,10) for a in range(random.randint(1,15))]
b=[random.randint(1,10) for a in range(random.randint(1,15))]
a=sorted(a,key=int);
b=sorted(b,key=int);
c=[]
 
print("The two lists are:\na = "+str(a)+"\nb = "+str(b))

for i in a:
    for j in b:
        if i==j:
            c.append(i)
            
k=1;

while k<len(c):
    if c[k]==c[k-1]:
        del c[k-1];
    else:
        k=k+1;
        
print("The common elements are:\nc = "+str(c))
    