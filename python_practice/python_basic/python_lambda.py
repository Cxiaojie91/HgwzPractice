"""
函数的高级用法：
可用Lambda关键字创建小的匿名函数
Lambda是一个表达式，仅仅能在Lambda中封装有限的逻辑，简短的函数可使用，长函数还是要使用def;
函数体非常简单的使用可以用
"""
fun_lambda =lambda x:x*2
print(fun_lambda(11))
# fun_lambda 和fun_lambda1等同
def fun_lambda1(x):
    return x*2
print(fun_lambda1())