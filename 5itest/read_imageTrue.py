# 读取并识别验证码
# 调取第三方的api，读取不规则的验证码图片

import requests
import pytesseract
from PIL import Image
from ShowapiRequest import ShowapiRequest

# 识别图片验证码是属于【识别 英数-文件】，对应的是“http://route.showapi.com/184-4”地址
r = ShowapiRequest("http://route.showapi.com/184-4","359461","973cb85f8d50466ba8a11bf5bcb8835d" )
# r.addBodyPara("img_base64", "D:/Image/imooc1.png")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
# r.addBodyPara("needMorePrecise", "0")
r.addFilePara("image",r"D:/Image/imooc1.png")
res = r.post()
text = res.json()['showapi_res_body']['Result']
print(text) # 返回信息