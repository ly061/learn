def insertion_sort(seq):
    if len(seq) > 1:
        for i in range(1, len(seq)):
            while i > 0 and seq[i] < seq[i - 1]:
                tmp = seq[i]
                seq[i] = seq[i - 1]
                seq[i - 1] = tmp
                i = i - 1
    return seq


li = [22, 1, 33, 4, 7, 6, 8, 9, 11]
# print(insertion_sort(li))


def insertion_sort1(seq):
    for i in range(1, len(seq)):
        for j in range(i, 0, -1):
            if seq[j] < seq[j-1]:
                seq[j], seq[j-1] = seq[j-1], seq[j]
    return seq


# print(insertion_sort1(li))
print("   ", li)
insertion_sort1(li)
