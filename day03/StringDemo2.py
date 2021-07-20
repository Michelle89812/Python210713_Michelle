word = 'height=170,weight=60'
print(word)

# 求 bmi = ? (利用 split)
array = word.split(',')
print(array, array[0], array[1])  # array[0] = height=170, array[1] = weight=60

h_array = array[0].split('=')
print(h_array, h_array[0], h_array[1])

h = float(h_array[1])
print(h, type(h))

w_array = array[1].split('=')
print(w_array, w_array[0], w_array[1])
w = float(w_array[1])
print(w, type(w))

bmi = w / ((h/100)**2)
print(bmi)