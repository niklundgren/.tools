import ase
import ase.io
from ase.io import *

atoms = read('coords.lmp',format='lammps-data', style='atomic')
write('coords.xyz', images=atoms, format='xyz')
