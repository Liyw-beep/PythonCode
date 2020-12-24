# 2-16、注册输入验证码流程整合
from selenium import webdriver
import time
import random
from PIL import Image
from ShowapiRequest import ShowapiRequest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()   # 打开Google浏览器
driver.get("http://www.5itest.cn/register")     # 打开 网址
time.sleep(3)           # 休息3秒
print(EC.title_contains("注册"))  # 判断网页标题是否包含“注册”
email_element = driver.find_element_by_id("register_email")  # 将定位邮箱输入框的元素方法封装
driver.save_screenshot("D:/Image/imooc.png")            # 截屏并保存图片
# getcode_num：验证码图片元素的id，这一步就是获取code元素坐标
# getcode_num识别的是验证码的定位元素，将这个定位的方法封装
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
# 将剪切下来的验证码图片保存
img.save("D:/Image/imooc2.png")

# 识别图片验证码是属于【识别 英数-文件】，对应的是“http://route.showapi.com/184-4”地址
r = ShowapiRequest("http://route.showapi.com/184-4","359461","973cb85f8d50466ba8a11bf5bcb8835d")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image",r"D:/Image/imooc2.png")  # 需要转换的文件对象,filePath为绝对路径
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息
time.sleep(2)
driver.find_element_by_id('captcha_code').send_keys(text)   # 在验证码输入框内输入验证码