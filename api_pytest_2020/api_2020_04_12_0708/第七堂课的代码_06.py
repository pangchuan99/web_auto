import requests
import json

url = "http://49.235.92.12:6009/api/v1/login"

body = {
	"username": "test",
	"password": "123456"
}
r = requests.post(url, json=body)
print(r.json())
token = r.json()["token"]
print(token)   # 获取到token

url2 = "http://49.235.92.12:6009/api/v1/userinfo"
h = {
    "Content-Type": "application/json",
    "Authorization": "Token %s"%token
    # "token":'{}'.format(token)
}
r2 = requests.get(url2, headers=h )
print(r2.text)
print(r2.json())
print(r2.json()['msg'])
mail = r2.json()['data'][0]["mail"]
assert mail == "XXXX@qq.com"
#
#

