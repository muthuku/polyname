# Polyname for Polymer name recognition in scientific text

A simple package to extract polymer names from a list of chemical entities outputted by a chemical extraction tool and get monomer names and monomer smiles from the existing polymers database, Pubchem or CIRPY.

Install:
	Create a conda environment using the environment.yml file and clone the repository:
	
	conda env create -f environment.yml
	git clone git@github.com:muthuku/polyname.git
	pip install any packages not installed in requirements.txt
Use:
	
1) Large scale data extraction with Chemdataextractor- see CDE_names_python.ipynb JUPYTER NOTEBOOK for detailed explanation
	
		from polyname import cde_func
		from polyname import uppercase
		from polyname import combine_files_cde
		from polyname import remove_duplicate_file
		from polyname import command_line_cde
		from polyname import polymer_extract
		import pandas as pd
		import os
	
		#RUN CDE ON ONE JSON FILE
		#variable set to path of a file
		file_path = 'cde_extract_example/example_article.pdf'
		#run cde_func which extracts all chemical entities and removes duplicates
		new_list = cde_func(file_path)
		#run upper case to make all terms capitalized 
		final_list = uppercase(new_list)
		df = pd.DataFrame(final_list, columns = ["All_names"])
		print(df)
		df.to_csv("polyname_example/all_names.txt", header = True, index = False)

2) Polymer names extraction- CHECK polyname_example.ipynb JUPYTER NOTEBOOK for detailed explanations

		from polyname import check_database
		from polyname import remove_duplicate_names_smiles
		from polyname import search_names
		from polyname import polymer_extract
		from polyname import strip_poly
		from polyname import get_pubchem_smiles
		from polyname import get_cirpy_smiles
		from polyname import get_pubchem_names
		from polyname import get_cirpy_names
		from polyname import lowercase
		import pandas as pd
	
EXTRACT POLYMERS FROM FILE WITH CHEMICAL ENTITIES
	
		#POLYMER EXTRACTION STEP
		#Input : chemical names outputted by the extraction step
		all_names_path = "polyname_example/all_names.txt"
		#in whatever method convert the file of names into a list of names
		df = pd.read_table(all_names_path)
		all_names_list = df["All_names"].to_list()
		print(all_names_list)

		#isolate the polymers using a list of chemical entities- function polymer_extract takes a list as input
		polymer_list = polymer_extract(all_names_list)
		#convert it to dataframe and write to a textfile with all isolated polymer names
		data = pd.DataFrame (polymer_list, columns = ['Isolated_poly_names'])
		print(data)
		data.to_csv("polyname_example/poly_exam_final_names.txt", index = False, header = False)

CHECK DATABASE STEP FOR EXISTING POLYMERS IN DATABASE AND GET MONOMER SMILES AND NAMES

		#CHECK DATABASE STEP
		#Input : database file name and extracted polymers file (poly_exam_final_names.txt)
		database_path = "polyname_example/poly_name_smiles_database.csv"
		all_polymers = "polyname_example/poly_exam_final_names.txt"
		#check database for each polymer name and remove duplicates
		name,smile = check_database(all_polymers,database_path)
		final_name,final_smile = remove_duplicate_names_smiles(name,smile)

		#add polymer names and monomer smiles to a file named "database_extract.csv"
		df = pd.DataFrame(final_name, columns = ["Polymer Names"])
		df.insert(1,'Monomer Smiles', final_smile)
		print(df)
		df.to_csv('polyname_example/database_extract.csv', index = None)

		#return a list with polymer names not found in database, Input: the all polymers names and final names found in DB
		search_name = search_names(all_polymers,final_name)

FOR ANY POLYMER NOT FOUND IN EXISTING DATABASE, GET THE MONOMER NAME AND SMILES FROM PUBCHEM AND CIRPY


		#EXTRACT MONOMER SMILES NAMES come back to this
		#Extract monomer smiles from the polymers that still need to be extracted 
		polymers_to_extract = 'polyname_example/polymer_extract_still.csv'
		#read textfile into dataframe
		data2 = pd.read_table(polymers_to_extract)
		print(data2)
		#get unique polymer names 
		dfnames2 = pd.DataFrame(data2.polymername.unique(),columns=['polyname'])
		print(dfnames2)
		stripstrings = [['poly(',')'],['poly[(',')]'],['poly[',']'],['poly{','}'],['poly-','']]
		dfnames2['stripped_monomer_name'] = dfnames2.apply(lambda row: strip_poly(row,stripstrings),axis=1)
		print(dfnames2)
		#pubchem is busy, works most times check pubchem_cirpy_polymer_extract.csv for an example
		monomer_names2 = dfnames2.apply(lambda row: strip_poly(row,stripstrings),axis=1)
		#dfnames2['Pubchem Smiles'] = monomer_names2.apply(lambda row: get_pubchem_smiles(row))
		dfnames2['Cirpy Monomer Smiles'] = monomer_names2.apply(lambda row: get_cirpy_smiles(row))
		#dfnames2['Pubchem Names'] = monomer_names2.apply(lambda row: get_pubchem_names(row))
		dfnames2['Cirpy Monomer Iupac Names'] = monomer_names2.apply(lambda row: get_cirpy_names(row))
		print(dfnames2)
		dfnames2.to_csv("polyname_example/cirpy_only_polymer_extract.csv", index = False)
