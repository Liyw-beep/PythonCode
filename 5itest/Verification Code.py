'''
2-12、如何解决验证码思路

	解决方法
	1. 设置一个万能验证码
	2. cookie绕过登录
	3. 让开发去掉验证码
	4. 先把验证码图片保存下来，再通过专业的软件把验证码所在的坐标识别，通过专业软件去解析
'''

'''
2-13、如何解决验证码代码实战
'''

from selenium import webdriver
import time
import random
from PIL import Image
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
time.sleep(5)
print(EC.title_contains("注册"))
email_element = driver.find_element_by_id("register_email")
# 保存整个网页的图片
driver.save_screenshot("D:/Image/imooc.png")
# getcode_num：验证码图片元素的id，这一步就是获取code元素坐标
code_element = driver.find_element_by_id("getcode_num")
# code_element.location：获取某个的位置
print(code_element.location)  # 打印出的结果类似：{"x":123,"y":345}
# 获取code图片坐标值，四个角的坐标值
left = code_element.location['x']   # 左上角坐标值
top = code_element.location['y']    # 右下角坐标值
right = code_element.size['width'] + left   # 宽度
height = code_element.size['height'] + top  # 高度


# 通过坐标值得到code image图
im = Image.open("D:/Image/imooc.png")
# 将crop中的left、top、right、bottom封装成一个元组crop((left,top,right,bottom))
img = im.crop((left, top, right, height))  #按照一定的坐标对图片进行裁剪(这里是把验证码图片从网页图片中裁剪出来)
img.save("D:/Image/imooc1.png")
