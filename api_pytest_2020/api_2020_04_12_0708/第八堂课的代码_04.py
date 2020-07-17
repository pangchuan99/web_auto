import requests
import re   #正则

s = requests.Session()
# 模拟第一次打开登录页面
url = "http://49.235.92.12:6009/admin/login/"

#第一次打开然后对cookie读取
r1=s.get(url)
print("第一次打开浏览器访问网址获取到的cookies",r1.cookies)   #返回RequestsCookieJar 类  可以转换成字典
print("第一次打开浏览器访问网址获取到的cookies转成字典取值",s.cookies["csrftoken"])
# print(r1.text)




#后面的登录 自动带过来cookies
#进行输入文本内容，但是有隐藏参数需要用正则进行获取
token =re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r1.text)
print("打开页面然后进行获取到的隐藏参数",token) #提取出来是list类型
print("打开页面然后进行获取到的隐藏参数",token[0])
body = {
    "csrfmiddlewaretoken": token[0],
    "username": "admin",
    "password": "yoyo123456",
    "next": "/admin/"
}
r2=s.post(url,data=body)
print("获取到的第二个cookies",s.cookies)
print("获取到的第二个cookies进行转字典",s.cookies["csrftoken"])
# print("获取到的第二个cookies进行转字典",s.cookies["sessionid"])



# 登录之后的页面
r3 = s.get("http://49.235.92.12:6009/admin/auth/group/")
print("登录之访问的cookies",s.cookies)
print(r3.text)

assert "Select group to change | Django site admin" in r3.text