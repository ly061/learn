class Tool(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Tool.count += 1


tool1 = Tool('斧头')
tool2 = Tool('宝剑')
tool3 = Tool('嘿嘿')
print(tool1.count)
tool1.count = 99
print(tool1.count)
print('工具对象总数{:}'.format(Tool.count))
