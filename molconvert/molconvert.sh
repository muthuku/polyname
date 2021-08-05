#!/bin/bash
export PATH=$PATH:/Applications/MarvinSuite/bin

file=$1

while read line; do
	echo $line
done < $file

cat $file

#cde extract $file -o results.json
#cde tokenize sentences $file 
#cde tokenize words $file

molconvert name $file -o names_mol.txt