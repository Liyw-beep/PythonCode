#! /user/bin/python
# -*- coding:UTF-8 -*-
"""
@product:PyCharm
@project:PythonCode_Study
@file:Class_Tuple.py
@AUTHOR:DELL - 李彦文
@time:2020/12/28
"""

'''
元组 tuple 符号()
1、可以存在空元祖 q = ()
2、元组内可以包含任何数据类型的数据，可以用 print(type(q)) 进行数据类型查看
3、元组里面的元素也是用逗号进行分割
4、元组里面的元素，也是有索引的，索引值从0开始
5、元组的切片，同字符串的操作   元组名[索引头:索引尾:步长]
'''
q = ()
a = (2, 4, True, [2, 5, 8], '小李',(4, 5.8, False), 99.85)
print(type(q))  # 打印结果为：<class 'tuple'>

print(a[4])     # 打印结果为：小李
print(a[-2])     # 打印结果为：(4, 5.8, False)


print(a[::2])     # 打印索引为偶数的值：结果为 (2, True, '小李', 99.85)
print(a[0:5:2])     # 打印索引为偶数的值，索引值为0,2,4：结果为 (2, True, '小李')

'''
操作数据库的时候，会存放一些条件
元组不支持任何的数据修改(增，删，改)
'''
a[3][-1] = '李彦文'    # a[3]的值是[2, 5, 8]，[2, 5, 8]的最后一个元素用-1表示，值为8 ，改成'李彦文'
print(a)        # 将a元组的第4个值，最后一位改成'李彦文'，结果显示为：(2, 4, True, [2, 5, '李彦文'], '小李', (4, 5.8, False), 99.85)

print(a[3][2])      # 将元组内索引值为3的元素(即数组)内，索引值为2的元素打印出来，结果为：李彦文

b = [2, 4, True, [2, 5, 8], '小李', (4, 5.8, False), 99.85]
# b[5][1] = 3.333
print(b)        # 报错：元组里面的数据不可以修改

b[5] = "昊天大帝"
print(b)        # 如果将元组整个替换掉是可以的，结果显示为：[2, 4, True, [2, 5, 8], '小李', '昊天大帝', 99.85]



c = (1)
print(type(c))  # 打印结果为 int

d = ('liyanwen')
print(type(d))      # 打印结果为 str

e = [1, 2, 3]
print(type(e))      # 打印结果为 list

# 如果你的元组里面只有一个元素，那么元素后面要加逗号才能被识别为元组
c1 = (1, )
print(type(c1))  # 打印结果为 tuple

d1 = ('liyanwen', )
print(type(d1))      # 打印结果为 tuple

e1 = ([1, 2, 3],)
print(type(e1))      # 打印结果为 tuple