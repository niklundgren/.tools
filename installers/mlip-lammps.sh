#!/bin/bash
# Builds a lammp build with the MLIP interface
# ** Make sure to have copied lib_mlip_interface.a from the MLIP build
# into this folder! **
git clone https://github.com/lammps/lammps mylammps
bash preinstall.sh
bash install.sh mylammps g++_openmpi > out.install
