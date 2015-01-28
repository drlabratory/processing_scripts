#!/usr/bin/env python

import ftplib, argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    	description='A script that downloads all fastq files from an SRR run',
    	epilog='Highly specific to EBI ENA')
    # parser.add_argument('-h', '--help')
    parser.add_argument('-f', '--file', required=True,
    	help='a file containing ENA read accesion strings, one per line')
    args = parser.parse_args()

ftp_username = "jeramiaory@kings.edu"

ftp = ftplib.FTP("ftp.sra.ebi.ac.uk")
ftp.login("anonymous",ftp_username)

file_list = open(args.file, 'rb')
for run_name in file_list:
	run_name = run_name.strip()
 	directory_sub = run_name[0:6]
 	if len(run_name) == 9:
 		ftp_cwd = "/vol1/fastq/"+directory_sub+"/"+run_name
	elif len(run_name) == 10:
		dir_stub = "00"+run_name[-1]
		ftp_cwd = "/vol1/fastq/"+directory_sub+"/"+dir_stub+"/"+run_name
	else:
		print "A naming scheme we haven't discovered yet!"
		sys.exit(2)
	ftp.cwd(ftp_cwd)
	for files in ftp.nlst():
		print "Downloading files in %s", run_name
		ftp.retrbinary('RETR %s' % files, open(files, 'wb').write)
