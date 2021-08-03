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

