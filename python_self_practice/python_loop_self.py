"""
猜数字游戏
计算机给出1-100的随机数由人来猜
计算机根据人猜的数字分别给出提示：大一点/小一点/猜对了的
"""
# 导入random的库
import random
# 计算机给的数字应该为随随机的
computer_number = random.randint(1, 100)
# print(computer_number)
while True:
    person_number = int(input("请输入一个数字："))
    if person_number > computer_number:
        print("小一点")
    elif person_number < computer_number:
        print("大一点")
    elif person_number == computer_number:
        print("猜对了")
        break
