#!/usr/bin/env python
from .isolate_polymer import polymer_extract
from .check_database import check_database
from .check_database import remove_duplicates
from .check_database import search_names
from .monomer import strip_poly
from .monomer import get_pubchem_smiles
from .monomer import get_cirpy_smiles
from .monomer import lowercase
from .cde_function import cde_func
from .cde_function import uppercase
from .combine_names import combine_name_cde
from .combine_names import remove_duplicate_cde
from .callCDEsh import command_line_cde


