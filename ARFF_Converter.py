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
	# Iris-setosa, Iris-versicolour, Iris-virginica 
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
		sampleDataPoint = [attr.strip() for attr in sampleDataPoint]
		
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
	classes = [c.strip() for c in classes]
	return classes

# Given the classes and attributes (with datatypes)
# Create and format an .arff file in the current directory
def createARFF(classes, attributes):
	global dataFile, classColumnIndex
	
	fileName = re.search('(\w)+\..', dataFile).group(0).split('.')[0]
	outputString = ""
	
	with open(dataFile, "r") as file:
		outputString += "@RELATION " + fileName + "\n"
		for  attr in attributes:
			outputString += "\n@ATTRIBUTE " + attr[0].replace(' ', '') + ' ' + attr[1]
		
		outputString += "\n@ATTRIBUTE class {"
		for c in classes:
			outputString += c
			if c.index is not len(classes)-1:
				outputString += ','
		
		outputString += "}\n"
		outputString += formatData() + "\n%\n%\n%\n"
		
	#create the ARFF file
	arffFile = fileName + ".arff"
	with open(arffFile, "w") as newFile:
		newFile.write(outputString)
	
	# print("\n\nOUTPUT")
	# print (outputString)

# TODO
###### NOTE: The data needs to be comma-separated with no spaces. So that needs to be checked before returning the data. If it is space-separated, then convert it to commas.
# Given the classes and attributes
# Format the @DATA section and return it as a string
def formatData():
	global dataFile
	with open(dataFile, 'r') as file:
		data = ""
		if re.search(".txt", dataFile) or re.search(".data", dataFile):
			data = "\n@DATA\n"
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
	
