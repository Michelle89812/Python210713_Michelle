# Python 基本資料結構
# list   列表 (元素內容可以重複, 元素內容可以修改)
# tuple  列表 (唯讀, Fast)
# set    列表 (元素內容不可重複, 元素內容可以修改)
# dict   字典列表 (元素內容可以重複, 元素內容可以修改)

# dict   字典列表 (key:value)
# key    的值不可以重複，若重複會將後者資料取代前者
# value  的值可以重複
scores = {'國文':100, '數學':90, '英文':90, '數學':60}
print('全科:', scores)
print('數學:', scores.get('數學'))
print('科目(keys):', scores.keys())
print('分數(values):', scores.values())

