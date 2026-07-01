# Open Reading Frame (ORF) Finder

## Objective

Identify potential Open Reading Frames (ORFs) in a DNA sequence.

---

## Biological Background

An **Open Reading Frame (ORF)** is a region of DNA that has the potential to encode a protein.

A typical ORF:

- Begins with a start codon (**ATG**)
- Ends with a stop codon (**TAA**, **TAG**, or **TGA**)

ORFs are fundamental for identifying protein-coding genes during genome annotation.

---

## Example

Input

```
ATGAAACCCGGGTAA
```

Output

```
Start : 1

End : 15

Length : 15 bp
```

---

## Python Concepts

- Nested loops
- Dictionaries
- Lists
- String slicing
- Conditional statements

---

## Applications

- Gene Prediction
- Genome Annotation
- Comparative Genomics
- Functional Genomics
