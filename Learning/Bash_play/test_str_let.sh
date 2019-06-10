#!/bin/bash

str="hey do you love bashing, i meant scripting"
echo Please enter a single character
read line

if [[ $str == *"$line"* ]]; then 
	echo The letter is in the string
else  
	echo 'The letter is not on the string'
	exit
fi


arr=$(echo $str | fold -w1)
echo $arr
pos=0
tim=0
for i in $arr;do
    if [ $i == $line ]; then
        echo We have $line on position $pos
        ((tim++))
        fi

    ((pos++))
    done
echo We have $line $tim times
