#!/usr/bin/env python
# Align reads with bwa mem, then merge and sort the sam/bam files

import os
import subprocess

project_name = os.getcwd().split('/')[-1].split('_')[-1]

PE1_reads = project_name+"_reads.PE.qc.1.fq.gz"
PE2_reads = project_name+"_reads.PE.qc.2.fq.gz"
SE_reads = project_name+"_reads.SE.qc.fq.gz"

PE_SAM = project_name+"_reads_aln.pe.sam"
SE_SAM = project_name+"_reads_aln.se.sam"
PE_SORTED = project_name+"_reads_aln_sorted.pe"
SE_SORTED = project_name+"_reads_aln_sorted.se"

PE_command = "bwa mem -t 8 ~/ref_genomes/H99_all.fa %s %s > %s" % (PE1_reads, PE2_reads, PE_SAM)
SE_command = "bwa mem -t 8 ~/ref_genomes/H99_all.fa %s > %s" % (SE_reads, SE_SAM)

PE_sort_command = "samtools view -bS %s | samtools sort - %s" % (PE_SAM, PE_SORTED)
SE_sort_command = "samtools view -bS %s | samtools sort - %s" % (SE_SAM, SE_SORTED)

sorted_bam = project_name+"_reads_aln_sorted.bam"

merge_command = "samtools merge %s %s %s" % (sorted_bam, PE_SORTED+".bam", SE_SORTED+".bam") 
index_command = "samtools index %s" % sorted_bam 

# Run BWA aligner
subprocess.call(PE_command, shell=True)
subprocess.call(SE_command, shell=True)

# convert to BAM and sort
subprocess.call(PE_sort_command, shell=True)
subprocess.call(SE_sort_command, shell=True)

# merge and index
subprocess.call(merge_command, shell=True)
subprocess.call(index_command, shell=True)

# Remove intermediary SAM/BAM files
os.remove(PE_SAM)
os.remove(SE_SAM)
os.remove(PE_SORTED+".bam")
os.remove(SE_SORTED+".bam")
