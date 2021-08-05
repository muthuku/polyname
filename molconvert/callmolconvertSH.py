#!/usr/bin/env python
'''a way to run molconvert on python since it is only a command line tool'''
import subprocess

def molconvert_call(file):
	subprocess.call("molconvert/molconvert.sh {}".format(file), shell = True)