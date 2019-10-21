class Salary(object):

    def __call__(self, money_month):
        day = money_month // 30
        hour = day // 8
        year = money_month * 12
        return day, hour, year, money_month


s = Salary()
print(s(10000))
