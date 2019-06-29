#!/bin/bash

# View environment variables
#echo "The value of home variable is: "
#echo $HOME

# Current directory
#Method 1
#echo "The current directory is: "
#pwd

#Method 2
#echo "The current directory is: $(pwd)"

#Method 3
#dir=$(pwd)                                 # Do not add whitespace characters
#echo "The current directory is: ${dir}"

# Taking arguments while running script
# @ takes all the arguments given 
#echo "I saw ${@} on the command line"

# 1 takes only the first argumemt give
#echo "I saw ${1} on the command line"

# Read input from user
#echo "Enter a value: "
#read userInput
#echo "The value entered is: ${userInput}"

# Making file using user's input
#echo "Enter file extension:"
#read ext
#touch "yourfile.${ext}"

# Conditional statements in Bash 

# Method 1
#if [ -d /usr/bin ]; then
#	echo "The directory exists"
#else
#	echo "The directory doesn't exist"
#fi                                      # to end the conditional statement

# Method 2
if [ -d ${1} ]; then
	echo "the directory exists"
else
	echo "Doesn't exist"
fi

#if false; then echo 'yes'; else echo 'no'; fi
