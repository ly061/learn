class MusicPlayer(object):

    # New方法是静态方法，但是定义在object基类里的，所以不需要@staticmethod声明，传递cls参数是因为方法被重写，需要让方法知道给谁分配空间
    def __new__(cls, *args, **kwargs):
        print('创建对象，分配空间')
        return super().__new__(cls)

    def __init__(self):
        print('播放器初始化')


player = MusicPlayer()
print(player)
