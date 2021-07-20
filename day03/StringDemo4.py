word = '''
        國文:100
        數學:80
        英文:90
        '''
# 提示斷行 = \n
array = word.split('\n')
print(array, len(array))
print('array[1] 沒有去除左右空白:', array[1])
print('array[1] 有去除左右空白:', array[1].strip())

chinese = float(array[1].split(':')[1].strip())  # strip() 去除二邊的空白
math = float(array[2].split(':')[1].strip())
english = float(array[3].split(':')[1].strip())
sum = chinese + math + english
print("總分: %d" % sum)
