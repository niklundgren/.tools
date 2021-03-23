#!/bin/bash
echo "Select Python input (without .py ext)"
read file
pyth=${file}.py
echo Running $file

#python file
python ${pyth} > logs/${file} 2>&1 & disown
echo Log, stdin and stderr directed to logs/${file}
