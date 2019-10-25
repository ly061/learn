def selection_sort(seq):
    for i in range(len(seq)):
        position = i
        for j in range(i, len(seq)):
            if seq[position] > seq[j]:
                position = j
        if position != i:
            tmp = seq[position]
            seq[position] = seq[i]
            seq[i] = tmp
