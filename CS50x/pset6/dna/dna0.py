seq = "AAGGTAAGTTTAGAATATAAAAGGTGAGTTAAATAGAATAGGTTAAAATTAAAGGAGATCAGATCAGATCAGATCTATCTATCTATCTATCTATCAGAAAAGAGTAAATAGTTAAAGAGTAAGATATTGAATTAATGGAAAATATTGTTGGGGAAAGGAGGGATAGAAGG"

seq_length = len(seq)

groups = []

for i in range(seq_length):
    subseq = {"seq[i]": 0}
    for j in range(seq_length(1, seq_length + 1)):
        if subseq == seq[j]:
            groups.append(["seq[i]": "count"])




print(subseqs)
print(seq_length)
