import random as r
pokers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
# random 內建洗牌
r.shuffle(pokers)
print(len(pokers), pokers)
