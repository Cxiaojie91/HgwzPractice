"""
1、元组tuple使用()进行定义，列表使用[]进行定义；
2、tuple、list、range都是序列数据类型；
3、tuple是不可变的，可以通过解包或索引来访问
"""
# 元组的定义
tuple_test = (1, 3, 5, 7, 9,)
tuple_test1 = 0, 2, 4, 6, 8
print(tuple_test, tuple_test1)
print(type(tuple_test), type(tuple_test1))

# 元组的不可变特性
list_test_1 = [11, 13, 15, 17, 19]
list_test_1[0] = "a"
print(list_test_1)
# 元组中的a一个变量指针，或者说是内存数字
# 特殊情况：元组中嵌套列表，所嵌套的列表可变
a = [100, 1000, 10000]
tuple_test2 = (10, 12, 14, 16, 18, a)
print(id(tuple_test2[5]))
tuple_test2[5][2] = "a"
# 元组不可通过索引改变元素，所以此行代码允许会报错 tuple_test2 [0] = "b"
print(tuple_test2)

# 元组的常用函数
# count：计算元素在元组中出现的次数
tuple_a = (10, 20, 30, 40, 50, "a", "a", "a")
print(tuple_a.count("a"))
# index：求对应元素的索引,重复的元素以第一个为主
print(tuple_a.index("a"))