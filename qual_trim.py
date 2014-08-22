#!/usr/bin/env python

import os
import sys
import subprocess
import glob

def trim_single(filebase, file1):
	trim_directory = filebase+'_trim'
	trim_command = (""
		""
		""
		""
		""
		) % (filebase, os.path.join("..",file1))
		if not os.path.exists(trim_directory):
		os.mkdir(trim_directory)
	os.chdir(trim_directory)
	if subprocess.call(trim_command, shell=True):
		os.chdir("..")
		return True
	else:
		os.chdir("..'")
		return False
