# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 20:13:53 2017

@author: Aaron McCarthy
@author: Elias Athey
@author: Tia Smith
"""
import sys
import re

if __name__ == "__main__":
    for file_name in sys.argv:
        if re.search(file_name, "\.name"): 
            convertName(file_name)
        elif re.match(file_name, "\.data"):
            convertData(file_name)
            
def convertName (file_name):
    with open(file_name, "r") as file:
        for line in file:
            if re.match(line, '7. Attribute Information:'):
                getAttributes()
                
def convertData (file_name):
    with open(file_name, "r") as file:
        for line in file:
             one_line_data = re.split(line, ',,')
                
    