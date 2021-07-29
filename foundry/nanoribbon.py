import numpy as np
from ase.io import write
from ase.build import graphene_nanoribbon as gnr

a = 2.4662

atoms = gnr(1, 1,
	type='armchair',
	C_C=a/np.sqrt(3))

# ase writes it in x z
# >>> switch to x y >>
x = atoms.positions[:, 0]
y = atoms.positions[:, 1]
z = atoms.positions[:, 2]
atoms.positions[:, 1] = z
atoms.positions[:, 2] = y

# ase makes a 1d cell,
# >>> 3d cell for lammps >>>
x = a
y = 2 * 2 * np.sin(60) * (a/3)
z = 30
cell = np.eye(3) * [x, y, z]
atoms.set_cell(cell)

write('ac-nanoribbon.lmp', images=atoms, format='lammps-data')
write('ac-nanoribbon.xyz', images=atoms, format='xyz')
