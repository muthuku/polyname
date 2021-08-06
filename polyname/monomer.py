#!/usr/bin/env python
# coding: utf-8

# In[32]:


import pandas as pd
import numpy as np
import itertools
import pubchempy as pcp
import cirpy

def lowercase(anylist):
    '''a function that takes the list of polymers and makes it lowercase
    input:
        anylist:
            description: a list of uppercase polymer names
            type: list
            example: Poly(butadiene), Poly(vinyl alcohol)]
    returns: a list of polymer names'''

    final_poly = []
    for string in anylist:
        string1 = string.lower()
        final_poly.append(string1)
    return final_poly

def strip_poly(row,stripstrings):
    '''goes through each row of a dataframe and strips it down to just monomer names
    inputs:
        row:
            decription: polymer name
            type: string
            example: poly(butadiene)
        stripstring:
            description: all the different poly names to strip away
            type: list of things to strip
            example: [
               ['poly(',')'],
               ['poly[(',')]'],
               ['poly[',']'],
               ['poly{','}'],
               ['poly-','']
               ]
        retunrs: monomer names'''
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
    '''function that gives the SMILE string for each polymer name using Pubchem API
    inputs:
        monomer_name:
            description:list of monomer names
            type: list
            example: [butadiene,ester,carbon]
    return: a SMILE string from pubchem'''
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
    '''function that gives the SMILE string for each polymer name using CIRPY API
    input:
        monomer_name: 
            description: list of monomer names
            type: list
            example: [butadiene,ester,carbon]
    return: a list of SMILE string from CIRPY'''
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

def get_pubchem_names(monomer_name):
    '''function that gives the iupac name for each polymer name using Pubchem API
    input:
        monomer_name:
            description: list of monomer names
            type: list
            example: [butadiene,ester,carbon]
        return: a list of SMILE string from CIRPY'''
    names_list = []
    for name in monomer_name:
        mname = name.replace("(","")
        nmane = mname.replace(")","")
        result = pcp.get_compounds(mmane,'name')
        if result == []:
            names_list.append("None")
        else:
            name = result[0].iupac_name
            names_list.append(name)
    return names_list

def get_cirpy_names(monomer_name):
    '''function that gives the iupac name for each polymer name using Pubchem API
        input:
            monomer_name:
                description: list of monomer names
                type: list
                example:[butadiene,ester,carbon]
        return: list of SMILE strings from cirpy'''
    cirpy_names = []
    for name in monomer_name:
        mname = name.replace("(", "")
        mname = mname.replace(")","")
        name= cirpy.resolve(mname, 'iupac_name')
        if name is None:
            cirpy_names.append("None")
        else:
            cirpy_names.append(name)
    return cirpy_names




