# split 與 dict

exam = '國文=100,數學=90,英文=80'
exam_dict = dict(ex.split('=') for ex in exam.split(","))

print(1, exam_dict)
print(2, exam_dict['國文'])
print(3, exam_dict.values())
print(4, list(exam_dict.values()))
print(5, list(map(int, exam_dict.values())))
print(6, sum(list(map(int, exam_dict.values()))))

# map
s = '1 3 5 7'
s_list = s.split()  # 空括號 = 空白切割
print(s, s_list)
s_int_list = list(map(int, s_list))
print(s_list)
print(s_int_list)
