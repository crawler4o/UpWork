#!/bin/bash

declare -i num1
declare -i num2
echo 'Please enter the first number'
read num1
echo 'Please enter the second number'
read num2


if [ $num1 -gt $num2 ];
then
	echo 'Number one is greater'
	
elif [ $num1 -lt $num2 ];
then
	echo 'Number two is greater'

else
	echo 'Both are equal'
fi
