import random
cash = 1000
limit = int(cash/3)
while cash > 0:
    price = random.randint(1, 100)

    if(cash - price >= 0):
        cash = cash - price
        print('禮物 $ %d (買到) 剩下 $ %d ' % (price, cash))

    else:
        print('禮物 $ %d (沒買到) 剩下 $ %d ' % (price, cash))
        # 若還剩下 1/3 繼續買
        if cash >= limit:
            continue
        else:
            break;



'''
禮物 $ 2 (買到) 剩下 $ 175 
禮物 $ 56 (買到) 剩下 $ 119 
禮物 $ 92 (買到) 剩下 $ 27 
禮物 $ 98 (買到) 剩下 $ -71 
改良
禮物 $ 2 (買到) 剩下 $ 175 
禮物 $ 56 (買到) 剩下 $ 119 
禮物 $ 92 (買到) 剩下 $ 27 
禮物 $ 98 (沒買到) 剩下 $ 1 
'''
