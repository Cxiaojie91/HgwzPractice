# 平方列表
list_square = []
for ls in range(9):
    list_square.append(ls**2)
print(list_square)
list_square2 = [ls**2 for ls in range(1, 99)]
print("list_square:", list_square2)

# 写法1
list_square3 = [ls**2 for ls in range(1, 10) if ls != 1]
print(list_square3)

# 写法2
# list_square3 = []
# for ls in range(1, 4):
#     if ls != 1:
#         list_square3.append(ls**2)
# print(list_square3)

# 嵌套循环
list_square4 = [ls * ls1 for ls in range(1, 11) for ls1 in range(1, 11)]
print(list_square4)
list_square4 = []
for ls in range(1, 11):
    for ls1 in range(1,11):
        list_square4.append(ls*ls1)
print(list_square4)
