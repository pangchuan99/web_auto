import requests
import json

s=requests.session()
url = "http://49.235.92.12:6009/api/v1/login"

body = {
	"username": "test",
	"password": "123456"
}
r = s.post(url, json=body)  #先登录
token =r.json()["token"]
print(token)

#保存token到session会话
# s.toekn=token
# # print(s.toekn)


h = {
    "Authorization": "Token {token}".format(token=token)
}
#token 需要update后面就自动关联了  然后cookies自动关联的
s.headers.update(h)
print(s.headers)


#后面请求就不需要传 Token
r2 = s.get("http://49.235.92.12:6009/api/v1/userinfo")
print(r2.text)



#修改个人信息   有session  就不用带token了
url3 = "http://49.235.92.12:6009/api/v1/userinfo"
body3 = {
    "name": "test",
    "sex": "M",
    "age": 24,
    "mail": "283340479@qq.com"
}
r3=s.post(url3,json=body3)
print(r3.text)
