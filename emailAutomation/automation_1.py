#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 02:11:35 2019

@author: JuanSuarez
"""

#from pynput.mouse import Button, Controller
#from pynput.keyboard import Key
import pynput
import time 
#import csv

mouse = pynput.mouse.Controller()
Button = pynput.mouse.Button

keyboard = pynput.keyboard.Controller()
Key = pynput.keyboard.Key

#************* LOCATIONS **************
refresh = (-1161.21484375, -92.609375)
getEarlyAccess = (-1033.86328125, 305.79296875)
textBox = (-725.61328125, 428.90234375)
submit = (-779.6640625, 505.6953125)

shift = (-1490.24609375, 744.9140625)
atSymbol = (-1433.94140625, 623.6171875)

testText = (-1714.46875, 30.29296875) 
testPosition = (-1714.46875, 30.29296875)

#*************************************

#********** HANDLE DATA **************

def get_data(filename):
    f=open(filename)
    listen=[]
    for line in f:
        listen.append(line)
    return listen

emails = get_data('totalEmailList.csv')
buEmails = get_data('buEmails.csv')

newList = []

newBu = []

for i in emails:
    if i not in newList:
        newList.append(i)
for x in buEmails:
    if i not in newBu:
        newBu.append(x)
        #print(x)
        
print(len(emails), len(newList), len(buEmails), len(newBu))

#*************************************

#********** MOVE MOUSE ***************

inputed = []

for inputs in range(20, len(newBu)):
    
    print("STARTED")
    
    email = newBu[inputs]
    inputed.append(email)
    
    print(email)
    
    #position at refresh 
    time.sleep(2)
    print("refresh")
    mouse.position = refresh
    time.sleep(2)
    mouse.click(Button.left,1)
    time.sleep(4)
    mouse.click(Button.left,1)
    
    #position at button
    print("button")
    time.sleep(1)
    mouse.position = getEarlyAccess
    time.sleep(2)
    mouse.click(Button.left, 1)
    time.sleep(2)
    print("text box")
    mouse.position = textBox
    mouse.click(Button.left,1)
    
    for c in range(len(email)):
        if (email[c] == "@"):
            print("typing @")
            
            time.sleep(1)
            mouse.position = shift
            time.sleep(1)
            mouse.click(Button.left,1)
            
            time.sleep(1)
            mouse.position = atSymbol
            time.sleep(1)
            mouse.click(Button.left,1)
            
            time.sleep(1)
            mouse.position = textBox
            time.sleep(1)
            #mouse.click(Button.left,1)
            
        elif(email[c] != "." and email[c] != "@" and email[c] != "\n" and email[c] != " " and email[c] != '"'  and email[c] != ","):
            print("typing")
            time.sleep(.05)
            keyboard.press(email[c])
            time.sleep(.05)
            keyboard.release(email[c])
            
    print("submit")        
    mouse.position = submit
    time.sleep(2)
    mouse.click(Button.left,1)
    time.sleep(2)
    mouse.click(Button.left,1)
    print(inputs)




  
"""    
with open('newList.csv', mode='w') as employee_file:
   newList_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
   
   #for i in newList:
   newList_writer.writerow(newList)
print("done")
   

"""


















 

 







