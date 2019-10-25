def insertion_sort(seq):
    if len(seq) > 1:
        for i in range(1, len(seq)):
            while i > 0 and seq[i] < seq[i - 1]:
                tmp = seq[i]
                seq[i] = seq[i - 1]
                seq[i - 1] = tmp
                i = i - 1
    return seq


