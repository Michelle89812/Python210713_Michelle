import json
file = open('桃園公共自行車即時服務資料.json', 'r', encoding='utf-8')
data = file.read()
youbike = json.loads(data)

# Lab 請列出所有站台的名稱 sna
# 提示利用 for 迴圈
# 串列變數 = range(起始值, 終止值)  # 不含終止值
for no in range(2001, 2412):
    sno = str(no)
    try:
        sna = youbike['retVal'][sno]['sna']
        print(sno, sna)
    except:
        pass




