"""
Python分支结构
1.顺序结构：一条一条语句顺序执行
2.分支结构：在判断条件之后选择某一条分支去执行
（1）关键字：if、elif、else，缩进（if条件成立下药执行多条语句，只要保证多条语句具有相同的缩进即可）
（2）格式：
     if 判断条件1:
        执行语句1......
     else:
        执行语句2......
（3）多重分支：
     if 判断条件1 ：
        执行语句1......
     elif 判断条件2:
        执行语句2......
     elif 判断条件3:
        执行语句3......
(4)嵌套分支：
     if 判断条件1 ：
        if 判断条件2......
           满足1+2，执行语句2......
        else:
        只满足1，没有满足2时，执行语句3......
     else:
        不满足1时，执行语句4......
"""

# 多重分支
a = 8
if a == 0:
    print("a = 0")
elif a == 2:
    print("a == 2")
else:
    print("a不等于0、2")

"""
嵌套分支：
分段函数求值：
3x - 5 (x > 1)
f(x) = x + 1 (-1 <= x <=1)
5x + 3 (x < -1)
"""
# 能使用扁平化就不要使用嵌套，所以2的写法比1好
# # 1.多重分支，嵌套
# x = 0
# if x > 1:
#     y = 3*x -5
# elif -1 <= x <=1:
#     y = x + 1
# elif x < -1:
#     y = 5 * x + 3
# print(y)
# 2.分支结构，扁平化
x = 8
if x > 1:
    y = 3 * x - 5
else:
    if x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
print(y)


