import subprocess as sp
import sys
from ase.io import read,write
from ase.lattice.hexagonal import *
import numpy as np
import os

folder='./'
# Make unit cell, really big C constant so only one sheet.
a = <s>; c = <c>;
atoms = Graphene('C', latticeconstant={'a':a, 'c':c}, size=(1, 1, 1), pbc=(1,1,1))

# Generate input files for LAMMPS and replicated super cell structure
write(folder+'graphene.lmp', format='lammps-data', images=atoms)
write(folder+'replicated_atoms.xyz', format ='extxyz', images=atoms.copy().repeat(supercell))
positions = atoms.copy().repeat(supercell).positions
maxes = np.max(positions, axis=0)
mins = np.min(positions, axis=0)
sizes = np.round(maxes - mins, 3)
lent = len(atoms.copy().repeat(supercell))

# Print reminder information
print('Supercell structures and LAMMPS input generated for %i atoms' % lent)
print('Supercell dimension is: ' + str(supercell))
print('Supercell size is: ' + str(sizes[0]) + 'A '
	+ str(sizes[1]) + 'A '
	+ str(sizes[2]) + 'A')
