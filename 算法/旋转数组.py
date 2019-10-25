def test_1(k=1000000):
    li = [1, 2, 3, 4, 5, 6, 7]
    if li:
        k = k % len(li)
        li = li[-k:] + li[:-k]
        print(li)
        return li


def test_2(k=1000000):
    li = [1, 2, 3, 4, 5, 6, 7]
    if li:
        k = k % len(li)
        for i in range(k):
            li.insert(0, li[-1])
            li.pop()
        print(li)
        return li


def test_3(k=1000000):
    li = [1, 2, 3, 4, 5, 6, 7]
    if li:
        old_li = li[:]
        lenth = len(li)
        for i in range(lenth):
            li[(k+i) % lenth] = old_li[i]
        print(li)
        return li

