#1/usr/bin/env python

import os, subprocess

project_name = os.getcwd().split('/')[-1].split('_')[-1]
sorted_bam = project_name+"_reads_aln_sorted.bam"
vcf_file = project_name+"_all_H99.vcf"

vcf_command = "freebayes-parallel ~/ref_genomes/H99_regions.txt 4 -j -p 100 -f ~/ref_genomes/H99_all.fa %s > %s" % (sorted_bam, vcf_file)

subprocess.call(vcf_command, shell=True)
