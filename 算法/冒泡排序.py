# 两种解法都可以，第一种是把最大的往后排，第二种是把最小的往前排


def bubble_sort1(seq):
    for i in range(len(seq)):
        for j in range((len(seq)-i-1)):
            if seq[j] > seq[j+1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    return seq


def bubble_sort(seq):
    for i in range(len(seq)):
        for j in range(i, len(seq)):
            if seq[j] < seq[i]:
                tmp = seq[j]
                seq[j] = seq[i]
                seq[i] = tmp
    return seq


seq = [22, 1, 33, 4, 7, 6, 8, 9, 11]
print(bubble_sort(seq))
print(bubble_sort1(seq))
