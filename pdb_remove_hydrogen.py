#!/usr/bin/env python
"""
MIT License

Copyright (c) 2023 Sunandan Mukherjee

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import re
import argparse

def filter_hydrogen_atoms(input_filename, output_filename):
    """
    Filter out lines representing hydrogen atoms from a PDB file.

    Parameters:
        input_filename (str): Input PDB file name.
        output_filename (str): Output PDB file name (optional).

    Returns:
        None
    """
    try:
        with open(input_filename, 'r') as input_file:
            if output_filename:
                with open(output_filename, 'w') as output_file:
                    for line in input_file:
                        # Use a regular expression to check if "H" is present in columns 13 to 17
                        if not re.search(r'^H', line[12:17].strip()):
                            output_file.write(line)
            else:
                for line in input_file:
                    if not re.search(r'^H', line[12:17].strip()):
                        print(line, end='')  # Print lines without hydrogen atoms
    except FileNotFoundError:
        print("File not found. Please check the file path.")
    except Exception as e:
        print("An error occurred:", str(e))

def main():
    parser = argparse.ArgumentParser(description="Filter out lines representing hydrogen atoms from a PDB file.")
    parser.add_argument("input_filename", help="Input PDB file name")
    parser.add_argument("-o", "--output_filename", help="Output PDB file name (optional)")

    args = parser.parse_args()

    input_filename = args.input_filename
    output_filename = args.output_filename

    filter_hydrogen_atoms(input_filename, output_filename)

if __name__ == "__main__":
    main()
