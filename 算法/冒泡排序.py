# 两种解法都可以，第一种是把最大的往后排，第二种是把最小的往前排


def bubble_sort1(seq):
    for i in range(len(seq)):
        for j in range((len(seq)-i-1)):
            if seq[j] > seq[j+1]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
    return seq


def bubble_sort(seq):
    for i in range(len(seq)):
        exchange = False                    # 如果哪一次数组没有变化说明已经排好序了，这时就可以退出循环了
        for j in range(i, len(seq)):
            if seq[j] < seq[i]:
                tmp = seq[j]
                seq[j] = seq[i]
                seq[i] = tmp
                exchange = True
        if not exchange:
            break
    return seq


def insertion_sort(seq):
    if len(seq) > 1:
        for i in range(1, len(seq)):
            while i > 0 and seq[i] < seq[i - 1]:
                tmp = seq[i]
                seq[i] = seq[i - 1]
                seq[i - 1] = tmp
                i = i - 1
    return seq


seq = [22, 1, 33, 4, 7, 6, 8, 9, 11]
print(bubble_sort(seq))
print(bubble_sort1(seq))
