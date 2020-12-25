#! /user/bin/python
# -*- coding:UTF-8 -*-
"""
@product:PyCharm
@project:PythonCode_Study
@file:Basic.py
@AUTHOR:DELL - 李彦文
@time:2020/12/25
"""

'''
模块命名规范
    1、由字母，数字，下划线组成，但是不能以数字开头
    2、见名知意
    3、不同的字母，数字之间，用下划线隔开，可提升代码的可读性
    4、模块命名不能使用Python的关键字
'''

'''
注释
    1、“#” 符号单号注释，ctrl+/ 是快捷键
    2、多行注释是成对的三个单引号，三个单引号内的内容即为被注释的内容，不会被Python执行
'''

'''
变量名 x = 1  y = x + 1;求y的值
print(输出内容)：输出函数，输出括号内的内容到控制台
当你要使用某个变量的时候，需要确定它已经被定义和赋值
'''
q = 2      # 变量赋值
print(q)   # 控制台输出结果为  2

'''
数据类型    条件语句    循环语句
数字：整型，浮点型
整型：关键字 int
浮点数： 关键字 float
'''
a = 10
print(a+20)

b = 10.24
print(1+b)


'''
布尔值: bool boolean
只有两个值：True 和 False，首字母需要大写，不然不能识别 
'''

'''
字符串：str
在Python里面，只要是成对的单引号，双引号，三引号括起来的内容都是字符串
'''
a1 = 'hello'
b1 = "hi"
c = '''666'''
d = """888"""
e = '0.023'
e1 = 0.023

# type(数据)：作用是判断括号内字符的数据类型
print(type(a1))     # str
print(type(b1))     # str
print(type(c))      # str
print(type(d))      # str
print(type(e))      # str
print(type(e1))     # float

# 字符串的一些使用
s = 'hello'