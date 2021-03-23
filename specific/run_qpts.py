import numpy as np
import subprocess as sp
import time
import sys
import os

lst = sys.argv[1:]
for x in lst:
	# Initialize variable names
	dir = 'q'+str(x)+'_'+str(x)+'_0'
	q_vec = str(x)+'. '+str(x)+'. 0.'
	files_to_move = ['Dyn.form', 'DYNMAT', 'THIRD']
	files_to_copy = ['CONFIG', 'CONTROL', 'OUTPUT']

	# Setup Directories
	if os.path.exists(dir):
		print(x+' is already calculated')
		#continue
	else:
		os.mkdir(dir)

	# Edit control File
	with open('CONTROL0') as f:
		text = f.readlines()
	text[11] = 'qvec '+q_vec+' third'
	with open('CONTROL', 'w') as f:
		f.writelines(text)

	# Run baby run
	print('Running '+q_vec)
	start = time.time()
	sp.run('mpirun -n 8 DLPOLY.X', shell=True)
	print(q_vec+' completed')
	stop = time.time(); total = (stop-start)/60
	print('Time Running '+q_vec+':\n '+str(total))

	# Move and copy outputs
	for f in files_to_move:
		os.rename(f, dir+'/'+f)
	for f in files_to_copy:
		sp.run('cp '+f+' '+dir+'/'+f, shell=True)

	print(q_vec+' data stored!')
