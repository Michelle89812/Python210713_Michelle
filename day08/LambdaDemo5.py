'''
分數
90~100 A
80~89  B
70~79  C
60~69  D
0~59   E
'''
score = 76

dict = {
    10: lambda: print('A'),
    9: lambda: print('A'),
    8: lambda: print('B'),
    7: lambda: print('C'),
    6: lambda: print('D'),
    5: lambda: print('E'),
    4: lambda: print('E'),
    3: lambda: print('E'),
    2: lambda: print('E'),
    1: lambda: print('E'),
    0: lambda: print('E'),
}
dict.get(score // 10)()

dict2 = {
    10: lambda: print('A'),
    9: lambda: print('A'),
    8: lambda: print('B'),
    7: lambda: print('C'),
    6: lambda: print('D')
}
dict2.get(score // 10, lambda: print('E'))()
