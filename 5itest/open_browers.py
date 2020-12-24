'''
打开浏览器，输入地址，判断输入的地址是否包含指定的关键字，来判断地址是否正确

expected_conditions模块收集了一系列的场景判断方法
'''

# 2-6、使用title_contains检查页面是否正确

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
# title_contains 判断当前页面的title是否包含预期字符串，返回布尔值
title = EC.title_contains(u"注册")
print(title(driver))

driver.quit()