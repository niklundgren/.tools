########## Transform.py ########################
# Transform coordinates to lammps compatible box
################################################
import sys
try:
	files = sys.argv[1:]
except:
	print('Usage: python transform.py <file>')
from ase.calculators.lammpslib import convert_cell
from ase.io import read,write
from ase.build import bulk
import numpy as np

print('queue', files)
for file in files:
	atoms = read(file)
	cell, transformation = convert_cell(atoms.cell)
	positions = atoms.get_positions()
	bounds = np.max(positions, axis=0)
	new = np.zeros_like(positions)
	for i in range(len(atoms)):
	    new[i] = np.dot(transformation, positions[i].T)
	atoms.set_positions(new)
	#write(file, images=atoms, format='xyz')

	# Comparison
	print(file)
	print('Old Coords')
	print('max:', np.max(positions, axis=0))
	print('min:', np.min(positions, axis=0))
	print('ave:', np.mean(positions, axis=0))

	print('\n\nTransformed Coords')
	print('max:', np.max(new, axis=0))
	print('min:', np.min(new, axis=0))
	print('ave:', np.mean(new, axis=0))

	tilt = cell.flatten(order='C')
	print('xy: %.5f' % tilt[1])
	print('xz: %.5f' % tilt[2])
	print('yz: %.5f' % tilt[5])

	print('bounds', bounds)

	print('cell', cell)
	print('trans', transformation)
