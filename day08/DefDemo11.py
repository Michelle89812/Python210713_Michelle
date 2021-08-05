# *args  **kwargs

def getSum(*scores):
    return sum(scores)


# 座號、 總分、 學生資料
def printStudentInfo(no, *scores, **info):
    print('座號:', no)
    print('分數:', scores)
    print('總分:', sum(scores))
    print('學生資料:', info)


if __name__ == '__main__':
    scoresSum = getSum(100, 90, 80)
    print(scoresSum)
    printStudentInfo(1, 100, 90, 80, 姓名='John', age=18)
