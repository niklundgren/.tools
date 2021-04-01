### Lammps Scripting
This is a directory for unloading helpful lammps scripts that are designed to do one off
calculations (e.g. dynamical matrix and third order matrix calculations) as
well as for sets of scripts designed to accomplish a goal (e.g. the melt
quench set).

# Files
make-diamond-unitcell.lmp # input file for creating diamond unit cell


# General Script
units <units type>
processors x y z	(processor allocation 1 2 1 
			allocates 2 processors and splits 
			the atoms in the xz plane)
boundary p p p		(periodic boundaries)
atom_style <style>	(options are atomic and full (adjusts output info)
atom_modify map yes	(maps atom id's to processors with array or hash)
read_data <filename>	(This is where you put your atoms.lmp file)

pair_style		(Load atomic potential data)
pair_coeff

mass 1			(specify atomic masses of each group)
mass ...

<commands>		(e.g. dynamical_matrix <args>)
