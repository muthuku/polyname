#!/usr/bin/env python
'''Isolate all polymer names from all chemical entities and use language rules to capitalize,
remove whitespace and output a textfile with cleaned up polynames'''
#import pandas, numby, itertools and csv
import pandas as pd
import numpy as np
import itertools
import csv

def polymer_extract(anylist):

	'''function that extracts all polymers from a list of chemical entities
	input:
		file:
			description: a file that contains all chemical names
			file type: textfile(.txt)
			example: /Users/pmuthuku/Documents/python_scripts_suli/workingscripts/polyname_scripts/all_names.txt

	returns: a list of polymers'''
	
	#initialize new list
	new_list = []
	#loop through df4 list with all polymer names
	for name in anylist:
		#if it starts with poly, capitalize 1st letter, add paraentehsis, strip whitespace etc. and return new list
		if name.startswith('poly') or name.startswith('Poly'):
			cap = name[:1].upper() + name[1:]
			string = cap.replace("(", "")
			string1 = string.replace(")","")
			string2 = string1.strip()
			string3 = ''.join(char for char in string2 if char.isalnum())
			string4 = string3[:4] + "(" + string3[4:]
			string5 = string4.rstrip("s")
			final_name = string5 + ")"
			new_list.append(final_name)
	return new_list
#using function, have a file name, run function polymer_extract which returns a list
'''files_path = '/Users/pmuthuku/Documents/python_scripts_suli/workingscripts/polyname_scripts/all_names.txt'
polymer_list = polymer_extract(files_path)


#turn list into dataframe
data = pd.DataFrame (polymer_list, columns = ['Isolated_poly_names'])
print(data)

data1 = data[data["Isolated_poly_names"].str.startswith("Poly")]
print(data1)
#output list to a textfile
data1.to_csv("polymername_final.txt", index = False)'''