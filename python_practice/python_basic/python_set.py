"""
集合：
1.集合是由不重复元素组成的无序的集；
2.基本用法包括成员检测和消除重复元素；
3.可以使用{}或者set()函数创建集合；
4.要创建一个空集合只能用set()而不能用{}
"""
set_test = {1}
set_test1 = set()
print(len(set_test1), len(set_test))
print(type(set_test), type(set_test1))

# 集合的内置函数
set_a = {"a", 1, 3, 5, 7, 9}
set_b = {"a", 0, 2, 4, 6, 8}
# 并集：union
print(set_a.union(set_b))
# 交集：intersection
print(set_a.intersection(set_b))
# 差集：我有你没有，即set_a有set_b没有，difference
print(set_a.difference(set_b))
# 集合添加元素
set_a.add("bb")
print(set_a)

# 集合可以使用列表推导式，求一串字符串中的内容
print({i for i in "aagdhagdaqudiqugascagckagakgfakgfckagkagkcgakgakga"})
set_c = "hajhchcahcaochohcahcjkckjahcka"
print(set(set_c))
