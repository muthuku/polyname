#!/usr/bin/env python
'''run Chemdataextractor on a directory of files PDF, XML, HTML and JSON and outputs textfile with all 
chemical entities, removes duplicates. One output file for each input in directory'''

#imports
import sys
import os
import pandas as pd
import re
import string
import nltk
from chemdataextractor import Document



def cde_func(filepath):

	'''python script to run CDE and extract chemical entities into a list, and remove duplicates before outputting a textfile

	Input: 
		description: a JSON, HTML or PDF input of a article
		filetype: .json,.html,.pdf
		example: article1.json

	Returns: a list of chemical entities'''

	#initialize list, open file
	chem_cems = []
	file = open(filepath,'rb')
	#create CDE Document object to be analyzed
	doc = Document.from_file(file)
	file.close()
	#run the CEMS function of Document object to get chemical entities in a list
	chem_list = doc.cems
	#loop through the list of CEMS and remove duplicates and then return the list
	for j in chem_list:
		string = str(j)
		string1 = string[0].lower() + string[1:]
		if string1 not in chem_cems:
			chem_cems.append(string1)
	return chem_cems

def uppercase(any_list):

	''' function to normalize the chemical names outputted and capitalize them

	Input: 
		description: a list of chemical entities
		type: list
		example: ['carbon', 'polyester']

	Returns: a list of capital chemical entities to be put into a file'''

	#initialze list
	final_cems = []
	#loop through list, capitalize and append to final list
	for string in any_list:
		string1 = string.capitalize()
		final_cems.append(string1)
	return final_cems

