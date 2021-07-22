import random as r


def point(p):  # 取得點數
    # A -> 1點, J, Q, K -> 0.5點
    if p == 'A':
        return 1
    if p == 'J' or p == 'Q' or p == 'K':
        return 0.5
    return int(p)


if __name__ == '__main__':
    pokers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
    r.shuffle(pokers)
    # 遊戲開始先拿到兩張牌
    # 之後透過詢問可以延續拿牌,連續計算分數
    my_cards = []  # 目前手中的牌
    my_cards.append(pokers.pop(0))
    my_cards.append(pokers.pop(0))
    print(my_cards)
    # 計算每一張牌的分數
    my_score = 0
    for p in my_cards:
        my_score = my_score + point(p)
    print(my_cards, my_score)

