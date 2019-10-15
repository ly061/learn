import copy
# 浅拷贝只拷贝自身，对深拷贝的任何操作都不会对源对象产生影响，但是浅拷贝某些操作会产生影响


def copy_qian():
    a = [1, 2, [3, 4]]
    b = copy.copy(a)
    print(a, b, sep='\n')
    b.append(5)
    b[2].append(6)
    print('a:', a)
    print('b', b)
    print('---------------------------------------------')


copy_qian()


def copy_shen():
    a1 = [1, 2, [3, 4]]
    b1 = copy.deepcopy(a1)
    print(a1, b1, sep='\n')
    b1.append(5)
    b1[2].append(6)
    print('a1:', a1)
    print('b1', b1)


copy_shen()