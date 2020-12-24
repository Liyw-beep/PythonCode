# 2-10、输入注册用户名字及获取用户信息

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
time.sleep(3)
print(EC.title_contains("注册"))

#判断元素是否可见
#element = driver.find_element_by_class_name("controls")
# 通过classname的方式 找到 controls
locator = (By.CLASS_NAME, "controls")
'''
class WebDriverWait(object):
    def __init__(self, driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None):
固定用法：
WebDriverWait(driver, 超时时长, 调用频率, 忽略异常).until(可执行方法, 超时时返回的信息)
'''
'''
visibility_of_element_located(locator) 判断某个locator元素是否可见
可见代表非隐藏、可显示，并且元素的宽和高都大于0
如果定位到就返回WebElement，找不到元素 报错Message: no such element: Unable to locate element

WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, 'su')))
打印结果是WebElement和显式等待结合后，如果定位到就返回WebElement，找不到元素 显式等待+报错
'''
WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))
# 把邮箱输入框元素的定位方法实例化
email_element = driver.find_element_by_id("register_email")
# get_attrubute:获取元素标签的内容;placeholder是邮箱输入框元素的名称，get_attrubute就是获取邮箱输入框内默认的内容
print(email_element.get_attribute("placeholder"))
# 邮箱输入框输入邮箱名称
email_element.send_keys("liyw@163.com")
# 打印出邮箱输入框里面输入的内容
print(email_element.get_attribute("value"))


driver.quit()

