"""
Nucleotide Counter

Description:
Counts the frequency of nucleotides
within a DNA sequence.
"""

def count_nucleotides(sequence):

    sequence = sequence.upper()

    counts = {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }

    return counts


if __name__ == "__main__":

    dna = input("Enter DNA sequence: ").strip()

    result = count_nucleotides(dna)

    print("\nNucleotide Counts")

    for base, count in result.items():
        print(f"{base}: {count}")
