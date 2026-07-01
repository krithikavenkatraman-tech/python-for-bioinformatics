"""
Motif Finder

Description:
Find all occurrences of a motif within
a DNA sequence.
"""

def find_motif(sequence, motif):

    sequence = sequence.upper()
    motif = motif.upper()

    positions = []

    for i in range(len(sequence)-len(motif)+1):

        if sequence[i:i+len(motif)] == motif:
            positions.append(i+1)

    return positions


if __name__ == "__main__":

    sequence = input("Enter DNA sequence: ").strip()

    motif = input("Enter motif: ").strip()

    print("\nMotif Positions")

    print(find_motif(sequence, motif))
