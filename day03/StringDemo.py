word = 'she sell sea shell on the sea shore'
# 取得字串長度
print(len(word))
# 某字的字串數目
print('sea 的數量', word.count('sea'))
# 判斷字首是否大寫
if(not word.istitle()):
    word = word.capitalize()
print(word)
# 是否有 shell 這個字
keyword = 'shell'
print(word.find(keyword))  # 會得到 shell 在 word 字串中的位置
if(word.find(keyword) >= 0):
    print('{} 中有 {}'.format(word, keyword))
else:
    print('{} 中沒有 {}'.format(word, keyword))
# 是否有 sun 這個字
keyword = 'sun'
print(word.find(keyword))  # 會得到 shell 在 word 字串中的位置
if(word.find(keyword) >= 0):
    print('{} 中有 {}'.format(word, keyword))
else:
    print('{} 中沒有 {}'.format(word, keyword))

# 利用 split 來切割字串
# She sell sea shell on the sea shore 中有 shell
array = word.split(' ')
print(array, array[1], len(array))


