#!/bin/bash
# Set Some Initial Variables
export OMP_NUM_THREADS=1
export MKL_NUM_THREADS=1
num_proc=28
step_num=00

# Header for README.md
echo "################" >> README.md
echo Automated output from step ${step_num} >> README.md
echo Running mlp train with ${num_proc} procs on ${OMP_NUM_THREADS} threads >> README.md

# Start Procs + timer
start=$SECONDS
mpirun -np ${num_proc} mlp train initial.mtp train.cfg --energy-weight=0.9 --force-weight=0.1 --valid-cfgs=test.cfg --max-iter=1000 --curr-pot-name=temp.mtp --trained-pot-name=trained.mtp
duration=$(( SECONDS - start ))
count=$(grep -c END train.cfg)
echo Training took ${duration} seconds to train on ${count} frames >> README.md
mlp select-add trained.mtp train.cfg train-big.cfg next_training.cfg --als-filename=${step_num}_state.als 
second=$(( SECONDS - duration - start ))
count=$(grep -c END train-big.cfg)
echo Select-add took ${second} seconds for ${count} frames to sort >> README.md
