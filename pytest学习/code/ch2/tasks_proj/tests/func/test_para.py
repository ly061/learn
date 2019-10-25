
import pytest

list1 = [(1,1,1),(3,3,9),(5,6,30)]
list2 = [(1,3,3),(2,3,6),(3,6,18)]
dic1 = [{'a': 1, 'b': 2, 'c': 3}]

def multi(a,b):
    return a*b


class TestParam:
    @pytest.mark.parametrize("a,b,c", [(1, 2, 3)])
    def test_1_multi(self,a,b,c):
        print("测试函数1的数据a是{},b是{}，c是{}".format(a, b, c))

    @pytest.mark.parametrize("data", list2)
    def test_2_multi(self, data):
        print(f"测试函数2的数据a是{data[0]},b是{data[1]}，c是{data[2]}")

    @pytest.mark.parametrize("data", dic1)
    def test_3(self, data):
        print(f"测试函数2的数据a是{data['a']},b是{data['b']}，c是{data['c']}")

if __name__ == '__main__':
    pytest.main()
