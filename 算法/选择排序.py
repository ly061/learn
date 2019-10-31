def selection_sort(seq):
    for i in range(len(seq)-1):
        position = i
        for j in range(i+1, len(seq)):
            if seq[position] > seq[j]:
                position = j                         # 先记录下位置，不动数组，等此次循环结束再去操作数组
        if position != i:
            seq[i], seq[position] = seq[position], seq[i]

    return seq


li = [1, 4, 5, 8, 66, 44, 589, 12, 3, 6, 6]
print(selection_sort(li))
