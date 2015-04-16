#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import glob

dist_files = glob.glob("*.dist")

for files in dist_files:
	new_base = '.'.join(files.split('.')[:-1])	
	x = np.loadtxt(files)
	# for rows in x:
	# 	if rows[3] == 1.0:
	# 		print rows
	# 		x_min = int(rows[0])
	# 		y_max = int(rows[1]/2)
	# 		break
	# 	else:
	# 		pass
	# for rows in x:
	# 	if sum(rows) == 0:
	# 		pass
	# 	elif rows[1] == 0:
	# 		print rows
	# 		x_max = rows[0]
	# 		break
	# 	else:
	# 		pass
	# print x_min, x_max, y_max
	plt.figure()
	plt.axis(xmin=1, xmax=30000, ymax=100)
	plt.axes().xaxis.grid(True)
	plt.plot(x[:,0], x[:,1])
	plt.savefig(new_base+'_all.png', bbox_inches='tight')
	# plt.axis(xmax=2000,ymax=50)
	# plt.plot(x[:,0], x[:,1])
	# plt.savefig(new_base+'_low.png', bbox_inches='tight')
	# plt.figure()
	# plt.axis(xmin=2000, xmax=8000, ymax=50)
	# plt.plot(x[:,0], x[:,1])
	# plt.savefig(new_base+'_high.png', bbox_inches='tight')
	