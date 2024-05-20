#!/usr/bin/env python

import argparse
from typing import List, Optional

def renum_pdb(pdb: List[str], start: Optional[int] = None) -> List[str]:
    """
    Renumber residues in a PDB file starting from a given number.

    Args:
        pdb (List[str]): List of lines from a PDB file containing ATOM records.
        start (Optional[int]): The starting residue number. If None, starts from 1.

    Returns:
        List[str]: List of renumbered PDB lines.
    """
    curr_res = set()
    renumbered = []
    
    start = (start - 1) if start else 0
    
    for line in pdb:
        res_num = None
        res_tag = line[17:27]
        
        if res_tag in curr_res:
            res_num = f"{start:4d}"
            renumbered.append(line[:22] + res_num + line[26:])
        else:
            curr_res.add(res_tag)
            start += 1
            res_num = f"{start:4d}"
            renumbered.append(line[:22] + res_num + line[26:])
            
    return renumbered 

def get_atoms(infile: str) -> List[str]:
    """
    Extract ATOM lines from a PDB file.

    Args:
        infile (str): Path to the input PDB file.

    Returns:
        List[str]: List of ATOM lines from the PDB file.
    """
    coordinates = []
    with open(infile) as f:
        for line in f:
            if line.startswith("ATOM"):
                coordinates.append(line)
    return coordinates

def main():
    """
    Main function to parse command-line arguments and renumber residues in a PDB file.
    """
    parser = argparse.ArgumentParser(description="Renumber PDB file residues.")
    parser.add_argument("infile", help="Input PDB file")
    parser.add_argument("outfile", nargs="?", help="Output PDB file (not valid if --inline is used)")
    parser.add_argument("--start", type=int, default=1, help="Starting residue number (default: 1)")
    parser.add_argument("--inline", "-i", action="store_true", help="Edit the input file inline")

    args = parser.parse_args()

    if args.inline and args.outfile:
        parser.error("The --inline option cannot be used with an output file.")

    atoms = get_atoms(args.infile)
    renumbered_atoms = renum_pdb(atoms, args.start)
    
    if args.inline:
        outfile_path = args.infile
    else:
        outfile_path = args.outfile

    with open(outfile_path, 'w') as f:
        for line in renumbered_atoms:
            f.write(line)
        
if __name__ == "__main__":
    main()
