"""
硬性规则：
变量名由字幕+数字+下划线勾成，数字不可作为开头
大小写敏感
不要跟关键字（有特殊含义的单词）和系统保留字（如函数、模块等名字）冲突
"""
a = 1
a1 = 2
a_b = 3
A = 4
print(a, a1, a_b, A)
# id 可以打印变量的存储地址
print(id(a), id(a1), id(a_b), id(A))

# 数字类型包括：整数int，浮点数float，复数complex（实部+虚部，如0.2j)
int_a = 1
float_a = 0.2
complex_a = 1j
# 可通过type查看变量的数据类型
print(type(int_a), type(float_a), type(complex_a))

"""
字符串
\：转义符
r：忽略转义符的作用
+以及空格：多个字符串连接
切片
"""
# 可以用\\n打印出\n
str_a = "12345"
str_b = "abcde"
str_c = str_a + str_b
print(str_a, str_b,str_c)
# 切片[start: stop: step]，[开始： 结束： 步长]
print(str_a[2])
print(str_a[0:3:2], str_c[0:7:4])

"""
List：定义、索引、切片
"""
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(list1[0])
print(list1[0:2:4])