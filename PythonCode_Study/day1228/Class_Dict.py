#! /user/bin/python
# -*- coding:UTF-8 -*-
"""
@product:PyCharm
@project:PythonCode_Study
@file:Class_Dict.py
@AUTHOR:DELL - 李彦文
@time:2020/12/28
"""

'''
字典：dict  符号{}  会无序输出
1、可以存在空字典 a = {}
2、字典里面数据存储的方式   key:value
3、字典内的value可以包含任何数据类型的数据
4、字典里面的元素也是用逗号进行分割
5、字典只能通过key去找对应的value
'''
a = {"class": "Python",
     "student": "liyanwen",
     "teacher": "柠檬",
     "age": 18,
     "score": [99, 88, 67, 89.5]}

print(len(a))   # 打印的值为：5
print(a)    # {'class': 'Python', 'student': 'liyanwen', 'teacher': '柠檬', 'age': 18, 'score': [99, 88, 67, 89.5]}

# 字典取值 ：字典[key]
print(a["score"])        # 打印的值为：[99, 88, 67, 89.5]
print(a["score"][-1])        # 打印的值为：89.5   取分数的最后一个值

# 字典删除 pop(key)，指明删除的值的key
a.pop("student")    # 将teacher的值和key删除
print(a)        # 打印的值为：{'class': 'Python', 'teacher': '柠檬', 'age': 18, 'score': [99, 88, 67, 89.5]}