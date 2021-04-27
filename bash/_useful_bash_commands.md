########## BASH BASICS #####################################
<c1> | <c2> #pipes the output of one command to the next

# for loop
for x in <list of stuff>
do
	<cmds>
done

# if else
if [${1} == 2]; then

else

fi

########## TEXT MANIPULATION ##############################
# returns unique results from a regex expression
grep -oP 'config_type=\K\w+' gap_carbon.xyz | sort --unique
# returns counts of unique results from a regex expression
grep -oP "config_type\s\K\w*" test.cfg | sort | uniq -c

## Find text in files
grep <exp> file
	# -c = counts
	# -n = line number
	# -r = all files in dir
	# -v <pattern> = excludes pattern
	# -oP "<pattern>"= use regex


############### SYSTEM ADMINISTRATION #######################
## Check for library
ldconfig -p | grep <library>
gcc -l<library> # returns "undefined reference to 'main'"

## Count CPUS
htop - show cores and usage!
lspcu
cat /proc/cpuinfo
top (press 1 to view cores, then 3 after loading to find a node)

## Check GPUs
nvidia-smi

## Find files
locate <filename>
# searches whole file system, pipe to grep
find <dir_to_search> --name <filename>

######### TIMING ###########################################
# Run stuff for a certain amount of time
timeout <t><s/m/h> <command>
# Run stuff after a certain amount of time
sleep <t><s/m/h>; <command>
