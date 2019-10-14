class Player(object):
    instance = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        if self.init_flag is False:
            print('init')
            self.init_flag = True
        # else:
        #     return


player1 = Player()
player2 = Player()
print(id(player1), id(player2))
