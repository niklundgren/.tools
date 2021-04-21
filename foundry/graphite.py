############ Graphite Creator ##################
# Makes graphite with the ASE library
# Run `python graphite.py ask` to be prompted for
# the required inputs.
# --Reqs------
# Modules: ASE
# Files: N/A
################################################
import sys
one = sys.argv[1]
if one.startswith('h'):
	print('Save graphite to coords.<format> (Defaults to xyz)')
	print('<x reps> <y reps> <layers> <a_const> <c_const> <format>')
from ase.io import write
from ase.lattice.hexagonal import *
print('Creating graphite unit cells')
print('Keep in mind a sheet with 1 layer corresponds to 2 graphene sheets')

extensions = { 'xyz':'xyz',
	'extxyz':'xyz',
	'lammps-dump-text':'lmp',
	'lammps-dump-binary':'lmp',
	'lammps-data':'lmp'}

# Collect input
if one == 'ask':
	try:
		m, n, layers = input('x y layers\n').split()
		print('DFT lattice constants: a=2.468A c=8.685A')
		constants = input('a c lattice constant (defaults to DFT vals)\n')
		if constants == '':
			a, c = 2.468, 8.865
		else:
			a, c = constants.split()
		format = input('format? (defaults to xyz)')
		if format == '':
			format = 'xyz'
		m, n, layers = int(m), int(n), int(layers) # convert to formats
		a, c = float(a), float(c)
		print('Printing %i x %i sheets with %i layers' % (m, n, layers))
		print('Lat a=%.5f c=%.5f' % (a, c))
		print('Filename: coords.%s' % extensions[format])
	except:
		print('Defaulting to 10 x 10 sheet with 2 layers')
		print('Using lattice constants a=2.468A c=8.685A')
		print('Writing to coords.xyz')
		m, n, layers= 10, 10, 2
		a, c = 2.468, 8.8685
		format = 'xyz'
else:
	try:
		m, n, layers, a, c, format = sys.argv[1:]
	except:
		print('Error parsing arguments')
		print('Use "python graphite.py ask"'+
			'or "python graphite.py help"')
		exit()
n_atoms = (m * n * 4) * layers
print('Creating %i atoms' % n_atoms)

atoms = Graphite('C',
		latticeconstant={'a':a, 'c':c},
		size=(m, n, layers))
write('coords.'+extensions[format],
	images=atoms,
	format=format)
