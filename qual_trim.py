#!/usr/bin/env python
# Trim all files in the current directory using Trimmomatic
# put trimmed reads in a new directory
# File handling highly specific to EBI ENA / SRA naming convention

import os
import sys
import subprocess
import glob

# Pass a filename base and either one or two files to Trimmomatic

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

file_list = glob.glob('SR*gz')
filebases = []

for filenames in file_list:
	if not filenames[:9] in filebases:
		filebases.append(filenames([:9]))

for bases in filebases:
	if bases+'_1.fastq.gz' in file_list:
		file1 = bases+'_1.fastq.gz'
		file2 = bases+'_2.fastq.gz'		
		sys.stdout.write("%s is paired end reads.\nTrimming for quality...\n" % bases)
		if trim_double(bases, file1, file2):
			sys.stdout.write("Trimming completed.")
		else:
			sys.stdout.write("Trimming failed!")
	elif bases+'.fastq.gz' in file_list:
		file1 = bases+'.fastq.gz'
		sys.stdout.write("%s is single end reads.\nTrimming for quality...\n" % bases)
		if trim_single(bases, file1):
			sys.stdout.write("Trimming completed.")
		else:
			sys.stdout.write("Trimming failed!")
	else:
		sys.stdout.write("Check file names, non-standard, skipping %s" % bases)
		
		
		