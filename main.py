def gc_content(sequence):
    g = sequence.count('G')
    c = sequence.count('C')
    return round(((g + c) / len(sequence)) * 100, 2)

# Example sequence
dna = "AGCTATAGCGCGATCGATC"
print("GC Content:", gc_content(dna), "%")
