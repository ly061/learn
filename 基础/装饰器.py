def outer(func):
    def innner(a, b):
        print('this is inner')
        return func(a, b)
    return innner


@outer
def func_add(a, b):
    return a + b


print(func_add(1,2))
