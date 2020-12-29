#! /user/bin/python
# -*- coding:UTF-8 -*-
"""
@product:PyCharm
@project:PythonCode_Study
@file:Class_Operator.py
@AUTHOR:DELL - 李彦文
@time:2020/12/29
"""

'''
运算符 有5个大类
算数运算符：+ - * / %
模运算/取余运算：可以判断某个数是偶数还是奇数
'''
a = 4       # 将4赋值给变量 a
print(a%2)  # 结果为0，即a除以2没有余数，得出a为偶数

# 赋值运算符 =  +=  -=
b = 5       # 赋值运算
b += 1      # 等同于 ：b = b + 1
print(b)    # 结果为  6

c = 7       # 赋值运算
c -= 1      # 等同于 ：c = c - 1
print(c)    # 结果为  6

# 比较运算符  >  >=  <  <=  !=  ==  6种比较关系
# 比较结果返回的值是布尔值 True False
d = 10
e = 5
print(d > e)       # 比较变量 d 大于 e ,结果是真的，返回 True
print(d >= e)       # 比较变量 d 大于等于 e ,结果是真的，返回 True
print(d < e)       # 比较变量 d 大于等于 e ,结果是假的，返回 False
print(d <= e)       # 比较变量 d 大于等于 e ,结果是假的，返回 False
print(d == e)       # 判断变量 d 恒等于 e ,结果是假的，返回 False
print(d != e)       # 判断变量 d 不等于 e ,结果是真的，返回 True
print('----------------------这里是分割线1----------------------------')
print("get" == "GET")       # 判断字符串 get 恒等于 GET ,结果是假的，返回 False，因为Python是区分大小写的
print("get".upper() == "GET")       # 判断字符串 get 恒等于 GET ,结果是真的，返回 True，因为.upper() 将 get  变成大写了
print("get" == "GET".lower())       # 判断字符串 get 恒等于 GET ,结果是真的，返回 True，因为.lower() 将 GET  变成小写了

print('----------------------这里是分割线2----------------------------')
# 逻辑运算符  and  or  拓展 ： not
# 逻辑运算符返回的值是布尔值 True False
# and ：左右两边的结果都为真，返回的结果才为真；只要有一个结果为假，返回的结果就为假---> 真真为真
# or : 左右两边的结果都为假，返回的结果才为假；只要有一个结果为真，返回的结果就为真---> 假假为假
f = 4
g = 3
print(f > 5 and g <7)       # 逻辑运算符前面的值为 False,那么整个结果就是 False
print(f > 5 or g <7)       # 逻辑运算符前面的值为 True,那么整个结果就是 True

print('----------------------这里是分割线3----------------------------')

# 成员运算符  in  /  not in
# 返回值也是布尔类型，True 和 False 这两种情况
h = 'hello'
i = [1, 2, 3]
print(3 not in i)       # 3 明显是在 i 这个数组内的，所以返回的值为 False
print(2 in i)       # 2 明显是在 i 这个数组内的，所以返回的值为 True

print('----------------------这里是分割线4----------------------------')

j = {"age": 18, "name": "咸鸭蛋"}
print(18 in j)          # 只判断key是否在这个数组内的，所以返回的值为 False
print("age" in j)       # 只判断key是否在这个数组内的，所以返回的值为 True