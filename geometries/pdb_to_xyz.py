import ase
import ase.io
from ase.io import *

for i in range(1,8):
	i = str(i)
	atoms = read('coords.'+i+'.pdb',format='proteindatabank')
	write('coords.'+i+'.xyz',atoms, format='xyz')
