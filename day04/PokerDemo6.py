# 10點半對戰
# 今天你有100元
# 可以自由下注
import day04.PokerDemo5 as poker

if __name__ == '__main__':
    balance = 100
    while True:
        print('balance:', balance)
        if balance == 0:
            print('你沒錢了，請離開遊戲...')
            break


        bet = int(input('請下注(0:離開): '))

        if bet == 0 and balance == 0:
            break
        elif bet > balance:
            print('下注金額不可超過balance，請重新下注')
            continue
        elif bet < 0:
            print('下注金額不可為負值')
            continue

        result = poker.playGame()
        # print(result)
        balance = balance + (result * bet)
        # print(balance)


