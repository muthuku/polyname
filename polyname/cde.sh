#!/bin/bash
#echo 'Input a file name'

#read input
file="/cde_extract_example/test_articles_html/example14.json"

while read line; do
	echo $line
done < $file

cat $file

cde extract $file -o article14.json
#cde tokenize sentences $file 
#cde tokenize words $file

#cde pos tag $file