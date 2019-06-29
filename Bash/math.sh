#!/bin/bash

# Only supports integer arithmetic
# Cannot deal with floating point numbers

# (()) double brackets are for expressions
if [ $((${1} % 2)) -eq 0 ]                  # Give space after 0 and ]
then 
	echo "Even"
else
	echo "Odd"
fi
