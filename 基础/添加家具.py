class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f"{self.name}的占地面积是{self.area}"


bed = HouseItem('bed', 10)
chest = HouseItem('chest', 5)


class House:
    def __init__(self, area, name):
        self.area = area
        self.name = name
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return f"户型{self.name}\n占地面积 {self.area}[剩余面积{self.free_area}]\n家具列表{self.item_list}"

    def add_item(self, item):
        print(f'要添加{item.name}')
        self.free_area -= item.area


two = House(60, "两室一厅")
two.add_item(bed)
print(two)