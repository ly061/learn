# 外层函数的变量可以被内部函数调用，但是不能被修改。需要nonlocal 声明之后才能进行修改
def outer(num):
    print('outing')
    test_num = 10

    def inner(num_inner):
        nonlocal test_num
        print(test_num)
        test_num += 1
        if type(num_inner) is int:
            print('是整数')
        else:
            print('不是整数')
    inner(num)


outer('1')
