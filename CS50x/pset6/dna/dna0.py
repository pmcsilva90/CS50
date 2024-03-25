seq = "AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG"

seq_length = len(seq)

start = 0
end = start + 4

subseqs = []

for i in range(seq_length):
    subseq = seq[start + i:end + i]
    if subseq in seq:
        subseqs.append(subseq)

print(subseqs)
print(seq_length)
