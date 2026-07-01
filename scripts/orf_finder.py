"""
Open Reading Frame (ORF) Finder

Description:
Identifies potential Open Reading Frames (ORFs)
by locating start codons (ATG) and terminating
at the nearest stop codon.

Applications:
- Gene Prediction
- Genome Annotation
"""

STOP_CODONS = {"TAA", "TAG", "TGA"}


def find_orfs(sequence):

    sequence = sequence.upper()

    orfs = []

    for i in range(len(sequence) - 2):

        codon = sequence[i:i+3]

        if codon == "ATG":

            for j in range(i + 3, len(sequence) - 2, 3):

                stop = sequence[j:j+3]

                if stop in STOP_CODONS:

                    orf = sequence[i:j+3]

                    orfs.append({
                        "Start": i + 1,
                        "End": j + 3,
                        "Length": len(orf),
                        "Sequence": orf
                    })

                    break

    return orfs


if __name__ == "__main__":

    dna = input("Enter DNA sequence: ").strip()

    orfs = find_orfs(dna)

    print("\nPotential ORFs\n")

    if not orfs:

        print("No ORFs detected.")

    else:

        for index, orf in enumerate(orfs, start=1):

            print(f"ORF {index}")
            print(f"Start   : {orf['Start']}")
            print(f"End     : {orf['End']}")
            print(f"Length  : {orf['Length']} bp")
            print(f"Sequence: {orf['Sequence']}\n")
