# 读取并识别验证码
# 不规则的验证码图片无法识别，只能识别规则的验证码图片

import pytesseract
from PIL import Image

image = Image.open("D:/Image/imooc1.png")
text = pytesseract.image_to_string(image)  # 将图片上的文字转化成文本格式
print(text)