import urllib.request
url = 'http://www.baidu.com'
response=urllib.request.Request(url)
html=urllib.request.urlopen(response)
print(html.getcode())
print(html.headers)