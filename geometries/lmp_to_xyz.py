import ase
import ase.io
from ase.io import *
import sys

try:
	atoms = read('coords.lmp', format='lammps-data', style='atomic')
except:
	try:
		atoms = read('coords.lmp', format='lammps-dump-text')
	except:
		print('Wrong format in coords.lmp')
		exit()
sym = atoms.get_chemical_symbols()

if sys.argv[1] == None:
	in_sym = input('Give chem symbol')
else:
	in_sym = sys.argv[1]

sym = [in_sym] * len(sym)
atoms.set_chemical_symbols(sym)
write('coords.xyz', images=atoms, format='xyz')
