import json
file = open('桃園公共自行車即時服務資料.json', 'r', encoding='utf-8')
data = file.read()
youbike = json.loads(data)
# print(youbike)
print(youbike['retVal']['2001'])
print(youbike['retVal']['2001']['sna'])
print(youbike['retVal']['2001']['tot'])
print(youbike['retVal']['2001']['sbi'])
print(youbike['retVal']['2001']['bemp'])
print(youbike['retVal']['2001']['lat'])
print(youbike['retVal']['2001']['lng'])

# 我所在地的經緯度 25.051249173402592, 121.28611345321114 蘆竹區聯福街聯福巷61-10號


