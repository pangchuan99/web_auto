import requests
import re   #正则

s = requests.Session()

url = "http://49.235.92.12:6009/admin/login/"
# 模拟第一次打开登录页面
r1 = s.get(url)
# print(r1.text) # HTML

# 获取页面隐藏参数csrf_token
token = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r1.text)  #前面是查找对象  后面这个r1.text是匹配的对象
print(token[0])  #提取出来是list类型

# cookie读取
print(s.cookies)  # RequestsCookieJar
print(dict(s.cookies))


# 后面的登录
body = {
    "csrfmiddlewaretoken": token[0],
    "username": "admin",
    "password": "yoyo123456",
    "next": "/admin/"
}

r2 = s.post(url, data=body)
# print(r2.text)

assert "Site administration | Django site admin" in r2.text

print(s.cookies)


# 登录之后的页面
r3 = s.get("http://49.235.92.12:6009/admin/auth/group/")
# print(r3.text)