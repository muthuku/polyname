#!/usr/bin/env python
# import Element class, tostring function
# from xml.etree.ElementTree library
from dict2xml import dict2xml
import json
 
# define a function to
# convert a simple dictionary
# of key/value pairs into XML
def dict_to_xml(tag, d):
	'''function to convert a JSON file into a XML file

	Input: 
		description: article in JSON file format
		file type: .json file format
		example: "example_data_1.json"
	Returns: article in XML format'''
	
	elem = Element(tag)
	for key, val in d.items():
		child = Element(key)
		child.text = str(val)
		elem.append(child)
	return elem

'''file_path = '/Users/pmuthuku/Documents/python_scripts_suli/workingscripts/example_data_1.json'

file = open(file_path)

data = json.load(file)

print(type(data))

xml = dict2xml(data)
print(xml)

xmlfile = open("dict.xml", "w")
xmlfile.write(xml)
xmlfile.close()'''