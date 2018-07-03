# -*- coding: utf-8 -*-
"""
Description:
Created on Fri Jun 29 04:29:33 2018
@author: Unmesh Jyoti Nitin
This Program allows user to take breaks between the studies after entering the time and number of break he/she wishes to take.
"""
import time
import webbrowser

def take_break():
    user_input = input('Enter the number of breaks you want to take: ')
    user_input_time = input('Please enter the time in SECONDS: ')
    total_breaks = int(user_input)
    counter = 0
    while counter < total_breaks:
        time.sleep(int(user_input_time))
        webbrowser.open('https://www.youtube.com/watch?v=CQ8ZHilxdm8')
        counter += 1

def get_current_time():
    print('This program was started on' + ' ' + str(time.ctime()))
    
def main():
    take_break()
    print()
    get_current_time()
main()
