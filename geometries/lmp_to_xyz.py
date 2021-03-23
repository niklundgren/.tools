import ase
import ase.io
from ase.io import *

conc = [15,20,25,50,75,100]
for c in conc:
	x = str(c)
	atoms = read('coords.'+i,format='lammps-data')
#	sym = atoms.get_chemical_symbols()
#	sym[sym == 'H'] = 'Si'
#	atoms.set_chemical_symbols(x)
	write('outs/xyz_structures/aSiGe2k_C'+x+'.xyz',atoms, format='xyz')
