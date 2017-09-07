# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 20:13:53 2017

@author: Aaron McCarthy
@author: Elias Athey
@author: Tia Smith
"""
import sys
import re
import os

# Converts the metadata file into ARFF format
# Attempts to retrieve attribute information from metadata
def convertName (file_name):
    with open(file_name, "r") as file:
        boolboi = True
        attributes = []
        for line in file:
            if re.match(line, "7. Attribute Information:"):
                boolboi = True
            if boobboi:
                attributes.append(line)
            if re.match(line, "8."):
                getAttributes(attributes, file)
                boolboi = False

def getAttributes(att, file):
    os.startfile(file)

# Converts a data file into the ARFF format
def convertData (file_name):
    with open(file_name, "r") as file:
        for line in file:
             one_line_data = re.split(line, ',,')

# Entry point of the program
# Calls conversion methods on associated files			 
if __name__ == "__main__":
	files = sys.argv
	files.remove(sys.argv[0])
	for file_name in files:
		if re.search(file_name, "\.name"):
			convertName(file_name)
		elif re.match(file_name, "\.data"):
			convertData(file_name)
		else:
			print("does this file contain data(y/n)")
			if re.match(input(), "n"):
				convertName(file_name)
			else:
				convertData(file_name)
              