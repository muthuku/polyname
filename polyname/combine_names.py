#!/usr/bin/env python
'''Code written to combine the CEMS from individual text files into a single text file and remove duplicates for further steps if needed'''

#imports
import os
import glob
import pandas as pd


def combine_name_cde(filepath):

	'''function that takes in a directory of textfiles and combines it into a single file
	input:
		filepath:
				description: a filepath to the directory with all files
				example: /Users/pmuthuku/Documents/python_scripts_suli/final_scripts/all_articles

	returns: a textfile with all chemical names '''

	#use glob to create a list of file names ending in .txt to be run in this script 
	txt_list = glob.glob('{}/*.txt'.format(filepath))
	print(txt_list)
	#open a new text file where all the names will be added
	with open("all_names.txt", "wb") as outfile:
		#loop through files in the text list
		for f in txt_list:
			#open each file and then write the contents into the all_names text files
			with open(f, "rb") as infile: 
				outfile.write(infile.read())


def remove_duplicate_cde(filename):

	''' a function that removes duplicates from textfile with all chemical names
	input:
		filename: a file that contains all chemical names
		file type: text file(.TXT)
		example: "all_names.txt"

	returns: a list with final chemical names and no duplicates'''
	final_cems = []
	#write a dataframe with all names in it with a tital final cems since each individual file doesnt have a header
	df = pd.read_csv("all_names.txt", names = ["Final_CEMS"])
	#list of names from df 
	list_of_names = df["Final_CEMS"].to_list()
	#loop through the list and remove duplicates, return the final list
	for j in list_of_names:
		string = str(j)
		string1 = string[0].upper() + string[1:]
		if string1 not in final_cems:
			final_cems.append(string1)
	return final_cems
'''
#use the functions to combine all txt files 
file_path = "/Users/pmuthuku/Documents/python_scripts_suli/final_scripts/all_articles"
combine_name(file_path)
#make a list with remove duplicated
new_list = remove_duplicates("all_names.txt")
#save this new list to a dataframe
final_df = pd.DataFrame(new_list, columns = ['Final_Cems'])
print(final_df)
#write final df to a textfile
final_df.to_csv("Final_Cems.txt", header = True, index = False)
'''



'''files = []
directory = os.fsencode("/Users/pmuthuku/Documents/python_scripts_suli/workingscripts/extracted_cde_names")
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	files.append(filename)

data = []
for f in files:
	with open(f) as file:
		for i,row in enumerate(file):
			data.append(row)

with open("all_names.txt", "w") as newfile:
	for row in data:
		newfile.write(row)'''
