#!/bin/bash

# Method 1
#for i in $(seq 10); do 
#	echo "Value is: ${i}"
#done

# Method 2
#for i in $(seq 10)
#do
#    echo "Value is: ${i}"
#done

# Method 3 (useful directly in shell)
#for i in $(seq 10); do echo "${i}"; done

#All 3 above works, new line is a semi-colon separator

for i in $(ls)
do 
	echo ${i}
done
