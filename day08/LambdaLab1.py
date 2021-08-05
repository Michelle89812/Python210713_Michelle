# lambda lab:
# 請利用 lambda 做出能夠判斷 odd 奇數, even 偶數的函式
# result(4) 得到 "even"
# result(3) 得到 "odd"
# 印出結果的函式也一律使用 lambda
# 假設 n = 3 odd
#     n = 4 even

# def odd(x):
#     if x % 2 == 0:
#         return "even"
#     else:
#         return "odd"
if __name__ == '__main__':
    result = lambda n: print('n =', n, "Even") if n % 2 == 0 else print('n =', n, "Odd")
    n = 3
    result(n)
    n = 4
    result(n)
# ________________________________________________

result      = lambda n : "Even" if n % 2 == 0 else "Odd"
printResult = lambda n, x : print(n, x)

n = 3
printResult(n, result(n))
n = 4
printResult(n, result(n))