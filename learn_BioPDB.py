#!/usr/bin/env python
#-*- coding:utf-8 -*-

import os
import sys
from Bio.PDB import PDBParser
from Bio.PDB import PDBIO
    
three = ["GLY","ALA","VAL","LEU","ILE","SER","THR","CYS","MET","GLU","ASP","GLN","ASN","LYS","ARG","HIS","PRO","PHE","TYR","TRP"]
one = ["G","A","V","L","I","S","T","C","M","E","D","Q","N","K","R","H","P","F","Y","W"]
d_map = dict(zip(three,one))

pdb_path = os.path.join(os.getcwd(),"Q86SJ6.pdb")
ifile_pdb = PDBParser()
structure = ifile_pdb.get_structure("Q86SJ6",pdb_path)
        
for model in structure:
    model_id = model.get_id()
    print model_id
    for chain in model:
        chain_id = chain.get_id()
        residues = chain.get_residues()
        l_pos = []
        l_seq = []
        print chain_id
        for residue in residues:
            residue_id = residue.get_id()
            residue_pos = residue_id[1]
            hetfield = residue_id[0]
            print residue_id
            if hetfield[0] == " ":
                print "1"
                l_pos.append(residue_pos)
                resname = residue.get_resname()
                l_seq.append(d_map[resname])
        seq = "".join(l_seq)
