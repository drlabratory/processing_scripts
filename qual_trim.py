#!/usr/bin/env python
# Trim all files in the current directory using Trimmomatic
# put trimmed reads in a new directory
# File handling highly specific to EBI ENA / SRA naming convention

import os
import sys
import subprocess
import glob

# Pass a filename base to Trimmomatic

def trim_any(filebase):
	trim_directory = filebase+'_trim'
	file_single = filebase+'.fastq.gz'
	file_1 = bases+'_1.fastq.gz'
	file_2 = bases+'_2.fastq.gz'	
	single_command = ("java -Xmx14g -jar "
		"/opt/Trimmomatic-0.33/trimmomatic-0.33.jar SE "
		"-phred33 -threads 4 %s %s "
		"ILLUMINACLIP:/opt/Trimmomatic-0.33/adapters/barcodes.fa:2:40:15 "  
		"LEADING:5 "
		"TRAILING:5 "  
		"SLIDINGWINDOW:4:5 "
		"MINLEN:26"
		) % (os.path.join("..",file_single), file_single+'_trimmed')
	double_command = ("java -Xmx14g -jar "
		"/opt/Trimmomatic-0.33/trimmomatic-0.33.jar PE "
		"-phred33 -threads 4 -baseout %s %s %s "
		"ILLUMINACLIP:/opt/Trimmomatic-0.33/adapters/barcodes.fa:2:40:15 "  
		"LEADING:5 "
		"TRAILING:5 "  
		"SLIDINGWINDOW:4:5 "
		"MINLEN:26"
		) % (filebase, os.path.join("..",file_1), os.path.join("..",file_2))
	if os.path.exists(file_single):
		if not os.path.exists(trim_directory):
			os.mkdir(trim_directory)
		os.chdir(trim_directory)
		sys.stdout.write("%s is single end reads.\nTrimming for quality...\n" % filebase)
		subprocess.call(single_command, shell=True)
		sys.stdout.write("Trimming of %s completed." % filebase)
		sys.stdout.flush()
		os.chdir("..")
		return True
	elif os.path.exists(file_1):
		if not os.path.exists(trim_directory):
			os.mkdir(trim_directory)
		os.chdir(trim_directory)
		sys.stdout.write("%s is double end reads.\nTrimming for quality...\n" % filebase)
		subprocess.call(double_command, shell=True)
		sys.stdout.write("Trimming of %s completed." % filebase)
		sys.stdout.flush()
		os.chdir("..")
		return True
	else:
		sys.stdout.write("Check file names, non-standard, skipping %s \n" % filebase)
		sys.stdout.flush()
		return False

file_list = glob.glob('SR*gz')
filebases = []

for filenames in file_list:
	if '_' in filenames:
		basename = filenames.split('_')[0]
	else:
		basename = filenames.split('.')[0]
	if not basename in filebases:
		filebases.append(basename)


if __name__ == "__main__":
	for bases in filebases:
		trim_any(bases)