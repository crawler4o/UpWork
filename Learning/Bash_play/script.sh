#!/bin/bash

declare -i n
n=0
cat test.txt | while read line; 
do
echo $n " " $line
n+=1

done
