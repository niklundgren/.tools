# Creates LAMMPS input files for Diamond
from ase.io import read,write
import numpy as np
import os

dir = './'
atoms = read(dir+'unit.xyz')

# Replicate the unit cell 'nrep'=5 times
#nrep = 6
#supercell = np.array([nrep, nrep, nrep])

# Generate input files for LAMMPS and replicated super cell structure
write(dir+'diamond.lmp', format='lammps-data', images=atoms)
write('replicated_atoms.xyz', format ='extxyz', images=atoms.copy().repeat(supercell))
positions = atoms.copy().repeat(supercell).positions
maxes = np.max(positions, axis=0)
mins = np.min(positions, axis=0)
sizes = np.round(maxes - mins, 2)
lent = len(atoms.copy().repeat(supercell))

# Print reminder information
print('Supercell structures and LAMMPS input generated for %i atoms' % lent)
print('Supercell dimension is: ' + str(supercell))
print('Supercell size is: ' + str(sizes[0]) + ' '
	+ str(sizes[1]) + ' '
	+ str(sizes[2]) + 'A')
