from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import datetime

# 导入谷歌浏览器的驱动
driver = webdriver.Chrome()

# 浏览器初始化
def driver_init():
    driver.get("http://192.168.142.131/ecshop/")  # 打开ecshop商城首页
    driver.maximize_window()  # 浏览器窗口最大化
    time.sleep(1)  # 休息1s
    # 通过xpath方法定位到“注册”按钮，注意里面的值要把双引号换成单引号
    driver.find_element_by_xpath("//*[@id='ECS_MEMBERZONE']/a[2]/img").click()
    time.sleep(2)  # 休息2s

# 根据对网页的分析我们把获取文本框的路径进行封装
# 封装获取id的方法 定义id变量
def get_regist_id(id):
    regist_id = driver.find_element_by_id(id)
    return regist_id

# 封装获取name的方法 定义name变量
def get_regist_name(name):
    regist_name = driver.find_element_by_name(name)
    return regist_name

# 为了满足较为真实的情况账号采用随机值,封装获取随机值的方法
def get_userinfo():
    user_info = "".join(random.sample("abcdefghijklmn1234567890", 8))  # 随机组成8个字符随机值
    return user_info

def get_contactinfo():
    user_int = "".join(random.sample("0123456789", 8))  # 随机组成11个字符随机值
    return user_int

# 编写主程序,调用封装的方法来实现注册
def run_main():
    user_name_info = get_userinfo()    # 用户名
    email = user_name_info + "@163.com"     # email
    user_contact_info = get_contactinfo()   # 密码
    driver_init()
    get_regist_id("username").send_keys(user_name_info)  # 用户名
    get_regist_id("email").send_keys(email)  # 邮箱
    get_regist_id("password1").send_keys("123456")  # 密码
    get_regist_id("conform_password").send_keys("123456")  # 确认密码
    get_regist_name("extend_field1").send_keys(user_contact_info)  # MSN
    get_regist_name("extend_field2").send_keys(user_contact_info)  # QQ
    get_regist_name("extend_field3").send_keys(user_contact_info)  # 办公电话
    get_regist_name("extend_field4").send_keys(user_contact_info)  # 家庭电话
    get_regist_name("extend_field5").send_keys(user_contact_info)  # 手机
    time.sleep(5)

    # 密码提示问题
    # 实例化select
    s = Select(driver.find_element_by_name("sel_question"))
    # 定位选项
    # selct_option_name = ['我最好朋友的生日？', '我儿时居住地的地址？', '我的座右铭是？', '我最喜爱的电影？', '我最喜爱的歌曲？', '我最喜爱的食物？', '我最大的爱好？', '我最喜欢的小说？', '我最喜欢的运动队？']
    # 先定义一个数组，把密码提示问题的value值放在数组里面，再通过random.chome方法随机选择一个值进行选择
    option_code = ['friend_birthday', 'old_address', 'motto', 'favorite_movie', 'favorite_song', 'favorite_food',
                   'interest', 'favorite_novel', 'favorite_equipe']
    # print(random.choice(option_code))
    s.select_by_value(random.choice(option_code))
    time.sleep(2)
    # 密码问题答案
    # 用当前的时间作为密码问题的答案
    now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    driver.find_element_by_name("passwd_answer").send_keys(now)
    time.sleep(5)
    # 点击【注册】按钮
    # driver.find_element_by_name("Submit").submit()
    driver.close()

run_main()
