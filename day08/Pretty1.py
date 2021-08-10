# 利用高階函式進行裝飾
def bread(func):
    print('我是麵包')
    return func


def hotdog():
    print('我是熱狗')


def egg():
    print('我是雞蛋')

def ham(func):
    print('我是火腿')
    return func

if __name__ == '__main__':
    b1 = bread(hotdog)
    b1()
    b2 = bread(egg)
    b2()
    b3 = bread(ham(egg))
    b3()