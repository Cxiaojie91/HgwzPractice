"""
字典是以关键字为索引，关键字可以是任意不可变类型，可以是字符串或数字；
元组只包含字符串、数字或元组，那么元组也可作为关键字
"""
dict_a = {"a": 1, "b": 2, "c": 3, "d": 4}
dict_b = dict(a=3, b=4)
print(dict_a, dict_b)
print(type(dict_b), type(dict_a))
# keys值不可变，是一个键值，a和b是keys值
print(dict_a.keys(), dict_a.values())
# pop会把values返回并把a的键值去掉
print(dict_a.pop("a"))
print(dict_a)
'''
popitem随机删除一个键值的内容并返回被删除的内容
'''
# 返回被删除的键值对
print(dict_a.popitem())
# 删除掉键值对之后还剩余的元素
print(dict_a)

dict_a1 = {}
dict_b1 = dict_a1.fromkeys([1, 2, 3, 4, 5], "a")
print(dict_b1)

print({i: i * 2 for i in range(1, 10)})