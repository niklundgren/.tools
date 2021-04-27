# COMMAND LINE UTILS
ctrl-u - cuts before cursor
crtl-y - pastes

# bang commands ##################################
# searches your commandline history 
# with regex under the hood
!! - reruns last command
	protip - sudo !!
	after failed command that needs sudo

!<exp> - executes the last command that startswith the exp
example: !mpirun - reruns your last mpirun command

!?<exp> - executes the last command that matches the exp
example: !?xyz - reruns your last command that used an xyz file
		(e.g. python converter.py <f>.xyz)

!-<n> - executes the n-th last command you used
example: !-3 runs the command you gave three commands ago

!<arg>:s^<old>^<new> - executes a command with substituded regex
example !!:s^file1^file2 reruns the last command with file2

!:p - prints your last command

### bang arguments
<cmd> !:n - executes command with arguments from nth command ago
example: lmp !:1 reruns lammps with the last flags you used

<cmd> !$ - repeats last arguments


