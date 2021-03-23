# useful grep expression
# returns unique results from a regex expression
grep -oP 'config_type=\K\w+' gap_carbon.xyz | sort --unique

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

## Find text in files
grep <exp> file
	# -c = counts
	# -n = line number
	# -r = all files in dir
	# -v <pattern> = excludes pattern

# Bash stuff
 <c1> | <c2> #pipes the output of one command to the next


