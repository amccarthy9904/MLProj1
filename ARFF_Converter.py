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
		if re.search(',', firstLine):
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
<<<<<<< Updated upstream
	global dataFile, classColumnIndex
	#with open(dataFile, "r") as file:
		#write @RELATION tag
		#write @ATTRIBUTE tags in the order the list is in
		#write final @ATTRIBUTE tag for class
		#write @DATA tag using a call to formatData(classes, attributes) - returns a string
		#close the writer
=======
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
		outputString += formatData(len(attributes))
		
	#create the ARFF file and write ouputString into the file
	arffFile = fileName + ".arff"
	with open(arffFile, "w") as newFile:
		newFile.write(outputString)
>>>>>>> Stashed changes

# TODO
# Given the number of attributes
# Format the @DATA section and return it as a string
<<<<<<< Updated upstream
def formatData():
    global dataFile, classColumnIndex
    with open(dataFile, 'r') as file:
        if re.match(dataFile, ".txt") or re.match(dataFile, ".data"):
            if re.match(file.readline(), " "):
                #get rid of it boi
            data = "\n @DATA \n"
            for line in file.readlines():
                data = data + line
        return data
	
=======
def formatData(numAttributes):
	global dataFile
	with open(dataFile, 'r') as file:

		#check for correct file extension
		# continue with warning if file extension wrong
		if not re.search("\.txt|\.data|\.csv", dataFile):
			print("File format not supported\nFile must be .txt, .data, or .csv")
			print("Data transfer continuing...\nResults may be unreliable")

		#make header
		data = "\n@DATA\n"
		lines = file.readlines()

		# check if the file is space delimited with range to account for class names with spaces
		# replace spaces with commas
		if len(re.split(" ", lines[0])) in range(numAttributes, numAttributes + 4):
			for i in range(0, len(lines)):
				# replace numAttributes number of spaces with commas on every line
				lines[i] = re.sub(" ", ",", lines[i], numAttributes)

		for line in lines:
			data = data + line
		data = data + "\n%\n%\n%\n"
		return data



>>>>>>> Stashed changes
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
	
