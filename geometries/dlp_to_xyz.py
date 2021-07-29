from ase.io import read,write

inputfile='CONFIG'
outputfile='replicated_atoms.xyz'

for x in (0, 5, 10, 15, 20, 25, 50, 75, 90, 100):
	atoms = read(str(x)+'/'+inputfile, format='dlp4')
	write(str(x)+'/'+outputfile, images=atoms, format='xyz')

