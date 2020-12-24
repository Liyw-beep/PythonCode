from selenium import webdriver
import time
import random
from ShowapiRequest import ShowapiRequest
from PIL import Image

driver = webdriver.Chrome()  # 实例化

# 浏览器初始化
def driver_init():  # 封装成一个初始化函数
	driver.get("http://www.5itest.cn/register")  # 取得测试地址
	driver.maximize_window()  # 最大化窗口
	time.sleep(5)

# 获取element信息
def get_element(id):
	element = driver.find_element_by_id(id)
	return element

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

# 获取随机数
def get_range_user():
	user_info = ''.join(random.sample('1234567890abcdefghijklmn', 8))
	return user_info

# 获取图片
def get_code_image(file_name):
	driver.save_screenshot(file_name)
	code_element = driver.find_element_by_id("getcode_num")
	print(code_element.location)  #打印出的结果类似：{"x":123,"y":345}
	left = code_element.location['x']
	top = code_element.location['y']
	right = code_element.size['width'] + left
	height = code_element.size['height'] + top
	im = Image.open(file_name)
	img = im.crop((left, top, right, height))
	img.save(file_name)

# 解析图片获取验证码
def code_online(file_name):
	r = ShowapiRequest("http://route.showapi.com/184-4","359461","973cb85f8d50466ba8a11bf5bcb8835d" )
	r.addBodyPara("typeId", "35")  # 验证码的长度
	r.addBodyPara("convert_to_jpg", "0")
	r.addFilePara("image",file_name)  # 文件上传时设置
	res = r.post()
	print(res.text)
	text = res.json()['showapi_res_body']['Result']
	return text

# 运行主程序
def run_main():
	user_name_info = get_range_user()
	user_email = user_name_info + "@163.com"
	file_name = "D:/Image/imooc2.png"
	driver_init()
	get_element("register_email").send_keys(user_email)
	get_element("register_nickname").send_keys(user_name_info)
	get_element("register_password").send_keys("123456")
	get_code_image(file_name)
	text = code_online(file_name)
	get_element("captcha_code").send_keys(text)
	get_element("register-btn").click()
	driver.quit()

# 调用主程序
run_main()