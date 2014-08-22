#!/usr/bin/env python

import os
import sys
import subprocess
import glob

# Pass a filename base and either one or two files to Trimmomtatic

def trim_single(filebase, file1):
	trim_directory = filebase+'_trim'
	trim_command = ("java -Xmx40g -jar "
		"/share/Trimmomatic-0.32/trimmomatic-0.32.jar SE "
		"-phred33 -threads 64 -baseout %s %s "
		"ILLUMINACLIP:/share/Trimmomatic-0.32/barcodes.fa:2:40:15 "  
		"LEADING:5 "
		"TRAILING:5 "  
		"SLIDINGWINDOW:4:5 "
		"MINLEN:26"
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

def trim_double(filebase, file1, file2):
	trim_directory = filebase+'_trim'
	trim_command = ("java -Xmx40g -jar "
		"/share/Trimmomatic-0.32/trimmomatic-0.32.jar PE "
		"-phred33 -threads 64 -baseout %s %s %s"
		"ILLUMINACLIP:/share/Trimmomatic-0.32/barcodes.fa:2:40:15 "  
		"LEADING:5 "
		"TRAILING:5 "  
		"SLIDINGWINDOW:4:5 "
		"MINLEN:26"
		) % (filebase, os.path.join("..",file1), os.path.join("..",file2))
	if not os.path.exists(trim_directory):
		os.mkdir(trim_directory)
	os.chdir(trim_directory)
	if subprocess.call(trim_command, shell=True):
		os.chdir("..")
		return True
	else:
		os.chdir("..'")
		return False
