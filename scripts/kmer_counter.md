# K-mer Counter

## Objective

Count the frequency of every k-mer (substring of length **k**) present in a DNA sequence.

---

## Biological Background

A **k-mer** is a sequence fragment of length *k*.

Example:

DNA

```
ATGCG
```

3-mers

```
ATG
TGC
GCG
```

K-mer analysis is one of the most widely used techniques in computational genomics.

---

## Example

Input

```
DNA Sequence

ATGCGATG

k = 3
```

Output

```
ATG : 2
CGA : 1
GAT : 1
GCG : 1
TGC : 1
```

---

## Python Concepts

- Dictionaries
- Loops
- String slicing
- Functions

---

## Applications

- Genome Assembly
- Comparative Genomics
- Sequence Classification
- Read Mapping
- Error Correction
