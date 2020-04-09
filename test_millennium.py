def test_1(max):
    a = 0
    for i in range(max):
        yield a
        a += 1

for i in test_1(5):
    print(i)