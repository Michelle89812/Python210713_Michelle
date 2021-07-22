#  骰子遊戲
#  有三顆骰子, 點數組合
#  3, 4, 5, 6, 7, 8, 9, 10 <-- 猜小
#  11,12,13,14,15,16,17,18 <-- 猜大
import random

if __name__ == '__main__':
    balance = 100 # 現金餘額
    while True:
        guess = int(input('現金前餘額: $%d , 猜大小, 大=1, 小=2, 離開=0: ' % balance))
        # 判斷 guess
        if guess == 0:
            print('離開')
            break;
        # 下注:
        bet = int(input('請下注 (金額不可超過 %d):' % balance))
        if bet > balance:
            print('下注金額: %d 超過目前可用餘額: %d' % (bet, balance))
            continue
        elif bet <= 0:
            print("下注金額不正確")
            continue

        # 擲骰子
        dice_number = random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

        if guess == 1:  # 猜大
            if(dice_number > 10):
                print('骰子點數: %d 猜大猜對了' % dice_number)
                balance = balance + bet
            else:
                print('骰子點數: %d 猜大猜錯了' % dice_number)
                balance = balance - bet
        elif guess == 2:  # 猜小
            if(dice_number <= 10):
                print('骰子點數: %d 猜小猜對了' % dice_number)
                balance = balance + bet
            else:
                print('骰子點數: %d 猜小猜錯了' % dice_number)
                balance = balance - bet
        else:
            print('資料不正確，請重新輸入')
            continue

