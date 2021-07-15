name = 'height'
value = 170
print(name, value)  # 中間預設使用空白隔開
print(name, value, sep="=")  # 中間使用 = 隔開

height = "身高"
h = 170
weight = "體重"
w = 60
# 身高=170&體重60
print(height, h, sep="=", end="&")  # 使用 & 符號結尾
print(weight, w, sep="=")  # 使用預設換行符號結尾
