import ase
import ase.io
from ase.io import *
import sys

idx = string(sys.argv[1])
atoms = read('coods'+idx+'.xyz', format='xyz')
write('coords'+idx+'.lmp', images=atoms, format='xyz')
