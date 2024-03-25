seq = "AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG"

seq_length = len(seq)

start = 0
end = start + 4

subseqs = []

for i in seq:
    subseq = seq[start:end]
    if subseq in seq:
        subseqs.append(subseq)

print(subseqs)
print(seq_length)
