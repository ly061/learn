class A:
    def a(self):
        print('aaaaaaaaaa')

class B:
    def b(self):
        print('bbbbbbbb')

class C(A, B):
    pass


c = C()
print(C.__mro__)

print(dir(A))
