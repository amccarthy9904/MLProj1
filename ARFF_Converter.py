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
	# Iris-setosa, Iris-versicolor, Iris-virginica 
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
		print("\nThank you.\nBelow is a sample data point.")
		print("Please enter the attribute names and associated data types in the order they appear in the sample.")
		print("---------------------------------------------------------------------------------------------------")
		print("Follow this format:\n\n\t<attributeName1>:<dataType1>, <attributeName2>:<dataType2>, ...etc\n\n<dataType> can be one of NUMERIC, STRING, DATE, or a nominal type.\nFormat nominal types as {nominalValue1 & nominalValue2 &...etc}\n")
		print("Here is the sample data point of the class", sampleClass + ".")
		print("Enter the " + str(len(sampleDataPoint)) + " attributes in the order they appear in the sample.")
		dashCount = len(sampleAttributes) + 4
		for dash in range(dashCount):
			print("-", end='')
		print("\n| " + sampleAttributes + " |")
		for dash in range(dashCount):
			print("-", end='')
		
		# check user input and return the attributes as a list of 2-tuples (attribute name, data type)
		oneAttrRegex = '([\w -]+:(NUMERIC|STRING|DATE|(\{(([\w-]+)|(([\w -]+&)+[\w -]+))\})))'
		formatRegex = '(' + oneAttrRegex + '(, )?){' + str(len(sampleDataPoint)) + '}'
		userInput = ""
		inputIsValid = False
		while not inputIsValid:
			userInput = input('\n> ')
			userInput = userInput.strip()
			if len(userInput) is 0:
				print("Error: You must enter the corresonding attributes.\n")
			elif not re.match(formatRegex, userInput):
				print("Error: You must enter the " + str(len(sampleDataPoint)) + " attributes in the specified format.\n")
			else:
				inputIsValid = True
		
		return [attrTuple.strip().split(':') for attrTuple in userInput.split(',')]
		

# Prompts the user for the data classes. Verifies the uses inputs a comma separated list
# Returns a list of the class names
def getClasses():
	classRegex = '(^(([\w -])+,)+([\w -])+$)|(^(\w-)+$)'
	classes = ""
	inputIsValid = False
	while not inputIsValid:
		print("Please enter the exact class names from the data (case sensitive) separated by commas:")
		classes = input('> ')
		classes = classes.strip()
		if len(classes) is 0:
			print("Error: You must enter at least 1 class name.\n")
		elif not re.match(classRegex, classes):
			print("Error: Class names must be separated by commas.\n")
		else:
			inputIsValid = True
		
	classes = classes.split(',')
	classes = [c.strip() for c in classes]
	return classes

# Given the classes and attributes (with datatypes)
# Create and format an .arff file in the current directory
def createARFF(classes, attributes):
	global dataFile
	fileName = re.search('(\w)+\..', dataFile).group(0).split('.')[0]
	outputString = ""
	
	# write @RELATION, @ATTRIBUTE, and @DATA tags specified by ARFF format
	with open(dataFile, "r") as file:
		outputString += "@RELATION " + fileName + "\n"
		for  attr in attributes:
			outputString += "\n@ATTRIBUTE " + attr[0].replace(' ', '') + ' ' + attr[1].replace(' ','').replace('&',',')
		
		outputString += "\n@ATTRIBUTE class {"
		for c in classes:
			outputString += c
			if classes.index(c) is not len(classes)-1:
				outputString += ','
		
		outputString += "}\n"
		outputString += formatData() + "\n%\n%\n%\n"
		
	#create the ARFF file and write ouputString into the file
	arffFile = fileName + ".arff"
	with open(arffFile, "w") as newFile:
		newFile.write(outputString)

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
	
