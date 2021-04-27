#!/bin/bash
for iter in 10.2 10.4 10.6 10.8 11.00 11.2
do
   sed "s/xxxx/${iter}/g" template.scf.in > scf.in
   mpirun -np 4 ~/Programs/QE/qe-6.3/bin/pw.x < scf.in > scf${iter}.log
   grep ! scf${iter}.log >> energies.dat
done

