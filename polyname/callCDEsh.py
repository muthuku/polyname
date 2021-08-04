#!/usr/bin/env python
#use this method to run any bash scripts, a useful way to run extraction tools that are only run in command line
import subprocess

def command_line_cde():
	subprocess.call("polyname/cde.sh", shell = True)
	return None