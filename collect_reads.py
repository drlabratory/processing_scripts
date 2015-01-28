!#/usr/bin/env python

import os
import subprocess
import glob

# This script is run after qual_trim.py, and goes into each *_trim
# directory and runs either intervleave-reads.py or cat
# them combines them into a single file

trim_directories = glob.glob("SRR*_trim")

for dir in trim_directories:
    filebase = dir.split('_')[0]
    new_PE = filebase+".PE.qc.fq"
    new_SE = filebase+".SE.qc.fq"
    PE_command = "interleave-reads.py *P > %s" % new_PE
    SE_command = "cat *U > %s" % new_SE
    os.chdir(dir)
    subprocess.call(PE_command, shell=True)
    subprocess.call(SE_command, shell=True)
    os.chdir("..")

#now combine all the trimmed reads into one file for kmer analysis

project_name = os.getcwd().split('/')[-1].split('_')[-1]
PE_join = "cat *_trim/*.PE.qc.fq > %s" % project_name+"_reads.PE.qc.fq"
SE_join = "cat *_trim/*.SE.qc.fq > %s" % project_name+"_reads.SE.qc.fq"

subprocess.call(PE_join, shell=True)
subprocess.call(SE_join, shell=True)

# get rid of the original read files (now pulling the trigger on this yet)
# also should delete *_trim directories

del_files = glob.glob("SRR*gz")

for files in del_files:
    print files
#     os.remove(files)