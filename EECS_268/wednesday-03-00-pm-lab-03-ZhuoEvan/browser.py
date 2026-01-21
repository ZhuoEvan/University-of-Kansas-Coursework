'''
Author: Evan Zhuo
KUID: 3109819
Date: 09/25/2024
Lab: lab03
Last modified: 9/28/2024
Purpose: Browser History
'''
#browser.py

#import linkedlist from LinkedList
from linkedlist import LinkedList

class Browser:
    def __init__(self):
        #Initial Variables
        self.browser_history = LinkedList()
        self._current_history = 0

    #Adding URL into Browser History
    def navigate_to(self, url):
        index = self._current_history
        #If there are URLs After the Current
        if self.browser_history.length() > index:
            for i in range(self.browser_history.length(), index, -1):
                #Range is Reversed (Value is Increased by 1)
                i = i - 1
                self.browser_history.remove(i)
            #Recursion
            self.navigate_to(url)
        else:
            self.browser_history.insert(index, url)
            self._current_history += 1
            
    #Change the Cursor Location Forward
    def forward(self):
        #Add Nothing if Cursor equals History Length
        if self._current_history == self.browser_history.length():
            self._current_history += 0
        #Add to Cursor
        else:
            self._current_history += 1

    #Change the Cursor Location Forward
    def back(self):
        #Subtract Nothing if Cursor equals 1
        if self._current_history == 1:
            self._current_history += 0
        #Subtract to Cursor
        else:
            self._current_history -= 1

    #Prints the History in a Specific Format
    def history(self):
        print('Oldest\n===========')
        #Getting Entry for the Entire LinkedList
        for i in range(0, self.browser_history.length()):
            #Cursor and URL Equal the Same Scenario
            if i == self._current_history - 1:
                print(f'{self.browser_history.get_entry(i)} <== current')
            #Printing All Other URLs
            else:
                print(self.browser_history.get_entry(i))
        print('===========\nNewest\n')
