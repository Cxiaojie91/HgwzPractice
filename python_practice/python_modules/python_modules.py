# 标准规则是导入的时候分开导入模块
import sys
# 正则匹配相关的方法，可以导入re
import re
import os
import json
import time

# 第三方开源模块，需要额外安装，可以直接在pycharm中安装，也可以在终端使用pip install
import yaml

# 导入自定义模块,可以采用from 模块 import 方法名、变量等（用 * 可以导入全部定义）
from python_practice.python_modules.baidu import *
# import python_practice.python_modules.baidu
search()
print(hello)


'''
dir()：找出当前模块定义的对象
dir(sys)：找出参数模块定义的对象
'''