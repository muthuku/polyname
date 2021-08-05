#!/usr/bin/env python
#imports
import pubchempy as pcp
import pandas as pd
import numpy as np

#remove duplicates function
def remove_duplicates_molconvert(file):

	'''Function that removes duplicates from a textfile 

	Input: 
		Description: a textfile (.txt) with all chemical names outputted by molconvert
		File type: textfile(.TXT)
		example: names_mol.txt
	
	Returns: a textfile(.txt) with chemical names and duplicates are removed'''

	#with open file, read lines and make a list
	with open(file) as f:
		content = f.readlines()
	content = [x.strip() for x in content]
	print(content)
	#initialize new list
	new_list = []
	#loop through the content list
	for compound in content:
		print(compound)
		#remove duplicates,
		if compound not in new_list:
			#append it to the list
			new_list.append(compound)

	print(new_list)
	#open a new textfile and write each item in list to textfile
	with open("final_mol.txt","w") as textfile:
		for i in new_list:
			textfile.write(i + "\n")
		textfile.close()

'''file = "names_mol.txt"
#run function
remove_duplicates(file)'''