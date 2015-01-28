import numpy as np
import matplotlib.pyplot as plt
import glob

dist_files = glob.glob("*.dist")

for files in dist_files:	
	x = np.loadtxt(files)
	plt.figure()
	plt.axis(xmax=2000,ymax=50)
	plt.plot(x[:,0], x[:,1])
	plt.savefig(files+'_low.png', bbox_inches='tight')
	plt.figure()
	plt.axis(xmin=2000, xmax=8000, ymax=50)
	plt.plot(x[:,0], x[:,1])
	plt.savefig(files+'_high.png', bbox_inches='tight')
