#!/bin/bash
#echo 'Input a file name'

#read input
file=$1

while read line; do
	echo $line
done < $file

cat $file

cde extract $file -o $file.json

#cde tokenize sentences $file 
#cde tokenize words $file

#cde pos tag $file