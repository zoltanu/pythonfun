# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 14:22:09 2018

@author: Udvardy
"""

"""This is exercise 3"""
print("This is excercise 3, please follow the instructions")

lista=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89];
lista2=[]
lista3=[]
print("The original list is [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]")

for element in lista:
    if element < 5:
        lista2.append(element)
print(lista2)

limit=int(input("\nGive me limit number and you will get the list elements that are smaller than that: "))
for element in lista:
    if element < limit:
        lista3.append(element)
print(lista3)