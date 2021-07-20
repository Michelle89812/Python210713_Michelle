word = '台積電買價:599；賣價:601；成交價:600'

array = word.split('；')
print(array)

bid = array[0].split(':')[1]
ask = array[1].split(':')[1]
price = array[2].split(':')[1]

bid = float(bid)
ask = float(ask)
price = float(price)

print(bid, ask, price)

# 1. 若要買進2000股，需要多少錢 (看成交價) ?
print(2000 * price)
# 2. 若要市價買進1000股，需要多少錢 (看賣價) ?
print(2000 * ask)
# 3. 若要市價買出1000股，需要多少錢 (看買價) ?
print(2000 * bid)
