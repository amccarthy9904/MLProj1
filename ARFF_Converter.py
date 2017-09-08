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

# Prompts the user for the attributes and associated data types
# Returns a list of 2-tuples, each corresonding to an attribute name and datatype pair
def getAttributes(classes):
	global dataFile, classColumnIndex
	# Iris-Setosa, Iris-Versicolour, Iris-Virginica 
	# sepal length:NUMERIC, sepal width:NUMERIC, petal length:NUMERIC, petal width:NUMERIC
	
	with open(dataFile, 'r') as file:
	
		# Get the first data point as a list of strings
		firstLine = file.readline().strip()
		sampleDataPoint = []
		
		# split data on commas or spaces
		if (re.search(',', firstLine)):
			sampleDataPoint = firstLine.split(',')
		else:
			sampleDataPoint = re.split('\s+', firstLine)
		sampleDataPoint = [attr.strip().lower() for attr in sampleDataPoint]
		
		# Finds the column in which the class is defined
		# Order of checking: last index, index 0, then index 1
		# This does not handle every case - open to other suggestions
		classColumnIndex = -1
		if (sampleDataPoint[len(sampleDataPoint) - 1] in classes):
			classColumnIndex = len(sampleDataPoint) - 1
		elif(sampleDataPoint[0] in classes):
			classColumnIndex = 0
		else:
			classColumnIndex = 1
		sampleClass = sampleDataPoint[classColumnIndex]
		sampleDataPoint.pop(classColumnIndex)
		sampleAttributes = re.sub('\[|\]|\'', '', str(sampleDataPoint))
		
		# Message to user and sample data point
		print("\nThank you.\nBelow is a sample data point.\nPlease enter the attribute names and associated data types in the order they appear in the sample.\nPlease follow this format: <attributeName1>:<dataType1>, <attributeName2>:<dataType2>, ...etc\n<dataType> can be one of NUMERIC, STRING, DATE, or a nominal value.\nIf an attribute has a nominal type, format <dataType> as {nominalValue1, nominalValue2,...,nominalValueN}\n")
		print("Here is the sample data point of the class", sampleClass + ".")
		print(sampleAttributes)
		
		# return user input as a list of tuples
		userInput = input()
		return [attrTuple.strip().split(':') for attrTuple in userInput.split(',')]
		

# Prompts the user for the data classes
# Returns a list of the class names
def getClasses():
	print("Please enter the class names separated by commas:")
	classes = input()
	classes = classes.split(',')
	classes = [c.strip().lower() for c in classes]
	return classes

# TODO
# Given the classes and attributes (with datatypes)
# Create and format an .arff file in the current directory
def createARFF(classes, attributes):
	global dataFile, classColumnIndex
	#with open(dataFile, "r") as file:
		#write @RELATION tag
		#write @ATTRIBUTE tags in the order the list is in
		#write final @ATTRIBUTE tag for class
		#write @DATA tag using a call to formatData(classes, attributes) - returns a string
		#close the writer

# TODO
# Given the classes and attributes
# Format the @DATA section and return it as a string
def formatData():
    global dataFile, classColumnIndex
    with open(dataFile, 'r') as file:
        if re.match(dataFile, ".txt") or re.match(dataFile, ".data"):
            data = "\n @DATA \n"
            for line in file.readlines():
                data = data + line
        return data
	
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
	
