#!/bin/bash

echo 'insert 3 numbers'

read num[0]
echo ok
read num[1]
echo ok
read num[2]
echo ok

while ! [[ "${num[0]}" =~ ^[0-9]+$ ]] | [[ "${num[1]}" =~ ^[0-9]+$ ]] | [[ "${num[2]}" =~ ^[0-9]+$ ]]; do
            echo "Sorry integers only"
	    read num[0]
	    echo ok
	    read num[1]
	    echo ok
	    read num[2]
	    echo ok
    done



if [ ${num[0]} -gt ${num[1]} ]; then
	a=${num[0]}
	num[0]=${num[1]}
	num[1]=$a
fi

if [ ${num[2]} -lt ${num[0]} ]; then
	num=("${num[2]}" "${num[@]:0:2}")
fi

if [ ${num[2]} -lt ${num[1]} ]; then
	num=("${num[0]}" "${num[2]}" "${num[1]}")
fi

echo So the ordered array is
echo ${num[@]}
