class Dog(object):
    def __init__(self, name):
        self.name = name

    def game(self):
        print(f'{self.name} 蹦蹦跳跳')

class XiaoTianQuan(Dog):
    def game(self):
        print(f'{self.name} 飞到填上去玩耍。。')

class Person(object):
    def __init__(self, name):
        self.name = name

    def game_with_dog(self, dog):
        print(f'{self.name}和{dog.name}在玩耍')
        dog.game()


# wangcai = Dog('旺财')
wangcai = XiaoTianQuan('飞天旺财')
xiaoming = Person('小明')
xiaoming.game_with_dog(wangcai)
