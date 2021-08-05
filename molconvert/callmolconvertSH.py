#!/usr/bin/env python
'''a way to run molconvert on python since it is only a command line tool'''
import subprocess

def molconvert_call(file):
	'''calls bash script molconvert.sh and runs the Chemcurator molconvert tool on a XML file to get chemical names

	Input: 
		description: article .XML file for article
		type: .json
		example: example2.xml

	Returns : a textfile (.TXT) with all names and data from article'''

	subprocess.call("molconvert/molconvert.sh {}".format(file), shell = True)