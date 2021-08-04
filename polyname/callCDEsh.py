#!/usr/bin/env python
#use this method to run any bash scripts, a useful way to run extraction tools that are only run in command line
import subprocess

def command_line(file):
	subprocess.call("./cde2.sh {}".format(file), shell = True)

#file = "/Users/pmuthuku/Desktop/test_articles_html/example2.json"
#command_line(file)
