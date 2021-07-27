'''
Lotto 機器
可以提供重複或不重複的彩球
例如 : 輸入1 -> 開獎今彩539: 1~39 之間取不重複的 5 個彩球
      輸入2 -> 開獎四星彩 : 4 個 0~9 可以重複的數字
      輸入0 -> Exit
'''
import random as r
import sys

def menu():
    print('--------------')
    print('1. 今彩539')
    print('2. 四星彩')
    print('0. Exit')
    print('--------------')

def userChoice():
    choice = int(input('請選擇: '))
    return choice

def lotto539():
    pass

def lotto4star():
    lotto = []
    for x in range(4):
        lotto.append(r.randint(0, 9))
    print('四星彩:', lotto)

if __name__ == '__main__':
    while True:
        # Lotto 開獎 menu()
        menu()
        # User 選擇
        choice = userChoice()
        if choice == 1:
            lotto539()
        elif choice == 2:
            lotto4star()
        elif choice == 0:
            print('離開程式')
            break
        else:
            print('輸入錯誤，請重新輸入 !')
            continue


        print('Enter...')
        sys.stdin.read(1)
