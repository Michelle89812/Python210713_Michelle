# 取得 x, y 最大值, 並將最大值 x 2
'''
有了 lambda 就不需要 def 這一段了
def max(x, y):
    if(x > y):
        return x
    else:
        return y
'''

if __name__ == '__main__':
    a = 10
    b = 15
    max_value = max(a, b)
    result = max_value * 2
    print(max_value, result)
    # _______________________________________
    max_value = lambda x, y: x if x > y else y
    result = max_value(a, b) * 2
    print(result)
