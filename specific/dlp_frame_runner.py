from ase.io import read,write
from datetime import date
import subprocess as sp
import numpy as np

###### Parameters ###############################################################
# num frames
# uncomment to run all frames, else create a value
# num_frames = int(sp.check_output(['grep', 'Lattice', 'gap.xyz', '-c']).strip())
num_frames = 10000
offset = 6000 # first 1000 frames done in dlp/compare1k.dat

# num procs
# For AMD Threadrippers ~32 would be pushing it. Reccomended 12-24
num_procs = 16

# Working directory
dir = 'dlp/'

# buffering -1 = sys default, 0 = unbuffered,
# 1 = line buffered, n = buffer of that size
energy_out = open(dir+'comparison.dat', 'w', buffering=1)
#print('GAP energy      NN energy      % diff      num diff', file=energy_out) # headers (style 1)
print('type        GAP energy (??)      NN energy (kJ/mol)      ratio', file=energy_out) # headers (style 2)

# DLPOLY output
dlp_out_name = 'out.dlp'
dlp_out = open(dlp_out_name, 'w', buffering=20)
print('DLPOLY OUTS FOR NN CALCULATIONS '+str(date.today()), file=dlp_out)
###### Program #################################################################
ratios = np.zeros(num_frames)
for n in range(num_frames):
	# read in frame
	atoms = read('gap.xyz', format='extxyz', index=(n+offset))
	size = atoms.get_global_number_of_atoms()
	type = atoms.info['config_type']
	E_gap = atoms.info['energy']

	### DLPOLY
	# write control files
	write(dir+'CONFIG', images=atoms, format='dlp4')
	with open(dir+'FIELD0') as f:
		text = f.readlines()
	text[4] = 'NUMMOLS '+str(int(size))+'\n'
	with open(dir+'FIELD', 'w') as f:
		f.writelines(text)
	# run process
	sp.call('mpirun -n '+str(num_procs)+' DLPOLY.X > outs.dlp',
		cwd=dir[:-1],
		shell=True)
	failed = False
	# grep energy
	try:
		nn_output = sp.check_output(['grep',
					'!',
					dir+'OUTPUT'])
		nn_output = nn_output.split()
		E_nn = float(nn_output[3])
	except:
		E_nn = 0
		failed = True
		print('Failed on type: '+str(type), dlp_out)
	E_ratio = E_nn/E_gap

	print("%s \t %.3f \t    %.3f \t    %.3f\n" % (type, E_nn, E_gap, E_ratio), file=energy_out)
	print(str(n)+" done")
	ratios[n] = E_ratio

print(np.mean(ratios))
sp.check_output(['grep',
		'Failed',
		'-c',
		'log'])
