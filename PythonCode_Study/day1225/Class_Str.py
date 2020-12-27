#! /user/bin/python
# -*- coding:UTF-8 -*-
"""
@product:PyCharm
@project:PythonCode_Study
@file:Class_Str.py
@AUTHOR:DELL - 李彦文
@time:2020/12/27
"""
s = ' hello!'  # 非空字符串
a = ""  # 空字符串
'''
1、字符串的分割  字符串.split(可以指定切割符，可以指定切割次数)
2、返回一个列表类型的数据
3、列表里面的子元素都是字符串类型【字符串类型：以成对单引号，双引号，三引号括起来的字符都是字符串】
4、指定的切割符被切走了，不再到列表里面显示
'''

print(s.split())   # 结果为 ： ['hello!']
print(s.split(" "))   # 指定空字符串为切割符，结果显示为 ： ['', 'hello!']
print(s.split("e"))   # 指定 e 为切割符，结果显示为 ： [' h', 'llo!']
print(s.split("l"))   # 指定 l 为切割符，结果显示为 ： [' he', '', 'o!']
print(s.split("l", 1))   # 指定 l 为切割符，结果显示为 ： [' he', 'lo!']
print(s.split("l", 2))   # 指定 l 为切割符，结果显示为 ： [' he', '', 'o!']

'''
字符串的替换   字符串.replace('指定替换值','新值', 替换次数)
不写次数的话，默认替换所有需要替换的值
'''
new = s.replace('o', '@')
print(new)      # 结果：hell@!

new1 = s.replace('l', '@')
print(new1)     # 结果：he@@o!

new2 = s.replace('l', '@', 1)
print(new2)     # 结果：he@lo!

'''
字符串的去除指定字符 字符串.strip(指定字符)
1、默认去掉空格
2、只能去字符串掉头部和尾部指定的字符，不能去除中间指定的字符
'''
print(len(s))       # 打印出去掉字符之前的字符串长度   7
new3 = s.strip('!') # 将去掉字符的字符串重新赋值给new3
print(len(new3))    # 打印出去掉字符之后的字符串长度   6
print(new3)         # 打印出去掉字符之后的字符串      hello
new4 = s.strip('l') # 将去掉字符的字符串重新赋值给new4
print(new4)         # 打印出去掉字符之后的字符串,不能去除字符串中间指定的字符  hello

'''
字符串的拼接 用 + 号
需要保证 + 左右的变量值数据类型要一致
'''
m = '中秋节, '
n = '学习Python很快乐'
l = 666             # 整数 str（数字）可以强制转换为str类型
print(m + n)        # 中秋节, 学习Python很快乐
print(m, n)         # 中秋节,  学习Python很快乐
print(m, n, l)      # 中秋节,  学习Python很快乐 666
# print(m + n + l)    # 报错：TypeError: can only concatenate str (not "int") to str；原因是m和n是字符串，l是整数，字符类型不同，不能拼接
print(m + n + str(l))   # 通过str(l)将 l 强制转换为  字符串，然后就可以正常拼接
print(m + n, l)         # 先将相同的字符串拼接，再显示l


'''
字符串格式化输出 % format
'''
age = 18
name = '小恒星'
score = 99.99
# print("Python学习班的"+name+"今年"+age+'岁')   # 报错：TypeError: can only concatenate str (not "int") to str；原因是age是整数，字符类型与其他内容不同，不能拼接
print("Python学习班的 "+name+"今年", age, '岁')
print("Python学习班的 "+name+"今年"+str(age)+'岁')

'''
格式化输出 1、format  特点 {}   用{} 来占坑
有多少个{},填多少个字符串
.format( , )括号里面没有指定填多少个参数，不需要那么多也可以多填一些
.format( , )括号里面第一个值填第一个坑，第二个值填第二个坑
前面输出内容的{}里面填写了顺序，则.format( , )括号里面的值按前面{}里的顺序依次填入
'''
print("Python学习班的 {0} , 今年 {1} 岁" .format(name, age))   # Python学习班的 小恒星 , 今年 18 岁
print("Python学习班的 {1} , 今年 {0} 岁" .format(name, age))   # Python学习班的 18 , 今年 小恒星 岁
print("Python学习班的 {1} , 今年 {1} 岁" .format(name, age))   # Python学习班的 18 , 今年 18 岁
print("Python学习班的 {0} , 今年 {0} 岁" .format(name, age))   # Python学习班的 小恒星 , 今年 小恒星 岁
print("-----------------------这是分隔符----------------------------")

'''
格式化输出 2、%  %s:字符串  %d:数字  %f:浮点数
只能按照顺序赋值
%s 占的坑，可以填任何数据；%d 占的坑，只能填数字和浮点数；%f 占的坑，只能填小数
'''
print("Python学习班的%s, 今年%d岁！" %(name, age))
print("Python学习班的%s, 今年%s岁！" %(name, age))
# print("Python学习班的%d , 今年%d岁！" %(name, age))  # 报错：TypeError: %d format: a number is required, not str，原因是：%s 占的坑，可以填任何数据，%d 占的坑，只能填数字
print("Python学习班的%s, 今年%s岁, 考了%s分" %(name, age, score))    # Python学习班的小恒星, 今年18岁, 考了99.99分;正常输出字符串分数
print("Python学习班的%s, 今年%s岁, 考了%d分" %(name, age, score))    # Python学习班的小恒星, 今年18岁, 考了99分;正常输出整数分数
print("Python学习班的%s, 今年%s岁, 考了%f分" %(name, age, score))    # Python学习班的小恒星, 今年18岁, 考了99.990000分;正常输出浮点型分数
print("Python学习班的%s, 今年%s岁, 考了%.2f分" %(name, age, score))  # Python学习班的小恒星, 今年18岁, 考了99.99分;正常输出浮点型分数,保留小数点后两位
print("Python学习班的%s, 今年%s岁, 考了%.1f分" %(name, age, score))  # Python学习班的小恒星, 今年18岁, 考了100.0分;正常输出浮点型分数,四舍五入后保留一位小数