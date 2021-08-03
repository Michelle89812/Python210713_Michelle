import json
import day07.Util as u
file = open('桃園公共自行車即時服務資料.json', 'r', encoding='utf-8')
data = file.read()
youbike = json.loads(data)
# print(youbike)
no = 2003
sno = str(no)
try:
    print(youbike['retVal'][sno])
    print(youbike['retVal'][sno]['sno'])
    print(youbike['retVal'][sno]['sna'])
    print(youbike['retVal'][sno]['tot'])
    print(youbike['retVal'][sno]['sbi'])
    print(youbike['retVal'][sno]['bemp'])
    print(youbike['retVal'][sno]['lat'])
    print(youbike['retVal'][sno]['lng'])
except:
    print('無此站台 %s' % sno)

# 我所在地的經緯度 25.051249173402592, 121.28611345321114 蘆竹區聯福街聯福巷61-10號
print(u.distance(25.051249173402592, 121.28611345321114, 24.968128, 121.194666))
print(u.distance(24.99047, 121.31187, 24.968128, 121.194666))




