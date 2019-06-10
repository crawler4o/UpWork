#!/bin/bash

str="hey do you love bashing, i meant scripting"
echo Please enter a single character
read line

if [[ $str == *"$line"* ]]; then 
	echo The letter is in the string
else  
	echo 'the letter is not on the string'
	exit
fi

declare -a -g arr
echo $str | fold -w1 | while read line; do
	#echo $line
	arr=("${arr[@]}" "${line}")
	echo ${arr[@]}	
done
