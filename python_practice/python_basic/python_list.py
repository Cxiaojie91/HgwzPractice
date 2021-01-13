"""
1.列表：
是Python中通过组合一些值，得到多种复合数据类型，是最常用的数据结构；
通过方括号括起、逗号分隔的一组值；
可以包括不同类型的元素，但通常使用时各个元素的类型相同。
2.列表的特性有很多，见以下
"""
list_practice = [1, 7, 2, 14, 21, 16]
# append 只能在列表末尾添加一个元素
list_practice.append(100)
# insert 需要指定位置和所要添加的元素
list_practice.insert(4, 10)
# remove 移除列表中第一个值为x的元素,读取的是列表中的值
list_practice.remove(10)
# pop 根据元素的索引来删除,不仅可以删除索引的值，还能返回这个值
p = list_practice.pop(1)
# sort 对列表中的元素进行排序,reverse为True时可以反序排序
list_practice.sort(reverse=True)
# reverse 反转列表中的元素排序
list_practice.reverse()
print(p)
print(list_practice)