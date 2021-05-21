#!/bin/bash
### Benchmarking tool ######################
# Files: threads - bash script appended to the end here. Used to declare threads
#        in.lmp  - script to mark
# Installs: lammps
############################################
# Check i procs x j thr (up to 32 total threads)
for i in 8 12; do
	for j in 2 4 6; do
		source threads ${j}
		mpirun -np ${i} lmp < in.lmp > out.${i}procs.${j}thr
	done
done


#** On many of my systems this is a **#
#** script in the .bin folder       **#
#### threads ##########################
# #!/bin/bash
# export OMP_NUM_THREADS=${1}
# export MKL_NUM_THREADS=${1}
#######################################
### > Spare Code ###

### < Spare Code ###
