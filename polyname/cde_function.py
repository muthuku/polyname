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


#chemdataextractor function to be fun on each file within directory, takes in path to file as an input
def cde_func(filepath):
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
#uppercase function to make sure names are normalized, takes in a list as input 
def uppercase(any_list):
	#initialze list
	final_cems = []
	#loop through list, capitalize and append to final list
	for string in any_list:
		string1 = string.capitalize()
		final_cems.append(string1)
	return final_cems
'''
#using the functions, write a file path where all articles are (15 JSON articles for this example)
files_path = '/Users/pmuthuku/Desktop/test_articles_html'
#loop through directory and generate a path to each filename
for filename in os.listdir(files_path):
	file_path = "{}/{}".format(files_path,filename)
	#run cde_func on each file to get a list of CEMS
	new_list = cde_func(file_path)
	#run uppercase function on list outputed from cde_func
	final_list = uppercase(new_list)
	#write a pandas dataframe with the list then write it to a text file with/without header
	df = pd.DataFrame(final_list, columns = ["Final_Chemical_Entities"])
	df.to_csv("{}.txt".format(filename), header = False, index = False)'''
