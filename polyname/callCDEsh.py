#!/usr/bin/env python
#use this method to run any bash scripts, a useful way to run extraction tools that are only run in command line
import subprocess

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
