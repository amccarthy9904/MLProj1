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

def getAttributes(classes):
	global dataFile
	# grab the first datapoint from dataFile
	# remove the class name from the list of values
	# The sample point should print this >> ClassName: datavalue1 datavalue2 ...
	
	#with open(dataFile, "r") as file:
	
	# Return a list of 2-tuples
	return [("attributeName1", "NUMERIC"), ("attributeName2", "{ Nominal1, Nominal2 }")]

# Prompts the user for the data classes and returns a list of the class names
def getClasses():
	print("Please enter the class names separated by a comma:")
	classes = input()
	classes = classes.split(',')
	classes = [c.strip() for c in classes]
	return classes
	
def createARFF(classes, attributes, data):
	return

# Entry point of the program
# Calls methods to collect classes and attributes, then sends that information to createARFF 		 
if __name__ == "__main__":
	global dataFile
	if len(sys.argv) > 1:
		dataFile = sys.argv[1]
		classes = getClasses()
		attributes = getAttributes(classes)
	else:
		print ("Error: must enter a valid datafile.")
	