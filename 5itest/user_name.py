# 2 - 11、如何生成用户名(参数化)

from selenium import webdriver
import time
import random
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# driver.get("http://www.5itest.cn/register")
time.sleep(5)
# print(EC.title_contains("注册"))
# email_element = driver.find_element_by_id("register_email")
'''
range()是一个函数， for i in range () 就是给i赋值：
含头不包尾，(5)则从0开始循环，从0开始计数,即：0,1,2,3,4

random:产生随机数

sample(list, k)返回一个长度为k新列表，新列表存放list所产生k个随机唯一的元素，多用于截取列表的指定长度的随机数

概述：
将序列中的元素以指定的字符连接生成一个新的字符串。

''.join
语法： ‘delimiter’.join(seq)
delimiter：分隔符。可以为空
delimiter：要连接的元素序列、字符串、元组、字典

返回通过指定字符连接序列中元素后生成的新字符串。
例如：seq为数组[f,5,z,3]，那么返回的是字符串:f5z3
'''
for i in range(5):  # 生成5个用户名
	user_email = ''.join(random.sample('1234567890abcdefg', 6)) + "@163.com"
	print(user_email)
	
	