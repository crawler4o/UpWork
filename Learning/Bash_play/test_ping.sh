#!/bin/bash

while ping www.dir.bg -n 1 &> /dev/null
do
	echo 'cool, there is ping'
done
