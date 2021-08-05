
# 加 10%
def add_ten(x):
    return x * 1.1


# 加 1%
def add_one(x):
    return x * 1.01


# 減 10%
def sub_ten(x):
    return x * 0.9


# 減 1%
def sub_one(x):
    return x * 0.99


def calc(func1, func2, x):
    if x >= 90:
        return func1(x) + func1(x)  # 超額獎勵
    elif x >= 60:
        return func1(x)
    else:
        return func2(x)


if __name__ == '__main__':
    #  分數 >= 60 加 10% 反之 減 10%
    x = 95
    print(calc(add_ten, sub_ten, x))
    x = 75
    print(calc(add_ten, sub_ten, x))
    x = 45
    print(calc(add_one, sub_ten, x))
    # _____________________________________
    x = 75
    print(calc(add_ten, sub_one, x))
    x = 45
    print(calc(add_one, sub_one, x))

