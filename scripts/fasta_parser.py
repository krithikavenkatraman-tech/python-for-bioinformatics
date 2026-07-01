"""
FASTA File Parser

Description:
Reads and displays sequences stored in
FASTA format.
"""

filename = "sample.fasta"

with open(filename, "r") as file:

    for line in file:

        if line.startswith(">"):

            print("\nHeader")

            print(line.strip())

        else:

            print("Sequence")

            print(line.strip())
