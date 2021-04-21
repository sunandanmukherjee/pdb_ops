#!/usr/bin/env python

import sys

def renum_pdb(pdb, start=None):
    curr_res = set()
    renumbered = []
    
    if start:
        start = start-1
    else:
        start = 0
    
    for line in pdb:
        res_num = None
        res_tag = line[17:27]
        
        if res_tag in curr_res:
            res_num = str("%4d" %start)
            renumbered.append(line[:22]+res_num+line[26:])
        else:
            curr_res.add(res_tag)
            start += 1
            res_num = str("%4d" %start)
            renumbered.append(line[:22]+res_num+line[26:])
            
    return renumbered 
        
def get_atoms(infile):
    coordinates = []
    for line in open(infile).readlines():
        if line.startswith("ATOM"):
            coordinates.append(line)
    return coordinates

def main():
    infile = sys.argv[1]
    outfile = open(sys.argv[2], 'w')
    
    for line in renum_pdb(get_atoms(infile)):
        outfile.write(line)
    outfile.close()
        
if __name__ == "__main__":
    main()
    
