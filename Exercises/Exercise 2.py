# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 15:27:13 2018

@author: Udvardy
"""

"""This is excercise two"""

print("This is exercise two, please follow the intructions")

numberone=int(input("Give me an integer number: "))

remainder=numberone%2;
remainder2=numberone%4;

if remainder == 0 and remainder2==0 :
    print("Your number was even and can be divided by 4")
elif remainder == 0 and remainder2 !=0:
    print("Your number was even but cannot be divided by 4")
else:
    print("Your number was odd")


print("\n \nNow I will need you to give me two numbers. \nThe first is num the second is the check. The program checks if the check divides evenly into num.")

num=int(input("Give me the num: "))
check=int(input("Give me the check: "))

remainder3=num%check;

if remainder3 == 0 :
    print("Congratulations! The check divides evenly into num.")
else:
    print("I'm sorry, the check do not divides evenly into num.")