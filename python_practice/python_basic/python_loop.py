# python的循环结构
"""
循环语句允许执行一个语句或语句组多次
Python提供了for循环和while循环
"""

# range：用于产生一个不变的数值序列，且该序列一般用在循环中
# for x in 循环
result = 0
for i in range(101):
    if i % 2 == 0:
        result = result + i
print(result)

result1 = 0
for i1 in range(2, 101, 2):
    result1 = result1 + i1
print(result1)

"""
while循环：
构造不知道具体循环次数的循环结果，能产生或转换出bool值的表达式来控制循环;
true则继续，false则结束循环
continue跳出当前的循环体
break跳出整个循环体
"""
a = 1
while a == 1:
    print("a = 1")
    a = a + 1
else:
    print("a不等于1")
# 简单语句组：类似于if，如果while循环体中只有一条语句，可以将它跟while写在同一行
a1 = 3
while a1 == 1: a1 = a1 + 1
else:
    print("a1 = 1")
    print("a1不等于1")
# break跳出整个循环体，跳出for和while的循环体，对应的else将不再执行
for bc in range(1, 10):
    if bc == 5:
        break
    print(bc)
# continue
for bc1 in range(1, 10):
    if bc1 == 5:
        continue
    print(bc1)