import ase
import ase.io
from ase.io import *

atoms = read('coords.pdb',format='proteindatabank')
write('coords.'+i+'.xyz',atoms, format='xyz')
