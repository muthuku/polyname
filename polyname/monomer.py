#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import numpy as np
import itertools
import pubchempy as pcp
import cirpy

def strip_poly(row,stripstrings):
    s = row.polyname
    new_list = []
    for stripstring in stripstrings:
        lstart = len(stripstring[0])
        lend = len(stripstring[1])
        if s[:lstart]==stripstring[0]:
            sreturn = s.replace(stripstring[0],'')
            if lend!=0:
                sreturn = sreturn[:-lend]
            row.polymername = sreturn
        else:pass
        if "-alt-" in row.polymername:
            row.polymername = row.polymername.split('-alt-')
        if "-co-" in row.polymername:
            row.polymername = row.polymername.split('-co-')
    if isinstance(row.polymername,list):
        return row.polymername
    else:
        return [row.polymername]
# Strip polymer nomenclature
stripstrings = [
               ['poly(',')'],
               ['poly[(',')]'],
               ['poly[',']'],
               ['poly{','}'],
               ['poly-','']
               ]

def get_pubchem_smiles(monomer_name):
    smile_list = []
    for name in monomer_name:
        mname = name.replace("(", "")
        mname = mname.replace(")", "")
        result = pcp.get_compounds(mname, 'name')
        if result == []:
            smile_list.append("None")
        else:
            smile = result[0].isomeric_smiles
            smile_list.append(smile)
    return smile_list

def get_cirpy_smiles(monomer_name):
    cirpy_smiles = []
    for name in monomer_name:
        mname = name.replace("(", "")
        mname = mname.replace(")", "")
        smiles = cirpy.resolve(mname, 'smiles')
        if smiles is None:
            cirpy_smiles.append("None")
        else:
            cirpy_smiles.append(smiles)
    return cirpy_smiles




