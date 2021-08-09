#!/usr/bin/env python
#COMMAND LINE TEST-works in terminal
#import certain functions needed for command line 
from polyname import command_line_cde
from polyname import extract_names
from polyname import remove_duplicates_list
import pandas as pd

#call the name of the file in the command line function
file = "example2.json"
command_line_cde(file)
#extract names from outputted "results.json" file 
list_of_CEMS = extract_names("{}.json".format(file))
print(list_of_CEMS)
#remove duplicates from this list and out put a final list
final_list = remove_duplicates_list(list_of_CEMS)
#put it into a df
df = pd.DataFrame(final_list, columns = ["All_names"])
print(df)
df.to_csv("names_extracted_cde_command_line.txt", header = True, index = False)

#check cde_command_line folder for outputs
