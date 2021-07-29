######## DISTANCE CALCULATOR ###################################
### Calculates inverse neighbor matrix where larger
### numbers correspond to atoms in closer proximity
################################################################
import numpy as np
from ase.io import read

def distances(frame, minmax=True, normalize=False, reciprocal=False):
	atoms = frame.positions
	n = len(atoms);	k = 0
	distances = np.zeros((n, n))
	for i in range(len(atoms)):
		iat = atoms[i]
		for j in range(len(atoms)):
			jat = atoms[j]
			norm = np.linalg.norm(np.subtract(iat, jat))
			distances[i, j] = norm
			k+=1
	if minmax:
		mean = np.mean(distances)
		diagonals = np.zeros(n)
		# exclude diagonals
		for i in range(len(atoms)):
			diagonals[i] = distances[i, i]
			distances[i] = mean
		print('min', np.min(distances))
		print('max', np.max(distances))
		for i in range(len(atoms)):
			distances[i, i] = diagonals[i]
	if normalize:
		distances = np.divide(distances, dmax)

	if reciprocal:
		dmax = np.max(distances)
		for i in range(len(atoms)): # clear diagonal
			distances[i, i] = dmax
		distances = np.reciprocal(distances)
	return distances

def bounding_box(frame):
	positions = frame.positions
	return np.max(positions, axis=0)

traj = read('trajectory.xyz', format='xyz', index=':')
box = bounding_box(traj[0])
print(box)

#### SCRAP CODE ---> ###############
# forming a lower right triangle in a neighbor matrix
# distances = np.zeros((np.floor_divide(n, 2)*n) +
#		(n % 2) * (np.floor_divide(n, 2) + 1))
#for frame in traj:
#	new_box = bounding_box(frame)
#	if np.linalg.norm(np.subtract(box, new_box)):
#		print('uhoh')
#for frame in traj:
#	distances(frame)

### <----- SCRAP ###################
