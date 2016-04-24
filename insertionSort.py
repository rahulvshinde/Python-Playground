seq = [3, 7, 1, 4, 2, 100, 10]
print("Unsorted List : ", seq)
for p in range(1, len(seq)):
    while p != 0 and seq[p] < seq[p-1]:
        seq[p], seq[p-1] = seq[p-1], seq[p]
        p -= 1
print("Sorted List : ", seq)