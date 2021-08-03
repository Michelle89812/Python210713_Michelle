import json
import requests
key = '6f6e5160e0d2b4b019e1ccff3232b603'  # 用自己的 key
q = 'taoyuan,tw'
url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % (q, key)
print(url)

