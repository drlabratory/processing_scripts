#!/usr/bin/env python

import os, shutil
import subprocess
import glob

# This script is run after qual_trim.py, and goes into each *_trim
# directory and renames files, then cats / moves
# them them into a single file

trim_directories = glob.glob("SRR*_trim")

for dir in trim_directories:
    filebase = dir.split('_')[0]
    # new_PE = filebase+".PE.qc.fq"
    new_PE1 = filebase+".PE.qc.1.fq"
    new_PE2 = filebase+".PE.qc.2.fq"
    new_SE = filebase+".SE.qc.fq"
    # PE_command = "interleave-reads.py *P > %s" % new_PE
    PE1_command = "mv %s %s" % (filebase+"_1P", new_PE1)
    PE2_command = "mv %s %s" % (filebase+"_2P", new_PE2)
    SE_command = "cat *U *_trimmed > %s" % new_SE
    os.chdir(dir)
    # subprocess.call(PE_command, shell=True)
    subprocess.call(PE1_command, shell=True)
    subprocess.call(PE2_command, shell=True)
    subprocess.call(SE_command, shell=True)
    os.chdir("..")

# now combine all the trimmed reads into one file
# checks to see if only one set of reads and moves instead of cats if so

project_name = os.getcwd().split('/')[-1].split('_')[-1]
if len(glob.glob('*_trim/*.PE.qc.1.fq')) > 1:
    PE1_join = "cat *_trim/*.PE.qc.1.fq > %s" % project_name+"_reads.PE.qc.1.fq"
    PE2_join = "cat *_trim/*.PE.qc.2.fq > %s" % project_name+"_reads.PE.qc.2.fq"
    SE_join = "cat *_trim/*.SE.qc.fq > %s" % project_name+"_reads.SE.qc.fq"
else:
    PE1_join = "mv -i *_trim/*.PE.qc.1.fq %s" % project_name+"_reads.PE.qc.1.fq"
    PE2_join = "mv -i *_trim/*.PE.qc.2.fq %s" % project_name+"_reads.PE.qc.2.fq"
    SE_join = "mv -i *_trim/*.SE.qc.fq %s" % project_name+"_reads.SE.qc.fq"


# subprocess.call(PE_join, shell=True)
subprocess.call(PE1_join, shell=True)
subprocess.call(PE2_join, shell=True)
subprocess.call(SE_join, shell=True)

# Compress all fq files
subprocess.call("pigz --best *.fq", shell=True)

# get rid of the original read files (not pulling the trigger on this yet)
# also should delete *_trim directories

del_files = glob.glob("SRR*fastq")
del_directories = glob.glob("*_trim")

for files in del_files:
    os.remove(files)
for directories in del_directories:
    shutil.rmtree(directories)

