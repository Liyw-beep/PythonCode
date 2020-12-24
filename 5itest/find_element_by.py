from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
time.sleep(5)
print(EC.title_contains("注册"))

# 2-7、使用不同的方式进行定位

# 定位邮箱地址输入框元素
driver.find_element_by_id("register_email").send_keys("447156220@qq.com")
# 定位用户名输入框元素
# 1、通过"form-control input-lg"无法准确定位到用户名的位置
	# driver.find_element_by_class_name("form-control input-lg").send_keys("447156220@qq.com")
'''
通过class_name方法定位用户名输入框，找到"form-control input-lg"元素，实际上这个元素是在class="controls"下，
但是class="controls"下有两个div，每个div下都有一个"form-control input-lg"元素。用户名输入框属于第二个，
所以要先定位到第二个"form-control input-lg"元素的位置即：driver.find_elements_by_class_name("controls")[1]
父节点定位好了后，再通过by_class_name定位到具体的class位置，再输入内容
'''
# 通过定位"form-control input-lg"的父节点的下标，找到第二个元素
user_name_element_node = driver.find_elements_by_class_name("controls")[1]
# 通过第二个元素找到"form-control input-lg"
user_element = user_name_element_node.find_element_by_class_name("form-control")
user_element.send_keys("Liyw001")
# 定位密码输入框元素
driver.find_element_by_name("password").send_keys("123456")
# 定位验证码输入框元素
driver.find_element_by_xpath("//*[@id='captcha_code']").send_keys("111111")
time.sleep(3)