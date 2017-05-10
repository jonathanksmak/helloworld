# -*- coding: utf-8 -*-
"""
Created on Tue May 02 16:22:07 2017

@author: Jonathan PC
"""

def username():
    prompt = "Hello, what is your name? ";
    name = raw_input(prompt);
    return name;

if __name__ == '__main__':
    print "Hello " + username()