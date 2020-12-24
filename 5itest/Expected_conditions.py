# 2-8、如何使用Expected_conditions判断元素是否可见

from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
time.sleep(3)
print(EC.title_contains("注册"))

# 判断元素是否可见
# element = driver.find_element_by_class_name("controls")
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

# 调用WebDriverWait方法，传入WebDriver实例和超时时间
WebDriverWait(driver, 10).until(EC.visibility_of_element_located(locator))
driver.quit()

# driver.find_element_by_id("register_email").send_keys("mushishi_01@163.com")
# user_name_element_node = driver.find_elements_by_class_name("controls")[1]
# user_element = user_name_element_node.find_element_by_class_name("form-control")
# user_element.send_keys("Liyw001")
# driver.find_element_by_name("password").send_keys("111111")
# driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("111111")