class Gun:
    def __init__(self, model):
        self.model = model
        self.bullet_num = 0

    def add_bullet(self, count):
        self.bullet_num += count

    def shoot(self):
        if self.bullet_num <= 0:
            print(f'{self.model}没有子弹了')
            return
        self.bullet_num -= 1
        print(f'{self.model}tututu...{self.bullet_num}')


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = None

    def fire(self):
        if self.gun is None:
            print(f'{self.name} did not have gun')
            return
        print(f'{self.name}gogogo')
        self.gun.add_bullet(50)
        self.gun.shoot()


ak47 = Gun("AK47")
xiaoming = Soldier("许三多")
xiaoming.gun = ak47
xiaoming.fire()
