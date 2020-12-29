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
6、字典六面的key必须是唯一的，如果存在两个一样的key，输出的值以后面那个key的值为准
'''
a = {"class": "Python",
     "student": "liyanwen",
     "teacher": "柠檬",
     "age": 18,
     "score": [99, 88, 67, 89.5]}

b = {"class": "Python全栈",
     "student": "李彦文",
     "teacher": "华华",
     "age": 28,
     "score": [79, 82, 77, 81.5]}

print(len(a))   # 打印的值为：5
print(a)    # {'class': 'Python', 'student': 'liyanwen', 'teacher': '柠檬', 'age': 18, 'score': [99, 88, 67, 89.5]}

# 字典取值 ：字典[key]
print(a["score"])             # 打印的值为：[99, 88, 67, 89.5]
print(a["score"][-1])         # 打印的值为：89.5   取分数的最后一个值

# 字典删除 pop(key)，指明删除的值的key
res = b.pop("student")        # 将 b 元组内key为student的值删除，并赋值给res
print(res)                    # 打印的值为：李彦文

# 字典新增数值 a[新key] = value;只能增加元组内不存在的key的值
b["stu_num"] = 110       # 在b元组内新增名为stu_num的key,key的值为110
print(b)                 # 打印出b元组新增key后的值，值为：{'class': 'Python全栈', 'teacher': '华华', 'age': 28, 'score': [79, 82, 77, 81.5], 'stu_num': 110}

# 字典数值修改  a[已存在的key] = 新的value     只能修改元组内已存在的key
a["teacher"] = '李彦文'     # 将a 元组内的teacher的值由“柠檬”改为“李彦文”
print(a)                   # 打印出b元组新增key后的值，值为 {'class': 'Python', 'student': 'liyanwen', 'teacher': '李彦文', 'age': 18, 'score': [99, 88, 67, 89.5]}
