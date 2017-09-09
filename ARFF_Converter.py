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

# TODO
# Prompts the user for the attributes and associated data types
# Returns a list of 2-tuples, each corresonding to an attribute name and datatype pair
def getAttributes(classes):
	global dataFile
	# grab the first datapoint from dataFile
	# remove the class name from the list of values
	# The sample point should print this >> ClassName: datavalue1 datavalue2 ...
	
	#with open(dataFile, "r") as file:
	
	# Return a list of 2-tuples
	return [("attributeName1", "NUMERIC"), ("attributeName2", "{ Nominal1, Nominal2 }")]

# Prompts the user for the data classes
# Returns a list of the class names
def getClasses():
	print("Please enter the class names separated by commas:")
	classes = input()
	classes = classes.split(',')
	classes = [c.strip() for c in classes]
	return classes

# TODO
# Given the classes and attributes (with datatypes)
# Create and format an .arff file in the current directory
def createARFF(classes, attributes):
	global dataFile
	#with open(dataFile, "r") as file:
		#write @RELATION tag
		#write @ATTRIBUTE tags in the order the list is in
		#write final @ATTRIBUTE tag for class
		#write @DATA tag using a call to formatData(classes, attributes) - returns a string
		#close the writer

# TODO
# Given the classes and attributes
# Format the @DATA section and return it as a string
def formatData(classes, attributes):
	global dataFile
	# Maybe switch stmt on file type and convert to ARFF format accordingly
	return "This will be a string of the data section in ARFF: \n @DATA \n atrbt1, atrbt2,...,class \n"
	
# Entry point of the program
# Calls methods to collect classes and attributes, then sends that information to createARFF
if __name__ == "__main__":
	global dataFile
	if len(sys.argv) > 1:
		dataFile = sys.argv[1]
		classes = getClasses()
		attributes = getAttributes(classes)
		createARFF(classes, attributes)
	else:
		print ("Error: must enter a single valid datafile to convert.")
	
