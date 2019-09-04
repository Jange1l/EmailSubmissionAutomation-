#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 10:54:38 2019

@author: JuanSuarez
"""


def get_data(filename):
    f=open(filename)
    listen=[]
    for line in f:
        listen.append(line)
    return listen

emails = get_data('cleaning.csv')

#print(emails)

newList = []

for i in emails:
    
    for char in range(len(i)):
        new = ""
        if i[char] == "<":
            for em in range(char, len(i)):
                if i[em] != "<" and i[em]!= ">" and i[em] != "," and i[em] != '"' :
                    print(i[em])
                    new += i[em]
                
                    
            print(new)
            newList.append(new)
            
            

            

            
    
            

                    
               
        
            
            
        
        
        

        