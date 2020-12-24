import configparser
class ReadIni(object):

    def __init__(self, file_name=None, node=None):
        # 如果file_name为None时，进行默认赋值
        if file_name == None:
            file_name = "E:/Git_PythonCode/selenium_python/5itest/config/LocalElement.ini"
        # 如果ini文件中的section为None时，默认赋值
        if node == None:
            self.node = "RegisterElement"
        # 否则就引用初始化时传入的值
        else:
            self.node = node
        self.cf = self.load_ini(file_name)

# 加载文件
    def load_ini(self, file_name):
        cf = configparser.ConfigParser()
        # 读取配置文件
        cf.read(file_name)
        return cf

# 获取配置文件中的值
    def get_value(self, key):
        data = self.cf.get(self.node,key)
        return data

if __name__ == '__main__':
    # 初始化对象
    read_init = ReadIni()
    print(read_init.get_value('user_email'))

'''
cf =configparser.ConfigParser()
cf.read(r"E:\\Git_PythonCode\\selenium_python\\5itest\\config\\LocalElement.ini")
print(cf.get('RegisterElement','user_email'))
'''