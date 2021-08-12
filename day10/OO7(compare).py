# 物件的比較
class Drink:
    __prices = {'milk': 80, 'coffee': 110}

    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.price = self.__prices.get(name)
        self.total = self.price * amount

    def __str__(self):
        return '%s 數量: %d 單價: $%d 小計: $%d' % \
               (self.name, self.amount, self.price, self.total)


if __name__ == '__main__':
    milk = Drink('milk', 3)
    print(milk)
    coffee = Drink('coffee', 2)
    print(coffee)

