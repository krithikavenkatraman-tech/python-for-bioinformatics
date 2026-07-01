"""
Sequence Length Calculator

Description:
Calculates the total number of nucleotides
in a DNA or RNA sequence.
"""

def sequence_length(sequence):
    """Return sequence length."""
    return len(sequence)


if __name__ == "__main__":

    sequence = input("Enter DNA/RNA sequence: ").strip().upper()

    print("\nSequence Length")
    print(sequence_length(sequence))
