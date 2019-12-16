def quick_sorted1(li):
    if len(li) < 2:
        return li
    mid = li[len(li)//2]
    left, right = [], []
    li.remove(mid)
    for li_index in li:
        if li_index >= mid:
            right.append(li_index)
        else:
            left.append(li_index)
    return quick_sorted1(left) + [mid] + quick_sorted1(right)


seq = [22, 1, 33, 4, 7, 6, 8, 9, 11]
print(quick_sorted1(seq))
