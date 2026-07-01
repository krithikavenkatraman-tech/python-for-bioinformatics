# DNA Reverse Complement Calculator

def reverse_complement(sequence):
    complement = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G'
    }

    sequence = sequence.upper()
    reverse = sequence[::-1]

    reverse_comp = ""

    for base in reverse:
        reverse_comp += complement.get(base, base)

    return reverse_comp


dna = input("Enter DNA sequence: ")

print("\nOriginal Sequence :", dna.upper())
print("Reverse Complement:", reverse_complement(dna))
