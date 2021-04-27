#!/bin/bash
### Benchmarking tool ######################
# Files: threads - bash script appended to the end here. Used to declare threads
#        in.lmp  - script to mark
# Installs: lammps
############################################
# Check i procs x j thr (up to 32 total threads)
for i in 1 2 4 8; do
	for j in 1 2 4; do
		source threads ${j}
		mpirun -np ${i} lmp < in.lmp > out.${i}procs.${j}thr
	done
done
for i in 8; do
	for j in 1 2 4; do
		source threads ${i}
		mpirun -np ${j} lmp < in.lmp > out.${j}procs.${i}thr
	done
done

# threads
# #!/bin/bash
# export OMP_NUM_THREADS=${1}
# export MKL_NUM_THREADS=${1}



### > Spare Code ###

### < Spare Code ###
