import json

x = '{"name":"John", "age":18}'
person = json.loads(x)
print(type(person))
print(person['name'], person['age'])
