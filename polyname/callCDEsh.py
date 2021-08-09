#!/usr/bin/env python
#use this method to run any bash scripts, a useful way to run extraction tools that are only run in command line
import subprocess
import sys
import os
import json
import glob
import pandas as pd

def command_line_cde(file):
	
	'''calls bash script molconvert.sh and runs the Chemdataextractor command line tool on a JSON file to get chemical entities

	Input: 
		description: article .JSON file for article
		type: .json
		example: example2.json

	Returns : a JSON file(.json) with all names and data from article'''

	subprocess.call("polyname/cde.sh {}".format(file), shell = True)

#file = "/Users/pmuthuku/Desktop/test_articles_html/example2.json"
#command_line(file)

def extract_names(file):
	'''from a .JSON file outputted by CDE command line tool extract all names column
	input:
		file:
			description: a results.json file outputted by CDE
			file type: .json file
			example: results.json
		returns: a list of chemical entities'''
	#open file and load it using json module
	f = open(file)
	data = json.load(f)
	print(type(data))
	#initialize new list
	new_list = []
	#for dict in the data 
	for dict1 in data:
		#if there is a key named "names", get the value which is a list
		if "names" in dict1:
			list1 = dict1['names']
			#for item in list, append every item
			for j in list1:
				new_list.append(j)
	return new_list

def remove_duplicates_list(anylist):
	'''a function that takes in a list and returns a list with no duplicates
	inputs:
		anylist:
			description: a list of chemical entities
			type: list
			example: [carbon, oxygen, silicon, carbon]
		returns: a list - [carbon, oxygen, silicon]'''
	#initialize list
	final_list = []
	#loop through the inputted list, find and remove duplicates and return the final list
	for j in anylist:
		string = str(j)
		string1 = string[0].upper() + string[1:]
		if string1 not in final_list:
			final_list.append(string1)
	return final_list