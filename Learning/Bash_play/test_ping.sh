#!/bin/bash

while ping 192.168.1.76 -n 1 &> /dev/null
do
	echo 'cool, there is ping'
done
