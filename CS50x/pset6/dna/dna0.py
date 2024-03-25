seq = "AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG"

seq_length = len(seq)

groups = []

for i in range(seq_length):
    subseq = {"subseq": seq[i]: "count": 0}
    for j in range(seq_length(1, seq_length + 1)):
        if seq[i] == seq[j] and seq[i] not in groups:
            groups.append(["subseq": seq[i] "count"])




print(subseqs)
print(seq_length)
