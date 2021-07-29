import json
# 讀檔
# 參數 : r 讀, w 寫, encoding='utf-8' 編碼

file = open('people.json', 'r', encoding='utf-8')
str = file.read()  # 將檔案內的資料存放到 x 變數中
print(type(str), str)

x = json.loads(str)  # 將 json 字串轉為 dict 物件
print(type(x), x)

# 計算並印出所有人的 bmi 值
for person in x:
    name = person['name']
    w = person['profile']['w']
    h = person['profile']['h']
    #print(type(w), type(h))
    bmi = w / pow(h/100, 2)
    print("%s bmi= %.2f" % (name, bmi))