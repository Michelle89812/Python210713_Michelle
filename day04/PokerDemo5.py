import random as r


def point(p):  # 取得點數
    # A -> 1點, J, Q, K -> 0.5點
    if p == 'A':
        return 1
    if p == 'J' or p == 'Q' or p == 'K':
        return 0.5
    return int(p)


def getScore(cards):  # 計算總分
    score = 0
    for p in cards:
        score = score + point(p)
    return score


if __name__ == '__main__':
    pokers = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
    r.shuffle(pokers)
    # 遊戲開始先拿到兩張牌
    my_cards = []  # 目前手中的牌
    my_cards.append(pokers.pop(0))
    my_cards.append(pokers.pop(0))

    # 計算每一張牌的分數
    my_score = getScore(my_cards)
    print(my_cards, my_score)

    # 之後透過詢問可以延續拿牌,連續計算分數 (Homework)
    response = input('是否延續拿牌(Y or N): ')
