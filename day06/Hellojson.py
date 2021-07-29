import json

x = '{"name":"John", "age":18}'
person = json.loads(x)
print(type(person))
print(person['name'], person['age'])

x = '{"name":"John", "age":18, "profile":{"w": 60.0, "h":170.0}}'
# 計算出 John 的 bmi
# bmi = w / (h/100)**2
person = json.loads(x)
profile = person["profile"]
print(type(profile), profile)
w = profile['w']
h = profile['h']
print(type(w), w, type(h), h)
bmi = w / (h/100)**2
print(bmi)




