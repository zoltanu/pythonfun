# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 11:40:18 2018

@author: Udvardy
"""

import datetime

print("This is excercise one, please follow the instructions")

name=input("Please type your name: ")
age=int(input("How old are you gonna be by the end of this year? "))
rep=int(input("How many times you want the sentence to be prined? "))

now= datetime.datetime.now()
print(now.year)
yearint=int(now.year)

hundred=yearint+100-age;

counter=1;

while counter<=rep:
    print(name + ", you will be 100 old in: " + str(hundred))
    counter=counter+1;