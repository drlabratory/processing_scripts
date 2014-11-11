import ftplib, sys, getopt


def main(argv):                         
    try:                                
        opts, args = getopt.getopt(argv, "hl", ["help", "list"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)


ftp = ftplib.FTP("ftp.sra.ebi.ac.uk")
ftp.login("anonymous","jeramiaory@kings.edu")
ftp.cwd("/vol1/fastq/SRR576/SRR576301")


for files in ftp.nlst():
	ftp.retrbinary('RETR %s' % files, open(files, 'wb').write)


if __name__ == "__main__":
    main(sys.argv[1:])