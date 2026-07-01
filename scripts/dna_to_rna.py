"""
DNA to RNA Transcription

Description:
Transcribes DNA into RNA by replacing
thymine (T) with uracil (U).
"""

def transcribe(sequence):
    """Convert DNA to RNA."""

    return sequence.upper().replace("T", "U")


if __name__ == "__main__":

    dna = input("Enter DNA sequence: ").strip()

    print("\nRNA Sequence")
    print(transcribe(dna))
