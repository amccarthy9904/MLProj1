# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 20:13:53 2017

@author: oopl
"""
import sys
import re

if __name__ == "__main__":
    for file_name in sys.argv:
        convert(file_name)
        
def convert (file_name):
    with open(file_name, "r") as file:
        for line in file:
            
    