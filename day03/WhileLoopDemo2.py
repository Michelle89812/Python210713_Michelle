import random
cash = 1000

while cash > 0:
    price = random.randint(1, 100)
    cash = cash - price
    print('買到一個禮物 %d, 剩下 $ %d ' % (price, cash))
