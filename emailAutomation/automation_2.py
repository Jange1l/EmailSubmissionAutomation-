#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  2 19:13:06 2019

@author: JuanSuarez
"""

import pynput
import time 

mouse = pynput.mouse.Controller()
Button = pynput.mouse.Button

keyboard = pynput.keyboard.Controller()
Key = pynput.keyboard.Key

#************* LOCATIONS **************
refresh = (-1181.6953125, -100.01953125)
getEarlyAccess = (-1091.9921875, 327.36328125)
textBox = (-754.265625, 419.1640625)
submit = (-811.84765625, 488.63671875)

shift = (-1423.9609375, 753.4765625)
atSymbol = (-1370.39453125, 635.80859375)

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
newList = []

for i in emails:
    if i not in newList:
        newList.append(i)
        
print(len(emails), len(newList))
#*************************************

#********** MOVE MOUSE ***************

inputed = []

for inputs in range(100,102):
    print("STARTED")
    
    email = newList[inputs]
    inputed.append(email)
    
    print(email)
    
    #position at refresh 
    time.sleep(.05)
    print("refresh")
    mouse.move(-1181.6953125, -100.01953125)
    time.sleep(.05)
    mouse.click(Button.left,1)
    mouse.click(Button.left,1)
    
    #position at button
    print("button")
    mouse.move(-1091.9921875, 327.36328125)
    time.sleep(.05)
    mouse.click(Button.left, 1)
    time.sleep(.05)
    print("text box")
    mouse.move(-754.265625, 419.1640625)
    mouse.click(Button.left,1)
    
    for c in range(len(email)):
        if (c == "@"):
            print("typing @")
            mouse.move(-1423.9609375, 753.4765625)
            time.sleep(.05)
            mouse.click(Button.left,1)
            mouse.move(-1370.39453125, 635.80859375)
            time.sleep(.05)
            mouse.click(Button.left,1)
            
            mouse.move(-754.265625, 419.1640625)
            time.sleep(.05)
            mouse.click(Button.left,1)
            
        if(c != "@" or "\n" or " "):
            print("typing")
            time.sleep(.05)
            keyboard.press(email[c])
            time.sleep(.05)
            keyboard.release(email[c])
            
    print("submit")        
    mouse.move(-811.84765625, 488.63671875)
    time.sleep(.05)
    mouse.click(Button.left,1)
    time.sleep(.05)
    mouse.click(Button.left,1)
  