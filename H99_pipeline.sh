#!/bin/bash

pwd_dir=`pwd`

for dirs in `ls |grep grubii |head -14 |tail -10`
do 
	echo "rsync -a $pwd_dir/$dirs/ /ssd/$dirs/"
	rsync -a $pwd_dir/$dirs/ /ssd/$dirs/
	echo "rsync done"
	cd /ssd/$dirs
	echo "downloading reads"
	for read_names in `cat run_names.txt`
	do 
		fastq-dump --split-3 $read_names
	done
	echo "Trimming reads"
	qual_trim.py
	echo "Collecting reads"
	collect_reads.py
	echo "aligning reads with BWA"
	align_reads.py
	echo "Syncing to home directory"
	rsync -a /ssd/$dirs/ $pwd_dir/$dirs
	cd $pwd_dir
	echo "Removing ssd files"
	rm -rf /ssd/$dirs
done


