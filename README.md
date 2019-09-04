# EmailSubmissionAutomation- 

While working as a brand ambassador for XYZ company it was my responsability to advertise XYZ prior to its launch. During this time, XYZ was preparing to expand their existing product in to the US. My job was to collect the emails of those who were interested in singing up early and submit them to a personal link that was used to track my performance. Throughout this time period I managed to collect a large amount of emails, too many to manually input them into the link. "

I created this python script to help me automate the email input process. Below I will explain in detail how the script works and what you can do to edit this for your own use.


THE PROCESS
***** Data ******
1. I created a csv file containing all the emails that I wanted to input into my personal brand ambassador link. 

2. Using python, I cleaned the csv file to remove duplicate emails, empty spaces, syntax errors, and any other discrepancies that might interfere with the input process. 

***** Automation ******
#This step doesn't require an external monitor but the monitor does help. 
3. I opened the link on one side of the monitor and my spyder editor on the other. This should be calibrated so that you can comfortably see the code and terminal window on one side, and the website on the other. 

4. Using the pynput library in python, I recorded all the screen coordinates of where each important button on the website was. I made this coordinates variables and named them the corresponding action of each button that they represent for consistency. 
  - To take the coordinates you can "print(mouse.location())" when you hover the mouse over the button and press fn + f5 to       run the script and get the location. Do not click outside of spyder or whatever IDE you might be using because fn + f5         will not run. 

5. Once all the buttons where outlined, I mapped out the process of what buttons needed to be clicked first, second, third, etc.

6. After mapping these steps, I imported the csv data into an array of strings and created a for loop that went through the whole array.

7. Uisng the same pynput library, I was able to simulate mouse movements to transition from button to button and I can also simulate keyboard inputs to type in the characters of the email string. 
  - Here I was presented with a ptoblem. The "@" symbol was not being typed in properly, so I had to open a virtual keyboard and whenver the "@" symbol showed up I would have to move the mouse to the virtual keyboard and click on the symbol to type it in. 

8. Once all of the logistics for typying in the emails were figured out, all I had to do was click run and the python script would follow the steps to submit every email. 


***** Improvements and Obstacles ******

Some obstacles that I encountered while writing this scrypt where associated with the characters not being typed in properly. As I mentioned previously, the @ symbol was not being registered by the keyboard controller. The way that I worked around this was by physically clicking on the @ symbol with the mouse on a virtual keybaord. 

Another problem that I encountered involved the website not loading fast enough and sometimes crashing as the automation would continue clikcing specific locations on the screen where different buttons might now be present. The quick fix for this was to increase a timer that would wait in between clicks, but this slowed down the entire process because the program would wait equal amounts of time for refresh/submit of the page. What I propose to solve this issue is to use the request library in python and use that to determine the state of the website. This would give the program some view into the state of the website as opposed to just blindly waiting and hoping that it is clicking on buttons at the right time. 

