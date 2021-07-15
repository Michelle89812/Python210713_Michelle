# if 判斷式
import random

n = 10
print(n % 2)
if n % 2 == 0:
    print("%d 是偶數" % n)

# if else 判斷式
n = 9
if n % 2 == 0:
    print("%d 是偶數" % n)
else:
    print("%d 是奇數" % n)

# if else 簡單判斷式
print(n, "偶數" if n % 2 == 0 else "奇數")

# if elif else 判斷式
# 90 ~ 100 -> A
# 80 ~ 90(不含) -> B
# 70 ~ 80

score = random.randint(0, 100)
print(score, end=" -> ")
if 90 <= score <= 100:
    print("A")
elif 80 <= score < 90:
    print("B")
elif 70 <= score < 80:
    print("C")
elif 60 <= score < 70:
    print("D")
else:
    print("E")