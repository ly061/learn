class Person:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __str__(self):
        return f"我的名字叫{self.name}体重是{self.weight}"

    def run(self):
        self.weight -= 0.5

    def eat(self):
        self.weight += 2

xiaoming = Person("小明", 75)
xiaoming.run()
xiaoming.eat()