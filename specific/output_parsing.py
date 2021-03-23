import numpy as np
import subprocess as sp
from glob import glob

files = ['comparison.dat', 'compare1k.dat', 'compare5k.dat']
for file in files:
	print(file)
	f = open('dlp/'+file, 'r')
	data = f.readlines()
	total = 0
	counts = 0
	for type in ['Defects', 'Amorphous_Bulk', 'Crystalline_Bulk', 'Crystalline_RSS', 'Fullerenes', 'Nanotubes', 'Graphene_Layer_Sep', 'SACAPA', 'Liquid_Interface', 'Liquid', 'Graphite', 'Graphene', 'Graphite_Layer_Sep', 'LD_Iter1']:
		letters = len(type)
		count = 0
		lines = []
		for n in range(len(data)):
			line = data[n]
			if line.startswith(type):
				count +=1
				lines.append(n)
				replacement = line[letters:]
				replacement = replacement.strip()
				data[n] = replacement
		errors = 0
		for n in range(len(lines)):
			line = data[lines[n]]
			if line.startswith('0.000') or line.startswith('-0.000'):
				errors += 1
		if count == 0:
			ratio = 0
		else:
			ratio = errors/count
		print(type)
		print('Failure Ratio: %.2f' % ratio)
		print('Total Samples: %i, Total Errors: %i' % (count, errors))
		total += count
		counts += errors

print('Grand Total\nFailure: %.2f\nTotal Samples:%i\nTotal Errors:%i' % ((counts/total), total, counts))
