import random as r
import time as t


ttt = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

def printTTT():
    for row in ttt:
        print(row)

def play():
    printTTT()
    # 使用者玩「O」
    n = int(input('請輸入位置 (0~8): '))
    if n == -1:
        return False
    ttt[n//3][n%3] = 'O'
    return True


if __name__ == '__main__':
    while play():
        pass


