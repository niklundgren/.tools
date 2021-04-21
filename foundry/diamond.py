############ Diamond Creator ##################
# Makes diamond with the ASE library
# Run `python diamond.py ask` to be prompted for
# the required inputs.
# --Reqs------
# Modules: ASE
# Files: N/A
################################################
import sys
one = sys.argv[1]
if one.startswith('h'):
	print('Save diamond to coords.<format> (Defaults to xyz)')
	print('<xyz reps> <a_const> <format>')
	print('xyz reps can receive one or three separate integers')
from ase.io import write
from ase.build import diamond100 as diamond
print('Creating diamond unit cells, with 8 atom basis')

extensions = { 'xyz':'xyz',
	'extxyz':'xyz',
	'lammps-dump-text':'lmp',
	'lammps-dump-binary':'lmp',
	'lammps-data':'lmp'}

# Collect input
if one == 'ask':
	try:
		reps = input('cell reps x y z (defaults to perfect '+
					'cube if one value given)\n')
		try:
			x, y, z = reps.split()
		except:
			x, y, z = reps, reps, reps # arm day
		print('DFT lattice constants: a=3.567')
		a = input('a lattice constant (defaults to DFT vals)\n')
		if a == '':
			a = 3.567
		format = input('format? (defaults to xyz)\n')
		if format == '':
			format = 'xyz'
		x, y, z = int(x), int(y), int(z) # convert to formats
		a = float(a)
		print('Printing %i %i %i block with 8 atom basis' % (x, y, z))
		print('Lat a=%.5f' % a)
		print('Filename: coords.%s' % extensions[format])
	except:
		print('Defaulting to cube of 2, with DFT lat param')
		print('Writing to coords.xyz')
		x, y, z, a, format = 2, 2, 2, 3.567, 'xyz'
else:
	try:
		x, a, format = sys.argv[1:]
		y = z = x
	except:
		try:
			x, y, z, a, format = sys.argv[1:]
		except:
			print('Error parsing arguments')
			print('Use "python graphite.py ask"'+
				'or "python graphite.py help"')
			exit()
n_atoms = (x * y * z) * 8
print('Creating %i atoms' % n_atoms)
m, n, l = x*2, y*2, z*2
atoms = diamond('C',
		a=a,
		size=(m, n, l))
write('coords.'+extensions[format],
	images=atoms,
	format=format)
