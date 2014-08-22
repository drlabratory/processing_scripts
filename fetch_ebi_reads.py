import ftplib

ftp = ftplib.FTP("ftp.sra.ebi.ac.uk")
ftp.login("anonymous","jeramiaory@kings.edu")
ftp.cwd("/vol1/fastq/SRR576/SRR576301")


for files in ftp.nlst():
	ftp.retrbinary('RETR %s' % files, open(files, 'wb').write)
	