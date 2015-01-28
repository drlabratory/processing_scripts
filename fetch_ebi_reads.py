import ftplib, argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
    	description='A script that downloads all fastq files from an SRR run',
    	epilog='Highly specific to EBI ENA')
    # parser.add_argument('-h', '--help')
    parser.add_argument('-f', '--file', required=True,
    	help='a file containing ENA read accesion strings, one per line')
    args = parser.parse_args()

print args

# ftp = ftplib.FTP("ftp.sra.ebi.ac.uk")
# ftp.login("anonymous","jeramiaory@kings.edu")

# file_list = open(args.file, 'rb')
# for run_name in file_list:
# 	print name


# ftp.cwd("/vol1/fastq/SRR576/SRR576301")


# for files in ftp.nlst():
# 	ftp.retrbinary('RETR %s' % files, open(files, 'wb').write)