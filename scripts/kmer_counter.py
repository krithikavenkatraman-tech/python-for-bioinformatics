"""
K-mer Counter

Description:
Counts the frequency of every k-mer (substring of length k)
present in a DNA sequence.

Applications:
- Genome Assembly
- Comparative Genomics
- Sequence Analysis
"""

def count_kmers(sequence, k):
    """
    Count all k-mers in a DNA sequence.

    Parameters
    ----------
    sequence : str
        DNA sequence
    k : int
        Length of each k-mer

    Returns
    -------
    dict
        Dictionary containing k-mer frequencies
    """

    sequence = sequence.upper()

    kmer_counts = {}

    for i in range(len(sequence) - k + 1):

        kmer = sequence[i:i+k]

        kmer_counts[kmer] = kmer_counts.get(kmer, 0) + 1

    return kmer_counts


if __name__ == "__main__":

    dna = input("Enter DNA sequence: ").strip()

    k = int(input("Enter k-mer length: "))

    result = count_kmers(dna, k)

    print("\nK-mer Frequencies\n")

    for kmer, count in sorted(result.items()):
        print(f"{kmer}: {count}")
