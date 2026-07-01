# GC Content Calculator

def gc_content(sequence):
    """Calculate GC percentage."""

    sequence = sequence.upper()

    gc = sequence.count("G") + sequence.count("C")

    return (gc / len(sequence)) * 100


if __name__ == "__main__":

    dna = input("Enter DNA sequence: ").strip()

    gc = gc_content(dna)

    print(f"\nGC Content = {gc:.2f}%")
